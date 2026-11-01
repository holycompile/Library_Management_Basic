from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book_entry")
def bookentry():
    return render_template("book_entry.html")

@app.route("/book_remove")
def bookremove():
    return render_template("book_remove.html")

if __name__=="__main__":
    app.run(debug=True)