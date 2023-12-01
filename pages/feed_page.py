import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Clicking on the specified order number')
    def click_on_created_order(self, order_number):
        locator = (By.XPATH, f".//p[text()='#0{str(order_number)}']")
        Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).click()

    @allure.step('Checking the visibility of the specified order number')
    def check_order_number_is_visible(self, order_number):
        locator = (By.XPATH, f".//p[text()='{str(order_number)}']")
        return Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator))

