class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    def sidebar_nav(self, orderNum):
        sidebar_items = self.driver.find_elements_by_css_selector("portal-sidebar section div");
        return sidebar_items[orderNum]