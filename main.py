# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from Pages.Dashboard import Dashboard
from Pages.Login import Login
from Test.Module.CreateAccount import CreateAccount
from Test.Module.CreateDelContact import CreateDelContact
from Test.Module.CreateDelGroup import CreateDelGroup
from Test.Module.CreateDelMessage import CreateDelMessage
from Test.Module.AddRemoveContactToGroup import AddRemoveContactToGroup

sys.path.append(".")
import random
from selenium import webdriver
import time




class AppTest:
    def __init__(self, driver, site_url, my_acc):
        self.driver = driver
        self.site_url = site_url
        self.my_acc = my_acc

    def run(self):
        # connect web page
        self.driver.get(self.site_url)

        # Create account test
        new_account = {
            "first_name": "fn_" + str(random.randint(100, 1000)),
            "last_name": "ln_" + str(random.randint(100, 1000)),
            "email": "email" + str(random.randint(100, 1000)) + "@py.com",
            "company_name": "cm_py_" + str(random.randint(100, 1000)),
            "password": "pwpy" + str(random.randint(100, 1000))
        }
        create_account = CreateAccount(self.driver, new_account)
        create_account.run()

        # site login
        login_page = Login(self.driver)
        login_page.login_modal_btn().click()
        time.sleep(3)

        # type login info and login
        input_li = login_page.login_input_li()
        for index in range(0, len(list(self.my_acc))):
            input_li[index].send_keys(self.my_acc[list(self.my_acc)[index]])
            time.sleep(1)

        login_page.login_btn().click()
        time.sleep(5)

        # create and delete contact
        new_contact = {
            "first_name": "ct_fn_" + str(random.randint(100, 1000)),
            "last_name": "ct_ln" + str(random.randint(100, 1000)),
            "phone": "12345678901"
        }
        c_d_contact = CreateDelContact(self.driver, new_contact)
        c_d_contact.run()

        # create and delete group
        new_group = {
            "group_name": "g_n_py_" + str(random.randint(100, 1000)),
            "group_desc": "g_d_py_" + str(random.randint(100, 1000))
        }
        c_d_group = CreateDelGroup(self.driver, new_group)
        c_d_group.run()

        # create and delete message
        new_msg = {
            "msg_title": "m_title_" + str(random.randint(100, 1000)),
            "msg_content": "m_text_" + str(random.randint(100, 1000))
        }
        c_d_msg = CreateDelMessage(self.driver, new_msg)
        c_d_msg.run()

        # add contact to group and remove it from group
        add_contact_to_g = AddRemoveContactToGroup(self.driver, new_group, new_contact)
        add_contact_to_g.run()
        time.sleep(3)
        c_d_group.check_from_table(1, 1)
        c_d_group.delete()
        time.sleep(3)

        dashboard_page = Dashboard(self.driver)
        dashboard_page.sidebar_nav(1).click()
        time.sleep(2)

        c_d_contact.check_from_table(2, 1)
        time.sleep(3)
        c_d_contact.delete()

        time.sleep(5)
        driver.quit()


def set_driver():
    # chrome web driver setting
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
    driver.maximize_window()
    return driver


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    site_url = "https://www.craftcall.io"
    my_acc = {
        "user_email": "fenglong37@outlook.com",
        "password": "Hsiangyu4233"
    }
    driver = set_driver()
    app_test = AppTest(driver, site_url, my_acc)
    app_test.run()

