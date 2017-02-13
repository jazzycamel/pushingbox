import os
import PushingBox

class TestClass:
	def test_one(self):
		p=PushingBox.PushingBox()
		devid=os.environ['PB_TEST_DEV1']
		assert p.push(devid)==True

	def test_two(self):
		p=PushingBox.PushingBox()
		devid="v0123456789ABCDE"
		assert p.push(devid)==False

	def test_three(self):
		p=PushingBox.PushingBox()
		assert p.endpoint=="http://api.pushingbox.com/pushingbox"

	def test_four(self):
		p=PushingBox.PushingBox()
		p.endpoint="http://test.url/api"
		assert p.endpoint=="http://test.url/api"