import threading

from customtkinter import (CTkButton, CTkEntry, CTkFrame, CTkLabel,
                           CTkOptionMenu, CTkTextbox, StringVar)
from dotenv import get_key, set_key

from settings import (my_genders, online_choices, purpose_choices,
                      purpose_code, search_gender)


class LogFrame(CTkFrame):
    """ Фрейм журнала событий и относящиеся к нему функции. """
    def __init__(self, master: any):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.log_label = CTkLabel(self, text='Журнал событий:')
        self.log_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='w')

        self.log = CTkTextbox(self, activate_scrollbars=True)
        self.log.grid(row=1, column=0, padx=10, pady=(5, 10), sticky='nswe')

    def print_to_log(self, text):
        """ Функция печати сообщения в журнал событий. """
        self.log.insert('1.0', text=f'{text}\n')


class BotControlFrame(CTkFrame):
    """ Фрейм запуска и остановки бота и относящиеся к нему функции. """
    def __init__(self, master, logger: LogFrame, get_settings, bot_main):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        self.log = logger
        self.bot_settings = get_settings
        self.bot_main = bot_main
        self.bot_thread = None
        self.stop = threading.Event()

        self.control_label = CTkLabel(self, text='Управление ботом:')
        self.control_label.grid(row=0, column=0, padx=10,
                                pady=(10, 5), sticky='nw')

        self.start_btn = CTkButton(self, text='Старт', state='disabled',
                                   command=self.start_bot)
        self.start_btn.grid(row=1, column=1, padx=10,
                            pady=(5, 10), sticky='nw')

        self.stop_btn = CTkButton(self, text='Стоп', state='disabled',
                                  command=self.stop_bot)
        self.stop_btn.grid(row=1, column=2, padx=10,
                           pady=(5, 10), sticky='nw')

        self.btns = [self.start_btn, self.stop_btn]

    def start_bot(self):
        """ Функция запуска бота в отдельном потоке. """
        self.log.print_to_log('Запускаю бота...')
        login, password, likes, simp_link = self.bot_settings()
        self.stop.clear()
        self.bot_thread = threading.Thread(
            target=self.bot_main,
            args=(login, password, likes, self.log, self.stop, simp_link)
        )
        self.bot_thread.start()

    def stop_bot(self):
        """ Функция остановки бота в отдельном потоке, через Event в потоке. """
        if self.bot_thread is not None:
            self.log.print_to_log('Останавливаю бота...')
            self.stop.set()
            self.bot_thread.join(0.0)


class UserDataFrame(CTkFrame):
    """ Фрейм ввода данных пользователя для входа на сайт. """
    def __init__(self, master: any, logger: LogFrame,
                 bot_control: BotControlFrame):
        super().__init__(master,)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        self.login_label = CTkLabel(self, text='Логин пользователя:')
        self.login_field = CTkEntry(self, placeholder_text='Введите логин...')
        self.login_btn = CTkButton(self, text='Ввод', command=self.set_login)
        self.login_label.grid(row=0, column=0, padx=10,
                              pady=(10, 5), sticky='nw')
        self.login_field.grid(row=0, column=1, padx=10,
                              pady=(10, 5), sticky='nw')
        self.login_btn.grid(row=0, column=2, padx=10,
                            pady=(10, 5), sticky='nw')
        self.reset_login_btn = CTkButton(
            self, text='Изменить', command=self.reset_login, state='disabled'
        )
        self.reset_login_btn.grid(row=0, column=3, padx=10,
                                  pady=(10, 5), sticky='nw')

        self.password_label = CTkLabel(self, text='Пароль пользователя:')
        self.password_field = CTkEntry(
            self, placeholder_text='Введите пароль...'
        )
        self.password_btn = CTkButton(
            self, text='Ввод', command=self.set_password
        )
        self.password_label.grid(row=1, column=0, padx=10,
                                 pady=(5, 10), sticky='nw')
        self.password_field.grid(row=1, column=1, padx=10,
                                 pady=(5, 10), sticky='nw')
        self.password_btn.grid(row=1, column=2, padx=10,
                               pady=(10, 5), sticky='nw')
        self.reset_password_btn = CTkButton(
            self, text='Изменить', command=self.reset_password,
            state='disabled'
        )
        self.reset_password_btn.grid(row=1, column=3, padx=10,
                                     pady=(10, 5), sticky='nw')
        self.log = logger
        self.bot = bot_control
        self.saved_user_settings()

    def set_login(self):
        """ Функция ввода логина или его получения из сохраненых данных. """
        login = self.login_field.get()
        set_key('.env', 'login', login)
        self.login_field.configure(state='disabled')
        self.log.print_to_log(f'Логин: {login}')
        self.login_btn.configure(state='disabled')
        self.reset_login_btn.configure(state='normal')
        if self.password_btn._state == 'disabled':
            for btn in self.bot.btns:
                btn.configure(state='normal')
        return login

    def reset_login(self):
        """ Функция изменения логина. """
        self.login_btn.configure(state='normal')
        self.login_field.configure(state='normal')
        self.reset_login_btn.configure(state='disabled')
        for btn in self.bot.btns:
            btn.configure(state='disabled')
        self.log.print_to_log('Можете ввести новый логин.')

    def set_password(self):
        """ Функция ввода пароля или его получения из сохраненых данных. """
        password = self.password_field.get()
        set_key('.env', 'password', password)
        self.password_field.configure(state='disabled')
        self.log.print_to_log(f'Пароль: {password}')
        self.password_btn.configure(state='disabled')
        self.reset_password_btn.configure(state='normal')
        if self.login_btn._state == 'disabled':
            for btn in self.bot.btns:
                btn.configure(state='normal')
        return password

    def reset_password(self):
        """ Функция изменения пароля. """
        self.password_btn.configure(state='normal')
        self.password_field.configure(state='normal')
        self.reset_password_btn.configure(state='disabled')
        for btn in self.bot.btns:
            btn.configure(state='disabled')
        self.log.print_to_log('Можете ввести новый пароль.')

    def saved_user_settings(self):
        """ Функция получения сохраненых данных при запуске программы. """
        if len(login := get_key('.env', 'login')):
            self.login_field.insert(0, login)
            self.login_field.configure(state='disabled')
            self.login_btn.configure(state='disabled')
            self.reset_login_btn.configure(state='normal')
            if self.password_btn._state == 'disabled':
                for btn in self.bot.btns:
                    btn.configure(state='normal')
        if len(password := get_key('.env', 'password')):
            self.password_field.insert(0, password)
            self.password_field.configure(state='disabled')
            self.password_btn.configure(state='disabled')
            self.reset_password_btn.configure(state='normal')
            if self.login_btn._state == 'disabled':
                for btn in self.bot.btns:
                    btn.configure(state='normal')


