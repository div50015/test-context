import configuration
import utils.data

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


check_txt = []

def test_print_var(context):
    print(f'var1 = {configuration.settings.var1}')
    print(utils.data.set_check_text(context))

    check_txt_t = utils.data.set_check_text(context)

    results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
    results.should(have.text(check_txt_t[0]))
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
    results.should(have.text(check_txt_t[1]))
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
    results.should(have.text(check_txt_t[2]))
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
    results.should(have.text(check_txt_t[3]))