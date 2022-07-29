import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress","localhost:8989")
s = Service('./chromedriver')
browser = webdriver.Chrome(service=s,options=options)
print("")

try:
    inboxmsgs = browser.find_elements(By.CLASS_NAME, "wrapper-3kah-n")
    
    indexNum = 0
    while indexNum < len(inboxmsgs):
        channelId = inboxmsgs[indexNum].get_attribute("data-list-item-id")
        channelId = channelId.replace("guildsnav___","")
        if channelId != "home":
            channelName = inboxmsgs[indexNum].get_attribute('aria-label')
            channelName = channelName.strip()
            print(indexNum,channelId+":"+channelName)
            # print(channelId)

        indexNum+=1


    
except:
    aa = "inbox button not found"
    print(aa)


