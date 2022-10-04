/*
 * @Author: liziwei01
 * @Date: 2022-10-04 07:28:39
 * @LastEditors: liziwei01
 * @LastEditTime: 2022-10-04 07:28:39
 * @Description: file content
 */

function htmlEnc(str) { 
	var s = "";
	if(str.length == 0) return "";
	s = str.replace(/&/g,"&amp;");
	s = s.replace(/</g,"&lt;");
	s = s.replace(/>/g,"&gt;");
	s = s.replace(/ /g,"&nbsp;");
	s = s.replace(/\'/g,"&#39;");
	s = s.replace(/\"/g,"&quot;");
	return s;  
}

function chooseTab(num) {
	// PATCH
	num = htmlEnc(num);
	// Dynamically load the appropriate image.
	var html = "Image " + parseInt(num) + "<br>";
	html += "<img src='/static/level3/cloud" + num + ".jpg' />";
	$('#tabContent').html(html);

	window.location.hash = num;

	// Select the current tab
	var tabs = document.querySelectorAll('.tab');
	for (var i = 0; i < tabs.length; i++) {
	if (tabs[i].id == "tab" + parseInt(num)) {
		tabs[i].className = "tab active";
		} else {
			tabs[i].className = "tab";
		}
	}

	// Tell parent we've changed the tab
	top.postMessage(self.location.toString(), "*");
}

window.onload = function() { 
	chooseTab(unescape(self.location.hash.substr(1)) || "1");
}

// Extra code so that we can communicate with the parent page
window.addEventListener("message", function(event){
	if (event.source == parent) {
	chooseTab(unescape(self.location.hash.substr(1)));
	}
}, false);