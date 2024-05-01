import allure


@allure.suite('Тест Восстановление пароля')
class TestPasswordRecover:

    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_password_recover_click(self, password_recovery_page):
        password_recovery_page.button_login_click()
        password_recovery_page.button_recover_click()
        password_recovery_page.check_recover()


    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль», ввод почты и клик '
                        'по кнопке Восстановить.')
    def test_password_recover_send_email_and_click(self, password_recovery_page):
        password_recovery_page.button_login_click()
        password_recovery_page.button_recover_click()
        password_recovery_page.send_email_and_button_recover_click()
        password_recovery_page.check_password_recover()


    @allure.title('Тест проверки клика по кнопке показать/скрыть пароль делает поле активным -'
    'подсвечивает его.')
    def test_password_recover_eye_button(self, password_recovery_page):
        password_recovery_page.button_login_click()
        password_recovery_page.button_recover_click()
        password_recovery_page.send_email_and_button_recover_click()
        password_recovery_page.check_eye_button()
