from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Locators_Facebook import *

def test_Facebook_ForgetPassword_with_correct_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword).click()
    # Click Forget Password link
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount).text
    # Display Find Your Account page
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    identifyEmail = driver.find_element(By.XPATH,IdentifyEmail_Element)
    # Enter Email address
    sleep(2)
    identifyEmail.clear()
    identifyEmail.send_keys(ForgetPassword_Valid_Email)
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()  # Click Search button
    sleep(2)
    IdentifyYourAccount_Page = driver.find_element(By.XPATH,IdentifyYourAccount_Element).text
    # Display Identify your account Page
    assert "Identify your account" == IdentifyYourAccount_Page
    sleep(2)
    driver.find_element(By.XPATH,MyAccount_Button).click()
    # Click This is my account button
    sleep(2)
    ResetYourPassword_Page = driver.find_element(By.XPATH,ResetYourPasswordPage_Element).text
    # Display Reset Your Password Page
    assert 'Reset Your Password' == ResetYourPassword_Page
    driver.find_element(By.XPATH,SendCodeViaEmailButton_Element).click()
    # Select "Send code via email" button
    sleep(2)
    driver.find_element(By.XPATH,ResetPassword_continueButton).click()
    # Click on Continue Button
    sleep(2)
    securityCodePage = driver.find_element(By.XPATH,EnterSecurityCodePage_Element).text
    # Display Enter security code page
    assert "Enter security code" == securityCodePage
    sleep(2)
    recovery_code_entry = driver.find_element(By.XPATH,RecoveryCodeEntry_Element)  # Recovery Code Entry
    sleep(2)
    recovery_code_entry.clear()
    recovery_code_entry.send_keys("740515")
    sleep(2)
    driver.find_element(By.XPATH,ResetPassword_continueButton).click()
    # Click on Continue Button
    sleep(2)
    newPassword_Page = driver.find_element(By.XPATH,NewPasswordPage_Element).text
    # Display New Password page
    assert "Choose a new password" == newPassword_Page
    newpassword_entry = driver.find_element(By.NAME, "password_new")
    newpassword_entry.send_keys("password1234")
    sleep(2)
    driver.find_element(By.XPATH,NewPassword_ContinueButton).click()
    # Click Continue Button
    sleep(2)
    Facebook_Home = driver.current_url
    # Display Facebook User Home page
    assert Facebook_Home == Facebook_Web_Address
    driver.close()
def test_Facebook_ForgetPassword_with_Incorrect_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword).click()
    # Click Forget Password link
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount).text
    # Display Find Your Account page
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    identifyEmail = driver.find_element(By.XPATH,IdentifyEmail_Element)  # Enter Email address
    sleep(2)
    identifyEmail.clear()
    identifyEmail.send_keys(ForgetPassword_Invalid_Email)  # email address
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()  # Click Search button
    sleep(2)
    errorMessage = driver.find_element(By.XPATH,NoSearchResults_ErrorMessage).text
    # Display Error Message
    assert "No search results" == errorMessage
    driver.close()
def test_Facebook_ForgetPassword_with_Null_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    sleep(2)
    driver.find_element(By.XPATH, ForgetPassword).click()
    # Click Forget Password
    sleep(2)
    findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount).text
    # Display Find Your Account page.
    assert "Find Your Account" == findYourAccount_Page
    sleep(2)
    driver.find_element(By.XPATH,Email_Search_Button).click()  # Click Search button
    sleep(2)
    IdentifyYourAccount_Page = driver.find_element(By.XPATH,PleaseFillInAtLeastOneField_ErrorMessage).text
    # Display Error Message
    assert "Please fill in at least one field" == IdentifyYourAccount_Page
    driver.close()