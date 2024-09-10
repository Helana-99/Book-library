from crypt import methods
from app.models import Book, db

from flask import render_template, request, url_for
from werkzeug.utils import redirect

from app.books import book_blueprint
from app.books.forms import BookForm



@book_blueprint.route('',endpoint='landing')
def landing():
    books = Book.query.all()
    return render_template("books/landing.html", books=books)



@book_blueprint.route('/form/create', methods=['POST','GET'], endpoint='form_create')
def create_book():
    form = BookForm()
    if request.method=="POST":
        if form.validate_on_submit():
          print(request.form)
        book= Book(id=request.form["id"],
                   title=request.form["title"],
                   description=request.form["description"],
                   image=request.form["image"],
                   num_pages=request.form["num_pages"]
                   )
        db.session.add(book)
        db.session.commit()

        return redirect(book.show_url)

    return render_template('books/forms/create.html', form=form)



@book_blueprint.route('/<int:id>',endpoint='show')
def show(id):
    book = db.get_or_404(Book, id)
    return render_template("books/show.html", book=book)



@book_blueprint.route('/<int:id>/delete',endpoint='delete' ,methods=["POST"])
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books.landing"))

