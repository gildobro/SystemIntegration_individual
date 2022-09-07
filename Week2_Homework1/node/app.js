import express from "express";
import fetch from 'node-fetch';
import fs from 'fs';
const app = express();


app.get("/endpoint", (req,res) =>{
    console.log("This works");
    res.send({message: "This message comes from the Node.js Server"});
});

app.get("/aboutmejson", (req, res) =>{
    fs.readFile('aboutme.json', (err, data) =>{
        if (err) throw err;
        let me = JSON.parse(data);
        console.log(me);
        res.send(me);
    });
});


app.listen(3000, ()=>{
    console.log("Server is running on", 3000);
});