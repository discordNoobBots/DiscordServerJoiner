# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:27
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import logging
import os
import sys
from typing import Optional

import undetected_chromedriver as uc
from loguru import logger
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager, ChromeType
from webdriver_manager.core.utils import get_browser_version_from_os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class ToolBox:
    """Portable Toolbox"""

    @staticmethod
    def init_log(**sink_path):
        """Initialize loguru log information"""
        event_logger_format = (
            "<g>{time:YYYY-MM-DD HH:mm:ss}</g> | "
            "<lvl>{level}</lvl> - "
            # "<c><u>{name}</u></c> | "
            "{message}"
        )
        logger.remove()
        logger.add(
            sink=sys.stdout,
            colorize=True,
            level="DEBUG",
            format=event_logger_format,
            diagnose=False,
        )
        if sink_path.get("error"):
            logger.add(
                sink=sink_path.get("error"),
                level="ERROR",
                rotation="1 week",
                encoding="utf8",
                diagnose=False,
            )
        if sink_path.get("runtime"):
            logger.add(
                sink=sink_path.get("runtime"),
                level="DEBUG",
                rotation="20 MB",
                retention="20 days",
                encoding="utf8",
                diagnose=False,
            )
        return logger


def get_challenge_ctx(silence: Optional[bool] = None, lang: Optional[str] = None):
    
    """
    Challenger drive for handling human-machine challenges

    :param silence: Control headless browser

    :param lang: Restrict the language of hCatpcha label.
    See https://github.com/QIN2DIM/hcaptcha-challenger/issues/13

    :return:
    """

    s = Service('C:\\Users\\ROG\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe')
    
    # Control headless browser
    silence = True if silence is None or "linux" in sys.platform else silence

    # - Restrict browser startup parameters
    options = uc.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("debuggerAddress","localhost:8989")

    # - Restrict the language of hCaptcha label
    # - Environment variables are valid only in the current process
    # and do not affect other processes in the operating system
    os.environ["LANGUAGE"] = "en" if lang is None else lang
    options.add_argument(f"--lang={os.getenv('LANGUAGE')}")

    if silence is True:
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")

    # - Use chromedriver cache to improve application startup speed
    # - Requirement: undetected-chromedriver >= 3.1.5.post2
    logging.getLogger("WDM").setLevel(logging.NOTSET)
    driver_executable_path = ChromeDriverManager().install()
    version_main = get_browser_version_from_os(ChromeType.GOOGLE).split(".")[0]





    logger.debug("🎮 Activate challenger context")
    try:
        return uc.Chrome(
            # options=options,
            # headless=silence,
            # # use_subprocess=True,
            # driver_executable_path=driver_executable_path,

            
            
            webdriver.Chrome(service=s,chrome_options=options)

        )
    except WebDriverException:
        return uc.Chrome(
            options=options,
            headless=silence,
            # use_subprocess=True,
            version_main=int(version_main) if version_main.isdigit() else None,
        )
