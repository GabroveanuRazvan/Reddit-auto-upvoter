## __Table of contents__
  - [Description](#description)
  - [Usage](#usage)
  - [Gallery](#gallery)
# __Description__
  Made in Python 3.11.2 using VSCode.

  The project is short and simple. It automates upvoting the posts and downvoting the adds on Reddit using pyautogui.

# __Usage__
  - the python code is made using pyautogui module. The module is not a part of python standard modules, thus it requires instalattion.
  - 
    - Windows:
    ```
    pip install pyautogui
    ```
    - macOS and Linux:
    ```
    pip3 install pyautogui
    ```
    
  - There is a 2 second delay after running the code so that the user will have time to open up Reddit. After the delay there will be a prompt message that asks for the number of scrolldowns.
  After this the program will start looking for upvotes/downvotes.
  - The searching is based on recognising certain .png images that are saved in the directory [useful_images](https://github.com/GabroveanuRazvan/Reddit-auto-upvoter/tree/main/useful_images).
  - __!Important__ Since the script relies on finding certain patterns based on some screenshots images, using this code on diffrent resolution might not work properly. My resolution is __1920x1080__.
  - __!Important__  Pyautogui has a failsafe set by default. Moving the cursor in any of the 4 corners of the main monitor will forcibly stop the program. More details [here](https://pyautogui.readthedocs.io/en/latest/index.html?highlight=failsafe).

# __Gallery__

[reddit_pyautogui_demo.webm](https://github.com/GabroveanuRazvan/Reddit-auto-upvoter/assets/126866447/c7cb390a-5014-4043-be7e-34cd29513ed8)

