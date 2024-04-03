from dataclasses import dataclass

# URL
main_page = 'https://victoretc.github.io/webelements_information/'


@dataclass
class User:
    first_name: str = None,
    last_name: str = None,
    full_name: str = None,
    address: str = None,
    phone_number: str = None,
    postcode: str = None