from selenium.webdriver.chrome.webdriver import WebDriver


def test_metr_to_feet_converter():

    driver = WebDriver(executable_path='D://gdrive//chromedriver.exe')
    driver.get('https://www.metric-conversions.org/length/meters-to-feet.htm')

    try:
        search_inp = driver.find_element_by_xpath('//input [@id="argumentConv"]')
        search_inp.send_keys(1)
        element = driver.find_element_by_xpath('//p[@id="answer"]')

        assert element.text == '1m= 3ft 3.370079in'

    finally:
        driver.quit()


def test_cels_to_f_converter():

    driver = WebDriver(executable_path='D://gdrive//chromedriver.exe')
    driver.get('https://www.metric-conversions.org//temperature//celsius-to-fahrenheit.htm')

    try:
        search_inp = driver.find_element_by_xpath('//input [@name="argumentConv"]')
        search_inp.send_keys(100)
        element = driver.find_element_by_xpath('//p[@id="answer"]')

        assert element.text == '100°C= 212.0000°F'

    finally:
        driver.quit()


def test_ounc_to_gr():

    driver = WebDriver(executable_path='D://gdrive//chromedriver.exe')
    driver.get('https://www.metric-conversions.org/weight/ounces-to-grams.htm')

    try:
        search_inp = driver.find_element_by_xpath('//*[@id="argumentConv"]')
        search_inp.send_keys(100)
        element = driver.find_element_by_xpath('//*[@id="answer"]')

        assert element.text == '100oz= 2834.952g'
    finally:
        driver.quit()


if __name__ == '__main__':
    test_metr_to_feet_converter()
    test_cels_to_f_converter()
    test_ounc_to_gr()
