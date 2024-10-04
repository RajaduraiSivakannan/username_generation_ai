import { clientService } from "./client"

export const username_creation=async (payload:any)=>{
    try{
        const response=await clientService("POST","http://localhost:3001/createuser",payload)
        return response
    }
    catch(error){
        console.log(error)
    }
}

export const surname_fetch=async ()=>{
    try{
        const response=await clientService("GET","http://localhost:3001/getnicknames",{})
        return response
    }
    catch(error){
        console.log(error)
    }
}

export const nickname_generation=async (payload:any)=>{
    try{
        const response=await clientService("POST","http://localhost:3001/userquerysearch",payload)
        return response
    }
    catch(error){
        console.log(error)
    }
}

export const nickname_regeneration=async (payload:any)=>{
    try{
        const response=await clientService("POST","http://localhost:3001/regeneratecall",payload)
        return response
    }
    catch(error){
        console.log(error)
    }
}