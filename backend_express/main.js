const express = require('express');
const axios = require('axios')
require("dotenv").config()
const mongoose = require('mongoose');
const app = express();
const moment = require('moment-timezone');
const port = process.env.port_number
const cors=require('cors')
app.use(express.json())
app.use(cors())
mongoose.connect(process.env.db_link)
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err))
const usercreds = new mongoose.Schema({
    name: String,
    mobile_number: String,
    namesviewed: [{
        nameviewed: String,
        datetime: Date
    }],
    searchedsurnames: [{
        nickname: String,
        datetime: Date
    }]
})
const nicknameall = new mongoose.Schema({
    nicknamelist: [String]
})
const nicknameusername = new mongoose.Schema({
    name: String,
    surname: String,
    generatednames: [String]
})
const nicknameusernamecompare = mongoose.model('nicknameusernamecompare', nicknameusername)
const nickname = mongoose.model('nickname', nicknameall)
const user = mongoose.model('user', usercreds)


// payload to  be  sent for create_api_link
// {
//     "name":"xxxx",
//     "mobile_number":"9999999999"
// }

app.post(process.en.create_api_link, async (req, res) => {
    const { name, mobile_number } = req.body
    let valid = true
    if (name.trim() === "") {
        valid = false
    }
    if (mobile_number.trim() === "" || mobile_number.trim().length !== 10) {
        valid = false
    }
    if (!valid) {
        return res.status(400).json({ "data": "Please check the sent payload correctly" })
    }
    try {
        const existing_mobile_number = await user.findOne({ mobile_number: mobile_number })
        if (existing_mobile_number) {
            return res.status(200).json({ "data": "user exists" })
        }
        else {
            const newuser = new user({ name, mobile_number })
            await newuser.save()
            return res.status(200).json({ "data": "new user created successfully" })
        }
    }
    catch (error) {
        console.log("The error is :", error)
        return res.status(500).json({ "data": "Internal Server Error" })
    }
})

// payload to be sent for for userquery_api_link
// {
//     "name":"xxx",
//     "mobile_number":"9999999999",
//     "usernickname":"lion"
// }

app.post(process.env.userquery_api_link, async (req, res) => {
    const { name, mobile_number, usernickname } = req.body
    if (!name.trim() || !mobile_number.trim() || mobile_number.trim().length !== 10 || !usernickname.trim()) {
        return res.status(400).json({ data: "Please check the sent payload correctly" });
    }
    try {
        let toxicresponse = await axios.post(process.env.toxic_api_link, { "data": usernickname })
        if (toxicresponse.status === 200) {
            if (toxicresponse.data.data === "toxic") {
                return res.status(200).json({ "data": "Toxic Word Detected ", "flag": "True" })
            }

            else {
                const userdetails = await user.findOne({ name: name, mobile_number: mobile_number })
                if (!userdetails) {
                    return res.status(400).json({ "data": "User not found" })
                }
                else {
                    userdetails.searchedsurnames.push({
                        nickname: usernickname,
                        datetime: moment().tz('Asia/Kolkata').toDate()
                    })
                    await userdetails.save()
                    let getnicknamedata = await nickname.findOne({})
                    if (getnicknamedata === null) {
                        const updateResult = await nickname.updateOne(
                            {},
                            {
                                $push: { nicknamelist: usernickname }
                            },
                            { upsert: true, new: true }
                        )
                    }
                    else {
                        let getnicknamelistdata = getnicknamedata.nicknamelist
                        checkingpresent = getnicknamelistdata.includes(usernickname)
                        if (!checkingpresent) {
                            const updateResult = await nickname.updateOne(
                                {},
                                {
                                    $push: { nicknamelist: usernickname }
                                },
                                { upsert: true, new: true }
                            )
                        }
                    }

                }
                const findrelation = await nicknameusernamecompare.findOne({ name: name, surname: usernickname })
                if (findrelation && findrelation.generatednames.length > 0) {
                    const addinggeneratednamestoUser= await user.findOne({name:name,mobile_number:mobile_number})
                    for (let i = 0; i < findrelation.generatednames.length; i++) {
                        addinggeneratednamestoUser.namesviewed.push({
                            nameviewed: findrelation.generatednames[i],
                            datetime: moment().tz('Asia/Kolkata').toDate()
                        })

                    }
                    await addinggeneratednamestoUser.save()
                    return res.status(200).json({ "data": findrelation.generatednames })
                }
                else {
                    let response = await axios.post(process.env.model_api_link, { data: name + usernickname })
                    if (response.status === 200) {
                        let response_data = response.data.data
                        const finduser = await user.findOne({ name: name, mobile_number: mobile_number })
                        if (!finduser) {
                            return res.status(400).json({ "data": "User not found" })
                        }
                        else {
                            for (let i = 0; i < response_data.length; i++) {
                                finduser.namesviewed.push({
                                    nameviewed: response_data[i],
                                    datetime: moment().tz('Asia/Kolkata').toDate()
                                })

                            }

                        }
                        await finduser.save()
                        let newtotaluser = await nicknameusernamecompare.findOne({ name: name, surname: usernickname });
                        if (!newtotaluser) {
                            newtotaluser = new nicknameusernamecompare({ name: name, surname: usernickname, generatednames: [] });
                        }
                        for (let i = 0; i < response_data.length; i++) {
                            newtotaluser.generatednames.push(
                                response_data[i]
                            )

                        }
                        await newtotaluser.save();
                        return res.status(200).json({ "data": response_data })

                    }
                    else {
                        console.log("error", response.status)
                        return res.status(500).json({ "data": "Internal Server Error" })
                    }

                }
            }
        }
        else{
            return res.status(500).json({"data":"Internal Server Error"})
        }

    }
    catch (error) {
        return res.status(500).json({ "data": "Internal Server Error" })
    }
})

