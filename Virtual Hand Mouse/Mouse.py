import numpy as np
import cv2
import HandTrackingModule as htm
import time
import autopy

wCam , hCam = 640, 480
wScr , hScr = autopy.screen.size()
frameR = 100 # Frame Reduction
smoothening = 7
# print(wScr, hScr)

plocX, plocY = 0,0
clocX, clocY = 0,0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.HandDetector(maxHands=1)



pTime = 0
while True:

    success, img = cap.read()
    img = detector.findHand(img)
    lmList = detector.findPosition(img)
    # 2. Get the tip of the Index and the Middle Fingers
    if(len(lmList)!=0):
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, x2,y1,y2)
        # 3. Check if fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR,frameR),(wCam - frameR, hCam -frameR),(0,0,255),2)
        # 4. Only Index Finger : Moving Mode
        if fingers[1]== 1 and fingers[2]==0:
            # 5 : Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR,hCam-frameR),(0,hScr))
            # 6 Smoothen Values
            clocX = plocX + (x3 - plocX)/smoothening
            clocY = plocY + (y3 - plocY)/smoothening

            # 7 Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1,y1), 15, (255,0,255),cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 8. Both index and Middle finger are up: Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance b/w fingers
            lenght, img , lineInfo = detector.findDistance(8,12,img)
            # print(lenght)
            # 10. Click Mouse if Distance is Short
            if lenght <40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                autopy.mouse.click()



        # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 3)

    # 12 . Display
    cv2.imshow("image",img)
    if cv2.waitKey(1) ==27:
        break