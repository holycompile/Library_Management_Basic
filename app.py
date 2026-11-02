from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


app=Flask(__name__)

app.secret_key=os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db= SQLAlchemy(app)


class Book(db.Model):
    __tablename__ ='books'
    id= db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(150))
    author=db.Column(db.String(150))
    category=db.Column(db.String(150))
    total_copies=db.Column(db.Integer)
    available_copies=db.Column(db.Integer)







@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"),500

@app.route("/book_entry", methods=["GET","POST"])
def bookentry():
    if request.method == 'POST':
        book_id=request.form.get("book_id")
        book_title= request.form.get("book_title")
        book_author=request.form.get("book_author")
        book_category=request.form.get("book_category")
        book_copies=request.form.get("book_copies")
        available_copies=request.form.get("available_copies")
        
        #1. Creating a New Book Record 
        
        new_book=Book(
            id=book_id,
            title=book_title,
            author=book_author,
            category=book_category,
            total_copies=book_copies,
            available_copies=available_copies
        )
        
        # 2. Add and commit to database
        db.session.add(new_book)
        db.session.commit()
        
        return redirect ( url_for("book_submitted_success", book_id=new_book.id))    
    return render_template("book_entry.html")

@app.route("/sucess_book_submit_acknowledgement/<int:book_id>")
def book_submitted_success(book_id):
    book=db.session.get(Book, book_id)
    return render_template("book_success.html", book=book)

@app.route("/book_remove")
def bookremove():
    return render_template("book_remove.html")



@app.route('/show_all_book')
def show_all_book():
    all_books=Book.query.all()
    return render_template("show_all_books.html",all_books=all_books)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)