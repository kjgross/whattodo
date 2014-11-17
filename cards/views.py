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


@app.route("/card/add", methods=["GET"])
#@login_required
def add_card_get():
    return render_template("add_card.html")


@app.route("/")
@app.route("/card/add", methods=["POST"])
#@login_required
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


@app.route("/card/edit/<int:card_id>", methods=["GET"])
#@login_required
def edit_card_get(card_id):

	cards = session.query(Card)
	cards = cards[card_id]

	return render_template("edit_card.html",
    	card=cards
	)

@app.route("/card/edit/<int:card>", methods=["POST"])
#@login_required
def edit_card_post(card):
	cards = session.query(Card)
	cards = cards[card]

	cards.name=request.form["name"]
	cards.image_link=request.form["image_link"]
	cards.link=request.form["link"]
	cards.weather=request.form["weather"]
	cards.cost=request.form["cost"]
	cards.num_people=request.form["num_people"]

    #session.merge(post)
	session.commit()
	return redirect(url_for("cards"))

@app.route("/")
@app.route("/concierge", methods=["GET"])
def concierge_get():

	return render_template("concierge.html")


@app.route("/")
@app.route("/concierge", methods=["POST"])
def concierge_post():
	card = Card(
		name = request.form["name"],
		link = request.form["link"],
		image_link = request.form["image_link"],
		weather = request.form["weather"],
		cost = request.form["cost"],
		num_people = request.form["num_people"],
	)
	for card in session.query(Card).filter(Card.weather == weather):
           print(card.id)



	return redirect(url_for("card/<int:card>"))


