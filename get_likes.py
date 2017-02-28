from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = ''
pwd = ''

def setup(phantom=False):
    if not phantom:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications":2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options = chrome_options)
    else:
        driver = webdriver.PhantomJS()
    driver.get('http://www.facebook.org')
    return driver

def login(driver):
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)

def likes(driver, id=''):
    driver.get('https://www.facebook.com/' + id)
    try:
        driver.find_element_by_class_name('profilePic').click()
        likes = driver.find_elements_by_class_name('_4arz')[1].text
    except Exception:
        likes = 0
    return likes

def quit(driver):
    driver.quit()

# my_driver = setup()
# login(my_driver)
# print(likes(my_driver))
# quit(my_driver)