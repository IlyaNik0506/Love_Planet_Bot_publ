import os

from customtkinter import CTk

from gui_frames import (BotControlFrame, BotSettingsFrame, LogFrame,
                        UserDataFrame)
from main import main


class LoveBot(CTk):
    """ Главное окно графического интерфейса бота. """
    def __init__(self):
        super().__init__()

        self.title('Loveplanet_bot')
        self.geometry('650x680')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        self.log_frame = LogFrame(self)
        self.log_frame.grid(row=3, column=0, padx=10,
                            pady=(5, 10), sticky='nswe')

        self.bot_control_frame = BotControlFrame(
            self, self.log_frame, self.get_settings, main
        )
        self.bot_control_frame.grid(row=1, column=0, padx=10,
                                    pady=(5, 5), sticky='nswe',)

        self.bot_settings_frame = BotSettingsFrame(self, self.log_frame)
        self.bot_settings_frame.grid(row=2, column=0, padx=10,
                                     pady=(5, 5), sticky='nswe',)

        self.userdata_frame = UserDataFrame(self, self.log_frame,
                                            self.bot_control_frame)
        self.userdata_frame.grid(row=0, column=0, padx=10,
                                 pady=(10, 5), sticky='nswe')

    def get_settings(self):
        """ Функция получения настроек при при наличии
            созраненых логина и пароля.
        """
        if (self.userdata_frame.login_field._state == 'disabled'
                and self.userdata_frame.password_field._state == 'disabled'):
            return [self.userdata_frame.set_login(),
                    self.userdata_frame.set_password(),
                    self.bot_settings_frame.set_likes(),
                    self.bot_settings_frame.set_link()]


if __name__ == '__main__':
    user_settings = ["login=\n", "password=\n", "likes=\n",
                     "online_setting='0'\n", "purpose='0'\n", "gender='3'\n",
                     "mygender='3'\n", "age_from=\n", "age_to=\n", "region=\n"]
    if not os.path.exists('.env'):
        with open('.env', 'w', encoding='utf-8') as file:
            file.writelines(user_settings)
    window = LoveBot()
    window.mainloop()
