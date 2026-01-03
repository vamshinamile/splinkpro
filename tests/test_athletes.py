import pytest
import json
import time
import random
from pages.athletes_page import AthletesPage

with open("config.json") as f:
    config = json.load(f)
athlete = config["athlete"]
coach = config["coach"]
validations = config["validations"]


# email-Replace placeholder with dynamic value
timestamp = int(time.time())
dynamic_email = f"nvamshi2225+{timestamp}@gmail.com"
athlete['email'] = dynamic_email
# Generate a random 10-digit number starting with 9 (or any digit you prefer)
dynamic_mobile = f"9{random.randint(100000000, 999999999)}"
athlete['mobile'] = dynamic_mobile

# #------onboard athlete test cases------#

@pytest.mark.usefixtures("driver")
def test_click_on_athlete_tab_and_navigation_to_athlete_screen(driver):
    page = AthletesPage(driver)
    page.click_athlete_tab()

# @pytest.mark.usefixtures("driver")
# def test_click_on_actions_dropdown_and_select_select_add_athlete(driver):
#     page = AthletesPage(driver)
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()

# @pytest.mark.usefixtures("driver")
# def test_enter_athlete_details(driver):
#     page = AthletesPage(driver)
#     page.create_first_name(athlete["first_name"])
#     page.create_last_name(athlete["last_name"])
#     page.click_and_select_dob(athlete["year"])
#     page.click_and_select_gender()
#     page.create_email(athlete["email"])
#     page.create_mobile(athlete["mobile"])

# @pytest.mark.usefixtures("driver")
# def test_click_submit_athlete_details_button(driver):
#     page = AthletesPage(driver)
#     page.click_create_button()
#     page.toast_message("Successful")
# #------------------------------------------#
# @pytest.mark.usefixtures("driver")
# def test_existing_email_validation_error(driver):
#     page = AthletesPage(driver)
#     time.sleep(2)
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name(athlete["first_name"])
#     page.create_last_name(athlete["last_name"])
#     page.click_and_select_dob(athlete["year"])
#     page.click_and_select_gender()
#     page.create_email(athlete["email"])
#     page.create_mobile(athlete["mobile"])
#     page.click_create_button()
#     page.toast_message("already exists")
#     page.click_cancel_button()

# @pytest.mark.usefixtures("driver")
# def test_mandatory_field_validation_errors(driver):
#     page = AthletesPage(driver)
#     page.click_athlete_tab()
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.click_create_button()
#     page.validation_messages()
#     page.click_cancel_button()

# @pytest.mark.usefixtures("driver")
# def test_entered_athlete_details_for_name_validation(driver):
#     page = AthletesPage(driver)
#     page.click_athlete_tab()
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name(athlete["first_name"])
#     page.create_last_name(athlete["last_name"])
#     page.click_and_select_dob(athlete["year"])
#     page.click_and_select_gender()
#     page.create_email(validations["static_email"])
#     page.create_mobile(athlete["mobile"])

# @pytest.mark.usefixtures("driver")
# def test_athlete_first_name_field_minimum_length_validation(driver):
#     page = AthletesPage(driver)
#     #firt name validation
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["min_value"])
#     page.click_create_button()
#     page.validation_messages()

# @pytest.mark.usefixtures("driver")
# def test_athlete_first_name_field_maximum_length_validation(driver):
#     page = AthletesPage(driver)
#     #validate max value
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["max_value"])
#     page.click_create_button()
#     time.sleep(2)
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_athlete_first_name_field_invalid_number_validation(driver):
#     page = AthletesPage(driver)
#     #numeric value
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["Number"])
#     page.click_create_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_athlete_first_name_field_invalid_symbol_validation(driver):
#     page = AthletesPage(driver)
#     #numeric value
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(validations["symbol"])
#     page.click_create_button()
#     page.validation_messages()
#     page.clear_field(page.first_name_input)
#     time.sleep(1)
#     page.create_first_name(athlete["first_name"])

# @pytest.mark.usefixtures("driver")
# def test_athlete_last_name_field_minimum_length_validation(driver):
#     page = AthletesPage(driver)
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["min_value"])
#     page.click_create_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_athlete_last_name_field_maximum_length_validation(driver):
#     page = AthletesPage(driver)
#     #validate max value
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["max_value"])
#     page.click_create_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_athlete_last_name_field_invalid_number_validation(driver):
#     page = AthletesPage(driver)
#     #numeric value
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["Number"])
#     page.click_create_button()
#     page.validation_messages()

