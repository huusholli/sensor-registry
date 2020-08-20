from flask import Blueprint

api = Blueprint('health_actions', __name__)

@api.route('/health')
def health():
  return 'OK'
