from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from seleniumclass import SeleniumClass


class FidNewClient(SeleniumClass):
    

    def __init__(self):
        self.NAME =            (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr[1]/td[2]/input')
        self.JUDICIAL_FORM =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr[2]/td[2]/div/span/input')
        self.ASSOC =           (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_4"]')
        self.RESP =            (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_1"]')
        self.ASSIS =           (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_2"]')
        self.RESP_LEG =        (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_5"]')
        self.ASSISS_LEG =      (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "roles")]/div/div/span/input[@id="ClientProposalRole_6"]')
        self.ADDRESS_LINE1 =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "line1")]')
        self.ADDRESS_BOX =     (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "box")]')
        self.ADDRESS_LINE2 =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "line2")]')
        self.ADDRESS_LINE3 =   (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[@placeholder="Ligne 3"]')
        self.ADDRESS_CITY =    (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "city")]')
        self.ADDRESS_ZIP =     (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/input[contains(@class, "postal-code")]')
        self.ADDRESS_COUNTRY = (By.XPATH,'//div[contains(@class, "container") and contains(@class, "prop")]/table/tbody/tr/td/fieldset[contains(@class, "address")]/div/span/input[@id="ClientProposalAddressCountry"]')



class FidNewClientSRL(FidNewClient):
    

    def __init__(self, d):
        FidNewClient.__init__(self)
        self.driver = d
        self.JUDICIAL_NAME = "Société à responsabilité limitée"
        self.BCE =     (By.XPATH, '/html/body/div[9]/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[3]/td[2]/input')
        self.VAT  =    (By.XPATH, '/html/body/div[9]/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/input')
        self.LANG =    (By.XPATH, '//*[@id="ClientProposalLng"]') 
        self.WALLET  = (By.XPATH, '//*[@id="ClientProposalPtf"]')
        self.VAT_DECLARATION = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobVatReport\')"]')
        self.VAT_DECLARATION_SELECT =    (By.XPATH, '//*[@id="jobPeriod_33"]') 
        self.ANNUAL_LISTING = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobVatList\')"]')
        self.ANNUAL_LISTING_SELECT =    (By.XPATH, '//*[@id="jobPeriod_36"]') 
        self.CLOSURE_COMPANY = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobClosureCompany\')"]')
        self.CLOSURE_COMPANY_SELECT =    (By.XPATH, '//*[@id="jobPeriod_37"]') 
        self.IPP = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobClosurePrivate\')"]')
        self.PATRIMONIAL_TAX = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobTax_wealth\')"]')
        self.PP = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobTax\')"]')
        self.PP_SELECT =    (By.XPATH, '//*[@id="jobPeriod_42"]') 
        self.PERIODIC_PLANNING = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobMonthlyPlanning\')"]')
        self.PERIODIC_PLANNING_PERIODE = (By.XPATH, '//*[@id="jobPeriod_49"]') 
        self.PERIODIC_PLANNING_OFFSET = (By.XPATH, '//*[@id="jobOffset_49"]') 
        self.UBO_INFORMATION = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobUbo_infoCli\')"]')
        self.UBO_REGISTER = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobUbo_register\')"]')
        self.FINANCIAL_STATE = (By.XPATH, '//div[@ng-click="toggleIsActiveJob(\'jobFinStand\')"]')
        self.PERIODIC_PLANNING_PERIODE = (By.XPATH, '//*[@id="jobPeriod_35"]') 
        self.PERIODIC_PLANNING_OFFSET = (By.XPATH, '//*[@id="jobOffset_35"]')  


    def create_client(self, c):
        # NAME
        self.insert_text("insert text in name", self.NAME, c['name'])
        # JUDICIAL FORM
        self.select_text("select judicial_form", self.JUDICIAL_FORM, self.JUDICIAL_NAME, True)
        # BCE
        self.insert_text("insert value in bce", self.BCE, c['bce'])
        # TVa
        self.insert_text("insert value in tva", self.VAT, c['tva'])
        # LANG
        self.selectNG_text("select lang", self.LANG, "Nederlands")
        # WALLET
        self.selectNG_text("select wallet", self.WALLET, "Portefeuille")
        # ASSOC
        self.select_text("select assoc", self.ASSOC, c['assoc'])
        # RESP
        self.select_text("select resp", self.RESP, c['resp'])
        # ASSIS
        self.select_text("select assis", self.ASSIS, c['assis'])
        # RESP LED
        self.select_text("select resp leg", self.RESP_LEG, c['resp_leg'])
        # ASSIS LEG
        self.select_text("select assis_leg", self.ASSISS_LEG, c['assis_leg'])
        # ADDRESS 1
        self.insert_text("insert text in adress 1", self.ADDRESS_LINE1, c['address_1'])
        # ADDRESS BOX
        self.insert_text("insert text in adress box", self.ADDRESS_BOX, c['address_box'])
        # ADDRESS 2
        self.insert_text("insert text in adress 2", self.ADDRESS_LINE2, c['address_2'])
        # ADDRESS 3
        self.insert_text("insert text in adress 3", self.ADDRESS_LINE3, c['address_3'])
        # ADDRESS CITY
        self.insert_text("insert text in adress ville", self.ADDRESS_CITY, c['address_city'])
        # ADDRESS ZIP
        self.insert_text("insert text in adress cp", self.ADDRESS_ZIP, c['address_zip'])
        # ADDRESS COUNTRY
        #self.selectNG_text("select address_country", self.ADDRESS_COUNTRY, c['address_country'])

        self.checkbox_click("check on VAT declaration", self.VAT_DECLARATION)
        self.checkbox_click("check on annual listing", self.ANNUAL_LISTING)
        self.checkbox_click("check on closure company", self.CLOSURE_COMPANY)
        self.checkbox_click("check on IPP", self.IPP)
        self.checkbox_click("check on patrimonial tax", self.PATRIMONIAL_TAX)
        self.checkbox_click("check on PP", self.PP)
        self.checkbox_click("check on periodic planning", self.PERIODIC_PLANNING)
        self.checkbox_click("check on UBO information ", self.UBO_INFORMATION)
        self.checkbox_click("check on UBO register", self.UBO_REGISTER)
        self.checkbox_click("check on financial state", self.FINANCIAL_STATE)


class FidNewClientPPI(FidNewClient):
    
    def __init__(self, d):
        FidNewClient.__init__(self)
        self.driver = d


class FidNewClientPP(FidNewClient):

    def __init__(self, d):
        FidNewClient.__init__(self)
        self.driver = d


class FidNewClientSComm(FidNewClient):
    
    def __init__(self, d):
        FidNewClient.__init__(self)
        self.driver = d




class Fid(SeleniumClass):
    USER =       (By.XPATH,'//*[@id="email"]')
    PASSWORD =  (By.XPATH,'//*[@id="password"]')
    BTN_SUBMIT =  (By.XPATH,'//*[@id="submit"]')
    MENU_CLIENT = (By.XPATH, '//*[@id="pageMenu"]/ul/li[2]/span')
    MENUITEM_ADD_CLIENT = (By.XPATH, '//*[@id="clientAddMenuItem"]/a')

    def __init__(self, d):
        self.driver = d
        self.fnc = FidNewClientSRL(self.driver)

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