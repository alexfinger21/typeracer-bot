from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
import random

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"
MIN_RACE_TEXT = 7
WPS = 700/60
CPS = WPS * 4.79
LOGIN_FLAG = 0
START_TEXT = "Go!" if LOGIN_FLAG else "The race is on!"

# Options
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
#chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=s, options=chrome_options)


def startRace():
    startElem = driver.find_element(By.TAG_NAME, "body")
    startElem.send_keys(Keys.CONTROL, Keys.ALT, "I")


def gameMode():
    gameView = driver.find_element(By.CLASS_NAME, "gameView")
    game_text = gameView.find_element(By.XPATH, "./*").text
    inp_box = gameView.find_element(By.CLASS_NAME, "txtInput")

    while "The race is about to start!" not in game_text:
        game_text = gameView.find_element(By.XPATH, "./*").text
        sleep(0.01)

    print(game_text)
    for txt in game_text.split('\n'):
        if len(txt.split(' ')) >= MIN_RACE_TEXT:
            game_text = txt
            break


    print("GAME TEXT", game_text)
    total_text = gameView.find_element(By.XPATH, "./*").text
    while (START_TEXT not in total_text):
        total_text = gameView.find_element(By.XPATH, "./*").text
        sleep(0.01)


    last_pair = None
    for c in game_text:
        tim = None
        if last_pair == None:
            tim = random.random() * 1/CPS * 2
            last_pair = tim
        else:
            tim = 1/CPS * 2 - last_pair
            last_pair = None
        sleep(tim)
        inp_box.send_keys(c)
        print(c)





driver.get("https://play.typeracer.com")
print(driver.title)
wait = input()
startRace()
wait = input()
gameMode()

while True:
    sleep(10)
