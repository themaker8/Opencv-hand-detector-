import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=3)


while (True):
    success, img = cap.read()
    hands, img = detector.findHands(img) 
    cv2.imshow('Image',img)
    cv2.waitKey(1)