import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """ 
    getsales figures input from the user
    """
    print('Please enter slaes data from the last market')
    print('Data should be six numbers, separated by commas.')
    print('Example: 12,23,12,24,12,23\n')

    data_str = input("Enter your data here: \n")
    
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Checks if data provided is 6 integers
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f'exactly 6 values required, you provided {len(values)} values'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again \n')

get_sales_data()

