from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book_entry", methods=["GET","POST"])
def bookentry():
    if request.method == 'POST':
        book_id=request.form.get("book_id")
        book_title= request.form.get("book_title")
        book_author=request.form.get("book_author")
        book_category=request.form.get("book_category")
        book_copies=request.form.get("book_copies")
        available_copies=request.form.get("available_copies")
        return f"Hello the book details you shared are: Book ID:{book_id},Author: {book_author},Ttitle:{book_title},Category:{book_category}, Copies:{book_copies}, Avaiilable:{available_copies}"
    return render_template("book_entry.html")

@app.route("/book_remove")
def bookremove():
    return render_template("book_remove.html")



if __name__=="__main__":
    app.run(debug=True)