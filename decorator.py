from functools import wraps
import time
import functools

def upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value.upper()
    return wrapper



def slow_down(func):
  
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@upper
@slow_down 
def multiplication(v1,v2):
    return f"{v1} multiplied by {v2} = {v1*v2}"


if __name__ == "__main__":
    print(multiplication(5,10))