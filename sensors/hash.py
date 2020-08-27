from datetime import datetime
from hashids import Hashids
from random import randint

def create_hash():
  timestamp = int(datetime.now().timestamp())
  return Hashids(str(randint(1, 1000))).encode(timestamp)
