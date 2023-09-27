import time
import pyautogui as pg
time.sleep(2)

"""
current resolution of my system:
1920x1080
"""


"""
Constants
# x.downvote-x.upvote=1
# y.downvote-y.upvote=64
# y.pressed_downvote-y.upvote=64
#y.add-y.upvote=7
"""

X_VOTE_DIFF = 1
Y_VOTE_DIFF = 64
Y_ADD_DIFF = 7


def moveToImg(img):
    """
    function that makes the cursor to move to the center 
    of an image
    takes a pyautogui box variable as a parameter
    """
    if (img):

        x, y, width, height = img
        # center the coordinates
        x += width//2
        y += height//2
        # move to chosen image during 1 second
        pg.moveTo(x, y, 1)
    return False


def menu():

    #the viewer will chose how many scrolldowns(iterations) will be ecevuted
    iterations=int(pg.prompt("Choose number of scrolldowns: "))
    time.sleep(1.5)
    """
    function that runs the script\n
    """
    i = 0

    while (i < iterations):

        # get the add image and upvote image
        upvoteImg = pg.locateOnScreen(
            "useful_images/reddit_upvote.png", confidence=0.7)
        addImg = pg.locateOnScreen(
            "useful_images/reddit_add.png", confidence=0.8)

        if (addImg):
            # what is needed from this unpacking is just the y coordinate of the images
            xUpvote, yUpvote, height, width = upvoteImg
            xAdd, yAdd, height, width = addImg

            # test if the current post is an add
            if yAdd-yUpvote in range(Y_ADD_DIFF-1, Y_ADD_DIFF+2):
                downvoteImg = pg.locateOnScreen(
                    "useful_images/reddit_downvote.png", confidence=0.9)
                xDownvote, yDownvote, height, width = downvoteImg
                if downvoteImg and yDownvote-yUpvote in range(Y_VOTE_DIFF-1, Y_VOTE_DIFF+2):
                    """
                    the downvote button will be pressed when there is an add on the screen and
                    when the selected upvote button is the pair of the selected downvote button
                    """
                    moveToImg(downvoteImg)
                    pg.click()
            elif upvoteImg:
                # when there is an add, but not on the current post the upvote button will be clicked
                moveToImg(upvoteImg)
                pg.click()
        elif upvoteImg:
            # when there is no add the upvote button will be clicked
            moveToImg(upvoteImg)
            pg.click()

        pg.scroll(-500)
        time.sleep(1)
        i += 1


menu()
