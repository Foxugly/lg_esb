#!/usr/bin/env python3
import getpass
import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_sleep():
    time.sleep(10)

def fid(driver, user, password):
    driver.get('https://lieutenantguillaume.fid-manager.be/')
    driver.find_element_by_id('email').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('submit').click()
    get_sleep()
    menu = driver.find_element_by_xpath('//*[@id="pageMenu"]/ul/li[2]/span')
    assert menu is not None
    menu.click() 
    get_sleep()
    menuitem_add_client = driver.find_element_by_xpath('//*[@id="clientAddMenuItem"]/a')
    assert menuitem_add_client is not None
    menuitem_add_client.click()
    get_sleep()
    col1 = '//div[contains(@class, "container")]/table/tbody'
    driver_col1 = driver.find_element_by_xpath(col1)
    assert col1 is not None
    for i in range(1, 8):
        path_label = '%s/tr[%s]/td[contains(@class, "cell-label")]/div' % (col1, i)
        e = driver.find_element_by_xpath(path_label).text
        path_input = '%s/tr[%s]/td[contains(@class, "cell-value")]' % (col1, i)
        print(path_input)
        div_input = driver.find_element_by_xpath(path_input)
        e_input = div_input.find_element_by_tag_name('input')
        if e in ["Full Name", "Nom Complet"]:
            print(e)
            e_input.send_keys("NAME")
        elif e in ["Legal form", "Forme juridique"]:

            e_input.send_keys("PP")
            e_input.send_keys(Keys.ENTER)
            print(e)
        elif e in ["CBE No.", "Nr. BCE"]:
            print(e)
            e_input.send_keys("0647566456")
        elif e == "NN":
            print(e)
            e_input.send_keys("83020414933")
        elif e in ["VAT", "TVA"]:
            print(e)
            e_input.send_keys("BE0647566456")
        elif e in ["Language", "Langue"]:
            print(e)
            e_input.send_keys("Fr")
            e_input.send_keys(Keys.ENTER)
        elif e in ["Portefeuille"]:
            print(e)
            e_input.send_keys("Po")
            e_input.send_keys(Keys.ENTER)

        elif e == "Responsible":
            print(e)
            e_input.send_keys("Alex")
            e_input.send_keys(Keys.ENTER)
        elif e == "Associate":
            print(e)
        elif e == "Assistant":
            print(e)

    address_box = driver_col1.find_element_by_tag_name('fieldset')
    addr_line1 = address_box.find_element_by_class_name('line1')
    addr_line1.send_keys("Ligne 1")
    addr_box = address_box.find_element_by_class_name('box')
    addr_box.send_keys("box")
    addr_line2 = address_box.find_element_by_class_name('line2')
    addr_line2.send_keys("Ligne 2")
    addr_city = address_box.find_element_by_class_name('city')
    addr_city.send_keys("Ixelles")
    addr_postal_code = address_box.find_element_by_class_name('postal-code')
    addr_postal_code.send_keys("1050")

    elem_job = driver_col1.find_elements_by_class_name("job")
    for i in range(0, int(len(elem_job) / 2)):
        div_label = elem_job[2 * i]
        div_ratio = elem_job[(2 * i) + 1]
        print("--------------- %s" % div_label.text)
        div_ratio.location_once_scrolled_into_view
        ratio = div_ratio.find_element_by_class_name('select-box')
        driver.execute_script("arguments[0].click();", ratio)
        time.sleep(2)
        if div_label.text == "VAT Planning":
            inputt = div_ratio.find_element_by_tag_name('input')
            time.sleep(5)
            select = div_ratio.find_element_by_class_name("selectedList").find_element_by_tag_name('span').click()
            time.sleep(5)
            inputt.send_keys('Quarterly')
            time.sleep(1)
            inputt.send_keys(Keys.ENTER)
        elif div_label.text == "VAT Listing":
            inputt = div_ratio.find_element_by_tag_name('input')
            time.sleep(5)
            select = div_ratio.find_element_by_class_name("selectedList").find_element_by_tag_name('span').click()
            time.sleep(5)
            inputt.send_keys('January')
            time.sleep(1)
            inputt.send_keys(Keys.ENTER)
        elif div_label.text == "Closure Company":
            inputt = div_ratio.find_element_by_tag_name('input')
            time.sleep(5)
            select = div_ratio.find_element_by_class_name("selectedList").click()
            time.sleep(5)
            inputt.send_keys('January')
            time.sleep(1)
            inputt.send_keys(Keys.ENTER)
        elif div_label.text == "Tax on Salary":
            inputt = div_ratio.find_element_by_tag_name('input')
            time.sleep(5)
            select = div_ratio.find_element_by_class_name("selectedList").find_element_by_tag_name('span').click()
            time.sleep(5)
            inputt.send_keys('Monthly')
            time.sleep(1)
            inputt.send_keys(Keys.ENTER)
        elif div_label.text == "Periodic planning":
            inputt = div_ratio.find_element_by_tag_name('input')
            div_ratio.find_element_by_class_name("selectedList").click()
            inputt.send_keys('Semi')
            time.sleep(1)
            inputt.send_keys(Keys.ENTER)
        elif div_label.text == "Financial Standing":
            div_period = div_ratio.find_element_by_class_name('client-proposal-job-period')
            time.sleep(5)
            inputt = div_period.find_element_by_tag_name('input')
            time.sleep(5)
            div_period.find_element_by_class_name("selectedList").find_element_by_tag_name('span').click()
            time.sleep(5)
            inputt.send_keys('Yearly')
            time.sleep(5)
            inputt.send_keys(Keys.ENTER)
            time.sleep(5)
            div_offset = div_ratio.find_element_by_class_name('client-proposal-job-offset')
            time.sleep(5)
            inputt = div_offset.find_element_by_tag_name('input')
            time.sleep(5)
            # div_offset.find_element_by_class_name("selectedList").click()
            # time.sleep(5)
            inputt.send_keys('March')
            time.sleep(1)
            inputt.send_keys(Keys.ENTER)
        print("----------------END")
    print("END")


if __name__ == "__main__":
    d = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    u = input('username')
    p = getpass.getpass("password : ")
    fid(d, u, p)
    d.close()
    d.quit()