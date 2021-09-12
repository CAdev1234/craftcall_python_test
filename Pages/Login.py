class Login:
    def __init__(self, driver):
        self.driver = driver

    def login_modal_btn(self):
        return self.driver.find_element_by_css_selector("#navbar nav div.nav-items.mt-md-1 span.nav-item.login")

    def login_input_li(self):
        input_li = self.driver.find_elements_by_css_selector("#auth-modal input")
        return input_li

    def login_btn(self):
        return self.driver.find_element_by_css_selector("#auth-modal form button")
