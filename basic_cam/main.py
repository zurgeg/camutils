import bootloader
if __name__ == "__main__":
    while rval:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("preview", frame)
        cv2.imshow("preview gray", gray)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    vc.release()
    cv2.destroyWindow("preview gray")
    cv2.destroyWindow("preview")
else:
  print("There was an error.")
