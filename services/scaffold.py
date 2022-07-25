# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:25
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from typing import Optional

from apis.scaffold import install, challenge
from services.settings import HCAPTCHA_DEMO_SITES, _SITE_KEYS, _HCAPTCHA_DEMO_API


class Scaffold:
    """System scaffolding Top-level interface commands"""

    challenge_language = "en"

    def __init__(self, lang: Optional[str] = None):
        if lang is not None:
            Scaffold.challenge_language = lang

    @staticmethod
    def install(model: Optional[str] = None):
        """Download Project Dependencies"""
        install.run(model=model)
    
    @staticmethod
    def demo(
        silence: Optional[bool] = False, model: Optional[str] = None, target: Optional[str] = None
    ):
        """
        Dueling with hCAPTCHA challenge using YOLOv5.

        Usage: python main.py demo
        ___________________________________________________
        or: python main.py demo --model=yolov5n6     |
        or: python main.py demo --target=discord     |
        or: python main.py demo --lang=en            |
        ---------------------------------------------------
        :param silence: Default False. Whether to silence the browser window.
        :param model: Default "yolov5s6". within [yolov5n6 yolov5s6 yolov5m6]
        :param target: Default None. Designate `Challenge Source`. See the global value SITE_KEYS.
        :return:
        """
        # if _SITE_KEYS.get(target):
        #     sample_site = _HCAPTCHA_DEMO_API.format(_SITE_KEYS[target])
        # else:
        #     sample_site = HCAPTCHA_DEMO_SITES[0]

        siteURL = input("Enter website Url: ")
        sample_site = siteURL


        challenge.runner(
            sample_site, lang=Scaffold.challenge_language, silence=silence, onnx_prefix=model
        )



    #this function was created for testing purpose until not needed anymote :D
    # @staticmethod
    # def dsu(
    #     silence: Optional[bool] = False, model: Optional[str] = None, target: Optional[str] = None
    # ):

    #     # siteURL = input("Enter website Url: ")
    #     # sample_site = siteURL
    #     # siteURL = input("Enter website Url: ")
    #     sample_site = "http://demos.codexworld.com/integrate-captcha-checkbox-with-hcaptcha-php/"        
    #     challenge.runner(
    #         sample_site, lang=Scaffold.challenge_language, silence=silence, onnx_prefix=model
    #     )


    @staticmethod
    def solver(browser):
        
        #i have no idea why its named ctx
        ctx = browser    
        challenge.runner(
            ctx, lang=Scaffold.challenge_language, silence=silence, onnx_prefix=model
        )
    