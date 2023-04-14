# Cleo Tang
# 261070795
import doctest
import requests

def dict_to_query(dic):
    ''' (dict) -> str
    Takes as input a dictionary and returns a string
    containing the keys and values with the format
    'key=value' and ampersands separating each.
    >>> dict_to_query({'email': 'jonathan.campbell@mcgill.ca', 'token': 'ABC'})
    'email=jonathan.campbell@mcgill.ca&token=ABC'
    >>> dict_to_query({'email': 'yixuan.tang@mail.mcgill.ca', 'token': '1B3'})
    'email=yixuan.tang@mail.mcgill.ca&token=1B3'
    >>> dict_to_query({'withdrawal_email': 'jonathan.campbell@mcgill.ca', 'token': 'ABC', 'deposit_email': 'yiuxan.tang@mail.mcgill.ca', 'amount': 5000})
    'withdrawal_email=jonathan.campbell@mcgill.ca&token=ABC&deposit_email=yiuxan.tang@mail.mcgill.ca&amount=5000'
    '''
    data_list = []
    for key, value in dic.items():
        data_list.append(str(key)+'='+str(value))
    return '&'.join(data_list)



class Account:
    '''A class stores all relevant data about a user’s
    COMP202COIN account and contains methods that operate on that data.
    
    Class Attribute:
    * API_URL: str
    
    Instance Attributes:
    * email: str
    * token: str
    * balance: int
    * request_log: list
    '''
    
    API_URL = 'https://coinsbot202.herokuapp.com/api/'
    
    def __init__(self, email, token):
        '''(str, str) -> NoneType
        Creates an object of type Account.
        >>> my_acc = Account('jonathan.campbell@mcgill.ca', 'ABC')
        >>> my_acc.email
        'jonathan.campbell@mcgill.ca'
        >>> my_acc.balance
        -1
        >>> my_acc = Account('yixuan.tang@mail.mcgill.ca', '3B6')
        >>> my_acc.request_log
        []
        >>> my_acc.token
        '3B6'
        >>> my_acc = Account('john.Mackenzie@gmail.com', '123')
        Traceback (most recent call last):
        AssertionError: invalid email address
        >>> my_acc = Account(190299042, '0987654321zc')
        Traceback (most recent call last):
        AssertionError: incorrect type of inputs of email and/or token
        '''
        if type(email) != str or type(token) != str:
            raise AssertionError('incorrect type of inputs of email and/or token')
        if email[-9:] != 'mcgill.ca':
            raise AssertionError('invalid email address')
        
        self.email = email
        self.token = token
        self.balance = -1
        self.request_log = []


    def __str__(self):
        ''' () -> str
        Takes no input and returns a string of the format
        'EMAIL has balance BALANCE' where EMAIL and BALANCE
        refer to the appropriate instance attributes.
        >>> my_acc = Account('jonathan.campbell@mcgill.ca', 'ABC')
        >>> str(my_acc)
        'jonathan.campbell@mcgill.ca has balance -1'
        >>> my_acc = Account('yixuan.tang@mail.mcgill.ca', '3B6')
        >>> print(my_acc)
        yixuan.tang@mail.mcgill.ca has balance -1
        >>> my_acc = Account('john.Mackenzie@gmail.com', '123')
        Traceback (most recent call last):
        AssertionError: invalid email address
        '''
        
        return self.email+' has balance '+str(self.balance)
    
    
    def call_api(self, endpoint, request_dict):
        '''(str, dict) -> dict
        Takes an endpoint (string) and request dictionary as ex-plicit
        inputs. Constructs an API request URL and sends the request.
        Adds a key 'token' into the dictionary with corresponding value.
        Returns a dictionary of request result, raising an AssertionError
        if any of the inputs are of wrong type or the contents are wrong.
        >>> my_acc = Account('jonathan.campbell@mcgill.ca', 'ABC')
        >>> my_acc.call_api('balance', {'email': my_acc.email})
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        >>> my_acc = Account('yixuan.tang@mail.mcgill.ca', 'aqnDZJLtgHlWiAx5')
        >>> endpoint_data = {'email': my_acc.email}
        >>> my_acc.call_api('balance', endpoint_data)
        {'message': 5634, 'status': 'OK'}
        >>> print(endpoint_data)
        {'email': 'yixuan.tang@mail.mcgill.ca', 'token': 'aqnDZJLtgHlWiAx5'}
        >>> my_acc = Account('yixuan.tang@mail.mcgill.ca', '3B6')
        >>> my_acc.call_api('transfer', ['withdrawal_account', 'jonathan.campbell@mcgill.ca'])
        Traceback (most recent call last):
        AssertionError: invalid endpoint and/or request dictionary
        >>> my_acc = Account('yixuan.tang@mail.mcgill.ca', '3B6')
        >>> my_acc.call_api('transfer', {'withdrawal_email': 'jonathan.campbell@mcgill.ca'})
        Traceback (most recent call last):
        AssertionError: Field deposit_email not present in API query.
        '''
        
        if type(endpoint) != str or type(request_dict) != dict or endpoint not in ['balance', 'transfer','make_it_rain']:
            raise AssertionError('invalid endpoint and/or request dictionary')
        
        request_dict['token'] = self.token
        query = dict_to_query(request_dict)
        request_url = self.API_URL+endpoint+'?'+query
        result = requests.get(url=request_url).json()
        
        if result['status'] != 'OK':
            raise AssertionError(result['message'])

        return result


    
    def retrieve_balance(self):
        '''() -> int
        Takes no explicit inputs.Calls the API to retrieve and 
        updates the balance for the current user email. Returns
        the integer of the balance.
        >>> my_acc = Account('yixuan.tang@mail.mcgill.ca', 'aqnDZJLtgHlWiAx5')
        >>> my_acc.retrieve_balance()
        5634
        >>> my_acc.balance == my_acc.retrieve_balance()
        True
        >>> my_acc = Account('jonathan.campbell@mcgill.ca', 'ABC')
        >>> my_acc.retrieve_balance()
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        '''
    
        balance = self.call_api('balance', {"email": self.email})['message']
        self.balance = balance
        return balance

    
    def transfer(self, amount_coins, email):
        '''(int, str) -> str
        Takes as inputs a positive integer of amount of coins transferred,
        and a string of the reveiving email. Returns the message in the
        result dictionary. Raise AssertionError when inputs are invalid.
        >>> my_acc = Account('yixuan.tang@mail.mcgill.ca', 'aqnDZJLtgHlWiAx5')
        >>> my_acc.balance
        -1
        >>> my_acc.transfer(25,'yinuo.han@mail.mcgill.ca')
        Traceback (most recent call last):
        AssertionError: could not transfer this amount of money.
        >>> my_acc.retrieve_balance()
        5634
        >>> my_acc.transfer(-500, 'jonathan.campbell@mcgill.ca')
        Traceback (most recent call last):
        AssertionError: could not transfer this amount of money.
        >>> my_acc.transfer(100000000000, 'jonathan.campbell@mcgill.ca')
        Traceback (most recent call last):
        AssertionError: could not transfer this amount of money.
        >>> my_acc.transfer(1, 'cleo.tang8@gmail.com')
        Traceback (most recent call last):
        AssertionError: invalid email address to transfer coins.
        >>> my_acc.transfer(100, 'yixuan.tang@mail.mcgill.ca')
        Traceback (most recent call last):
        AssertionError: could not transfer coins to the current user email!
        >>> my_acc.transfer([10], 'jonathan.campbell@mcgill.ca')
        Traceback (most recent call last):
        AssertionError: invalid inputs types of amount of coins and/or email.
        '''
        
        if type(amount_coins) != int or type(email) != str:
            raise AssertionError('invalid inputs types of amount of coins and/or email.')
        if email[-9:] != 'mcgill.ca':
            raise AssertionError('invalid email address to transfer coins.')
        if email == self.email:
            raise AssertionError('could not transfer coins to the current user email!')        
        if self.balance == -1 or amount_coins > self.balance or amount_coins <= 0:
            raise AssertionError('could not transfer this amount of money.')
        request_dict = {'withdrawal_email': self.email, 'deposit_email': email, 'amount': amount_coins}
        return self.call_api('transfer', request_dict)['message']
        
        
        
        
        
if __name__ == '__main__':
    doctest.testmod()