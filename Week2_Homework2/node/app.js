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

app.get("/getbin", async (req, res) =>{
    const pythonResponse = await fetch("http://127.0.0.1:8000/convertBin");
    const pythonmessage = await pythonResponse.json();

    res.send({"The python server can convert a random integer into a binary number: ": pythonmessage})
});

app.get("/getlength", (req, res) =>{
    var randomString = "Hello my name is Gil and I am a student at KEA.";
    console.log(randomString.length);

    res.send({"The length of the string is: ": randomString.length})
})


app.listen(3000, ()=>{
    console.log("Server is running on ", 3000);
});