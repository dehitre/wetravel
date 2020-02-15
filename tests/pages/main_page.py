from pages.base_page import BasePage
from pages.locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Click on Try it now")
    def click_on_try_button(self):
        try_button = self.browser.find_element(*MainPageLocators.TRY_BTN)
        try_button.click()

    @allure.step("Check url")
    def should_open_trip_creation_page(self):
        assert self.browser.current_url == "https://www.wetravel.com/itinerary_builder/new"
