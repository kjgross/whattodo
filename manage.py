import os
from cards import app, database
from flask.ext.script import Manager

from cards.models import Card, User
from cards.database import session, Base

manager = Manager(app)

@manager.command
def seed():
	name = "Picnic in a park"
	link = "https://google.com"
	image_link = "http://sallysbakingaddiction.com/wp-content/uploads/2013/03/Easy-Homemade-Funfetti-Cake.-Get-the-recipe-at-sallysbakingaddiction.com-2.jpg"
	weather = "outside"
	cost = "free"
	num_people = "group"

	for i in range(20):
		card = Card(
			name=name,
			link=link,
			image_link=image_link,
			weather=weather,
			cost=cost,
			num_people=num_people
		)
		session.add(card)
	session.commit()



@manager.command
def run():
	port = int(os.environ.get('PORT', 8080))
	app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
	manager.run()



