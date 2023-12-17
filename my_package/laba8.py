def make_calc(operator, initial=0):

    result = initial



    def calc(num):

        nonlocal result

        if operator == "+":

            result += num

        elif operator == "-":

            result -= num

        elif operator == "*":

            result *= num

        elif operator == "/":

            result /= num

        return result



    return calc
calc = make_calc("*", initial=1)

print(calc(5))

print(calc(10))
print(calc(2))
print(calc(3))
from functools import wraps



def f(n):

    def decorator(func):

        @wraps(func)

        def wrapper(*args, **kwargs):

            results = []

            for _ in range(n):

                result = func(*args, **kwargs)

                results.append(result)

            return results

        return wrapper

    return decorator
@f(4)

def multiply_by_two(n):

    return n * 2
results = multiply_by_two(4)

print(results)