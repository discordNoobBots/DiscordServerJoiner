import time

import os

from apis.scaffold import challenge

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("debuggerAddress","localhost:8989")

s = Service('./chromedriver')
browser = webdriver.Chrome(service=s,options=options)

#----------------------------------------------------------------

def dmVerificationCheck(browser):
    #check for double counter or alt dfiner in dms
    word1 = "Double Counter"
    word2 = "AltDentifier"

    browser.get("https://discord.com/channels/@me")
    time.sleep(2)
    logo = True
    while logo == True:
        try:
            browser.find_element(By.CSS_SELECTOR,".ready-3BZNWT")
        except:
            logo = False
    time.sleep(2)
    try:
        directMessages = browser.find_elements(By.CLASS_NAME,"link-39sEB3")
        latest = directMessages[1]
        latestText = latest.text
        print(latestText)
        latest.click()     
    except:
        print("Error Finding Latest Dm")


    if word2 in latestText:

        linksToVerify = browser.find_elements(By.XPATH,'//div[@class="grid-1aWVsE"]//a[@class="anchor-1MIwyf anchorUnderlineOnHover-2qPutX embedTitleLink-1QbYA- embedLink-1TLNja embedTitle-2n1pEb"]')
        linkIndex = len(linksToVerify) - 1
        if linkIndex > -1:
            link = linksToVerify[linkIndex].get_attribute("href")
            firstwindow = browser.window_handles[0]
            linksToVerify[linkIndex].click()
            print("Clicked Verification")
            time.sleep(4)
            secondwindow = browser.window_handles[1]
            browser.switch_to.window(secondwindow)
            browser.close()
            browser.switch_to.window(firstwindow)

    elif word1 in latestText:

        linksToVerify = browser.find_element(By.XPATH,"//a[normalize-space()='Click me to verify!']")

        firstwindow = browser.window_handles[0]
        linksToVerify.click()
        print("Clicked Verification")
        time.sleep(8)
        secondwindow = browser.window_handles[1]
        browser.switch_to.window(secondwindow)
        browser.close()
        browser.switch_to.window(firstwindow)
    return browser


################################################################
def checkMembers():
    time.sleep(5)
    membersCountCond = ""
    try:
        element = browser.find_element(By.CSS_SELECTOR, "div[class='pill-qMtBTq'] span[class='defaultColor-24IHKz text-sm-normal-3Zj3Iv pillMessage-3pHz6R']")
        temp = element.text
        membersCountList = temp.split(" ")
        membersCount = membersCountList[0]
        membersCount = int(membersCount)

        if membersCount > 250:
            membersCountCond = "High"
        else:
            membersCountCond = "Low"
    except:
        try:
            for handle in browser.window_handles:
                captcha = handle
            browser.switch_to.window(captcha)
            element = browser.find_element(By.XPATH, "//iframe[contains(@title,'checkbox')]")
            membersCountCond = "High"
        except:
            successurl = browser.current_url
            successWord = "https://discord.com/channels/"
            if successWord in successurl:
                membersCountCond = "High"
            else:
                try:
                    element = browser.find_element(By.XPATH, "//button[@type='button']")
                    buttonNameCon = element.text
                    #check if button name is accept invite, then only click it
                    if buttonNameCon == "Continue to Discord":
                        membersCountCond = "Low"
                except:
                    aa = "nothing"



    return membersCountCond
################################################################
#accept invite btn click function
def acceptInvtBtn():
    buttonName = ""
    BtnSuccess = False
    try:

        element = browser.find_element(By.XPATH, "//button[@type='button']")
        buttonName = element.text
        #check if button name is accept invite, then only click it
        if buttonName == "Accept Invite":
            browser.find_element(By.XPATH, "//button[@type='button']").click()
            time.sleep(3)

            #this condition is just for checking if button has been clicked or not
            try:
                element = browser.find_element(By.XPATH, "//button[@type='button']")
                buttonName = element.text
                if buttonName == "Accept Invite":
                    browser.find_element(By.XPATH, "//button[@type='button']")
            except:
                BtnSuccess = True
        else:
            BtnSuccess = True
    except:
        print("Accept Invite Error")

    return BtnSuccess

