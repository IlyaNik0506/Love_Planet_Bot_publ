from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from gui_frames import LogFrame
from utils import bot_find_element, bot_click


def education_check(driver: WebDriver, logger: LogFrame) -> int:
    '''Функция проверки наличия высшего образования.
    В случае если его нет или не указано.'''
    pass


def love_pass(driver: WebDriver, logger: LogFrame, education: int):
    '''Функция, которая на основе параметров ставит кандидату лайк или
    дизлайк, пока на  основе наличия высшего образования'''
    pass
