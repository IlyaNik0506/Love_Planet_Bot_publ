import time
import threading
import traceback

from driver import init_driver
from gui_frames import LogFrame
from replies import reply_to_messages
from selection import education_check, love_pass


def main(login: str, password: str, likes: str,
         logger: LogFrame, stop: threading.Event, simp_link):
    """ Главная функция бота.  """
    try:
        driver = init_driver(login, password, logger, simp_link)
        like_limit = int(likes)
        reply_pin = 5
        logger.print_to_log(
            'Начитнаю проверку входящих сообщений и игру в симпатии...'
        )
        while not stop.is_set():
            if reply_pin == 0:
                reply_to_messages(driver, logger)
                reply_pin = 15
            if like_limit != 0:
                print('Проверяю анкету...')
                logger.print_to_log('Проверяю анкету...')
                education = education_check(driver, logger)
                love_pass(driver, logger, education)
                time.sleep(3)
            like_limit -= 1 if like_limit > 0 else 0
            reply_pin -= 1
            time.sleep(3)
        exit()
    except Exception as error:
        logger.print_to_log(error)
        traceback.print_exc()
