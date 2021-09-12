class Contacts:
    def __init__(self, driver):
        self.driver = driver

    def add_contact_modal_btn(self):
        a_li = self.driver.find_elements_by_css_selector("contacts portal-table section div.top-bar a")
        return a_li[0]

    def new_contact_input_li(self):
        input_li = self.driver.find_elements_by_css_selector("add-contact input")
        return input_li

    def add_contact_to_table_btn(self):
        return self.driver.find_element_by_css_selector("add-contact button")

    def add_contact_submit_btn(self):
        bottom_btn_li = self.driver.find_elements_by_css_selector("add-contact a")
        return bottom_btn_li[1]

    def edit_modal_btn(self, index):
        # index = 0 = > INACTIVE button
        # index = 1 = > CLEAR GROUP button
        # index = 2 = > EXPORT CONTACT button
        # index = 3 = > DELETE button
        # index = 4 = > CANCEL button
        # index = 5 = > SAVE button
        btn_li = self.driver.find_elements_by_css_selector("edit-contact button")
        return btn_li[index]

    def all_contact_tr_li(self):
        return self.driver.find_elements_by_css_selector("contacts table tbody tr")
