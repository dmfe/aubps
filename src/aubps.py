import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


TNS_UTIL_URL = "https://lk.nn.tns-e.ru"
TNS_TITLE_PART = "ТНС энерго"

TNS_ACCOUNT_ID = "account_ls"
TNS_PASSWORD_ID = "account_pwd"

TNS_ENTER_ELEMENT_VALUE = "войти"
TNS_SUBMIT_PAGE_LINK_TEXT = "Передача показаний"

TNS_DAY_ZONE_INPUT_ELEMENT_ID = "sch_3502722_num_1"
TNS_DAY_ZONE_INPUT_ELEMENT_ERROR_ZONE = "День"
TNS_NIGHT_ZONE_INPUT_ELEMENT_ID = "sch_3502722_num_2"
TNS_NIGHT_ZONE_INPUT_ELEMENT_ERROR_ZONE = "Ночь"

TNS_SUBMIT_DATA_ELEMENT_ID = "submit_digital_page"
TNS_SUBMIT_DATA_ELEMENT_VALUE = "передать показания"


# Input data -----------------
# Obtain account and password
account = "" # place here your tns account number
password = "" # place here your tns password

# Obtain data that should be submitted
day_value = "12000" # place here day value
night_value = "5000" # place here night value
# ----------------------------

def main():
    browser = webdriver.Firefox()

    # Navigate to utility resource
    browser.get(TNS_UTIL_URL)
    time.sleep(3)
    assert TNS_TITLE_PART in browser.title


    # Find auth elements
    acc_num_elem = browser.find_element_by_id(TNS_ACCOUNT_ID)
    acc_num_elem.send_keys(account)
    pwd_elem = browser.find_element_by_id(TNS_PASSWORD_ID)
    pwd_elem.send_keys(password)
    enter_element = browser.find_element_by_xpath(
        f"//input[@value = '{TNS_ENTER_ELEMENT_VALUE}']")
    enter_element.send_keys(Keys.ENTER)

    time.sleep(10)

    # Find data submission link
    submit_date_element = browser.find_element_by_xpath(
        f"//a[div/text() = '{TNS_SUBMIT_PAGE_LINK_TEXT}']")
    submit_date_element.click()

    # Find data input fields
    day_zone_input_element = browser.find_element_by_xpath(
        f"//input[\
            @id = '{TNS_DAY_ZONE_INPUT_ELEMENT_ID}' and \
            @error-zone-name = '{TNS_DAY_ZONE_INPUT_ELEMENT_ERROR_ZONE}'\
        ]"
    )
    day_zone_input_element.send_keys(day_value);

    night_zone_input_element = browser.find_element_by_xpath(
        f"//input[\
            @id = '{TNS_NIGHT_ZONE_INPUT_ELEMENT_ID}' and \
            @error-zone-name = '{TNS_NIGHT_ZONE_INPUT_ELEMENT_ERROR_ZONE}'\
        ]"
    )
    night_zone_input_element.send_keys(night_value);

    # Find submit input element
    submit_input_element = browser.find_element_by_xpath(
        f"//input[\
            @id = '{TNS_SUBMIT_DATA_ELEMENT_ID}' and \
            @value = '{TNS_SUBMIT_DATA_ELEMENT_VALUE}'\
        ]"
    )
    #submit_input_element.send_keys(Keys.ENTER)

    print(submit_input_element)

    #browser.quit()


if __name__ == "__main__":
    main()

