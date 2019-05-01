if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
if rval:
  print("OK")
else:
  print("FAILED")
