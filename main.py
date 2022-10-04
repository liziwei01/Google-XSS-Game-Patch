'''
Author: liziwei01
Date: 2022-10-04 02:21:36
LastEditors: liziwei01
LastEditTime: 2022-10-04 08:03:13
Description: file content
'''
from flask import Flask, request, render_template, redirect, make_response
import html
import random
 
app = Flask(__name__)
RANDOM_NONCE = "".join(random.sample("ABCDEFGHIJKIMNOPQ", 3))

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script src="/static/game-frame.js"></script>
    <link rel="stylesheet" href="/static/game-frame-styles.css" />
  </head>
 
  <body id="level1">
    <img src="/static/logos/level1.png">
      <div>
"""
 
page_footer = """
    </div>
  </body>
</html>
"""
 
main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""

@app.route("/")
def level0():
	resp = make_response(redirect("/level1"))
	return resp

@app.route("/level1")
def level1():
	query = request.args.get("query")
	if query is None:
		resp = make_response(page_header + main_page_markup + page_footer)
		return resp
	else:
		# PATCH
		message = "Sorry, no results were found for <b>" + html.escape(query) + "</b>."
		message += " <a href='?'>Try again</a>."
		resp = make_response(page_header + message + page_footer)
		return resp

@app.route("/level2")
def level2():
	resp = make_response(render_template("level2.html"))
	return resp

@app.route("/level3")
def level3():
	resp = make_response(render_template("level3.html"))
	return resp

@app.route("/level4")
def level4():
	timer = request.args.get("timer")
	if timer is None:
		resp = make_response(render_template("level4.html"))
		return resp
	else:
		# PATCH
		timer = html.escape(timer)
		resp = make_response(render_template("timer.html", timer=timer))
		return resp

@app.route("/level5")
def level5():
	resp = make_response(redirect("/level5/frame/welcome"))
	return resp

@app.route("/level5/frame/welcome")
def level5fw():
	resp = make_response(render_template("welcome.html"))
	return resp

@app.route("/level5/frame/signup")
def level5fs():
	next = request.args.get("next")
	# PATCH
	next = html.escape(next)
	resp = make_response(render_template("signup.html", next=next))
	return resp

@app.route("/level5/frame/confirm")
def level5fc():
	next = request.args.get("next")
	# PATCH
	next = html.escape(next)
	if next is None:
		next = "welcome"
	resp = make_response(render_template("confirm.html", next=next))
	return resp

@app.route("/level6")
def level6():
	resp = make_response(redirect("/level6/frame#/static/gadget.js"))
	return resp

@app.route("/level6/frame")
def level6f():
	resp = make_response(render_template("level6.html"))
	return resp

@app.after_request
def CSP2(resp):
	h = "default-src 'self' https://*.somewebsiteswetrusted.com;script-src 'self';img-src *;object-src *;form-action 'self';connect-src 'self';"

	try:
		resp.headers['Content-Security-Policy'] = resp.headers['Content-Security-Policy'] + h
	except:
		resp.headers['Content-Security-Policy'] = h
		
	return resp

@app.after_request
def CSP3(resp):
	h = ("worker-src 'nonce-"+ RANDOM_NONCE +"';"
	+ "child-src 'nonce-"+ RANDOM_NONCE +"';"
	+ "media-src 'nonce-"+ RANDOM_NONCE +"';"
	+ "frame-src 'nonce-"+ RANDOM_NONCE +"';"
	+ "font-src 'nonce-"+ RANDOM_NONCE +"';"
	+ "manifest-src 'nonce-"+ RANDOM_NONCE +"';")
	
	try:
		resp.headers['Content-Security-Policy'] = resp.headers['Content-Security-Policy'] + h
	except:
		resp.headers['Content-Security-Policy'] = h

	return resp
	
 
if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8000, debug=False)