# @pytest.mark.usefixtures("driver")
# def test_athlete_last_name_field_invalid_symbol_validation(driver):
#     page = AthletesPage(driver)
#     #numeric value
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(validations["symbol"])
#     page.click_create_button()
#     page.validation_messages()
#     page.clear_field(page.last_name_input)
#     time.sleep(1)
#     page.create_last_name(athlete["last_name"])
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_email_field_invalid_email_validation(driver):
#     page = AthletesPage(driver)
#     #firt name validation
#     page.clear_field(page.email_input)
#     time.sleep(1)
#     page.create_email(validations["invalid_email"])
#     page.click_create_button()
#     page.validation_messages()
  
# @pytest.mark.usefixtures("driver")
# def test_email_field_invalid_number_validation(driver):
#     page = AthletesPage(driver)
#     #numeric value
#     page.clear_field(page.email_input)
#     time.sleep(1)
#     page.create_email(validations["Number"])
#     page.click_create_button()
#     page.validation_messages()
#     page.clear_field(page.email_input)
#     time.sleep(1)
#     page.create_email(validations["static_email"])
#     time.sleep(1)

# @pytest.mark.usefixtures("driver")
# def test_mobile_number_field_minimum_length_validation(driver):
#     page = AthletesPage(driver)
#     #firt name validation
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(validations["invalid_mobile_less9"])
#     page.click_create_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_mobile_number_field_invalid_text_validation(driver):
#     page = AthletesPage(driver)
#     #validate max value
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(validations["invalid_mobile_text"])
#     page.click_create_button()
#     page.validation_messages()
# @pytest.mark.usefixtures("driver")
# def test_mobile_number_field_invalid_mobile_starts_with_zero_validation(driver):
#     page = AthletesPage(driver)
#     #numeric value
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(validations["invalid_mobile_zero"])
#     page.click_create_button()
#     page.validation_messages()
#     page.clear_field(page.mobile_input)
#     time.sleep(1)
#     page.create_mobile(athlete["mobile"])
#     page.click_cancel_button()
#     time.sleep(1)


# @pytest.mark.usefixtures("driver")
# def test_enter_athlete_details_for_dob_validation(driver):
#     page = AthletesPage(driver)
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name(athlete["first_name"])
#     page.create_last_name(athlete["last_name"])
# @pytest.mark.usefixtures("driver")
# def test_dob_field_with_age_greater_than_70_validation(driver):
#     page = AthletesPage(driver)
#     #age above 70 yrs
#     page.click_and_select_dob(validations["age>70"])
#     page.click_and_select_gender()
#     page.create_email(validations["static_email"])
#     page.create_mobile(athlete["mobile"])
#     page.click_create_button()
#     page.validation_messages()
#     page.click_cancel_button()
#     time.sleep(2)
# @pytest.mark.usefixtures("driver")
# def test_dob_field_with_age_less_than_5_validation(driver):
#     page = AthletesPage(driver)
#     #age below 5 yrs
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name(athlete["first_name"])
#     page.create_last_name(athlete["last_name"])
#     page.click_and_select_dob(validations["age<5"])
#     time.sleep(1)
#     page.check_parent_guardian_heading_displayed()
#     page.click_cancel_button()




# #----duplicate email & mobile number validation while onboarding athlete----#
# #1. Athlete onboarded email & mobile user should not be used again as athlete
# @pytest.mark.usefixtures("driver")
# def test_existing_email_mobile_validation_error(driver):
#     page = AthletesPage(driver)
#     time.sleep(2)
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name(athlete["first_name"])
#     page.create_last_name(athlete["last_name"])
#     page.click_and_select_dob(athlete["year"])
#     page.click_and_select_gender()
#     page.create_email(athlete["email"])
#     page.create_mobile(athlete["mobile"])
#     page.click_create_button()
#     page.toast_message("already exists")
#     page.click_cancel_button()

# #2. Coach onboarded email & mobile user should be used for athlete onboard
# @pytest.mark.usefixtures("driver")
# def test_coach_email_mobile_can_be_used_for_athlete(driver):
#     page = AthletesPage(driver)
#     coach_email = coach["email"]
#     coach_mobile = coach["mobile"]
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("CoachAthlete")
#     page.create_last_name("Test")
#     page.click_and_select_dob(athlete["year"])
#     page.click_and_select_gender()
#     page.create_email(coach_email)
#     page.create_mobile(coach_mobile)
#     page.click_create_button()
#     page.toast_message("Successful")
#     page.click_cancel_button()

