# from behave import given, when, then
# from selenium.common import NoSuchElementException
#
# from features.pages.login_page import LoginPage
#
#
# @given(u'The Facebook login page is loaded')
# def step_impl(context):
#     context.Login_page = LoginPage(context.driver)
#
#
# @given(u'The user and test details for login')
# def step_impl(context):
#     context.Login_page = LoginPage(context.driver)
#
#
# @when(u'the user attempts to login with "{email}" and "{password}"')
# def step_impl(context, email, password):
#     context.Login_page.enter_email(email)
#     context.Login_page.enter_password(password)
#     context.Login_page.click_login()
#
#
# @when(u'the user attempts to login with phone "{phone}" and "{password}"')
# def step_impl(context, phone, password):
#     context.Login_page.enter_email(phone)
#     context.Login_page.enter_password(password)
#     context.Login_page.click_login()
#
#
# @when(u'the user attempts to login with empty fields')
# def step_impl(context):
#     context.Login_page.click_login()
#
#
# @when(u'the user attempts to login with "{data}" and empty password')
# def step_impl(context, data):
#     context.Login_page.enter_email(data)
#     context.Login_page.click_login()
#
#
# @then(u'the user should get a "We couldn\'t find an account that matches what you entered, but we\'ve found one that '
#       u'closely matches."')
# def step_impl(context):
#     context.Login_page.verify_email_error("We couldn't find an account that matches what you entered, but we've found "
#                                           "one that closely matches.")
#
#
# @then(u'the user should get a "Welcome to Facebook"')
# def step_impl(context):
#     context.Login_page.verify_login("Welcome to Facebook")
#
#
# @then(u'the user should get a "The email address you entered isn\'t connected to an account."')
# def step_impl(context):
#     try:
#         context.Login_page.verify_phone_error("The email address you entered isn't connected to an account. ")
#     except NoSuchElementException:
#         context.Login_page.verify_phone_error("The email address or mobile number you entered isn't connected to an "
#                                               "account. Find your account and log in.")
#
#
# @then(u'the user should get a "The password you\'ve entered is incorrect."')
# def step_impl(context):
#     try:
#         context.Login_page.verify_password_error("The password you've entered is incorrect.")
#     except NoSuchElementException:
#         context.Login_page.verify_Password_error_("Log in to Facebook")
#
#
# @then(u'the user should get a "The password you\'ve entered is incorrect"')
# def step_impl(context):
#     try:
#         context.Login_page.verify_password_error("The password you've entered is incorrect.")
#     except NoSuchElementException:
#         context.Login_page.verify_Password_error_("Log in to Facebook")
#
#
# @then(u'the user should get a "The email address or mobile number you entered isn\'t connected to an account. Find '
#       u'your account and log in."')
# def step_impl(context):
#     context.Login_page.verify_phone_error("The email address or mobile number you entered isn't connected to an "
#                                           "account. Find your account and log in.")