################################################################################################
def captchaSolver():
    captchaSuccess = False
    SucessOrNot = False
    try:
        for handle in browser.window_handles:
            captcha = handle
        browser.switch_to.window(captcha)
        element = browser.find_element(By.XPATH, "//iframe[contains(@title,'checkbox')]")
        #calling runner from hcaptcha main folder by passing our browser.
        while SucessOrNot == False:
            SucessOrNot = challenge.runner(browser)
        time.sleep(3)
        #again search for captcha button
        try:
            element = browser.find_element(By.XPATH, "//iframe[contains(@title,'checkbox')]")
        except:
            captchaSuccess = True
    except:
        captchaSuccess = True
    return captchaSuccess
################################################################################################
infile = "1.txt"

with open(infile, encoding="utf-8") as fin:
    count = 0
    for line in fin:
        if line != "\n":
            count += 1

            link = line
            browser.get(link)
            time.sleep(5)

            checkMembTemp = ""
            #the loop should meet 2 conditions, 1 = accept invite, 2 = captcha solution. if none found then both will be true.
            finalCond = False
            
            while finalCond == False:

                inviteAcceptionProcess = [False,False,False]
                SkipConds = False
                checkMembersCond = checkMembers()

                checkMembTemp = checkMembersCond

                if checkMembersCond == "High":
                    inviteAcceptionProcess[2] = True
                
                elif checkMembersCond == "Low":
                    with open("LowMembers.txt", "a+", encoding="utf-8") as file_object:
                        file_object.seek(0)
                        data = file_object.read(100)
                        if len(data) > 0 :
                            file_object.write("\n")
                        print(count,line,"Low Members")
                        file_object.write(line)
                        print("Low Members Detected, Data Saved in LowMembers.txt!\n")
                        count = count - 1
                        #all conditions will be set to true this way. so nothing gets accept for this specific link with low members.
                        inviteAcceptionProcess[2] = True
                        SkipConds = True
                else:
                    print("Unknown Error")                
                if SkipConds == True:
                    #this directly skips the accept invite steps.
                    inviteAcceptionProcess[0] = True
                    inviteAcceptionProcess[1] = True
                else:
                    #calls accept invite function and start the process
                    time.sleep(5)
                    accpetInviteCond = acceptInvtBtn()
                    if accpetInviteCond == True:
                        inviteAcceptionProcess[0] = True
                        print("Moved Next Page")
                    time.sleep(5)
                    #calls captcha solver function
                    captchaSolverCond = captchaSolver()
                    if captchaSolverCond == True:
                        inviteAcceptionProcess[1] = True
                        print("")

                if (inviteAcceptionProcess[0] == True) and (inviteAcceptionProcess[1] == True) and (inviteAcceptionProcess[2] == True):
                    finalCond = True
        
            print("wait time 70 seconds")
            if checkMembTemp == "High":
                print(count,link, "[SUCCESS] [ABOVE 250 MEMBERS]")
                #Only way to skip that popup would u like to open discord in app? 
                firstwindow = browser.window_handles[0]
                browser.switch_to.new_window()
                secondwindow = browser.window_handles[1]

                browser.switch_to.window(firstwindow)
                browser.close()
                browser.switch_to.window(secondwindow)
                #closing and opening tabs to avoid cpu consumption. Browsers Sucks!
                try:
                    #Only way to skip that popup would u like to open discord in app? 
                    browser = dmVerificationCheck(browser)
                except:
                    print("Nothing")
            else:
                #Only way to skip that popup would u like to open discord in app? 
                firstwindow = browser.window_handles[0]
                browser.switch_to.new_window()
                secondwindow = browser.window_handles[1]

                browser.switch_to.window(firstwindow)
                browser.close()
                browser.switch_to.window(secondwindow)
                #closing and opening tabs to avoid cpu consumption. Browsers Sucks!

        # # if you want to add speicifc numbers from servers.txt
        if count == 100:
            print("Max Number servers reached")
            os._exit(0)
        time.sleep(60)

            # time.sleep(60)
