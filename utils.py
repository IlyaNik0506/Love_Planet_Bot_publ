import random
import time
from typing import List

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from gui_frames import LogFrame


def mutual_like_check(driver: WebDriver, logger: LogFrame):
    '''Функция проверяет всплывающее окно взаимного лайка
    и отправляет привет'''
    pass


def bot_click(driver: WebDriver, logger: LogFrame, to_click: WebElement):
    '''Функция клика на элемент с проверкой на всплывающее окно.'''
    pass

def bot_find_element(
        driver: WebDriver, logger: LogFrame, by_type, to_find,
        find_in: WebElement = None, many=False, ignore=False, time=10):
    '''
    Функция поиска элемента с проверкой на всплывающее окно.\n
    driver: WebDriver - элемент драйвера,\n
    logger: LogFrame - объект журнала событий,\n
    by_type - тип искомого эемента, e.g. By.ID, By.CLASS_NAME e.t.c.\n
    to_find - искомый элемент,\n
    find_in - элемент в котором нужно найти искомый(необезательный),\n
    many - True, если идет поиск нескольких элементов (по умолчанию: False),\n
    ignore - игнорировать, если элемент не найден (по умолчанию: False)
    time - время на поиск (по умолчанию: 10)
    '''
    pass


def get_phone(driver: WebDriver, logger: LogFrame,
              messages: List[WebElement]):
    '''
    Получения телефона из сообщений.
    '''
    pass


def get_chat(driver: WebDriver, logger: LogFrame,
             messages: List[WebElement], name: str) -> str:
    '''
    Функция подгатавливающая текст переписки и телефон для сохранения.
    '''
    pass


def is_in_file(path: str, to_find: str, str_args: list) -> int:
    '''
    Проверяет наличие строки с задаными аргументами в файле.\n
    path: str - путь к файлу\n
    to_find: str - строка для поиска\n
    str_args: list - список аргументов содержащихся в строке\n
    '''
    pass


def collect_data(driver: WebDriver, chat: List[WebElement]) -> list:
    '''Функция сбора информации о пользователе с которым ведется переписка.\n
        Возвращает список:\n
        [имя: str, возвраст: int, регион: str, ссылка: str,
        телефон = None, переписка = None]'''
    pass


def click_rand_contact(driver: WebDriver, logger: LogFrame):
    '''
    Функция сбрасывает контакт от которого читала новые сообщения,
    выбирая в списке всех контактов либо первый, где нет симпатии, либо,
    если такого нет, случайный.
    '''
    pass


def refresh_click(driver: WebDriver, logger: LogFrame, btn_to_click: int):
    """ Осуществляет клик по кнопке с переданным индексом в меню чата. """
    pass


def click_to_new_messages(driver: WebDriver, logger: LogFrame):
    """ Обновляет блок новых сообщений через переход в другой блок
        и возврат в новые сообщения.
    """
    pass

def name_for_message(driver: WebDriver, logger: LogFrame):
    """ Извлекает имя контакта. """
    pass


def rand_message(msg_file: str):
    """ Получение случайной строки из текстового файла. """
    pass
