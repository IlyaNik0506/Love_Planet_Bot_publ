import os
import time
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from db import add_update_simp
from gui_frames import LogFrame
from utils import (bot_find_element, click_rand_contact, click_to_new_messages,
                   collect_data, rand_message, get_chat,
                   is_in_file, bot_click)


def send_message(driver: WebDriver, logger: LogFrame, message: str):
    '''Функция отправки сообщений в чате.'''
    pass


def check_my_last_message(
        driver: WebDriver, logger: LogFrame,
        messages: List[WebElement], contact_info: list
        ):
    '''
    Функция в зависимости от найденого сообщения от бота определяет фазу
    общения (0 - бот сообщений не отправлял; 1 - бот отправил первое сообщение;
    3 - бот отправил последние сообщение или по взаимной симпатии) и возвращает
    её порядковый номер.\n
    \tmessages: List[WebElement] - переписка с пользователем\n
    \tcontact_info: list - список с информацией о том с кем ведется общение\n
    [имя, возвраст, регион, ссылка, телефон, переписка]\n
    В случае, если фаза "3", то помимо  возврата номера фазы, дополняет
    contact_info номером телефона и историей переписки.
    '''
    pass


def phase_action(driver: WebDriver, logger: LogFrame, phase: int,
                 contact_info: list):
    '''Выполняет  действия в зависимости от фазы взаимодействия с симпатией'''
    pass


def reply_to_messages(driver: WebDriver, logger: LogFrame):
    '''Функция ответа на новые сообщения'''
    pass