from selenium.webdriver.common.by import By

# кнопка конструктор
constructor_button = [By.XPATH, "//p[text()='Конструктор']"]
# кнопка лента заказов
order_feed_button = [By.XPATH, "//p[text()='Лента Заказов']"]
# текст соберите бургер
assemble_the_burger_text = [By.XPATH, "//h1[text()='Соберите бургер']"]

# текст лента заказов
order_feed_text = [By.XPATH, "//h1[text()='Лента заказов']"]

# ингредиент булка
ingredient_button = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
# детали ингредиента
ingredient_text = [By.XPATH, "//h2[text()='Детали ингредиента']"]


# кнопка закрыть окно ингредиента
exit_button = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/*[1]/*[2]"]
# место куда перетягивать ингредиента
place_for_ingredient = [By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']"]
# количество элементов ингредиента
ingredient_elements = [By.XPATH, "//ul[1]/a[1]//p[@class='counter_counter__num__3nue1']"]

# кнопка оформления заказа
order_button = [By.XPATH, "//button[text()='Оформить заказ']"]
# текст начала готовки заказа
cook_start_text = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
