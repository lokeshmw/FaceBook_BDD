#
#
# from behave import given, when, then
# from selenium.common import NoSuchElementException
# from features.pages.login_page import LoginPage
# from utilities.logger import log_as_json
# import logging
#
# logging.basicConfig(filename='facebook_login_logs.json', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
#
# logger = logging.getLogger(__name__)
#
#
# @given(u'The Facebook login page is loaded')
# def step_impl(context):
#     context.Login_page = LoginPage(context.driver)
#     log_as_json("facebook_login_logs.json", "Facebook login page loaded successfully.")
#
#
# @given(u'The user and test details for login')
# def step_impl(context):
#     context.Login_page = LoginPage(context.driver)
#     log_as_json("facebook_login_logs.json", "User and test details for login retrieved.")
#
#
# @when(u'the user attempts to login with "{email}" and "{password}"')
# def step_impl(context, email, password):
#     context.Login_page.enter_email(email)
#     context.Login_page.enter_password(password)
#     context.Login_page.click_login()
#     log_as_json("facebook_login_logs.json",
#                 f"User attempted login with email: {email} and password : {password}.")
#
#
# @when(u'the user attempts to login with phone "{phone}" and "{password}"')
# def step_impl(context, phone, password):
#     context.Login_page.enter_email(phone)
#     context.Login_page.enter_password(password)
#     context.Login_page.click_login()
#     log_as_json("facebook_login_logs.json",
#                 f"User attempted login with phone: {phone} and password : {password}.")
#
#
# @when(u'the user attempts to login with empty fields')
# def step_impl(context):
#     context.Login_page.click_login()
#     log_as_json("facebook_login_logs.json", "User attempted login with empty fields.")
#
#
# @when(u'the user attempts to login with "{data}" and empty password')
# def step_impl(context, data):
#     context.Login_page.enter_email(data)
#     context.Login_page.click_login()
#     log_as_json("facebook_login_logs.json", f"User attempted login with data: {data} and empty password.")
#
#
# @then(u'the user should get a "We couldn\'t find an account that matches what you entered, but we\'ve found one that '
#       u'closely matches."')
# def step_impl(context):
#     expected_error = ("We couldn't find an account that matches what you entered, but we've found one that closely "
#                       "matches.")
#     log_as_json("facebook_login_logs.json", "Verifying expected error message(s).")  # Log verification attempt
#     try:
#         context.Login_page.verify_email_error(expected_error)
#         log_as_json("facebook_login_logs.json", f"Received expected error message: {expected_error}")
#     except NoSuchElementException:
#         log_as_json("facebook_login_logs.json", "Error message verification failed. Element not found.")
#
#
# @then(u'the user should get a "Welcome to Facebook"')
# def step_impl(context):
#     expected_message = "Welcome to Facebook"
#     log_as_json("facebook_login_logs.json", "Verifying expected success message.")  # Log verification attempt
#     try:
#         context.Login_page.verify_login(expected_message)
#         log_as_json("facebook_login_logs.json", f"Received expected success message: {expected_message}")
#     except NoSuchElementException:
#         log_as_json("facebook_login_logs.json", "Success message verification failed. Element not found.")
#
#
# @then(u'the user should get a "The email address you entered isn\'t connected to an account."')
# def step_impl(context):
#     expected_error1 = "The email address you entered isn\'t connected to an account."
#     expected_error2 = ("The email address or mobile number you entered isn\'t connected to an account. Find your "
#                        "account and log in.")
#     log_as_json("facebook_login_logs.json", "Verifying expected error message(s).")  # Log verification attempt
#     try:
#         context.Login_page.verify_phone_error(expected_error1)  # Try verifying with expected_error1 first (email case)
#         log_as_json("facebook_login_logs.json", f"Received expected error message: {expected_error1}")
#     except NoSuchElementException:
#         try:
#             context.Login_page.verify_phone_error(expected_error2)  # If not found, try expected_error2 (phone case)
#             log_as_json("facebook_login_logs.json", f"Received expected error message: {expected_error2}")
#         except NoSuchElementException:
#             log_as_json("facebook_login_logs.json", "Error message verification failed. Element not found.")
# @then(u'the user should get a "The email address or mobile number you entered isn\'t connected to an account. Find your account and log in."')
# def step_impl(context):
#     expected_error1 = "The email address you entered isn\'t connected to an account."
#     expected_error2 = ("The email address or mobile number you entered isn\'t connected to an account. Find your "
#                        "account and log in.")
#     log_as_json("facebook_login_logs.json", "Verifying expected error message(s).")  # Log verification attempt
#     try:
#         context.Login_page.verify_phone_error(expected_error1)  # Try verifying with expected_error1 first (email case)
#         log_as_json("facebook_login_logs.json", f"Received expected error message: {expected_error1}")
#     except NoSuchElementException:
#         try:
#             context.Login_page.verify_phone_error(expected_error2)  # If not found, try expected_error2 (phone case)
#             log_as_json("facebook_login_logs.json", f"Received expected error message: {expected_error2}")
#         except NoSuchElementException:
#             log_as_json("facebook_login_logs.json", "Error message verification failed. Element not found.")
#
#
# @then(u'the user should get a "The password you\'ve entered is incorrect."')
# def step_impl(context):
#     expected_error = "The password you've entered is incorrect."  # Replace with the actual expected error message
#     log_as_json("facebook_login_logs.json", "Verifying expected error message(s).")  # Log verification attempt
#
#     try:
#         context.Login_page.verify_password_error(expected_error)  # Replace with the appropriate verification method
#         log_as_json("facebook_login_logs.json", f"Received expected error message: {expected_error}")
#     except NoSuchElementException:
#         log_as_json("facebook_login_logs.json", "Error message verification failed. Element not found.")
