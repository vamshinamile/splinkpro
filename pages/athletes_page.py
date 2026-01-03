from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class AthletesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #locators
    athletes_tab = (By.XPATH, "//button[normalize-space(.//span)='Athletes']")
    Actions_dropdown = (By.XPATH, "//button[normalize-space(text())='Actions']")
    onboard_athletes_button =(By.XPATH, "//button[normalize-space()='+ Onboard Athlete']")
    add_Athlete= (By.XPATH, "//div[@role='menuitem' and text()='Add Athlete']")
    first_name_input = ((By.XPATH, "//input[@name='athlete_firstname' and @placeholder=\"Enter Athletes first name\"]"))
    last_name_input = (By.XPATH,"//input[@name='athlete_lastname' and @placeholder=\"Enter Athletes last name\"]")
    date_button = (By.XPATH, "//button[@aria-haspopup='dialog' and .//span[text()=\"Enter Athletes date of birth\"]]")
    year_dropdown=(By.XPATH, "//select[contains(@class, 'rdp-years_dropdown')]")
    date_value_button= (By.XPATH, "//button[normalize-space(text())='5']")
    gender_dropdown=(By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'Select gender')]]")
    email_input = (By.XPATH, "//input[@name='athlete_email' and @placeholder=\"Enter Athletes email\"]")
    email_input_in_update = (By.XPATH, "//input[@name='athlete_email' and @placeholder=\"Enter athlete's email\"]")
    mobile_input_in_update = (By.XPATH, "//input[@name='athlete_mobile' and @placeholder=\"Enter athlete's mobile number\"]")
    mobile_input = (By.XPATH, "//input[@name='athlete_mobile' and @placeholder=\"Enter Athletes mobile number\"]")
    search_input = (By.XPATH, "//input[contains(@placeholder, 'Search athletes')]")  
    #--parent/guardian info locators--#
    parent_first_name_input = ((By.XPATH, "//input[@name='parent_firstname' and @placeholder=\"Enter parent's first name\"]"))
    parent_last_name_input = (By.XPATH,"//input[@name='parent_lastname' and @placeholder=\"Enter parent's last name\"]")
    parent_date_button = (By.XPATH, "//button[@aria-haspopup='dialog' and .//span[text()=\"Enter parent's date of birth\"]]")
    parent_year_dropdown=(By.XPATH, "//select[contains(@class, 'rdp-years_dropdown')]")
    parent_date_value_button= (By.XPATH, "//button[normalize-space(text())='5']")
    parent_gender_dropdown=(By.XPATH, "//button[@role='combobox' and .//span[contains(text(), 'Select gender')]]")
    parent_email_input = (By.XPATH, "//input[@name='parent_email' and @placeholder=\"Enter parent's email\"]")
    parent_mobile_input = (By.XPATH, "//input[@name='parent_mobile' and @placeholder=\"Enter parent's mobile number\"]")
    create_button = (By.XPATH, "//button[@type='submit' and text()='Create Athlete']")
    cancel_button=(By.XPATH, "//button[text()='Cancel']")



    # def onboard_athlete(self, first_name, last_name, year,email, mobile): 
    def click_athlete_tab(self):
        # 1. Click on athletes tab
        self.wait.until(EC.element_to_be_clickable(self.athletes_tab)).click()
        time.sleep(2)  
    def click_actions_dropdown(self):
        # 2. Click on 'on action athletes' button
        self.wait.until(EC.element_to_be_clickable(self.Actions_dropdown)).click()
        #select onboard athlete
    def click_athlete_onboard(self):
        self.wait.until(EC.element_to_be_clickable(self.add_Athlete)).click()
        time.sleep(2)
    def create_first_name(self,first_name):
        # 3. Enter first name
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        print(f"✅ Entered first name: {first_name}")
    def create_last_name(self,last_name):
        # 4. Enter last name
        self.wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)
        print(f"✅ Entered last name: {last_name}")
    def click_and_select_dob(self,year):
        # 5. click on  date of birth 
        self.wait.until(EC.element_to_be_clickable(self.date_button)).click()
        # Wait for the dropdown to be present
        year_dropdown = Select(self.wait.until(EC.presence_of_element_located(self.year_dropdown)))
        # Select year by visible text
        year_dropdown.select_by_visible_text(year)
        # Wait for the date button and click
        self.wait.until(EC.element_to_be_clickable(self.date_value_button)).click()
        time.sleep(1)
        print(f"✅ Selected DOB year: {year}")
    def click_and_select_gender(self):
        # 6. Select gender dropdown
       # Wait for the "Choose a sport" dropdown button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable(self.gender_dropdown)).click()
        time.sleep(2) 
        # Use keyboard to navigate (DOWN + ENTER)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(2)  
        print("✅ Gender Selected")
    def create_email(self,email):
        # 7. Enter email
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        print(f"✅ Entered email: {email}")
    def create_email_in_update(self,email):
        # 7. Enter email
        self.wait.until(EC.visibility_of_element_located(self.email_input_in_update)).send_keys(email)
        print(f"✅ Entered email: {email}")
    def create_mobile(self,mobile):
        # 8. Enter mobile number
        self.wait.until(EC.visibility_of_element_located(self.mobile_input)).send_keys(mobile)
        print(f"✅ Entered mobile number: {mobile}")
    def create_mobile_in_update(self,mobile):
        # 8. Enter mobile number
        self.wait.until(EC.visibility_of_element_located(self.mobile_input_in_update)).send_keys(mobile)
        print(f"✅ Entered mobile number: {mobile}")

    #--parent/guardian info methods--#

    def create_parent_first_name(self,first_name):
        # 3. Enter first name
        self.wait.until(EC.visibility_of_element_located(self.parent_first_name_input)).send_keys(first_name)
        print(f"✅ Entered first name: {first_name}")
    def create_parent_last_name(self,last_name):
        # 4. Enter last name
        self.wait.until(EC.visibility_of_element_located(self.parent_last_name_input)).send_keys(last_name)
        print(f"✅ Entered last name: {last_name}")
    def click_and_select_parent__dob(self,year):
        # 5. click on  date of birth 
        self.wait.until(EC.element_to_be_clickable(self.parent_date_button)).click()
        # Wait for the dropdown to be present
        year_dropdown = Select(self.wait.until(EC.presence_of_element_located(self.parent_year_dropdown)))
        # Select year by visible text
        year_dropdown.select_by_visible_text(year)
        # Wait for the date button and click
        self.wait.until(EC.element_to_be_clickable(self.parent_date_value_button)).click()
        time.sleep(1)
        print(f"✅ Selected DOB year: {year}")
    def create_parent_email(self,email):
        # 7. Enter email
        self.wait.until(EC.visibility_of_element_located(self.parent_email_input)).send_keys(email)
        print(f"✅ Entered email: {email}")
    def create_parent_mobile(self,mobile):
        # 8. Enter mobile number
        self.wait.until(EC.visibility_of_element_located(self.parent_mobile_input)).send_keys(mobile)
        print(f"✅ Entered mobile number: {mobile}")


    def click_create_button(self):
        # 9. Click on create button
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()
        print("✅ Clicked Create button")
    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()
        print("✅ Clicked Cancel button")

    def clear_field(self, locator):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        print(f"✅ Cleared field: {locator}")

    def javascript_clear_field(self,locator):
        element =self.wait.until(EC.element_to_be_clickable(locator))
        # driver.find_element(By.XPATH, "//input[@name='athlete_email' and @placeholder=\"Enter athlete's email\"]")
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)

            
    def toast_message(self, message, timeout=10):
      try:
          # Use string formatting to insert the message parameter into the XPath
          toast = WebDriverWait(self.driver, timeout).until(
              EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{message}')]"))
          )
          # Print the toast message
          print("Toast appeared:", toast.text)
          return toast.text
      except Exception as e:
          print(f"Error: {str(e)}")
          return None
    def validation_messages(self):
              errors = {}
              error_elements = self.driver.find_elements(By.CSS_SELECTOR, "p.text-destructive")

              for elem in error_elements:
                  error_text = elem.text.strip()
                  if not error_text:
                      continue

                  # Find the nearest input/label above the error message
                  field_name = "Unknown field"
                  try:
                      label_elem = elem.find_element(By.XPATH, "./preceding::label[1]")
                      field_name = label_elem.text.strip()
                  except:
                      try:
                          input_elem = elem.find_element(By.XPATH, "./preceding::input[1]")
                          field_name = input_elem.get_attribute("placeholder") or "Unknown field"
                      except:
                          pass

                  errors[field_name] = error_text
                  print("Mandatory field validations are captured:")
                  print(f"{field_name}: {error_text}")

              return errors


    def remove_athlete_and_capture_error(self):  
       athlete_name = "John Doe"  

    # XPath to locate the ellipsis icon associated with the athlete  
       ellipsis_xpath = f"//div[@data-slot='card'][.//h3[contains(text(), '{athlete_name}')]]//*[name()='svg'][contains(@class, 'lucide-ellipsis-vertical')]"  

    #   try:  
        # Wait for the SVG element to be clickable  
       ellipsis_icon = self.wait.until(  
            EC.element_to_be_clickable((By.XPATH, ellipsis_xpath))  
        )  

        #   try:  
            # Try native Selenium click  
       ellipsis_icon.click()  
        #   except Exception as e:  
        #     print("Native click failed. Trying JavaScript click.")  
       self.driver.execute_script(  
                "arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true }));", ellipsis_icon  
            )  

        # Step 2: Click on "Remove Athlete"  
       remove_xpath = "//div[@role='menuitem' and normalize-space(text())='Remove Athlete']"  
       remove_button = self.wait.until(  
            EC.element_to_be_clickable((By.XPATH, remove_xpath))  
        )  
       remove_button.click()  

        # Step 3: Confirm deletion  
       delete_button_xpath = "//button[normalize-space()='Delete' and contains(@class,'bg-destructive')]"  
       self.wait.until(  
       EC.element_to_be_clickable((By.XPATH, delete_button_xpath))  
           ).click()  

    def check_parent_guardian_heading_displayed(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[contains(text(), 'Parent/Guardian Information')]")
            )
        )
        print("✅ Athlete Age below 18 yrs then Heading appeared:", heading.text)
        return heading.text
    
    def get_parent_first_name(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.parent_first_name_input))
        return elem.get_attribute("value")

    def get_parent_last_name(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.parent_last_name_input))
        return elem.get_attribute("value")

    def get_parent_mobile(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.parent_mobile_input))
        return elem.get_attribute("value")

    def get_parent_dob(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.parent_date_button))
        return elem.text




    def enter_search_text(self, athlete_name):  
        search = self.wait.until(EC.visibility_of_element_located(self.search_input))  
        search.clear()  
        search.send_keys(athlete_name + Keys.RETURN)  
        print(f"✅ Searched for athlete: {athlete_name}")
        time.sleep(3)  
  
    def click_three_dots_on_search_result(self, athlete_name):
        """
        Clicks on the 3-dot (ellipsis) menu inside the first card matching the given athlete name.
        """
        try:
            lower_name = athlete_name.lower()

            # Target the flex-shrink-0 div (3 dots container) inside the card header
            three_dots_xpath = (
                "(//h3[contains(translate(normalize-space(), "
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
                f"'{lower_name}')]/ancestor::div[@data-slot='card-header']//div[contains(@class, 'flex-shrink-0')])[1]"
            )

            # Wait until the 3 dots container is clickable
            three_dots = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, three_dots_xpath))
            )

            try:
                three_dots.click()
                print(f"✅ Clicked 3 dots (flex-shrink-0 div) for athlete: {athlete_name}")
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", three_dots)
                print(f"⚙️ Used JS click for 3 dots (flex-shrink-0 div) for athlete: {athlete_name}")

        except TimeoutException:
            print(f"❌ 3 dots not found or not clickable for athlete: {athlete_name}")
        except Exception as e:
            print(f"⚠️ Unexpected error while clicking 3 dots for {athlete_name}: {e}")
   
    def click_edit_athlete_option(self):
        try:
            edit_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and normalize-space(text())='Edit Athlete']"))
            )
            edit_option.click()
            print("✅ Clicked on 'Edit Athlete' option.")
        except TimeoutException:
            print("❌ 'Edit Athlete' option not found or not clickable.")

    def click_update_athlete_button(self):
            update_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Update Athlete')]"))
            )
            update_button.click()
            print("✅ Clicked Update Athlete button")