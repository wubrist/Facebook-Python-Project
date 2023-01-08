from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators_Facebook import *
from time import sleep

def test_Facebook_correct_Registering_with_correct_informations():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_Page).text
    # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("wubrist")  # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME,LastName_Element)
    surname_box.send_keys("asnakew")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("your email@************************.com")
    # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_Element)
    registerReEnterEmail_box.send_keys("your email@*******************.com")
    # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("password1234")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthDay_box.send_keys("5")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_Element)
    birthMonth_box.send_keys("july")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()
    # Click Sign Up Button
    sleep(5)
    email_conformation_Page = driver.find_element(By.XPATH,Email_ConformationPath).text
    # Display Email conformation page
    assert 'Enter the code from your email' == email_conformation_Page
    driver.close()
    enterConformationNumber = driver.find_element(By.NAME, "code")
    enterConformationNumber.send_keys("123456")
    # entering conformation number
    sleep(2)
    driver.find_element(By.XPATH,Continue_Button).click()  # Click Continue Button
    accountConform_page = driver.find_element(By.NAME,"Account Confirmed").text
    # Display Account conformation page
    assert 'Account Confirmed' == accountConform_page
    driver.find_element(By.XPATH,Ok_ButtonPath).click()  # Click Ok button
    Facebook_Home = driver.current_url
    # Display Facebook User Home page
    assert Facebook_Home == Facebook_Web_Address
    driver.close()


def test_Facebook_correct_Registering_with_Incorrect_informations():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()
    # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_nullAll).text
    # Display Error Message
    assert '************************' == error_Message
    driver.close()


def test_Facebook_correct_Registering_with_Incorrect_Email():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_Page).text
    # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("wubrist")  # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME,LastName_Element)
    surname_box.send_keys("asnakew")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("wubristasnakew@gmail.com")
    # entering email address
    registerEmail_box.send_keys("wubristasnakew@gmail.com")
    # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_Element)
    registerReEnterEmail_box.send_keys("wubristasnakew@gmail.com")
    # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("password1234")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthDay_box.send_keys("5")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_Element)
    birthMonth_box.send_keys("july")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1999")
    # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_InvalidEmail).text
    # Display Error Message
    assert '' == error_Message
    driver.close()


def test_Facebook_Validate_Registering_With_Null_Gender():

    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_Page).text
    # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("wubrist")
    # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME,LastName_Element)
    surname_box.send_keys("asnakew")
    # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("wubristasnakew12@gmail.com")
    # entering email address
    registerEmail_box.send_keys("wubristasnakew@gmail.com")
    # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_Element)
    registerReEnterEmail_box.send_keys("wubristasnakew@gmail.com")
    # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("password1234")  # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthDay_box.send_keys("5")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_Element)
    birthMonth_box.send_keys("jul")  # enter Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()  # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_nullGender).text
    # Display Error Message
    assert '*********************' == error_Message
    driver.close()



def test_Facebook_correct_Registering_with_Null_FirstName():

    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_Page).text
    # Display Signup page
    assert 'Sign Up' == signUp_Page
    surname_box = driver.find_element(By.NAME, LastName_Element)
    surname_box.send_keys("asnakew")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("wubristasnakew12@gmail.com")
    # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_Element)
    registerReEnterEmail_box.send_keys("wubristasnakew@gmail.com")
    # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("password1234")
    # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthDay_box.send_keys("5")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_Element)
    birthMonth_box.send_keys("july")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1999")
    # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_Element).click()
    # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()
    # Click Sign Up Button
    sleep(5)
    # Display Error Message
    error_Message = driver.find_element(By.XPATH,Error_nullFirstName).text
    # Display Error Message
    assert '*********************' == error_Message
    driver.close()


def test_Facebook_Registering_with_Null_LastName():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_Page).text
    # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("wubrist")  # entering first name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("your email@***************.com")
    # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_Element)
    registerReEnterEmail_box.send_keys("your email@**************.com")
    # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("password1234")
    # entering password
    sleep(2)
    birthDay_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthDay_box.send_keys("1")  # entering Birth Day
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_Element)
    birthMonth_box.send_keys("july")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1999")  # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_Element).click()
    # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()
    # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_nullLastName).text
    # Display Email conformation page
    assert '*******************' == error_Message
    driver.close()


def test_Facebook_Registering_with_Null_Birthday():
    driver = webdriver.Chrome()
    driver.get(Facebook_Web_Address)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, CreateNewAccount).click()
    # Click Create New Account button
    sleep(2)
    signUp_Page = driver.find_element(By.XPATH,SignUp_Page).text
    # Display Signup page
    assert 'Sign Up' == signUp_Page
    firstName_box = driver.find_element(By.NAME,FirstName_Element)
    firstName_box.send_keys("wubrist")
    # entering first name
    sleep(2)
    surname_box = driver.find_element(By.NAME, LastName_Element)
    surname_box.send_keys("asnakew")  # entering Last name
    sleep(2)
    registerEmail_box = driver.find_element(By.NAME,EmailInput_Element)
    registerEmail_box.send_keys("wubristasnakew@gmail.com")
    # entering email address
    sleep(2)
    registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_Element)
    registerReEnterEmail_box.send_keys("your email@*************.com")
    # entering Re-enter email address
    sleep(2)
    registerPassword_box = driver.find_element(By.NAME,Password_Element)
    registerPassword_box.send_keys("password1234")  # entering password
    sleep(2)
    birthMonth_box = driver.find_element(By.XPATH,BirthMonth_Element)
    birthMonth_box.send_keys("july")  # entering Birth Month
    sleep(2)
    birthYear_box = driver.find_element(By.XPATH,BirthDay_Element)
    birthYear_box.send_keys("1999")
    # entering Birth Year
    sleep(2)
    driver.find_element(By.XPATH,GenderSelect_Element).click()
    # Select Gender
    sleep(2)
    driver.find_element(By.XPATH,SignUp_Button).click()
    # Click Sign Up Button
    sleep(5)
    error_Message = driver.find_element(By.XPATH,Error_Birthday).text
    # Display Email conformation page
    assert '*************' == error_Message
    driver.close()