def get_users_by_country(data: dict, country: str) -> list[dict]:
    '''get users by country
    
    Args:
        data (dict): users data
        country (str): country name

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
    for count in data["results"]:
        if count['location']['country'] == country:
            return count


def get_users_by_age(data: dict, age: int) -> list[dict]:
    '''get users by age
    
    Args:
        data (dict): users data
        age (int): age

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''


def get_users_by_city(data: dict, city: str) -> list[dict]:
    '''get users by city
    
    Args:
        data (dict): users data
        city (str): city name

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''


def get_users_by_nat(data: dict, nat: str) -> list[dict]:
    '''get users by nat
    
    Args:
        data (dict): users data
        nat (str): user nat

    Returns: 
        list: list of users. item ex: {'full_name': f'{first} {last} {title}', 'age': int}
    '''
