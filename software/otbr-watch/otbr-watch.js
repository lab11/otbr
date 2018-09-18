#! /usr/bin/env node

var exec = require('child_process').exec

function check_ncp_state() {
  exec("wpanctl status", function(err, stdout, stderr) {
    if (err) {
      console.log(err);
    }
    //console.log(stdout);
    var search_string = "\"NCP:State\" => ";
    var sub_string = stdout.slice(stdout.indexOf(search_string) + search_string.length);
    var start = sub_string.indexOf('"');
    var end = sub_string.indexOf('"', 1);
    var state = sub_string.slice(start+1, end);
    console.log("wpanctl status:" + state);
    if(state !== "associated") {
      console.log("rebooting due to uninitialized thread ncp");
      exec("reboot");
    }
    else {
      console.log("all is good!");
    }
  });

  setTimeout(check_ncp_state, 5*60*1000);
}

check_ncp_state();
