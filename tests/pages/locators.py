from selenium.webdriver.common.by import By


class TripPageLocators:
    LOCATION = (By.CSS_SELECTOR, "#location")
    LOCATION_NEXT_BTN = (By.CSS_SELECTOR, "#next_step")
    START_DATE = (By.CSS_SELECTOR, "#startDate")
    START_DAY = (By.XPATH, '//div[contains(@class, "CalendarMonth--horizontal")][2]//td[contains'
                           '(@class,"CalendarDay--today")]//button')
    END_DATE = (By.CSS_SELECTOR, "#endDate")
    END_DAY = (By.XPATH, '//div[contains(@class, "CalendarMonth--horizontal")][3]//tr[1]//td[contains'
                         '(@class,"CalendarDay--valid")][1]//button')
    DATE_NEXT_BTN = (By.CSS_SELECTOR, "#next_step")
    PRIVATE_TRIP_RBTN = (By.XPATH, "//div[@class='trip-privacy']/label[1]")
    PRIVACY_NEXT_BTN = (By.CSS_SELECTOR, "#next_step")
    CLS_MODAL = (By.CSS_SELECTOR, ".wt-modal__close")
    LOGO = (By.XPATH, "//img[@alt='wetravel logo']")