class BotSettingsFrame(CTkFrame):
    """ Фрейм для настройки данных на сайте для поиска людей. """
    def __init__(self, master: any, logger: LogFrame,):
        super().__init__(master)

        self.bot_set_label = CTkLabel(self, text='Настройки бота:')
        self.bot_set_label.grid(
            row=0, column=0, padx=10, pady=(10, 5), sticky='w'
        )

        self.bot_set_likes_l = CTkLabel(self, text='Лайки:')
        self.bot_set_likes_l.grid(
            row=1, column=0, padx=10, pady=(5, 10), sticky='w'
        )
        self.bot_set_likes_e = CTkEntry(
            self, placeholder_text='Количество лайков...'
        )
        self.bot_set_likes_e.grid(
            row=1, column=1, padx=10, pady=(5, 10), sticky='w'
        )
        self.e_set_likes_btn = CTkButton(
            self, text='Ввод', command=self.set_likes
        )
        self.e_set_likes_btn.grid(
            row=1, column=2, padx=10, pady=(5, 10), sticky='w'
        )
        self.c_set_likes_btn = CTkButton(
            self, text='Изменить', command=self.reset_likes,
            state='disabled'
        )
        self.c_set_likes_btn.grid(
            row=1, column=3, padx=10, pady=(5, 10), sticky='w'
        )
        self.log = logger

        saved_mygender_set = StringVar(
            value=my_genders[int(get_key('.env', 'mygender')) - 1]
        )
        self.mygender_setting = CTkOptionMenu(
            self, values=my_genders,
            command=self.set_mygender, variable=saved_mygender_set
        )
        self.mygender_setting.grid(
            row=2, column=0, padx=10, pady=(10, 10), sticky='w'
        )
        saved_gender_set = StringVar(
            value=search_gender[int(get_key('.env', 'gender')) - 1]
        )
        self.gender_setting = CTkOptionMenu(
            self, values=search_gender,
            command=self.set_gender, variable=saved_gender_set
        )
        self.gender_setting.grid(
            row=2, column=1, padx=10, pady=(10, 10), sticky='w'
        )
        saved_online_set = StringVar(
            value=online_choices[int(get_key('.env', 'online_setting'))]
        )
        self.online_setting = CTkOptionMenu(
            self, values=online_choices, command=self.set_online,
            variable=saved_online_set
        )
        self.online_setting.grid(
            row=2, column=2, padx=10, pady=(10, 10), sticky='w'
        )

        saved_purpose_set = StringVar(
            value=next(purpose for purpose, code in purpose_code.items()
                       if code == int(get_key('.env', 'purpose')))
        )
        self.purpose_setting = CTkOptionMenu(
            self, values=purpose_choices, command=self.set_purpose,
            variable=saved_purpose_set
        )
        self.purpose_setting.grid(
            row=2, column=3, padx=10, pady=(10, 10), sticky='w'
        )
        self.age_frame = CTkFrame(self)
        self.age_frame.grid(
            row=3, column=0, padx=10, pady=(10, 10), sticky='w', columnspan=3
        )
        get_age_from = get_key('.env', 'age_from')
        saved_age_from_set = StringVar(
            value=(get_age_from if get_age_from is not None else None))
        self.age_from_setting = CTkEntry(
            self.age_frame,  width=30,
            textvariable=saved_age_from_set
        )
        self.age_from_setting.grid(
            row=0, column=0, padx=(10, 5), pady=(10, 10), sticky='w',
        )
        self.dash = CTkLabel(self.age_frame, width=0, text='--')
        self.dash.grid(
            row=0, column=1, padx=5, pady=(10, 10), sticky='w',
        )
        get_age_to = get_key('.env', 'age_to')
        saved_age_to_set = StringVar(
            value=(get_age_to if get_age_to is not None else None))
        self.age_to_setting = CTkEntry(
            self.age_frame,  width=30,
            textvariable=saved_age_to_set
        )
        self.age_to_setting.grid(
            row=0, column=2, padx=(5, 10), pady=(10, 10), sticky='w'
        )

        self.region_setting = CTkEntry(
            self, placeholder_text='geo- из ссылки: 123,456,222',
            width=200,
        )
        self.region_setting.grid(
            row=3, column=1, padx=(5, 10), pady=(10, 10),
            sticky='w', columnspan=2
        )

        self.set_link_btn = CTkButton(
            self, text='Создать ссылку', command=self.set_link
        )
        self.set_link_btn.grid(
            row=3, column=3, padx=(5, 10), pady=(10, 10),
            sticky='w',
        )

        self.saved_user_settings()

    def set_gender(self, choice):
        """ Установка пола партнера для поиска. """
        set_key(
            '.env', 'gender',
            next(str(x + 1) for x, gender in enumerate(search_gender)
                 if choice == gender)
        )

    def set_mygender(self, choice):
        """ Установка своего пола для поиска. """
        set_key(
            '.env', 'mygender',
            next(str(x + 1) for x, gender in enumerate(my_genders)
                 if choice == gender)
        )

    def set_online(self, choice):
        """ Установка статуса нахождения на сайте. """
        set_key('.env', 'online_setting', choice)
        set_key(
            '.env', 'online_setting',
            next(str(x) for x, ch in enumerate(online_choices)
                 if ch == choice)
        )

    def set_purpose(self, choice):
        """ Установка цели знакомства. """
        set_key('.env', 'purpose', str(purpose_code[choice]))

    def set_likes(self):
        """ Установка ограничения лайков для бота. """
        likes = self.bot_set_likes_e.get()
        if not likes.isdigit():
            self.log.print_to_log(
                'Количество лайков должно быть числом, проверьте ввод.\n'
                'Выставляю значение по умолчанию: 10'
            )
            self.bot_set_likes_e.delete('0', 'end')
            self.bot_set_likes_e.insert(0, '10')
            likes = '10'
        set_key('.env', 'likes', likes)
        self.bot_set_likes_e.configure(state='disabled')
        self.log.print_to_log(f'Бот поставит {likes} лайков.')
        self.e_set_likes_btn.configure(state='disabled')
        self.c_set_likes_btn.configure(state='normal')
        return likes

    def reset_likes(self):
        """ Изменение ограничения лайков для бота. """
        self.e_set_likes_btn.configure(state='normal')
        self.bot_set_likes_e.configure(state='normal')
        self.c_set_likes_btn.configure(state='disabled')
        self.log.print_to_log('Введите количество лайков.')

    def saved_user_settings(self):
        """ Функция получения сохраненых данных при запуске программы. """
        if len(likes := get_key('.env', 'likes')):
            self.bot_set_likes_e.insert(0, likes)
            self.bot_set_likes_e.configure(state='disabled')
            self.e_set_likes_btn.configure(state='disabled')
            self.c_set_likes_btn.configure(state='normal')
        else:
            self.bot_set_likes_e.insert(0, '10')
            set_key('.env', 'likes', '10')
            self.bot_set_likes_e.configure(state='disabled')
            self.e_set_likes_btn.configure(state='disabled')
            self.c_set_likes_btn.configure(state='normal')
        if len(region := get_key('.env', 'region')):
            self.region_setting.insert(0, region)

    def set_link(self):
        """ Получение итоговой ссылки для поиска партнера. """
        age_from = self.age_from_setting.get()
        age_to = self.age_to_setting.get()
        region = self.region_setting.get()
        set_key('.env', 'age_from', age_from)
        set_key('.env', 'age_to', age_to)
        set_key('.env', 'region', region)
        return ('https://loveplanet.ru/a-searchlik/d-1/pol-'
                f'{get_key(".env", "mygender")}/spol-'
                f'{get_key(".env", "gender")}/geo-{get_key(".env", "region")}'
                f'/purp-{get_key(".env", "purpose")}'
                f'/online-{get_key(".env", "online_setting")}/newface-1/tage-'
                f'{get_key(".env", "age_to")}/bage-'
                f'{get_key(".env", "age_from")}')
