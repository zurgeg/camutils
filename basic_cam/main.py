import bootloader
if __name__ == "__main__":
    while bootloader.rval:
        cv2.imshow("feed", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    vc.release()
    cv2.destroyWindow("feed")
else:
  print("There was an error.")
