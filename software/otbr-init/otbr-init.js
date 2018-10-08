#!/usr/bin/env node

var exec = require('child_process').exec;

exec("wpanctl status", function(err, stdout, stderr) {
  if (err) {
    throw(err);
  }
  var search_string = "\"NCP:State\" => ";
  var sub_string = stdout.slice(stdout.indexOf(search_string) + search_string.length);
  var start = sub_string.indexOf('"');
  var end = sub_string.indexOf('"', 1);
  var state = sub_string.slice(start+1, end);
  console.log("wpanctl status:" + state);
  if(state !== "associated") {
    exec('wpanctl reset');
    exec('wpanctl setprop Network:PANID 0xFACE');
    exec('wpanctl setprop Network:XPANID DEAD00BEEF00CAFE');
    exec('wpanctl setprop Network:Key 00112233445566778899aabbccddeeff');
    exec('wpanctl form OpenThread -T r');
    exec('wpanctl config-gateway -d fd11:22::');
  }
});

