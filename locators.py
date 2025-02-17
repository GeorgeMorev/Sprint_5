from selenium.webdriver.common.by import By


class Locators:
    EMAIL_INPUT_LOG_IN = "//input[@name='name']"  #Поле емейл
    PASSWORD_INPUT_LOG_IN = "//input[@name='Пароль']"  #Поле Пароль
    SIGN_IN_BUTTON_LOG_IN_PAGE = "//button[contains(text(), 'Войти')]"  #Кнопка "Вход" на странице логина
    LOG_IN_PAGE_TITLE = "//h2[contains(text(),'Вход')]"  #Заголовок "Вход" на странанице логина
    PERSONAL_ACCOUNT_BUTTON = "//p[contains(text(),'Личный Кабинет')]"  #Кнопка "Личный Кабинет"
    MAKE_ORDER_BUTTON = ("//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                         "button_button_size_large__G21Vg']")  #Кнопка "Оформить заказ"
    WRONG_PASSWORD_ERROR_HIGHLIGHT = "//p[@class='input__error text_type_main-default']"
    MAIN_LOGIN_BUTTON = ("//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                         "button_button_size_large__G21Vg']")  #Кнопка "Войти в аккаунт" на главной странице
    NAME_INPUT_REGISTRATION = "(//input[@type='text'])[1]"  #Поле "Имя" на странице регистрации
    EMAIL_INPUT_REGISTRATION = "(//input[@type='text'])[2]"  #Поле "Email"  на странице регистрации
    PASSWORD_INPUT_REGISTRATION = "(//input[@type='password'])[1]"  #Поле "Пароль"  на странице регистрации
    REGISTRATION_BUTTON = ("//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                           "button_button_size_medium__3zxIa']")  #Кнопка "Зарегистрироваться"  на странице регистрации
    SIGN_IN_BUTTON_REGISTRATION_PAGE = "//a[@class='Auth_link__1fOlj']"  #Кнопка "Войти"  на странице регистрации
    SIGN_IN_BUTTON_PASSWORD_REPARE_PAGE = "//a[@class='Auth_link__1fOlj']"  #Кнопка "Войти" на странице восстановления пароля
    PERSONAL_ACCOUNT_PAGE_TITLE = ("//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive "
                                   "Account_link_active__2opc9']") #Звголовок "Профиль" на странице Личного кабинета
    CONSTRUCTOR_BUTTON = "//p[contains(text(),'Конструктор')]"  #Кнопка "Конструктор"
    LOGO_BUTTON = "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']"  # Логотип на главной странице
    BREAD_BUTTON = "//span[contains(text(),'Булки')]"  # Кнопка выбора хлеба на странице выбора ингредиентов
    BREAD_TITLE = "//h2[contains(text(),'Булки')]"  # Заголовок секции хлеба на странице выбора ингредиентов
    SAUCE_BUTTON = "//span[contains(text(),'Соусы')]"  # Кнопка выбора соусов на странице выбора ингредиентов
    SAUCE_TITLE = "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]"  # Название одного из соусов на странице выбора ингредиентов
    TOPPING_BUTTON = "//span[contains(text(),'Начинки')]"  # Кнопка выбора начинки на странице выбора ингредиентов
    ACTIVE_TOPPING_BUTTON = "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]"  # Название одной из начинок на странице выбора ингредиентов