# #3. Athlete mobile number is unique but existing email should not be allowed while onboarding athlete
# @pytest.mark.usefixtures("driver")
# def test_existing_email_with_unique_mobile_should_fail(driver):
#     page = AthletesPage(driver)
#     unique_mobile = f"9{random.randint(100000000, 999999999)}"
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("EmailUniqueMobile")
#     page.create_last_name("Test")
#     page.click_and_select_dob(athlete["year"])
#     page.click_and_select_gender()
#     page.create_email(athlete["email"])  # existing email
#     page.create_mobile(unique_mobile)    # new mobile
#     page.click_create_button()
#     page.toast_message("already exists")
#     page.click_cancel_button()

# #4. Athlete email is unique but existing mobile should not be allowed while onboarding athlete
# @pytest.mark.usefixtures("driver")
# def test_unique_email_with_existing_mobile_should_fail(driver):
#     page = AthletesPage(driver)
#     unique_email = f"athlete{int(time.time())}@otsi.co.in"
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("MobileUniqueEmail")
#     page.create_last_name("Test")
#     page.click_and_select_dob(athlete["year"])
#     page.click_and_select_gender()
#     page.create_email(unique_email)         # new email
#     page.create_mobile(athlete["mobile"])   # existing mobile
#     page.click_create_button()
#     page.toast_message("already exists")
#     page.click_cancel_button()
# #5. Parent email & mobile number can be used multiple times while onbording athletes
# #5-1. Onboarding child athlete with parent email & mobile number
# @pytest.mark.usefixtures("driver")
# def test_onboard_child_athlete_with_unique_mail_and_mobile_and_parent_unique_details(driver):
#     page = AthletesPage(driver)
#     unique_email = f"nvamshi2225+{int(time.time())}@gmail.com"
#     unique_mobile = f"9{random.randint(100000000, 999999999)}"
#     parent_first_name = "ParentFirst"
#     parent_last_name = "ParentLast"
#     parent_dob = athlete["parent_year"]

#     # Store parent details for use in next test
#     global parent_email_5_1, parent_mobile_5_1, parent_first_name_5_1, parent_last_name_5_1, parent_dob_5_1
#     parent_email_5_1 = unique_email
#     parent_mobile_5_1 = unique_mobile
#     parent_first_name_5_1 = parent_first_name
#     parent_last_name_5_1 = parent_last_name
#     parent_dob_5_1 = parent_dob

#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("Child")
#     page.create_last_name("Child")
#     page.click_and_select_dob(athlete["child_year"])
#     page.click_and_select_gender()
#     page.create_email(unique_email)
#     page.create_mobile(unique_mobile)
#     page.create_parent_email(unique_email)
#     time.sleep(1)
#     page.create_parent_first_name(parent_first_name)
#     page.create_parent_last_name(parent_last_name)
#     page.click_and_select_parent__dob(parent_dob)
#     page.click_and_select_gender()
#     page.create_parent_mobile(unique_mobile)
#     page.click_create_button()
#     page.toast_message("Successful")

# #5-2. Onboarding another child2 athlete with same parent email & mobile number, check auto-filled parent details
# @pytest.mark.usefixtures("driver")
# def test_onboard_child2_with_same_parent_email_mobile_and_check_autofill(driver):
#     page = AthletesPage(driver)
#     child2_email = f"athlete{int(time.time())+1}@otsi.co.in"
#     child2_mobile = f"9{random.randint(100000000, 999999999)}"

#     # Use parent details from previous test
#     parent_email = globals().get("parent_email_5_1")
#     parent_mobile = globals().get("parent_mobile_5_1")
#     parent_first_name = globals().get("parent_first_name_5_1")
#     parent_last_name = globals().get("parent_last_name_5_1")

#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("Child2")
#     page.create_last_name("Child2")
#     page.click_and_select_dob(athlete["child_year"])
#     page.click_and_select_gender()
#     page.create_email(child2_email)
#     page.create_mobile(child2_mobile)
#     page.create_parent_email(parent_email)
#     time.sleep(1)

#     # Check auto-filled parent details
#     auto_first_name = page.get_parent_first_name()
#     auto_last_name = page.get_parent_last_name()
#     auto_mobile = page.get_parent_mobile()
#     print( "Auto-filled Parent First Name, Last Name, Mobile:", auto_first_name, auto_last_name, auto_mobile)
#     print( "Expected Parent First Name, Last Name, Mobile:", parent_first_name, parent_last_name, parent_mobile)
 
#     assert auto_first_name == parent_first_name, "Parent first name not auto-filled correctly"
#     assert auto_last_name == parent_last_name, "Parent last name not auto-filled correctly"
#     assert auto_mobile == parent_mobile, "Parent mobile not auto-filled correctly"

#     page.click_create_button()
#     page.toast_message("Successful")

