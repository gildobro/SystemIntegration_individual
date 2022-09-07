import express from "express";
import fetch from 'node-fetch';

const app = express();


app.get("/", (req, res) =>{
    console.log("This works!");
    res.send({message: "OK OK OK"});
});

app.get("/timestamp", (req, res) =>{
    var date = new Date();
    console.log(date.toISOString())
    res.send({Date: date})
});

app.get("/datetime", async (req,res) =>{
    const pythonResponse = await fetch("http://127.0.0.1:8000/getdate");
    const pythonmessage = await pythonResponse.json();

    res.send({"Response from Python Server: ": pythonmessage})
})



app.listen(3000, ()=>{
    console.log("Server is running on ", 3000);
});