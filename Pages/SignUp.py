class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def register_modal_btn(self):
        register_modal_btn = self.driver.find_elements_by_css_selector("#auth-modal button")
        return register_modal_btn[1]

    def register_btn(self):
        register_btn = self.driver.find_element_by_css_selector("#auth-modal form button")
        return register_btn

    def register_input_li(self):
        input_li = self.driver.find_elements_by_css_selector("#auth-modal form input")
        return input_li

    def remember_check_box(self):
        checkbox = self.driver.find_elements_by_css_selector("#auth-modal form label")
        return checkbox[5].find_elements_by_tag_name("span")[0]