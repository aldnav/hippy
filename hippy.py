
import time
from datetime import datetime
from sys import argv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from settings import USERNAME, PASSWORD, CHATROOM, urls

if len(argv) >= 2:
    _, is_time_in = argv
    try:
        is_time_in = int(is_time_in)
    except:
        pass
else:
    is_time_in = True # time in is default
time_now = datetime.now().strftime('%I:%m %p')
log_template = '{}'.format(time_now)
is_time_in = bool(is_time_in)
print is_time_in
if is_time_in:
    log_template = 'time in: ' + log_template
else:
    log_template = 'time out: ' + log_template
# PHANTOM_PATH = '/usr/bin/phantomjs'
service_args = ['--load-images=false',
                '--ignore-ssl-errors=true',
                '--ssl-protocol=tlsv1']
# setup webdriver and sign in
# driver = webdriver.PhantomJS(service_args=service_args)
driver = webdriver.Firefox()
driver.get(urls['room'])
if driver.current_url != urls['room']:
    element = driver.find_element_by_xpath('//*[@id="email"]')
    element.send_keys(USERNAME)
    element = driver.find_element_by_xpath('//*[@id="password"]')
    element.send_keys(PASSWORD)
    element.submit()
# wait for room to load. @NOTE: there must be a better way for this
timeout = 15
print 'loading room',
for _ in xrange(timeout):
    print '.',
    time.sleep(1)
print 'done.'
# send time to chatroom
element = driver.find_element_by_xpath('//*[@id="hc-message-input"]')
element.send_keys(log_template)
element.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