# # #5-3. Onboarding child3 athlete without email and mobile number & add same parent email & mobile number
# @pytest.mark.usefixtures("driver")
# def test_onboard_child3_without_email_mobile_with_parent(driver):
#     # Use parent details from previous test
#     parent_email = globals().get("parent_email_5_1")

#     # Use parent details from previous test
#     parent_email = globals().get("parent_email_5_1")
#     parent_mobile = globals().get("parent_mobile_5_1")
#     parent_first_name = globals().get("parent_first_name_5_1")
#     parent_last_name = globals().get("parent_last_name_5_1")

#     page = AthletesPage(driver)
#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("Child3")
#     page.create_last_name("Child3")
#     page.click_and_select_dob(athlete["child_year"])
#     page.click_and_select_gender()
#     # No email/mobile for child3
#     page.create_parent_email(parent_email)
#     time.sleep(1)
#      # Check auto-filled parent details
#     auto_first_name = page.get_parent_first_name()
#     auto_last_name = page.get_parent_last_name()
#     auto_mobile = page.get_parent_mobile()
#     print( "Auto-filled Parent First Name, Last Name, Mobile:", auto_first_name, auto_last_name, auto_mobile)
#     print( "Expected Parent First Name, Last Name, Mobile:", parent_first_name, parent_last_name, parent_mobile)
 
#     assert auto_first_name == parent_first_name, "Parent first name not auto-filled correctly"
#     assert auto_last_name == parent_last_name, "Parent last name not auto-filled correctly"
#     assert auto_mobile == parent_mobile, "Parent mobile not auto-filled correctly"

#     page.click_create_button()
#     page.toast_message("Successful")
#     time.sleep(2)
#     page.click_cancel_button()    

# #5-4. Onboarding child4 athlete with existing parent email & diff mobile number & adding parent email
# @pytest.mark.usefixtures("driver")
# def test_onboard_child4_with_existing_parent_email_diff_mobile(driver):
#     page = AthletesPage(driver)
#     # Use parent details from previous test
#     parent_email = globals().get("parent_email_5_1")
#     parent_first_name = globals().get("parent_first_name_5_1")
#     parent_last_name = globals().get("parent_last_name_5_1")
#     parent_mobile = globals().get("parent_mobile_5_1")
    
#     child4_email =parent_email  # parenet email for child4 
#     child4_mobile = f"9{random.randint(100000000, 999999999)}"

#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("Child4")
#     page.create_last_name("Child4")
#     page.click_and_select_dob(athlete["child_year"])
#     page.click_and_select_gender()
#     page.create_email(child4_email)
#     page.create_mobile(child4_mobile)
#     page.create_parent_email(parent_email)
#     time.sleep(1)

#     # Check auto-filled parent details
#     auto_first_name = page.get_parent_first_name()
#     auto_last_name = page.get_parent_last_name()
#     auto_mobile = page.get_parent_mobile()
#     print("Auto-filled Parent First Name, Last Name, Mobile:", auto_first_name, auto_last_name, auto_mobile)
#     print("Expected Parent First Name, Last Name, Mobile:", parent_first_name, parent_last_name, parent_mobile)

#     # If your app auto-fills only first/last name, but not mobile, adjust assertions accordingly
#     assert auto_first_name == parent_first_name, "Parent first name not auto-filled correctly"
#     assert auto_last_name == parent_last_name, "Parent last name not auto-filled correctly"
#     # Mobile may not auto-fill if different, so you may want to skip or adjust this assertion

#     page.click_create_button()
#     page.toast_message("Successful")
#     page.click_cancel_button()

# # #5-5. Onboarding child5 athlete with existing parent mobile number & diff email & adding parent email & mobile
# @pytest.mark.usefixtures("driver")
# def test_onboard_child5_with_existing_parent_mobile_diff_email(driver):
#     page = AthletesPage(driver)

#     # Use parent details from previous test
#     parent_mobile = globals().get("parent_mobile_5_1")
#     parent_email = globals().get("parent_email_5_1")
#     parent_first_name = globals().get("parent_first_name_5_1")
#     parent_last_name = globals().get("parent_last_name_5_1")

#     child5_mobile = parent_mobile  # parent mobile for child5
#     child5_email = f"athlete{int(time.time())+3}@otsi.co.in"

#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("Child5")
#     page.create_last_name("Child5")
#     page.click_and_select_dob(athlete["child_year"])
#     page.click_and_select_gender()
#     page.create_email(child5_email)
#     page.create_mobile(child5_mobile)
#     page.create_parent_email(parent_email)
#     time.sleep(1)

