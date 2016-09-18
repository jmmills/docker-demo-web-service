import hug

from platform import node
from datetime import datetime

START_TIME = datetime.utcnow()

VERSION = None

try:
  with open('VERSION', 'r') as version:
    VERSION = version.read().strip()
except FileNotFoundError:
  VERSION = 'bleed'

@hug.get()
def health(request):
  uptime = datetime.utcnow() - START_TIME
  return {
      'node': node(),
      'up_since': START_TIME.isoformat(),
      'running_for': uptime.total_seconds(),
      'uptime': str(uptime),
      'access_route' : request.access_route,
      'version': VERSION
      }

