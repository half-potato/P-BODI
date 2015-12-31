import PBOD as p
import cv2
import time

c = p.PBOD( 11, 547, 365, 1.130973, 0.8011061, [0, -11, 25])
print(c.getDistanceAtHeight(365 - 266)) #15
print(c.getDistanceAtHeight(365 - 184)) #25
print(c.getDistanceAtHeight(365 - 227)) #19
print(c.getDistanceAtHeight(365)) #19

image = cv2.imread("testlow2.jpg")
windows = c.getWindows([4.0, 4.0, 4.0], image, 10)
for (x, y, window) in windows:
    cv2.imshow("window", image)
    if window.shape[0] < 10 or window.shape[1] < 10:
        continue

    clone = image.copy()
    cv2.rectangle(clone, (x, y), (x - window.shape[1], y - window.shape[0]), (0, 255, 0), 2)
    cv2.imshow("window", clone)
    cv2.waitKey(1)
    time.sleep(0.005)
