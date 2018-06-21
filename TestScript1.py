from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import TestData
import time

class classScript1:
    def _init_self(self):
        pass

    #Registration Step 1: Enter personal information
    def sign_in(self):
        try:
            #Step: Open the System Under Test
            global driver, wait, elem
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get("https://test-consumer.commutyble.com/#/")
            wait = WebDriverWait(driver, 10)
            elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Login')]")))
            print("Log: System Under Test opened!")

            #Step: User Sign in
            driver.find_element_by_xpath("//a[@href = '/login']").click()
            driver.find_element_by_xpath("//input[@name = 'email']").send_keys(TestData.email)
            driver.find_element_by_xpath("//input[@name = 'password']").send_keys(TestData.password)
            print("Log: Email and Password entered")
            driver.find_element_by_xpath("//button[@class='btn btn-primary btn-md btn-block']").click()
            elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/home']")))
            print("Log:----Verifying Sign In---- ")
            if elem.is_displayed():
                print("Log: [CheckPoint]: Sign In - [Test Passed]")
            else:
                print("Log: [CheckPoint]: Sign In - [Test Failed]")

        except Exception as e:
            print(e)
            time.sleep(5)
            driver.quit()

    def edit_profile(self):
        try:
            #Step: Edit Profile
            elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/home']")))
            driver.find_element_by_xpath("//*[contains(text(), 'Profile')]").click()
            print("Log: Profile page opened")

            elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Edit')]")))
            driver.find_element_by_xpath("//button[contains(text(), 'Edit')]").click()
            print("Log: Edit Basic Info triggered")

            elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'first_name']")))
            first_name = driver.find_element_by_xpath("//input[@name = 'first_name']")
            first_name.clear()
            first_name.send_keys("Myles M")

            last_name = driver.find_element_by_xpath("//input[@name = 'last_name']")
            last_name.clear()
            last_name.send_keys("SP Tester")

            address1 = driver.find_element_by_xpath("//input[@name = 'address1']")
            address1.clear()
            address1.send_keys("701 1st Ave")

            city = driver.find_element_by_xpath("//input[@name = 'city']")
            city.clear()
            city.send_keys("Sunnyvale")

            postal_code = driver.find_element_by_xpath("//input[@name = 'postal_code']")
            postal_code.clear()
            postal_code.send_keys("90210")

            phone_number = driver.find_element_by_xpath("//input[@name = 'phone_number']")
            phone_number.clear()
            phone_number.send_keys("9171234567")
            print("Log: Basic Info entered")

            driver.find_element_by_xpath("//*[contains(text(), 'Save')]").click()
            print("Log: Saving Basic Info...")

            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'OK')]")))
            elem = driver.find_element_by_xpath("//*[contains(text(),'OK')]")

            print("Log:----Verifying Edit Basic Info---- ")
            if elem.is_displayed():
                print("Log: [CheckPoint]: Edit Basic Info - [Test Passed]")
            else:
                print("Log: [CheckPoint]: Edit Basic Info - [Test Failed]")
            elem.click()

        except Exception as e:
            print(e)
            time.sleep(5)
            driver.quit()


    def edit_security(self):
        try:
            #Step: Edit security
            # driver.find_element_by_xpath("//*[contains(text(), 'Profile')]").click()
            driver.find_element_by_xpath("//a[@href='/personal/security']").click()

            driver.find_element_by_xpath("//input[@name='current_password']").send_keys(TestData.password)
            driver.find_element_by_xpath("//input[@name='new_password']").send_keys(TestData.new_password)
            driver.find_element_by_xpath("//input[@name='password_confirmation']").send_keys(TestData.new_password)

            driver.find_element_by_xpath("//button[contains(text(), 'Update Password')]").click()
            time.sleep(5)

            elem = driver.find_element_by_xpath("//*[contains(text(),'OK')]")

            print("Log:----Verifying Edit Security---- ")
            if elem.is_displayed():
                print("Log: [CheckPoint]: Edit Security - [Test Passed]")
            else:
                print("Log: [CheckPoint]: Edit Security - [Test Failed]")
            elem.click()


        except Exception as e:
            print(e)
            time.sleep(5)
            driver.quit()

    def sign_in_new_password(self):
        try:
            #Step: Edit security
            driver.find_element_by_xpath("//input[@name = 'email']").send_keys(TestData.email)
            driver.find_element_by_xpath("//input[@name = 'password']").send_keys(TestData.new_password)
            print("Log: Email and New Password entered")
            driver.find_element_by_xpath("//button[@class='btn btn-primary btn-md btn-block']").click()
            elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/home']")))
            print("Log:----Verifying Sign In with New Password---- ")
            if elem.is_displayed():
                print("Log: [CheckPoint]: Sign In with New Password - [Test Passed]")
            else:
                print("Log: [CheckPoint]: Sign In with New Password - [Test Failed]")

        except Exception as e:
            print(e)
            time.sleep(5)
            driver.quit()

    def edit_security_revert_password(self):
        try:
            #Step: Edit security
            # time.sleep(3)
            driver.find_element_by_xpath("//*[contains(text(), 'Profile')]").click()
            elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Edit')]")))                        
            driver.find_element_by_xpath("//a[@href='/personal/security']").click()

            driver.find_element_by_xpath("//input[@name='current_password']").send_keys(TestData.new_password)
            driver.find_element_by_xpath("//input[@name='new_password']").send_keys(TestData.password)
            driver.find_element_by_xpath("//input[@name='password_confirmation']").send_keys(TestData.password)

            driver.find_element_by_xpath("//button[contains(text(), 'Update Password')]").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'OK')]")))
            elem = driver.find_element_by_xpath("//*[contains(text(),'OK')]")

            print("Log:----Reverting Password---- ")
            if elem.is_displayed():
                print("Log: [CheckPoint]: Revert Password - [Test Passed]")
            else:
                print("Log: [CheckPoint]: Revert Password - [Test Failed]")
            elem.click()

        except Exception as e:
            print(e)
            time.sleep(5)
            driver.quit()
