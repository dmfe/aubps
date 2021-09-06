import sys
import time

from web_util import WebDriver
from web_util import ENTER

from selenium.common.exceptions import NoSuchElementException


GASNN_UTIL_URL = "https://www.gas-nn.ru"
GASNN_TITLE_PART = "НижегородЭнергоГазРасчет"
GASNN_NOTIFICATION_HEADER = "Уважаемые абоненты!"
GASNN_CLOSE_BUTTON_CLASS = "close"
GASNN_ACCOUNT_LINK_TEXT = "Личный кабинет"
GASNN_LAST_NAME_INPUT_NAME = "fam"
GASNN_ACCOUNT_NUM_INPUT_ID = "lschet"
GASNN_ACCOUNT_ENTER_INPUT_NAME = "go"
GASNN_ACCOUNT_ENTER_INPUT_VALUE = "Войти"
GASNN_SEND_COUNTER_DATA_HREF = "form.php"
GASNN_SEND_COUNTER_DATA_TEXT = "Передать показания счетчика"


# Input data -----------------
# Obtain last name and account number
last_name = "" # place here your tns account number
account_num = "" # place here your tns password

# Obtain data that should be submitted
value = "12000" # place here day value
# ----------------------------


class GASNN:

  def run(self):
    error = None

    with WebDriver() as wd:

      # Navigate to utility resource
      wd.navigate(GASNN_UTIL_URL)

      time.sleep(3)

      wd.check_title(GASNN_TITLE_PART)


      # Close notification window
      try:
        close_button_element = wd.find_by_xpath(
          f"//button[\
            @class = '{GASNN_CLOSE_BUTTON_CLASS}'\
          ]"
        )
      except NoSuchElementException:
        error = sys.exc_info()[0]

      if error is None:
        close_button_element.click()
      else:
        print(f"close button not found: {error}")


      # Find Go to Personal Account link and press
      account_link = wd.find_by_xpath(
        f"//a[text() = '{GASNN_ACCOUNT_LINK_TEXT}']"
      )
      account_link.click()


      # Find auth elements
      last_name_input_element = wd.find_by_xpath(
        f"//input[@name = '{GASNN_LAST_NAME_INPUT_NAME}']"
      )
      last_name_input_element.send_keys(last_name)

      account_num_input_element = wd.find_by_xpath(
        f"//input[@id = '{GASNN_ACCOUNT_NUM_INPUT_ID}']"
      )
      account_num_input_element.send_keys(account_num)

      account_enter_input_element = wd.find_by_xpath(
        f"//input[\
          @name = '{GASNN_ACCOUNT_ENTER_INPUT_NAME}' and\
          @value = '{GASNN_ACCOUNT_ENTER_INPUT_VALUE}'\
        ]"
      )
      account_enter_input_element.send_keys(ENTER)

      time.sleep(7)


      # Find Send Counter Data Link
      send_counter_data_link = wd.find_by_xpath(
        f"//a[\
          @href = '{GASNN_SEND_COUNTER_DATA_HREF}' and\
          div/text() = '{GASNN_SEND_COUNTER_DATA_TEXT}'\
        ]"
      )
      send_counter_data_link.click()

      time.sleep(5)

