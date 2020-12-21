from selenium import webdriver

import webbrowser
import os
import sys
from pathlib import Path


if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    bundle_dir = Path(sys._MEIPASS)
    print('The bundle dircectory is: ', bundle_dir)
else:
    bundle_dir = Path(__file__).parent

chromedriver_path = Path.cwd() / bundle_dir / "chromedriver/chromedriver"
print('path to data is: ', chromedriver_path)



print('********driver test******')
driver = webdriver.Chrome(chromedriver_path)

driverTest = 'https://www.sligorovers.com'
driver.get(driverTest)