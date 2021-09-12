import time

from Pages.Contacts import Contacts
from Pages.Dashboard import Dashboard


class CreateDelContact:
    def __init__(self, driver, new_contact):
        self.driver = driver
        self.new_contact = new_contact

    def create(self):
        dashboard_page = Dashboard(self.driver)
        dashboard_page.sidebar_nav(1).click()

        # new contact modal active
        contact_page = Contacts(self.driver)
        contact_page.add_contact_modal_btn().click()
        time.sleep(3)

        # type new contact info into form and create
        input_li = contact_page.new_contact_input_li()
        for index in range(0, len(list(self.new_contact))):
            input_li[index].send_keys(self.new_contact[list(self.new_contact)[index]])
            time.sleep(1)

        add_btn = contact_page.add_contact_to_table_btn()
        add_btn.click()
        time.sleep(2)
        bottom_btn = contact_page.add_contact_submit_btn()
        bottom_btn.click()
        time.sleep(2)

        # go to panel
        dashboard_page.sidebar_nav(1).click()
        time.sleep(3)

    def delete(self):
        # delete contact from edit modal
        contact_page = Contacts(self.driver)
        contact_page.edit_modal_btn(3).click()
        time.sleep(3)

    def run(self):
        self.create()
        existed = self.check_from_table(2, 1)
        time.sleep(3)
        if existed:
            self.delete()

    def check_from_table(self, check_td_num, click_num):
        # get all contacts created and check if new contact exist or not
        existed = False
        contact_page = Contacts(self.driver)
        all_contact = contact_page.all_contact_tr_li()
        for index in range(0, len(all_contact)):
            td_li = all_contact[index].find_elements_by_tag_name("td")

            phone_number = td_li[check_td_num].text
            if phone_number.find(self.new_contact["phone"]) != -1:
                print("Contact was successfully created. It was checked.")
                existed = True
                td_li[click_num].find_element_by_tag_name("span").click()
                break
        if not existed:
            print("Contact isnot existed...")
        return existed
