import time
from selenium.webdriver.common.keys import Keys


class SeleniumClass:

    @staticmethod
    def get_sleep(i=10):
            time.sleep(i)


    def insert_text(self, text, field, value, enter=False):
        print(text)
        try:
            f = self.driver.find_element(*field)
            f.send_keys(value)
            self.get_sleep(2)
            if enter:
                f.send_keys(Keys.ENTER)
                self.get_sleep(2)
        except Exception as e:
            print("ERROR :", e)

    def select_text(self, text, field, value, first_click=False):
        print(text)
        try:
            f = self.driver.find_element(*field)
            if first_click:
            	f.click()
            f.send_keys(value)
            self.get_sleep(2)
            f.send_keys(Keys.ENTER)
            self.get_sleep(2)
        except Exception as e:
            print("ERROR :", e)


    def btn_click(self, text, btn):
        print(text)
        try:
            f = self.driver.find_element(*btn)
            f.click()
            self.get_sleep(2)
        except Exception as e:
            print("ERROR :", e)