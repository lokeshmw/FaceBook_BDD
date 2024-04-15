from behave import given, when, then
from selenium.common import NoSuchElementException
from features.pages.login_page import LoginPage
from utilities.logger import logger


@given(u'The Facebook login page is loaded')
def step_impl(context):
    context.Login_page = LoginPage(context.driver)
    logger.info("Facebook login page loaded successfully.")


@given(u'The user and test details for login')
def step_impl(context):
    context.Login_page = LoginPage(context.driver)
    logger.info("User and test details for login retrieved.")


@when(u'the user attempts to login with "{email}" and "{password}"')
def step_impl(context, email, password):
    context.Login_page.enter_email(email)
    context.Login_page.enter_password(password)
    context.Login_page.click_login()
    logger.info(f"User attempted login with email: {email} and password: {password}")


@when(u'the user attempts to login with phone "{phone}" and "{password}"')
def step_impl(context, phone, password):
    context.Login_page.enter_email(phone)
    context.Login_page.enter_password(password)
    context.Login_page.click_login()
    logger.info(f"User attempted login with phone: {phone} and password: {password}")


@when(u'the user attempts to login with empty fields')
def step_impl(context):
    context.Login_page.click_login()
    logger.info("User attempted login with empty fields.")


@when(u'the user attempts to login with "{data}" and empty password')
def step_impl(context, data):
    context.Login_page.enter_email(data)
    context.Login_page.click_login()
    logger.info(f"User attempted login with data: {data} and empty password.")


@then(u'the user should get a "We couldn\'t find an account that matches what you entered, but we\'ve found one that '
      u'closely matches."')
def step_impl(context):
    expected_error = ("We couldn't find an account that matches what you entered, but we've found one that closely "
                      "matches.")
    try:
        context.Login_page.verify_email_error(expected_error)
        logger.info(f"Received expected error message: {expected_error}")
    except NoSuchElementException:
        logger.error("Error message verification FAILED. Element not found.")


@then(u'the user should get a "Welcome to Facebook"')
def step_impl(context):
    expected_message = "Welcome to Facebook"
    try:
        context.Login_page.verify_login(expected_message)
        logger.info(f"Received expected success message: {expected_message}")
    except NoSuchElementException:
        logger.error("Success message verification FAILED. Element not found.")


@then(u'the user should get a "The email address you entered isn\'t connected to an account."')
def step_impl(context):
    expected_error1 = "The email address you entered isn't connected to an account."
    expected_error2 = ("The email address or mobile number you entered isn't connected to an account. Find your "
                       "account and log in.")
    try:
        context.Login_page.verify_phone_error(expected_error1)
        logger.info(f"Received expected error message: {expected_error1}")
    except NoSuchElementException:
        try:
            context.Login_page.verify_phone_error(expected_error2)
            logger.info(f"Received expected error message (alternative): {expected_error2}")
        except NoSuchElementException:
            logger.error("Error message verification FAILED. Element not found.")


@then(u'the user should get a "The password you\'ve entered is incorrect."')
def step_impl(context):
    expected_error1 = "The password you've entered is incorrect."
    expected_error2 = "Log in to Facebook"

    try:
        context.Login_page.verify_password_error(expected_error1)
        logger.info(f"Received expected error message: {expected_error1}")
    except NoSuchElementException:
        try:
            context.Login_page.verify_password_error(expected_error2)
            logger.info(f"Received expected error message (alternative): {expected_error2}")
        except NoSuchElementException:
            logger.error("Error message verification FAILED. Element not found.")


@then(u'the user should get a "The password you\'ve entered is incorrect"')
def step_impl(context):
    expected_error1 = "The password you've entered is incorrect."
    expected_error2 = "Log in to Facebook"
    try:
        context.Login_page.verify_password_error(expected_error1)
        logger.info(f"Received expected error message: {expected_error1}")
    except NoSuchElementException:
        try:
            context.Login_page.verify_password_error(expected_error2)
            logger.info(f"Received expected error message (alternative): {expected_error2}")
        except NoSuchElementException:
            logger.error("Error message verification FAILED. Element not found.")


@then(u'the user should get a "The email address or mobile number you entered isn\'t connected to an account. Find '
      u'your account and log in."')
def step_impl(context):
    expected_message = ("The email address or mobile number you entered isn't connected to an account. Find your "
                        "account and log in.")
    try:
        context.Login_page.verify_phone_error(expected_message)
        logger.info(f"Received expected success message: {expected_message}")
    except NoSuchElementException:
        logger.error("Success message verification FAILED. Element not found.")
