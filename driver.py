import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from gui_frames import LogFrame
from settings import (browser_args, driver_path)
from utils import bot_find_element


def clean_login(driver: WebDriver, login, password) -> None:
    """ Осуществляет вход на сайт. """
    pass


def captcha_block(driver: WebDriver, logger: LogFrame, login) -> None:
    """ Проверяет наличие всплываюшего окна с капчей. """
    pass


def alt_login_block(driver: WebDriver, logger: LogFrame, login, password) -> None:
    """ Вход на сайт через всплывающее окно. """
    pass


def init_driver(login: str, password: str,
                logger: LogFrame, simp_link) -> WebDriver:
    """ Функция инициализация драйвера браузера и вход на сайт,
        через логин и пароль или cookies.
    """
    pass