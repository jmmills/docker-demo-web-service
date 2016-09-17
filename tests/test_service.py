import hug
import jmmills.service
import unittest

class TestService(unittest.TestCase):

  def test_root(self):
    resp = hug.test.get(jmmills.service, '/')
    assert resp.status == '404 Not Found'
    assert isinstance(resp.data['documentation']['handlers']['/health'], dict)

  def test_health(self):
    resp = hug.test.get(jmmills.service, '/health')
    assert resp.status == '200 OK'
    
    for k in ['uptime' ,'up_since', 'node', 'running_for']:
      assert k in resp.data