#     # Check auto-filled parent details
#     auto_first_name = page.get_parent_first_name()
#     auto_last_name = page.get_parent_last_name()
#     auto_mobile = page.get_parent_mobile()
#     print("Auto-filled Parent First Name, Last Name, Mobile:", auto_first_name, auto_last_name, auto_mobile)
#     print("Expected Parent First Name, Last Name, Mobile:", parent_first_name, parent_last_name, parent_mobile)

#     assert auto_first_name == parent_first_name, "Parent first name not auto-filled correctly"
#     assert auto_last_name == parent_last_name, "Parent last name not auto-filled correctly"
#     # Mobile may auto-fill, but email is new, so adjust assertions if needed

#     page.click_create_button()
#     page.toast_message("Successful")

# #5-6. Onboarding child6 athlete with diff email & mobile number & adding same parent email & mobile from previous parent details
# @pytest.mark.usefixtures("driver")
# def test_onboard_child6_with_diff_email_mobile_same_parent(driver):
#     page = AthletesPage(driver)
#     child6_email = f"athlete{int(time.time())+4}@otsi.co.in"
#     child6_mobile = f"9{random.randint(100000000, 999999999)}"

#     # Use parent details from previous tests (5-1)
#     parent_email = globals().get("parent_email_5_1")
#     parent_mobile = globals().get("parent_mobile_5_1")
#     parent_first_name = globals().get("parent_first_name_5_1")
#     parent_last_name = globals().get("parent_last_name_5_1")
#     parent_dob = globals().get("parent_dob_5_1")

#     page.click_actions_dropdown()
#     page.click_athlete_onboard()
#     page.create_first_name("Child6")
#     page.create_last_name("Child6")
#     page.click_and_select_dob(athlete["child_year"])
#     page.click_and_select_gender()
#     page.create_email(child6_email)
#     page.create_mobile(child6_mobile)
#     page.create_parent_email(parent_email)
#     time.sleep(1)

#     # Check auto-filled parent details
#     auto_first_name = page.get_parent_first_name()
#     auto_last_name = page.get_parent_last_name()
#     auto_mobile = page.get_parent_mobile()
#     print("Auto-filled Parent First Name, Last Name, Mobile:", auto_first_name, auto_last_name, auto_mobile)
#     print("Expected Parent First Name, Last Name, Mobile:", parent_first_name, parent_last_name, parent_mobile)

#     assert auto_first_name == parent_first_name, "Parent first name not auto-filled correctly"
#     assert auto_last_name == parent_last_name, "Parent last name not auto-filled correctly"
#     assert auto_mobile == parent_mobile, "Parent mobile not auto-filled correctly"

#     page.click_create_button()
#     page.toast_message("Successful")

##6-------update option child athlete details-------##
##6-1. try to update child athlete email with existing another athlete email
@pytest.mark.usefixtures("driver")
def test_update_child_athlete_email_with_existing_athlete_email(driver):
    page = AthletesPage(driver)
    # Search for previously created child athlete
    
    child_name = "child child"
    page.enter_search_text(child_name)
    time.sleep(2)
    page.click_three_dots_on_search_result(child_name)
    page.click_edit_athlete_option()
    time.sleep(2)
    # Try to update email with an existing athlete email
    existing_email = athlete["email"]

    # page.clear_field(page.email_input_in_update)
    page.javascript_clear_field(page.email_input_in_update)
    time.sleep(1)
    page.create_email_in_update(existing_email)
    page.click_update_athlete_button()
    page.toast_message("already exists")
    page.click_cancel_button()
# ##6-2. try to update child athlete mobile with existing another athlete mobile
@pytest.mark.usefixtures("driver")
def test_update_child_athlete_mobile_with_existing_athlete_mobile(driver):
    page = AthletesPage(driver)
    # Search for previously created child athlete
    child_name = "child child"
    page.enter_search_text(child_name)
    time.sleep(2)
    page.click_three_dots_on_search_result(child_name)
    page.click_edit_athlete_option()
    time.sleep(2)
    # Try to update email with an existing athlete email
    existing_mobile = athlete["mobile"]
    page.javascript_clear_field(page.mobile_input_in_update)
    time.sleep(1)
    page.create_mobile_in_update(existing_mobile)
    page.click_update_athlete_button()
    page.toast_message("already exists")
    page.click_cancel_button()


#7. coach email & mobile number can be used for athlete onboard
#7-1. Onboarding athlete with existing coach email & mobile number-->onboarded successfully
#7-2. Onboarding athlete with duplicate coach email & mobile--->already exists error
# #7-3 Onboarding athlete with existing coach email & diff mobile number-->correctly mapped with existing coach email and mobile number
   


    


