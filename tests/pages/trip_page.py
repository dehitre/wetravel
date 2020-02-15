from pages.base_page import BasePage
from pages.locators import TripPageLocators
import allure


class TripPage(BasePage):
    @allure.step("Choose destination")
    def add_destination(self, destination):
        location = self.browser.find_element(*TripPageLocators.LOCATION)
        location.send_keys(destination)
        next_button = self.browser.find_element(*TripPageLocators.LOCATION_NEXT_BTN)
        next_button.click()

    @allure.step("Choose dates")
    def choose_dates(self):
        start_date = self.browser.find_element(*TripPageLocators.START_DATE)
        start_date.click()
        start_day = self.browser.find_element(*TripPageLocators.START_DAY)
        start_day.click()
        end_date = self.browser.find_element(*TripPageLocators.END_DATE)
        end_date.click()
        end_day = self.browser.find_element(*TripPageLocators.START_DAY)
        end_day.click()
        next_button = self.browser.find_element(*TripPageLocators.DATE_NEXT_BTN)
        next_button.click()

    @allure.step("Choose private trip")
    def choose_private_trip(self):
        privacy_button = self.browser.find_element(*TripPageLocators.PRIVATE_TRIP_RBTN)
        privacy_button.click()
        next_button = self.browser.find_element(*TripPageLocators.PRIVACY_NEXT_BTN)
        next_button.click()

    @allure.step("Close welcome pop-up")
    def close_welcome_pop_up(self):
        close_button = self.browser.find_element(*TripPageLocators.CLS_MODAL)
        close_button.click()

    @allure.step("Check logo")
    def should_be_logo_on_page(self):
        assert self.is_element_present(*TripPageLocators.LOGO)
