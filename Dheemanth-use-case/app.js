var express = require('express');
var bodyParser = require('body-parser');
var mongodb = require('mongodb');

var dbConn = mongodb.MongoClient.connect('mongodb://DheemanthAlva:<password>@cluster0-shard-00-00.dx68z.mongodb.net:27017,cluster0-shard-00-01.dx68z.mongodb.net:27017,cluster0-shard-00-02.dx68z.mongodb.net:27017/FoodDeliveryManagment?ssl=true&replicaSet=atlas-nm23if-shard-0&authSource=admin&retryWrites=true&w=majority');
console.log("Connected to the mongoDB cloud cluster successfully")

var app = express();

app.use(bodyParser.urlencoded({ extended: false }));

app.get('/public',(request, response) => {
    response.sendFile(__dirname + '/index.html')
})


app.post('/post-feedback', function (req, res) {
    dbConn.then(function(db) {
        delete req.body._id; // for safety reasons
        db.collection('CustomerFeedbackComments').insertOne(req.body);
    });    
    res.send('Data received:\n' + JSON.stringify(req.body));
});

app.get('/view-feedbacks',  function(req, res) {
    dbConn.then(function(db) {
        db.collection('CustomerFeedbackComments').find({}).toArray().then(function(feedbacks) {
            res.status(200).json(feedbacks);
        });
    });
});


app.listen(process.env.PORT || 3000, process.env.IP || '0.0.0.0', ()  => {
       console.log("App is listening at http://localhost:3000")
});


