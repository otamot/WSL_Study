var express = require('express');
var router = express.Router();

test_json = {"firstName":"boss", "lastName":"天才"} 

/* GET home page. */
router.get('/', function(req, res, next) {
  res.json(test_json);
});

module.exports = router;
