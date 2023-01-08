from selenium import webdriver
from selenium.webdriver.common.by import By
from facebook.base_test.login_locatories import *
from time import sleep

def test_Facebook_Login_with_Correct_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address)
    sleep(2)
    email.clear()
    email.send_keys(Login_correct_Email)
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password)
    sleep(2)
    password.clear()
    password.send_keys(Login_correct_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()
    # Click login button
    sleep(5)
    Facebook_Home = driver.current_url
    assert Facebook_Home == Facebook_Web_Address
    driver.close()
def test_Facebook_Login_with_InCorrect_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address)
    sleep(2)
    email.clear()
    email.send_keys(Login_Incorrect_Email)
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password)
    sleep(2)
    password.clear()
    password.send_keys(Login_Incorrect_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()
    # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_Incorrect_EmailAndPassword_ErrorMessage).text
    assert 'invalid username or password' == Error_message
    sleep(5)
    driver.close()
def test_Facebook_Login_with_Correct_Email_and_Incorrect_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address)
    sleep(2)
    email.clear()
    email.send_keys(Login_correct_Email)
    sleep(2)
    password = driver.find_element(By.XPATH, input_login_Password)
    sleep(2)
    password.clear()
    password.send_keys(Login_Incorrect_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()
    # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_correctEmail_And_InvalidPassword_ErrorMessage).text
    assert 'invalid username or password' == Error_message
    sleep(5)
    driver.close()
def test_Facebook_Login_with_Incorrect_Email_and_correct_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    email = driver.find_element(By.XPATH, Input_Login_Email_Address)
    sleep(2)
    email.clear()
    email.send_keys(Login_Incorrect_Email)
    sleep(2)
    password = driver.find_element(By.XPATH,input_login_Password)
    sleep(2)
    password.clear()
    password.send_keys(Login_correct_Password)
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()
    # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_IncorrectEmail_And_ValidPassword_ErrorMessage).text
    assert 'invalid username or password' == Error_message
    sleep(5)
    driver.close()
def test_Facebook_Login_with_incorrect_Email_and_Password():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, Login_Button).click()
    # Click login button
    sleep(2)
    Error_message = driver.find_element(By.XPATH, Login_Blank_EmailAndPassword_ErrorMessage).text
    assert "Find your account and log in." == Error_message
    sleep(5)
    driver.close()