browser_args = [
    'user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    '--disable-blink-features=AutomationControlled',
    '--disable-blink-features'
]

driver_path = 'chromedrivers'

DB_NAME = 'simp.db'

online_choices = ['не имеет значения', 'сейчас онлайн', 'недавняя активность']
purpose_choices = ['не имеет значения', 'дружба', 'романтика', 'семья', 'свобод. отнош.', 'совмест. путеш.']
purpose_code = {
    'не имеет значения': 0, 'дружба': 1, 'романтика': 2, 'семья': 128,
    'свобод. отнош.': 4096, 'совмест. путеш.': 64
}
my_genders = ['Я парень', 'Я девушка', 'Мой пол']
search_gender = ['Ищу парня', 'Ищу девушку', 'Ищу пол']
