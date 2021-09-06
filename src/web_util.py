from selenium import webdriver
from selenium.webdriver.common.keys import Keys


ENTER = Keys.ENTER


class WebDriver:

  def __enter__(self):
    self.__webdriver = webdriver.Firefox()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.__webdriver.quit()
    if exc_val:
        raise

  def navigate(self, url = ""):
    return self.__webdriver.get(url)

  def check_title(self, title = ""):
    assert title in self.__webdriver.title

  def find_by_id(self, _id = ""):
    return self.__webdriver.find_element_by_id(_id)

  def find_by_xpath(self, xpath = ""):
    return self.__webdriver.find_element_by_xpath(xpath)

