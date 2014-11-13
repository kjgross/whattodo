import unittest
import os
import json
from urlparse import urlparse

# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "cards.config.TestingConfig"

from cards import app
from cards import models
from cards.database import Base, engine, session