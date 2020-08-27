from datetime import datetime
from hashids import Hashids

def create_hash():
  timestamp = int(datetime.now().timestamp())
  return Hashids().encode(timestamp)
