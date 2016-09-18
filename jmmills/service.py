import hug

from platform import node
from datetime import datetime

START_TIME = datetime.utcnow()

@hug.get()
def health(request):
  uptime = datetime.utcnow() - START_TIME
  return {
      'node': node(),
      'up_since': START_TIME.isoformat(),
      'running_for': uptime.total_seconds(),
      'uptime': str(uptime),
      'access_route' : request.access_route
      }

