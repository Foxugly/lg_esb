from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from seleniumclass import SeleniumClass


class FidNewClient(SeleniumClass):
    NAME =               (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr[1]/td[2]/input')
    JUDICIAL_FORM =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr[2]/td[2]/div/span/input')
    ASSOC =           (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_4"]')
    RESP =               (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_1"]')
    ASSIS =           (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_2"]')
    RESP_LEG =           (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_5"]')
    ASSISS_LEG =       (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_6"]')
    ADDRESS_LINE1 =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "line1")]')
    ADDRESS_BOX =       (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "box")]')
    ADDRESS_LINE2 =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "line2")]')
    ADDRESS_LINE3 =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "line3")]')
    ADDRESS_CITY =    (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "city")]')
    ADDRESS_ZIP =       (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "postal-code")]')
    ADDRESS_COUNTRY = (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/span/input[@id="ClientProposalAddressCountry"]')

    def __init__(self, driver):
    	self.driver = driver


    def create_client(self, c):
        # NAME
        self.insert_text("insert text in name", self.NAME, c['name'])
        # JUDICIAL FORM
        self.select_text("select judicial_form", self.JUDICIAL_FORM, c['judicial_form'], True)
        # ASSOC
        self.select_text("select assoc", self.ASSOC, c['assoc'])
        # RESP
        self.select_text("select resp", self.RESP, c['resp'])
        # ASSIS

        # RESP_LEG

        # ASSISS_LEG

        # ADDRESSE_LINE1


class Fid(SeleniumClass):
    USER =       (By.XPATH,'//*[@id="email"]')
    PASSWORD =  (By.XPATH,'//*[@id="password"]')
    BTN_SUBMIT =  (By.XPATH,'//*[@id="submit"]')
    MENU_CLIENT = (By.XPATH, '//*[@id="pageMenu"]/ul/li[2]/span')
    MENUITEM_ADD_CLIENT = (By.XPATH, '//*[@id="clientAddMenuItem"]/a')

    def __init__(self, d):
        self.driver = d
        self.fnc = FidNewClient(self.driver)

    def auth(self, url, u, p):
        self.URL = url
        self.u = u
        self.p = p
        self.driver.get(self.URL)
        self.insert_text("insert text in user", self.USER, self.u)
        self.insert_text("insert text in password", self.PASSWORD, self.p)
        self.btn_click("click auth", self.BTN_SUBMIT)

    def create_new_client(self, d):
        self.btn_click("click menu client", self.MENU_CLIENT)
        self.btn_click("click menuitem add client", self.MENUITEM_ADD_CLIENT)
        self.fnc.create_client(d)
