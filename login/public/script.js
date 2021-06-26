const path = require('path');
const express = require('express');
const app = express();
const request = require('request');

app.use(express.static(__dirname + '/public'))

app.get('/',function(req,res){
    res.sendFile(path.join(__dirname + '/index.html'))
})
app.post('/data/getlogindetails/',function(req,res){
    const username = req.body.username;
    const password = req.body.password;
    const response = {
        username : req.body.username,
        password : req.body.password,
        };
    console.log(response);
    return res.json(response);
 });

//  const username = "hello";
//  const password = "hai";
//  const response = {
//      username : username,
//      password : password,
//      };
//  request.post({
//     url: "https://ce8f019ec731.ngrok.io/data/getlogindetails/", 
//      json: response
// }, function(error, response, body) {
//     res.send(response)
// })
 app.listen(5005)