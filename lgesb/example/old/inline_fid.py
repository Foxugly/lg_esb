import getpass
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_sleep(i=10):
        time.sleep(i)


c = {'name':"coucou", 'judicial_form':"Personne physique", 'assoc':"Alexander", 'resp':"Alexandru"}
p = getpass.getpass("password : ")
url = 'https://website.com'
u = 'username'
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

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
url = url
user = u
password = p 
driver.get(url)
driver.find_element_by_id('email').send_keys(user)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('submit').click()
get_sleep()
menu = driver.find_element_by_xpath('//*[@id="pageMenu"]/ul/li[2]/span')
menu.click()
get_sleep()
menuitem_add_client = driver.find_element_by_xpath('//*[@id="clientAddMenuItem"]/a')
menuitem_add_client.click()
get_sleep()
# NAME
driver.find_element(*NAME).send_keys(c['name'])
# JUDICIAL FORM
jf = driver.find_element(*JUDICIAL_FORM)
jf.send_keys(c['judicial_form'])
get_sleep(5)
jf.send_keys(Keys.TAB)
# ASSOC
assoc = driver.find_element(*ASSOC)
#assoc.click()
assoc.send_keys(c['assoc'])
get_sleep(5)
assoc.send_keys(Keys.ENTER)
get_sleep(5)
# RESP
resp = driver.find_element(*RESP)
#resp.click()
resp.send_keys(c['resp'])
get_sleep(5)
resp.send_keys(Keys.ENTER)
get_sleep(5)
# ASSIS

# RESP_LEG

# ASSISS_LEG

# ADDRESSE_LINE1
print("fin")