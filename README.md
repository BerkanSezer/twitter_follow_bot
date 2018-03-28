# TWITTER PYTHON AUTO FOLLOW BOT

## You Need:
  - Python3.6
  - Chrome Webdriver
  - Python Virtual Environment

## How to Run:
  - Install python3.6 and pip
  - Create a new Virtual Environment
  ```
  pyvenv ~/<PATH>/<TO>/venv
  ```
  - Enter the Virtual Environment;
  ```
  source venv/bin/activate
  ```
  - Install requirements use;
  ```
  pip3 install -r requirements.txt
  ```
  - And run;
  ```
  python3 twitter_bot.py <any_twitter_account> <follower_count_as_integer>
  ```

## How to Works:
  - It opens hidden browser window and try login with your account.
  - Your username and password just stay your computer. It send anywhere.
  - It follows Everyone

## Arguments
  - argv[1] = twitter page for follower find
  - argv[2] = follower number
