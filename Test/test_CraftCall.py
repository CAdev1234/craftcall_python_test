# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import random
import time
import pytest

from selenium import webdriver

from Config.TestData import TestData
from Pages.Dashboard import Dashboard
from Pages.Login import Login
from Test.Module.CreateAccount import CreateAccount
from Test.Module.CreateDelContact import CreateDelContact
from Test.Module.CreateDelGroup import CreateDelGroup
from Test.Module.CreateDelMessage import CreateDelMessage
from Test.Module.AddRemoveContactToGroup import AddRemoveContactToGroup
from conftest import InitDriver

sys.path.append(".")


class TestCraftCall(InitDriver):

    @pytest.mark.create_new_account
    def test_create_account(self):
        new_account = TestData.new_account
        create_account = CreateAccount(self.driver, new_account)
        create_account.run()

    @pytest.mark.login
    def test_login(self):
        # site login
        my_acc = {
            "user_email": TestData.USER_EMAIL,
            "password": TestData.USER_PASSWORD
        }
        login_page = Login(self.driver)
        login_page.login_modal_btn().click()
        time.sleep(3)

        # type login info and login
        input_li = login_page.login_input_li()
        for index in range(0, len(list(my_acc))):
            input_li[index].send_keys(my_acc[list(my_acc)[index]])
            time.sleep(1)

        login_page.login_btn().click()
        time.sleep(5)

    @pytest.mark.create_del_contact
    def test_create_del_contact(self):
        self.test_login()
        # create and delete contact
        new_contact = TestData.new_contact
        c_d_contact = CreateDelContact(self.driver, new_contact)
        c_d_contact.run()

    @pytest.mark.create_del_group
    def test_create_del_group(self):
        self.test_login()
        # create and delete group
        new_group = TestData.new_group
        c_d_group = CreateDelGroup(self.driver, new_group)
        c_d_group.run()

    @pytest.mark.create_del_msg
    def test_create_del_msg(self):
        self.test_login()
        # create and delete message
        new_msg = TestData.new_msg
        c_d_msg = CreateDelMessage(self.driver, new_msg)
        c_d_msg.run()

    @pytest.mark.add_contact_to_group
    def test_add_contact_to_group(self):
        self.test_login()
        # add contact to group and remove it from group
        new_group = TestData.new_group
        new_contact = TestData.new_contact
        c_d_group = CreateDelGroup(self.driver, new_group)
        c_d_contact = CreateDelContact(self.driver, new_contact)

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


