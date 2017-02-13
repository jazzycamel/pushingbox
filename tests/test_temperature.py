import os
import PushingBox

class TestClass:
	def test_one(self):
		p=PushingBox.PushingBox()
		devid=os.environ['PB_TEST_DEV2']
		assert p.push(devid, room="office", temperature="25.1")==True