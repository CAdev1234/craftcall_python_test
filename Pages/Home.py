class Home:
    def __init__(self, driver):
        self.driver = driver

    def login_modal_btn(self):
        return self.driver.find_element_by_css_selector("#navbar nav div.nav-items.mt-md-1 span.nav-item.login")