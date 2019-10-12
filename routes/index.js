var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  var myPythonScriptPath = './script.py';
  const { PythonShell } = require("python-shell");
  var pyshell = new PythonShell(myPythonScriptPath);
  pyshell.send('hello world')
  pyshell.on('message', function(message) 
  {
    console.log(message);
  })

 
  const f = () => {
	  console.log("Test title");
	  return 'Tinder';
  }
  
  const g = () => {
	  console.log("Test name");
	  return "Uggi";
  }
  
  res.render('index', { title: f(), name: g() });
  pyshell.end(function(err){
    if(err){
      throw err;
    };
  console.log('finished');
  })
});


router.post('/')

module.exports = router;
