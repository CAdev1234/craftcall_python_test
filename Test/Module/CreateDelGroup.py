import time

from Pages.Dashboard import Dashboard
from Pages.Groups import Groups


class CreateDelGroup:
    def __init__(self, driver, new_group):
        self.driver = driver
        self.new_group = new_group

    def create(self):
        dashboard_page = Dashboard(self.driver)
        dashboard_page.sidebar_nav(2).click()

        # new group modal active
        group_page = Groups(self.driver)
        group_page.add_group_modal_btn().click()
        time.sleep(3)

        # type group info into form and create
        input_li = group_page.add_group_input_li()
        for index in range(0, len(list(self.new_group))):
            input_li[index].send_keys(self.new_group[list(self.new_group)[index]])
            time.sleep(1)
        group_page.add_group_to_table_btn().click()
        time.sleep(2)

        group_page.add_group_submit_btn().click()
        time.sleep(3)

        # go to panel
        dashboard_page.sidebar_nav(2).click()
        time.sleep(3)

    def delete(self):
        group_page = Groups(self.driver)
        group_page.edit_modal_btn_li(1).click()
        time.sleep(3)

    def run(self):
        self.create()
        existed = self.check_from_table(1, 1);
        time.sleep(3)
        if existed:
            self.delete()

    def check_from_table(self, check_td_num, click_num):
        # get all contacts created and check if new contact exist or not
        group_page = Groups(self.driver)
        existed = False
        all_group = group_page.all_group_tr_li()
        for index in range(0, len(all_group)):
            td_li = all_group[index].find_elements_by_tag_name("td")
            group_name = td_li[check_td_num].text
            if group_name.find(self.new_group["group_name"]) != -1:
                print("Group was successfully created. It was checked.")
                existed = True
                td_li[click_num].find_element_by_tag_name("span").click()
                break
        if not existed:
            print("Contact isnot existed...")
        return existed

    def assign_contact_to_group(self, contact):
        group_page = Groups(self.driver)
        existed_contact = False
        existed_group = self.check_from_table(1, 1)
        if existed_group:
            contact_li = self.driver.find_elements_by_css_selector("#areaListControl mat-list-option")
            for index in range(0, len(contact_li)):
                contact_title = contact_li[index].text
                if contact_title.find(contact["first_name"] + " " + contact["last_name"]) != -1:
                    contact_li[index].click()
                    existed_contact = True
                    time.sleep(2)
                    break
            if existed_contact:
                group_page.edit_modal_btn_li(3).click()
                time.sleep(3)
            else:
                print("Sorry, there is no contact")
                group_page.edit_modal_btn_li(2).click()
                time.sleep(3)

    def remove_contact_from_group(self, contact):
        group_page = Groups(self.driver)
        existed_contact = False
        existed_group = self.check_from_table(1, 1)
        if existed_group:
            contact_li = self.driver.find_elements_by_css_selector("#areaListControl mat-list-option")
            for index in range(0, len(contact_li)):
                contact_title = contact_li[index].text
                if contact_title.find(contact["first_name"] + " " + contact["last_name"]) != -1:
                    contact_li[index].click()
                    existed_contact = True
                    time.sleep(2)
                    break
            if existed_contact:
                group_page.edit_modal_btn_li(3).click()
                time.sleep(3)
            else:
                print("Sorry, there is no contact")
                group_page.edit_modal_btn_li(2).click()
                time.sleep(3)
