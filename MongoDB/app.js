// http://127.0.0.1:8081/index_wallet.html

var express = require('express');
var hbs = require('express-handlebars');
var path = require('path');
var app = express();
var mongo = require('mongodb');
var bodyParser = require('body-parser');
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/demo');
var db=mongoose.connection;


db.on('error', console.log.bind(console, "connection error")); 
db.once('open', function(callback){ 
    console.log("connection succeeded"); 
})
// 创建 application/x-www-form-urlencoded 编码解析
var urlencodedParser = bodyParser.urlencoded({ extended: false })
 
app.use('/public', express.static('public')); //讀取靜態檔案
 
app.get('/index_wallet.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index_wallet.html" );
}) //__dirname : 獲取當前執行文件所在目錄的完整目錄名

// get home page
//app.get('/',function(req,res,next){
  //res.render('index');
//});




app.engine('hbs', hbs({extname:'.hbs', defaultLayout:'layout',layoutsDir:'views'}));
app.set('views',path.join(__dirname,'views'));
app.set('view engine', 'hbs')


 // 新增資料 
app.post('/add_one', urlencodedParser, function (req, res) {
  // if (req.body.add_firstname != "" & req.body.add_lastname != ""){
  if (req.body.talking!= "") {
    var items = {
        // "first_name": req.body.add_firstname, 
        "talking" : req.body.talking,
        
    };
    
    db.collection('details').insertOne(items,function(err, collection){
        if (err) throw err;
        console.log("Record inserted Successfully!!!"); 
        // db.close();//如果關起來就只能執行一次
    });

  };
   console.log(items);
   res.redirect('/get_data'); //建入db後，頁面返回原始輸入頁
   res.end(JSON.stringify(items));
    
});


// 查詢
app.get('/get_data',function(req,res){
  
  // var arr = [];
  db.collection('details').find().toArray(function(err, result){
    if (err) throw err;
    // arr.push(result);
    for (var i=0;i<result.length;i++){
      console.log("第",i,"筆的talking:",result[i].talking);
     
    }
    
    res.render('index', {items: result, layout:'layout' }); //將資料送到index.hbs
    // db.close(); //如果關起來就只能執行一次
     
  });
  
  // res.redirect('/');
  
});


// 啟動服務
var server = app.listen(8081, function () {
 
  // var host = server.address().address
  // var port = server.address().port
  server.address().address
  server.address().port

  console.log("http://127.0.0.1:8081/index_wallet.html")
  
})

