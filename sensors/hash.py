from datetime import datetime
from hashids import Hashids
from random import randint

def create_hash():
  timestamp = int(datetime.now().timestamp())
  return Hashids(randint(0, 1000)).encode(timestamp)
