import time

from Pages.Dashboard import Dashboard
from Test.Module.CreateDelContact import CreateDelContact
from Test.Module.CreateDelGroup import CreateDelGroup


class AddRemoveContactToGroup:
    def __init__(self, driver, new_group, new_contact):
        self.driver = driver
        self.new_group = new_group
        self.new_contact = new_contact

    def run(self):
        # first create contact
        c_d_contact = CreateDelContact(self.driver, self.new_contact)
        c_d_contact.create()

        # select group panel
        dashboard_page = Dashboard(self.driver)
        dashboard_page.sidebar_nav(2).click()
        time.sleep(2)

        # create group
        c_d_group = CreateDelGroup(self.driver, self.new_group)
        c_d_group.create()

        time.sleep(3)
        c_d_group.assign_contact_to_group(self.new_contact)
        c_d_group.remove_contact_from_group(self.new_contact)
