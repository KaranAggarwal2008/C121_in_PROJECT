import cv2
import time
import numpy as np
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)
time.sleep(2)
bg = 0
for i in range(60):
    ret, bg = cap.read()
bg = np.flip(bg, axis=1)
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    u_black=np.array([104,153,70])
    l_black=np.array([30,30,0])
    mask_1 = cv2.inRange(hsv, u_black, l_black)
    lower_black = np.array([170, 120, 70])
    upper_black = np.array([180, 255, 255])
    mask_2 = cv2.inRange(hsv, lower_black, upper_black)
    complete_mask = mask_1 + mask_2
    complete_masksk = cv2.morphologyEx(complete_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    complete_mask = cv2.morphologyEx(complete_mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    res_1 = cv2.bitwise_and(img, img, mask=mask_1)
    res_2 = cv2.bitwise_and(bg, bg, mask=mask_1)
    final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
    output_file.write(final_output)
    cv2.imshow("OUTPUT", final_output)
    cv2.waitKey(2)
cap.release()
out.release()
cv2.destroyAllWindows()