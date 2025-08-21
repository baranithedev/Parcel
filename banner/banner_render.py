from .banner import banner
from random import choice
from time import sleep 

def randombanner(banner: list)-> str:
    return choice(banner)

bannertext=randombanner([banner])

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        print(f"Parcel - Transfer without conscience\n")
        return result
    return wrapper_function


@decorator_function 
def show_banner():
    for line in bannertext.splitlines():
        print(line)
        sleep(0.025)
    print()
