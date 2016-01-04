import PBOD as p
import cv2
import time
import Heatmap as hm

c = p.PBOD( 11, 547, 365, 1.130973, 0.8011061, [0, -11, 25])
image = cv2.imread("testlow.jpg")
m = hm.Heatmap(20, 3, 1.1)
print(m.hmap)
image = m.visualize(image, 50)

while 1==1:
    cv2.imshow("window", image)
    cv2.waitKey(1)
    time.sleep(0.04)

#windows = c.getWindows([4.0, 4.0, 4.0], image, 20)
"""
for (x, y, window) in windows:
    cv2.imshow("window2", window)
    #if window.shape[0] < 10 or window.shape[1] < 10:
        #continue

    clone = image.copy()
    cv2.rectangle(clone, (x, y), (x + window.shape[1], y + window.shape[0]), (0, 255, 0), 2)
    cv2.imshow("window", clone)
    cv2.waitKey(1)
    time.sleep(0.001) """
