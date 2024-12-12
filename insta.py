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
        # initializing the username
        self.username = username
         
        # initializing the password
        self.password = password
         
        # passing the list of users or initializing
        self.audience = audience
         
        # passing the message or initializing
        self.message = message
         
        # initializing the base url
        self.base_url = 'https://www.instagram.com/'
         
        # here it calls the driver to open chrome web browser
        self.Bot = driver
         
        # initializing the login function we will create
        self.login()
        
    def login(self):
        self.Bot.get(self.base_url)
        
        # entering the username for login into Instagram 
        enter_username = WebDriverWait(self.Bot, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        enter_username.send_keys(self.username)
        
        # entering the password for login into Instagram
        enter_password = WebDriverWait(self.Bot, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        enter_password.send_keys(self.password)
        
        # returning the password and login into account 
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
    
    # Function to send messages
    def send_messages(self):
        for user in self.audience:
            self.Bot.get(f'https://www.instagram.com/{user}/')
            time.sleep(3)
            
            # Click the message button on user's profile
            message_button = WebDriverWait(self.Bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_gq"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div[2]/div'))
            )
            message_button.click()
            time.sleep(2)
            
            # Find the message input box
            message_box = WebDriverWait(self.Bot, 20).until(
                 EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_ZZ"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div'))
            )
            message_button.click()
            time.sleep(2)
            
            
            message_box.send_keys(self.message)
            message_box.send_keys(Keys.RETURN)
            time.sleep(2)

# Replace these with your Instagram username and password
username = 'chocolatebtrfly'
password = '7@qb74mK'

audience = ['propertyofmycodeblog']
message = "testing of a bot"

# Create an instance of the Bot class and log in
my_bot = Bot(username, password, audience, message)

# Call the method to send messages
my_bot.send_messages()
