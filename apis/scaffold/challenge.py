# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:25
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import time
from typing import Optional

from selenium.common.exceptions import WebDriverException

from services.hcaptcha_challenger import ArmorCaptcha, ArmorUtils
from services.hcaptcha_challenger.exceptions import ChallengePassed
from services.settings import logger, HCAPTCHA_DEMO_SITES, DIR_MODEL, DIR_CHALLENGE
from services.utils import get_challenge_ctx

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


@logger.catch()
def runner(ctx):  
    print("language set to English")
    print("language can be changed to some other in apis>>scaffold>>challenge.py --> line 34")
    print("")
    lang: Optional[str] = "en"
    silence: Optional[bool] = False
    onnx_prefix: Optional[str] = None
    """Human-Machine Challenge Demonstration | Top Interface"""
    # Instantiating Challenger Components
    challenger = ArmorCaptcha(dir_workspace=DIR_CHALLENGE, lang=lang, debug=True)
    challenger_utils = ArmorUtils()

    # Instantiating the Challenger Drive
    
    # ctx = get_challenge_ctx(silence=silence, lang=lang)
    # opt=Options()
    # opt.add_experimental_option("debuggerAddress","localhost:8989")
    # s = Service('C:\\Users\\ROG\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe')
    # ctx = webdriver.Chrome(service=s,chrome_options=opt)

    try:
        for i in range(1):
            SucessOrNot = False
        
            try:
                # Read the hCaptcha challenge test site
                # ctx.get(sample_site)
                # ctx.current_url
                # print(ctx.current_url)

                
                # Detects if a clickable `hcaptcha checkbox` appears on the current page.
                # The `sample site` must pop up the `checkbox`, where the flexible wait time defaults to 5s.
                # If the `checkbox` does not load in 5s, your network is in a bad state.


                if not challenger_utils.face_the_checkbox(ctx):
                    break

                start = time.time()

                # Enter iframe-checkbox --> Process hcaptcha checkbox --> Exit iframe-checkbox
                challenger.anti_checkbox(ctx)

                # Enter iframe-content --> process hcaptcha challenge --> exit iframe-content
                resp = challenger.anti_hcaptcha(ctx, dir_model=DIR_MODEL, onnx_prefix=onnx_prefix)
                if resp == challenger.CHALLENGE_SUCCESS:
                    challenger.log(f"End - total: {round(time.time() - start, 2)}s")
                    logger.success(f"PASS[{i + 1}|5]".center(28, "="))
                    SucessOrNot = True
                elif resp == challenger.CHALLENGE_RETRY:
                    SucessOrNot = False
                    logger.error(f"RETRY[{i + 1}|5]".center(28, "="))

            # Do not capture the `ChallengeReset` signal in the outermost layer.
            # In the demo project, we wanted the human challenge to pop up, not pass after processing the checkbox.
            # So when this happens, we reload the page to activate hcaptcha repeatedly.
            # But in your project, if you've passed the challenge by just handling the checkbox,
            # there's no need to refresh the page!
            except ChallengePassed:
                ctx.refresh()
                logger.success(f"PASS[{i + 1}]".center(28, "="))
            except WebDriverException as err:
                logger.exception(err)
    finally:
        print("*******************[Finally Statement Reached]*******************")
        try:
            successurl1 = ctx.current_url
            successWord1 = "https://discord.com/channels/"

            element = ctx.find_element(By.XPATH, "//button[@type='button']")
            buttonName = element.text
            if buttonName == "Accept Invite":
                ctx.find_element(By.XPATH, "//button[@type='button']").click() 
                
            #check if url starts with discord.com/channels or not           
            elif successWord1 in successurl1:
                SucessOrNot = True
        except:
            successurl = ctx.current_url
            successWord = "https://discord.com/channels/"
            if successWord in successurl:
                SucessOrNot = True
                    
        print("This used to be exit but has been commented for this project purpose")
        print("This can be found in challenge.py > line 93")
        print("")
        time.sleep(5)
        # temp = input("enter to exit")
        # ctx.quit()
    
    return SucessOrNot


@logger.catch()
def test():
    """Check if the Challenger driver version is compatible"""
    ctx = get_challenge_ctx(silence=True)
    try:
        ctx.get(HCAPTCHA_DEMO_SITES[0])
    finally:
        temp = input("enter to exit")
        ctx.quit()

    logger.success("The adaptation is successful")
