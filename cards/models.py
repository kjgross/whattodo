import datetime

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base, engine


class Card(Base):
	__tablename__ = "cards1"
	id = Column(Integer, Sequence('card_id_sequence'), primary_key = True)
	name = Column(String(1024))
	link = Column(String(1024))
	image_link = Column(String(1024))
	weather = Column(String(128))
	cost = Column(String(128))
	num_people = Column(String(128))
	date_time = Column(DateTime, default=datetime.datetime.now)


	def as_dictionary(self):
		card = {
			"id": self.id,
			"name": self.name,
			"link": self.link,
			"image_link": self.image_link,
			"weather": self.weather,
			"cost": self.cost,
			"num_people": self.num_people,
			"date_time": self.datetime
		}
		return card

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, Sequence('user_id_sequence'), primary_key = True)
	first_name = Column(String(1024))
	email = Column(String(1024))
	password = Column(String(1024))

	def as_dictionary(self):
		user = {
			"id": self.id,
			"first_name": self.first_name,
			"email": self.email,
		}
		return user

Base.metadata.create_all(engine)


