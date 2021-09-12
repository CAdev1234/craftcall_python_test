class Groups:
    def __init__(self, driver):
        self.driver = driver

    def add_group_modal_btn(self):
        top_btn_li = self.driver.find_elements_by_css_selector("groups portal-table section div.top-bar a")
        return top_btn_li[0]

    def add_group_input_li(self):
        input_li = self.driver.find_elements_by_css_selector("add-group input")
        return input_li

    def add_group_to_table_btn(self):
        btn = self.driver.find_element_by_css_selector("add-group button")
        return btn

    def add_group_submit_btn(self):
        save_btn = self.driver.find_element_by_css_selector("add-group a")
        return save_btn

    def edit_modal_btn_li(self, index):
        # index = 0 => EXPORT GROUP AND CONTACT button
        # index = 1 => DELETE GROUP button
        # index = 2 => CANCEL button
        # index = 3 => SAVE button
        btn_li = self.driver.find_elements_by_css_selector("edit-group button")
        return btn_li[index]

    def all_group_tr_li(self):
        return self.driver.find_elements_by_css_selector("groups table tbody tr")

    def contact_li_in_edit_group(self):
        return self.driver.find_elements_by_css_selector("#areaListControl mat-list-option")

