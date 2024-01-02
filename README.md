# TypingBots
Creating typing bots for major typing websites

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

- This repository has code for typing bots to most major typing websites such as:
    - MonkeyType
    - 10FastFingers

## How to use this repository?
1. Clone this repository:
    - Go to your terminal / Command prompt and type
        ```shell
        git clone https://github.com/adwii-iii/TypingBots.git
        ```
    - Change directory into the cloned folder using:
        ```shell
        cd TypingBots
        ```
    - Open the folder in your favorite code editor, for opening it in VS Code, use:
        ```shell
        code .
        ```

2. Install dependancies
    - Open a new terminal and install the required dependancies using:
        ```python
        pip install -r requirements.txt
        ```

3. After all the above steps all you need to do is run the required python script
    - For MonkeyType, run the autoTypeMT.py
    - For 10FastFingers run the autoType10FF.py

## Things to keep in mind
### For MonkeyType
- If you want to add the test results to your account in MonkeyType, manually login while keeping the pythonGUI window open, then follow the instructions given by the GUI after you login

- For MonkeyType, if you want to make sure that the test is not flagged as a bot, try running it with an interval of 0.06/0.07

### For 10FastFingers
- Nothing in particular

## What does the tests.py do?
- Nothing really, It was just there for basic testing to check where the python files were going wrong, it's pretty much obsolete now, you can still run it using:
    ```python
    pytest tests.py
    ```
    or
    ```python
    python -m pytest tests.py
    ```
- However it shpuld fail both the tests, as it was just meant to be there to troubleshoot what was going wrong with the code during the development, the code however is perfectly working (As long as the CI passes, it means it still hasn't broken)