app.get(process.env.get_api_link, async (req, res) => {
    try {
        const names = await nickname.findOne({})
        if (names) {
            let namedatas = names.nicknamelist
            return res.status(200).json({ "data": namedatas })
        }
        else {
            return res.status(200).json({ "data": [] })
        }
    }
    catch (error) {
        return res.status(500).json({ "data": "Internal Server Error" })
    }
})
// payload to be sent for for regenerate_api_link
// {
//     "name":"xxxx",
//     "mobile_number":"9999999999",
//     "usernickname":"lion"
// }
app.post(process.env.regenerate_api_link, async (req, res) => {
    try {
        const { name, mobile_number, usernickname } = req.body
        if (!name.trim() || !mobile_number.trim() || mobile_number.trim().length !== 10 || !usernickname.trim()) {
            return res.status(400).json({ data: "Please check the sent payload correctly" });
        }
        let response = await axios.post(model_api_link, { data: name + usernickname })
        if (response.status === 200) {
            let response_data = response.data.data
            const finduser = await user.findOne({ name: name, mobile_number: mobile_number })
            if (!finduser) {
                return res.status(400).json({ "data": "User not found" })
            }
            else {
                for (let i = 0; i < response_data.length; i++) {
                    finduser.namesviewed.push({
                        nameviewed: response_data[i],
                        datetime: moment().tz('Asia/Kolkata').toDate()
                    })

                }
                finduser.searchedsurnames.push({
                    nickname: usernickname,
                    datetime: moment().tz('Asia/Kolkata').toDate()
                })

            }
            await finduser.save()
            let findusertotalnickname = await nicknameusernamecompare.findOne({ name: name, surname: usernickname })
            if (findusertotalnickname) {
                let previousdata = findusertotalnickname.generatednames
                let finalizeddata = response_data.filter(element => !previousdata.includes(element))
                for (let i = 0; i < finalizeddata.length; i++) {
                    findusertotalnickname.generatednames.push(finalizeddata[i])
                }
                await findusertotalnickname.save()
                return res.status(200).json({ "data": finalizeddata })
            }
            else {
                return res.status(422).json({ "data": "error occured during inserting datas to Db" })
            }


        }
        else {
            return res.status(500).json({ "data": "Internal Server Error" })
        }

    }
    catch (error) {
        return res.status(500).json({ "data": "Internal Server Error" })
    }
})


const gracefulShutdown = (signal) => {
    console.log(`Received ${signal}. Closing MongoDB connection...`);
    mongoose.disconnect()
        .then(() => {
            console.log('MongoDB connection closed.');
            process.exit(0);
        })
        .catch(err => {
            console.error('Error while closing MongoDB connection:', err);
            process.exit(1);
        });
}

process.on('SIGINT', () => gracefulShutdown('SIGINT'));
process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));

app.listen(port, () => {
    console.log(`http://localhost:${port}`)
})