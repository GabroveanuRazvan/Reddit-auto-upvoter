import time
import pyautogui as pg
import keyboard
time.sleep(2)

"""
Constants
# x.downvote-x.upvote=1
# y.downvote-y.upvote=64
# y.pressed_downvote-y.upvote=64
#y.add-y.upvote=7
"""

X_VOTE_DIFF=1
Y_VOTE_DIFF=64
Y_ADD_DIFF=7

def moveToImg(img):
    if(img):
        
        x,y,width,height=img
        #center the coordinates
        x+=width//2
        y+=height//2
        #move to chosen image during 1 second
        pg.moveTo(x,y,1)
    return False

def menu(iterations):

    i=0

    while(i<iterations):

        #get the add image and upvote image
        upvoteImg=pg.locateOnScreen("useful_images/reddit_upvote.png",confidence=0.7)
        addImg=pg.locateOnScreen("useful_images/reddit_add.png",confidence=0.8)

        if(addImg):
            #what is needed from this unpacking is just the y coordinate of the images
            xUpvote,yUpvote,height,width=upvoteImg
            xAdd,yAdd,height,width=addImg

            
            #test if the current post is an add
            if yAdd-yUpvote in range(Y_ADD_DIFF-1,Y_ADD_DIFF+2):
                downvoteImg=pg.locateOnScreen("useful_images/reddit_downvote.png",confidence=0.9)
                xDownvote,yDownvote,height,width=downvoteImg
                if downvoteImg and yDownvote-yUpvote in range(Y_VOTE_DIFF-1,Y_VOTE_DIFF+2):
                    moveToImg(downvoteImg)
                    pg.click()
            elif upvoteImg:
                
                moveToImg(upvoteImg)
                pg.click()
        elif upvoteImg:
            moveToImg(upvoteImg)
            pg.click()

        


        pg.scroll(-500)
        time.sleep(1)
        i+=1

menu(2)
# upvoteImg=pg.locateOnScreen("reddit_upvote.png",confidence=0.7)
# moveToImg(upvoteImg)
# time.sleep(1)
# promoted=pg.locateOnScreen("reddit_add.png",confidence=0.8)
# moveToImg(promoted)
# print(upvoteImg,promoted)

