import allure


@allure.suite('Личный кабинет')
class TestLkPage:

    @allure.title('Тест перехода в Личный кабинет')
    def test_check_go_to_lk(self, lk_page):
        lk_page.button_login_click()
        lk_page.wait_login()
        lk_page.authorization()
        lk_page.button_login_click()
        lk_page.check_lk_page()
        lk_page.button_exit_click()

    @allure.title('Тест перехода в раздел История заказов в личном кабинете')
    def test_check_lk_history_orders(self, lk_page):
        lk_page.button_login_click()
        lk_page.wait_login()
        lk_page.authorization()
        lk_page.button_order_click()
        lk_page.check_history_orders()
        lk_page.button_exit_click()

    @allure.title('Тест выхода из ЛК')
    def test_check_lk_logout(self, lk_page):
        lk_page.button_login_click()
        lk_page.wait_login()
        lk_page.authorization()
        lk_page.button_login_click()
        lk_page.button_exit_click()
        lk_page.check_exit()


