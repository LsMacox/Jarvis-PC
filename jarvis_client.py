import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

server_addr = 'http://192.168.0.103:8000'
chrome_opt = Options()
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--disable-gpu')  # Last I checked this was necessary.
chrome_opt.add_argument('--unsafely-treat-insecure-origin-as-secure=' + server_addr)
chrome_opt.add_argument('--ignore-certificate-errors')
chrome_opt.add_argument('--ignore-urlfetcher-cert-requests')
chrome_opt.add_argument('--disable-user-media-security=true')
chrome_opt.add_argument("user-data-dir=" + os.path.dirname(os.path.abspath(__file__)) + '/options/chrome-selenium-profile')

chrome_opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    # "profile.default_content_setting_values.media_stream_camera": 1,
    # "profile.default_content_setting_values.geolocation": 1,
    # "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(chrome_options=chrome_opt, executable_path='./options/chromedriver')
driver.get(server_addr + "/server")