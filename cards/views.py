import mistune
from flask import request, redirect, url_for, render_template, flash

from cards import app
from database import session
from models import Card, User

from flask.ext.login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash


@app.route("/")
@app.route("/page/<int:page>")
def pages(page=1, paginate_by=3):
    # Zero-indexed page
    page_index = page - 1

    count = session.query(Card).count()

    start = page_index * paginate_by
    end = start + paginate_by

    total_pages = (count - 1) / paginate_by + 1
    has_next = page_index < total_pages - 1
    has_prev = page_index > 0

    cards = session.query(Card)
    cards = cards.order_by(Card.date_time.desc())
    cards = cards[start:end]

    return render_template("pages.html",
        cards=cards,
        has_next=has_next,
        has_prev=has_prev,
        page=page,
        total_pages=total_pages
    )



@app.route("/")
@app.route("/card/<int:card>")
def cards(card=1, paginate_by=1):
    # Zero-indexed  
    page_index = card #- 1

    count = session.query(Card).count()

    start = page_index * paginate_by
    end = start + paginate_by

    total_pages = (count - 1) / paginate_by + 1
    has_next = page_index > 0
    has_prev = page_index < total_pages - 1

    cards = session.query(Card)
    cards = cards.order_by(Card.date_time)
    cards = cards[start:end]

    return render_template("cards.html",
        cards=cards,
        has_next=has_next,
        has_prev=has_prev,
        card=card,
        total_pages=total_pages
    ) 







@app.route("/")
@app.route("/card/add", methods=["POST"])
@login_required
def add_card_post():
	card = Card(
		name = request.form["name"],
		link = request.form["link"],
		image_link = request.form["image_link"],
		weather = request.form["weather"],
		cost = request.form["cost"],
		num_people = request.form["num_people"],
	)
	session.add(card)
	session.commit()
	return redirect(url_for("cards"))


