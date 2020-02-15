from pages.trip_page import TripPage
import allure


class TestLoginFromMainPage:
    @allure.title("Check logo")
    def test_guest_can_go_to_login_page(self, browser):
        link = "https://www.wetravel.com/itinerary_builder/new#/"
        page = TripPage(browser, link)
        page.open()
        page.add_destination("Amsterdam, Netherlands")
        page.choose_dates()
        page.choose_private_trip()
        page.close_welcome_pop_up()
        page.should_be_logo_on_page()

