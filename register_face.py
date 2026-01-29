import cv2
import os

name = input("Enter your name: ")

path = "dataset/" + name
os.makedirs(path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Register Face", frame)

    if cv2.waitKey(1) == ord('s'):
        count += 1
        cv2.imwrite(f"{path}/{count}.jpg", gray)
        print("Saved image", count)

    if count == 20:
        break

cap.release()
cv2.destroyAllWindows()
print("Face registration complete")
