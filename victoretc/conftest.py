import random

import pytest
from selenium import webdriver
from random import *


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

