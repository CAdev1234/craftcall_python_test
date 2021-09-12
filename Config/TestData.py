import random


class TestData:
    SITE_URL = "https://www.craftcall.io"
    USER_EMAIL = "fenglong37@outlook.com"
    USER_PASSWORD = "Hsiangyu4233"
    CHROME_DRIVER_PATH = "E:\\programming\\python\\CraftCallTest\\chromedriver.exe"
    new_account = {
        "first_name": "fn_" + str(random.randint(100, 1000)),
        "last_name": "ln_" + str(random.randint(100, 1000)),
        "email": "email" + str(random.randint(100, 1000)) + "@py.com",
        "company_name": "cm_py_" + str(random.randint(100, 1000)),
        "password": "pwpy" + str(random.randint(100, 1000))
    }
    new_contact = {
        "first_name": "ct_fn_" + str(random.randint(100, 1000)),
        "last_name": "ct_ln" + str(random.randint(100, 1000)),
        "phone": "12345678901"
    }
    new_group = {
        "group_name": "g_n_py_" + str(random.randint(100, 1000)),
        "group_desc": "g_d_py_" + str(random.randint(100, 1000))
    }
    new_msg = {
        "msg_title": "m_title_" + str(random.randint(100, 1000)),
        "msg_content": "m_text_" + str(random.randint(100, 1000))
    }
