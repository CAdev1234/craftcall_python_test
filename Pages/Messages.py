class Messages:
    def __init__(self, driver):
        self.driver = driver

    def add_msg_modal_btn(self):
        top_btn_li = self.driver.find_elements_by_css_selector("messages portal-table section div.top-bar a")
        return top_btn_li[0]

    def add_msg_title_input(self):
        return self.driver.find_element_by_css_selector("add-message input")

    def add_msg_content_textarea(self):
        return self.driver.find_element_by_css_selector("add-message textarea")

    def btn_from_add_msg_modal(self, index):
        # index = 0 => CANCEL button
        # index = 1 => SAVE button
        # index = 2 => SEND button
        bottom_btn_li = self.driver.find_elements_by_css_selector("add-message button")
        return bottom_btn_li[index]

    def del_modal_btn(self):
        btn_li = self.driver.find_elements_by_css_selector("messages portal-table a")
        return btn_li[1]

    def del_msg_btn(self):
        btn_li = self.driver.find_elements_by_css_selector("delete-message button")
        return btn_li[1]

    def all_msg_tr_li(self):
        all_msg = self.driver.find_elements_by_css_selector("messages table tbody tr")
        return all_msg