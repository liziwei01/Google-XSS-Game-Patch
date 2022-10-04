'''
Author: liziwei01
Date: 2022-10-04 02:21:36
LastEditors: liziwei01
LastEditTime: 2022-10-04 05:25:48
Description: file content
'''
from flask import Flask, request, render_template, redirect
import html
 
app = Flask(__name__)

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

@app.route("/level1")
def level1():
	query = request.args.get("query")
	if query is None:
		return page_header + main_page_markup + page_footer
	else:
		message = "Sorry, no results were found for <b>" + html.escape(query) + "</b>."
		message += " <a href='?'>Try again</a>."
		return page_header + message + page_footer

@app.route("/level2")
def level2():
	return render_template("level2.html")

@app.route("/level3")
def level3():
	return render_template("level3.html")

@app.route("/level4")
def level4():
	timer = request.args.get("timer")
	if timer is None:
		return render_template("level4.html")
	else:
		timer = html.escape(timer)
		return render_template("timer.html", timer=timer)

@app.route("/level5")
def level5():
	return redirect("/level5/frame/welcome")

@app.route("/level5/frame/welcome")
def level5fw():
	return render_template("welcome.html")

@app.route("/level5/frame/signup")
def level5fs():
	next = request.args.get("next")
	next = html.escape(next)
	return render_template("signup.html", next=next)

@app.route("/level5/frame/confirm")
def level5fc():
	next = request.args.get("next")
	next = html.escape(next)
	if next is None:
		next = "welcome"
	return render_template("confirm.html", next=next)

@app.route("/level6")
def level6():
	return redirect("/level6/frame#/static/gadget.js")

@app.route("/level6/frame")
def level6f():
	return render_template("level6.html")
	
 
if __name__ == "__main__":
	app.run(port=8000)