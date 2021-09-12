import time
from selenium.webdriver.common.action_chains import ActionChains

from Pages.Home import Home
from Pages.SignUp import SignUp


class CreateAccount:
    def __init__(self, driver, new_account):
        self.driver = driver
        self.new_account = new_account

    def run(self):
        # login modal active
        home_page = Home(self.driver)
        home_page.login_modal_btn().click()
        time.sleep(3)

        # register modal active
        signup_page = SignUp(self.driver)
        signup_page.register_modal_btn().click()
        time.sleep(3)

        # type new account and click register button
        signup_page.register_btn().click()
        print("Form validation...")
        time.sleep(2)

        input_li = signup_page.register_input_li()
        for index in range(0, len(list(self.new_account))):
            input_li[index].send_keys(self.new_account[list(self.new_account)[index]])
            time.sleep(1)

        checkbox = signup_page.remember_check_box().click()
        time.sleep(2)
        signup_page.register_btn().click()
        time.sleep(2)
        print("Register Success!!!")

        # close modal by clicking (30, 30)
        time.sleep(5)
        self.driver.execute_script("var dd = document.elementFromPoint(30, 30);dd.click()")
        time.sleep(3)
