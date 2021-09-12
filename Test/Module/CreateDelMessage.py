import time

from Pages.Dashboard import Dashboard
from Pages.Messages import Messages


class CreateDelMessage:
    def __init__(self, driver, new_msg):
        self.driver = driver
        self.new_msg = new_msg

    def create(self):
        dashboard_page = Dashboard(self.driver)
        dashboard_page.sidebar_nav(3).click()
        time.sleep(3)

        # new message modal active
        msg_page = Messages(self.driver)
        msg_page.add_msg_modal_btn().click()
        time.sleep(3)

        # type new message detail into form and create
        input_ele = msg_page.add_msg_title_input()
        text_area = msg_page.add_msg_content_textarea()
        input_ele.send_keys(self.new_msg["msg_title"])
        time.sleep(1)
        text_area.send_keys(self.new_msg["msg_content"])
        time.sleep(1)
        msg_page.btn_from_add_msg_modal(1).click()
        time.sleep(5)

    def delete(self):
        msg_page = Messages(self.driver)
        msg_page.del_msg_btn().click()
        time.sleep(3)

    def run(self):
        msg_page = Messages(self.driver)
        self.create()
        existed = self.check_from_table(1, 0)
        time.sleep(3)
        # delete modal active
        msg_page.del_modal_btn().click()
        time.sleep(3)
        if existed:
            self.delete()

    def check_from_table(self, check_td_num, click_num):
        # get all contacts created and check if new contact exist or not
        msg_page = Messages(self.driver)
        existed = False
        all_msg = msg_page.all_msg_tr_li()
        for index in range(0, len(all_msg)):
            td_li = all_msg[index].find_elements_by_tag_name("td")
            msg_title = td_li[check_td_num].text
            if msg_title.find(self.new_msg["msg_title"]) != -1:
                print("Contact was successfully created. It was checked.")
                existed = True
                td_li[click_num].find_element_by_tag_name("span").click()
                break
        if not existed:
            print("Contact isnot existed...")
        return existed
