import { useEffect, useState } from 'react';
import './style.css'
import { nickname_generation, nickname_regeneration, surname_fetch, username_creation } from './api';
export const Nicknamepage = () => {
    const [user_details, setuser_details] = useState({
        "user_name": "",
        "mobile_number": ""
    })
    const [page1validation, setpage1validation] = useState({
        "user_name": "",
        "mobile_number": ""
    })
    const [page2validation, setpage2validation] = useState({
        "selected_name": ""
    })
    const [page, setpage] = useState(0)
    const [surnames, setsurnames] = useState([])
    const [selectedname, setselectedname] = useState({
        "selected_name": ""
    })
    const [generatedname, setgeneratedname] = useState([])
    const [loading, setloading] = useState(false)
    useEffect(() => {
        if (page === 1) {
            fetch_surnames()
        }

    }, [page])

    const onchangeFunction = (event: any) => {
        let id = event.target.id
        let value = event.target.value
        if (id === "selectedname") {
            setselectedname({ ...selectedname, selected_name: value })
        }
        else {
            setuser_details({ ...user_details, [id]: value })
        }
    }
    const fetch_surnames = async () => {
        const response: any = await surname_fetch()
        if (response.status === 200) {
            setsurnames(response.data.data)
        }
        else {
            alert("Error Occured Please Retry")
            setpage((prev) => (0))
            setuser_details((prev) => ({
                "user_name": "",
                "mobile_number": ""
            }))

        }
    }
    const handleSubmit = async () => {
        try {
            let validation = {
                "user_name": "",
                "mobile_number": ""
            }
            let valid = true
            const user_name_regex = /^[A-Za-z\s]+$/
            const mobileRegex = /^\d{10}$/

            if (user_details.user_name.trim() === "") {
                valid = false
                validation.user_name = "Please enter your name"
            }
            if (user_name_regex.test(user_details.user_name) === false) {
                valid = false
                validation.user_name = "please enter only alphabets"
            }
            if (mobileRegex.test(user_details.mobile_number) === false) {
                valid = false
                validation.mobile_number = "please enter mobile number correctly"
            }
            if (valid === false) {
                setpage1validation(validation)
            }
            else {
                let payload = {
                    "name": user_details.user_name,
                    "mobile_number": user_details.mobile_number
                }
                let response: any = await username_creation(payload)
                if (response.status === 200) {
                    if (response.data.data === "user exists" || response.data.data === "new user created successfully")
                        setpage((prev) => (1))
                }
                else {
                    alert("Error Occured Please retry ")
                    setuser_details((prev) => ({
                        "user_name": "",
                        "mobile_number": ""
                    }))
                }
            }
        }
        catch (error) {
            console.log(error)
        };


    }
    const handleNameClick = (name: any) => {
        setselectedname((prev) => ({ selected_name: name }))
    }
    const handleGenerateUsername = async () => {
        try {
            let validation = { "selected_name": "" }
            let valid = true
            if (selectedname.selected_name === "") {
                valid = false
                validation.selected_name = "Please select a name"
            }
            if (valid === false) {
                setpage2validation(validation)
            }
            else {
                setloading((prev)=>(true))
                let payload = {
                    "name": user_details.user_name,
                    "mobile_number": user_details.mobile_number,
                    "usernickname": selectedname.selected_name
                }
                const response: any = await nickname_generation(payload)
                if (response.status === 200) {
                    if(response.data.flag==="True"){
                        setloading((prev)=>false)
                        alert("Please Avoid Toxic Language")
                        setpage((prev)=>1)
                        setselectedname((prev)=>({"selected_name":""}))
                    }
                    else{
                    setgeneratedname((prev) => (response.data.data))
                    setloading((prev)=>false)
                    setpage((prev)=>2)
                    }
                }
                else {
                    setloading((prev)=>(false))
                    alert("Error occured please retry ")
                    setpage(0)
                    setuser_details((prev) => ({
                        "user_name": "",
                        "mobile_number": ""
                    }))
                    setselectedname((prev) => ({ selected_name: "" }))
                }

            }
        }
        catch (error) {
            console.log(error)
        }

    }

    const handleBackClick=()=>{
        setpage(1)
    }
    const handleRegenerateClick= async ()=>{
        setloading((prev)=>(true))
        let payload = {
            "name": user_details.user_name,
            "mobile_number": user_details.mobile_number,
            "usernickname": selectedname.selected_name
        }
        const response :any = await nickname_regeneration(payload)
        if(response.status===200){
            if(response.data.data.length ===0){
                alert("Please retry again max limit reached")
                setloading((prev)=>(false))
                setpage((prev)=>(2))
            }
            else{
            setgeneratedname((prev)=>response.data.data)
            setloading((prev)=>(false))
            }
        }
        else{
            setloading((prev)=>(false))
            alert("Error occured please retrt")
            setpage(1)
        }
    }
    return (
        <>
            {page === 0 && (
                <div className="page-container">
                    <div className="input-container">
                        <div className="input-group">
                            <label htmlFor="name">Name:</label>
                            <input
                                type="text"
                                id="user_name"
                                value={user_details.user_name}
                                onChange={onchangeFunction}
                                className="input-field"
                                required
                            />
                        </div>
                        <div className="input-group">
                            <label htmlFor="mobile">Mobile Number:</label>
                            <input
                                type="text"
                                id="mobile_number"
                                value={user_details.mobile_number}
                                onChange={onchangeFunction}
                                className="input-field"
                                required
                            />
                        </div>
                        <button onClick={handleSubmit} className="submit-button">Next 🔎</button>
                    </div>
                </div>)
            }
            {
                page === 1 && (
                    <div className="name-selector">
                        <input
                            type="text"
                            className="name-input"
                            placeholder="Select or type a name"
                            id='selectedname'
                            value={selectedname.selected_name}
                            onChange={onchangeFunction}
                        />
                        <div className="name-list">
                            {surnames.map((name, index) => (
                                <div
                                    key={index}
                                    className={`name-item ${selectedname.selected_name === name ? 'selected' : ''}`}
                                    onClick={() => handleNameClick(name)}
                                >
                                    {name}
                                </div>
                            ))}
                        </div>
                        <button className="generate-button" onClick={handleGenerateUsername}>
                            Generate Username
                        </button>
                    </div>
                )
            }
            {
                loading === true && (
                    <div className="loading-spinner"></div>
                )
            }
            {
                page===2 && loading===false && (
                    <div className="name-container">
            <div className="name-list">
                {generatedname.map((name, index) => (
                    <div
                        key={index}
                        className={`name-item ${index === name ? 'highlight' : ''}`}
                    >
                        {name}
                    </div>
                ))}
            </div>
            <div className="button-container">
                <button className="back-button" onClick={handleBackClick} >
                    Back
                </button>
                <button className="regenerate-button" onClick={handleRegenerateClick}>
                    Regenerate
                </button>
            </div>
        </div>
                )
            }
        </>
    );
};
