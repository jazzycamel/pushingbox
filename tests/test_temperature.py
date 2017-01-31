from context import PushingBox

if __name__=="__main__":
    p=PushingBox.PushingBox()
    devid=input("Enter a valid PushingBox DevID to test: ")
    p.push(devid, room="Office", temperature="25.1")
