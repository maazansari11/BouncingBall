import numpy as np
import cv2
k = 0

def bouncing():
    img = np.zeros((480,640,3),dtype='uint8')
    dx,dy =1,1
    x,y = 100,100
    while True:
        
        # Display the image
        cv2.imshow('BouncingBall',img)
        k = cv2.waitKey(10)
    
        img = np.zeros((480,640,3),dtype='uint8') # for black screen display
        # Increment the position
        x = x+dx
        y = y+dy
        cv2.circle(img,(x,y),20,(100,255,0),-1)
##        if k != -1:
##            break
        # Change the sign of increment on collide with the boundary
        if y >=480:
            dy *= -1
        elif y<=0:
            dy *= -1
        if x >=640:
            dx *= -1
        elif x<=0:
            dx *= -1
    cv2.destroyAllWindows()


import cv2
import numpy as np

while True:
  
    bouncing()
    if k == 72:
        exit()

    cv2.destroyAllWindows()




