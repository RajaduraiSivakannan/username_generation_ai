import axios from 'axios'
export const clientService = async (method:any, endpoint:any, payload:any) => {
    try {
        let Request = {
            "method": method,
            "url": endpoint,
            "data": payload,
            "headers": {
                "content": "application/json"
            }
        }
        let response = await axios(Request)
        return response
    }
    catch (error) {
        console.log(error)
    }
}