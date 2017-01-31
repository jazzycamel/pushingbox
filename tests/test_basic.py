import logging
from context import PushingBox

FORMAT="%(name)s.%(module)s %(levelname)s: %(message)s"
logging.basicConfig(format=FORMAT)

if __name__=="__main__":
    p=PushingBox.PushingBox()
    devid=input("Enter a valid PushingBox DevID to test: ")
    p.push(devid)
