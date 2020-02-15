from pages.main_page import MainPage
from pages.trip_page import TripPage
import allure


class TestAddTrip:
    @allure.title("Open destination creation page")
    def test_open_trip_creation(self, browser):
        link = "https://www.wetravel.com/"
        page = MainPage(browser, link)
        page.open()
        page.click_on_try_button()
        page.should_open_trip_creation_page()

    @allure.title("Check logo after trip creation")
    def test_create_trip(self, browser):
        link = "https://www.wetravel.com/itinerary_builder/new#/"
        page = TripPage(browser, link)
        page.open()
        page.add_destination("Amsterdam, Netherlands")
        page.choose_dates()
        page.choose_private_trip()
        page.close_welcome_pop_up()
        page.should_be_logo_on_page()
