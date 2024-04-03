from dataclasses import dataclass

# AUTH

login = 'standard_user'
password = 'secret_sauce'

# URLS

main_page = 'https://www.saucedemo.com/'
catalogue = 'https://www.saucedemo.com/inventory.html'
checkout_complete = 'https://www.saucedemo.com/checkout-complete.html'
about = 'https://saucelabs.com/'

@dataclass
class User:
    first_name: str = None,
    last_name: str = None,
    full_name: str = None,
    address: str = None,
    phone_number: str = None,
    postcode: str = None
