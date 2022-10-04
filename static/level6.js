/*
 * @Author: liziwei01
 * @Date: 2022-10-04 07:28:51
 * @LastEditors: liziwei01
 * @LastEditTime: 2022-10-04 07:30:29
 * @Description: file content
 */

function setInnerText(element, value) {
	if (element.innerText) {
		element.innerText = value;
	} else {
		element.textContent = value;
	}
}

function includeGadget(url) {
	var scriptEl = document.createElement('script');

	// This will totally prevent us from loading evil URLs!
	if (url.match(/^https?:\/\//)) {
		setInnerText(document.getElementById("log"),
		"Sorry, cannot load a URL containing \"http\".");
		return;
	}

	// Load this awesome gadget
	scriptEl.src = url;

	// Show log messages
	scriptEl.onload = function() { 
		setInnerText(document.getElementById("log"),  
		"Loaded gadget from " + url);
	}
	scriptEl.onerror = function() { 
		setInnerText(document.getElementById("log"),  
		"Couldn't load gadget from " + url);
	}

	document.head.appendChild(scriptEl);
}

// Take the value after # and use it as the gadget filename.
function getGadgetName() { 
	// PATCH
	return "/static/gadget.js";
}

includeGadget(getGadgetName());

// Extra code so that we can communicate with the parent page
window.addEventListener("message", function(event){
	if (event.source == parent) {
		includeGadget(getGadgetName());
	}
}, false);