import time
url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_nalichi_knopki_v_korzinu(browser):
    browser.get(url)
    time.sleep(30)
    assert browser.find_element_by_css_selector('button.btn-primary')