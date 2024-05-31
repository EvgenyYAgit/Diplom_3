from selenium.webdriver.common.by import By

# кнопка войти в аккаунт
login_button = [By.XPATH, "//button[text()='Войти в аккаунт']"]
# надпись восстановить пароль
restore_password = [By.XPATH, "//a[text()='Восстановить пароль']"]
# текст восстановление пароля
text_restore_password = [By.XPATH, "//h2[text()='Восстановление пароля']"]

# строка ввода email
string_input_email = [By.XPATH, "//input[@type='text']"]
# кнопка восстановить
restore_button = [By.XPATH, "//button[text()='Восстановить']"]
# кнопка сохранить
save_button = [By.XPATH, "//button[text()='Сохранить']"]

# кнопка показать/скрыть пароль
eya_password = [By.XPATH, "//div[@class='input__icon input__icon-action']"]
# подсвеченное поле пароль
area_light_password = [By.XPATH,
                       "//label[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused']"]
