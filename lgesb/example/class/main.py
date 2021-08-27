
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import getpass

from fid import Fid


c = {'name':"Foo", 'judicial_form':"Personne physique", 'assoc':"Alexander", 'resp':"Alexandru"}
u = input("username :")
p = getpass.getpass("password : ")
URL = "website.com"
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
f = Fid(driver)
f.auth(URL, u, p)
f.create_new_client(c)
print("fin")
