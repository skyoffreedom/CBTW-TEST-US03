from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


import time


desired_capabilities = {
    'platformName': 'Android',
    'deviceName': 'Thuan S23 Ultra',
    'app': 'Users/thien/Desktop/CBTW Test/Automation/Mobile US03 Python/src',
    'appPackage': 'com.exness.android.pa',
    'appActivity': 'com.exness.android.pa.MainActivity',
    'automationName': 'UiAutomator2'
}

# Create Appium driver instance
app_options = UiAutomator2Options()
app_options.load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://localhost:4723/wd/hub', options=app_options)


def login(email, password):
    login_start_button = driver.find_element((AppiumBy.ID, "signInView"))
    login_start_button.click()
    time.sleep(5)

    email_field = driver.find_element(AppiumBy.ID, "emailInput")
    email_field.send_keys(email)

    password_field = driver.find_element(AppiumBy.ID, "passwordInput")
    password_field.send_keys(password)

    login_button = driver.find_element(AppiumBy.ID, "signInButton")
    login_button.click()

    passcode_field = driver.find_element((AppiumBy.ID, "num1"))
    for _ in range (6):
        passcode_field.click()
    time.sleep(5)

    for _ in range (6):
        passcode_field.click()


def view_portfolio():
    time.sleep(5)
    portfolio_button = driver.find_element(AppiumBy.ID,
                                           "nameView")
    portfolio_button.click()

    time.sleep(5)
    portfolio_title = driver.find_element(AppiumBy.ID,
                                          "accountNameView")
    assert portfolio_title.is_displayed()


login("tbservice133@gmail.com", "Tbservice@133")
view_portfolio()

driver.quit()