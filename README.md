# instagram_automation
# Instagram Automated Messaging Bot

This project uses **Selenium** and **Python** to automate sending direct messages on Instagram. The bot allows you to log into an Instagram account and send messages to a predefined list of users. 

## Prerequisites

Before running the bot, you will need to have the following installed:

- Python 3.x
- `selenium` Python package
- `webdriver_manager` Python package

### Install dependencies

You can install the required Python libraries using `pip`:

```bash
pip install selenium
pip install webdriver_manager
Setup Instructions
Create a Bot Instance: You need to pass the following information to the Bot class:

username: Your Instagram username.
password: Your Instagram password.
audience: A list of Instagram usernames (the people you want to send messages to).
message: The message to be sent.
Running the Bot: After setting the username, password, audience, and message, the bot will:

Log into Instagram.
Send the specified message to each user in the audience.
Code Explanation
The bot is initialized by passing your Instagram login details, the list of users to message, and the message you want to send.


audience = ['propertyofmycodeblog']
message = "testing of a bot"
my_bot = Bot(username, password, audience, message)




1. Login Function:
The bot navigates to Instagram's login page and enters your username and password.
It waits for the page elements to load using Selenium's WebDriverWait and then logs in.
2. Sending Messages:
The bot navigates to each user's profile in the audience list.
It clicks the message button on their profile.
It then finds the message input box and sends the predefined message.


def send_messages(self):
    for user in self.audience:
        self.Bot.get(f'https://www.instagram.com/{user}/')
        # Wait for message button and click it
        message_button = WebDriverWait(self.Bot, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="..."]'))
        )
        message_button.click()
        # Send the message
        message_box.send_keys(self.message)
        message_box.send_keys(Keys.RETURN)
        time.sleep(2)


3. Driver Setup:
Selenium WebDriver: The bot uses the Chrome WebDriver, which is set up via webdriver_manager to automatically download the required ChromeDriver version.
python
Copy code

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)




4. Waiting for Elements:
The bot waits for elements to load before interacting with them. This is done using WebDriverWait and expected_conditions.



from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Configure the service to use ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

class Bot:
    def __init__(self, username, password, audience, message):
        self.username = username
        self.password = password
        self.audience = audience
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.Bot = driver
        self.login()

    def login(self):
        self.Bot.get(self.base_url)
        enter_username = WebDriverWait(self.Bot, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.Bot, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

    def send_messages(self):
        for user in self.audience:
            self.Bot.get(f'https://www.instagram.com/{user}/')
            time.sleep(3)
            message_button = WebDriverWait(self.Bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="..."]'))
            )
            message_button.click()
            time.sleep(2)
            message_box = WebDriverWait(self.Bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="..."]'))
            )
            message_box.send_keys(self.message)
            message_box.send_keys(Keys.RETURN)
            time.sleep(2)

audience = ['propertyofmycodeblog']
message = "testing of a bot"
my_bot = Bot(username, password, audience, message)
my_bot.send_messages()


