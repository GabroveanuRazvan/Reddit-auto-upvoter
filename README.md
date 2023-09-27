## __Table of contents__
  - Description
  - Usage
  - Gallery
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

  - The searching is based on recognising certain png images that are saved in ![](useful_images)
