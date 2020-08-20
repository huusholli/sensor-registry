from flask import g
from flask import current_app

from tinydb import TinyDB

def get_db():
  if 'db' not in g:
    g.db = TinyDB(current_app.config['DATABASE'])

  return g.db
