var express = require('express');
var router = express.Router();

/* GET home page. */
profiles = [{
  name: 'Rahul',
  bio: 'Plays a lot of football',
  age: 19,
  gender: 'male',
  image: 'image.jpg'
}
,{
  name: 'Abhiman',
  bio: 'Does not play football',
  age: 20,
  gender: 'male'
}
,{
  name: "Sidharth",
  bio: 'loves cricket',
  age: 25,
  gender: 'male'
}]
router.get('/', function(req, res, next) {
  var myPythonScriptPath = './script.py';
  const { PythonShell } = require("python-shell");
  var pyshell = new PythonShell(myPythonScriptPath);
  pyshell.send('hello world')
  pyshell.on('message', function(message) 
  {
    console.log(message);
  })
  
  pyshell.end(function(err){
    if(err){
      throw err;
    };
    res.render('index', { title: 'Express', name: profiles[0]["name"], bio: profiles[0]["bio"]});
  console.log('finished');
  })
});
var username = 'hello'
router.get('/test', function(req, res, next){
  res.render('test', {username: profiles[0]['name']})

})
let st = 'hello';


module.exports = router;
