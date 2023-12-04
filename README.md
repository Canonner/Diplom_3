## Диплом Задание 2

Тесты UI сервиса [StellarBurger](https://stellarburgers.nomoreparties.site//)

### Список файлов и описание проверок:

### Папка tests содержит файлы:
#### 1. test_password_recovery.py 
<i>Проверяет функциональность восстановления пароля.</i>

Класс TestPasswordRecovery содержит тесты:
- test_click_on_pass_recovery_button_opens_pass_recovery_page
- test_input_email_and_click_on_pass_recovery_button_opens_reset_pass_page
- test_highlight_pass_entry_field


#### 2. test_account_functionality.py
<i>Проверяет функциональность личного кабинета.</i>

Класс TestAccountFunctionality содержит тесты:
- test_click_on_account_button_opens_profile_page
- test_click_on_order_history_url_opens_orders_history_page
- test_click_on_exit_url_logs_out_from_account


#### 3. test_main_functionality.py
<i>Проверяет основной функционал.</i>

Класс TestMainFunctionality содержит тесты:
- test_transition_to_constructor_and_feed_pages
- test_click_on_ingredient_opens_popup_window
- test_click_on_ingredient_details_window_close_button_closes_window
- test_increase_of_ingredient_counter
- test_authorised_user_place_order


#### 4. test_feed_functionality.py
<i>Проверяет раздел "Лента заказов".</i>

Класс TestFeedFunctionality содержит тесты:
- test_click_on_order_opens_details_popup_window
- test_user_order_displayed_on_feed_page
- test_increase_completed_counters
- test_order_number_displayed_in_progress_section


#### 5. conftest.py
Содержит фикстуры
- driver
- get_forgot_pass_page
- create_user_and_sign_in
- create_new_order_and_get_its_number

### Папка pages:
Содержит файлы с базовыми методами и специфическими методами страниц

### Папка locators:
Содержит файл locators.py с локаторами элементов, разбитых на классы по страницам


Кроме того, в корневой папке проекта находятся:
- файл data.py c тестовыми данными, 
- файл requirements.txt c зависимостями проекта и
- файл .gitignore.
