import inspect
from collections import OrderedDict
import random

def my_cache(max_cache_size=5):
    def decorator(func):
        cache = OrderedDict()
        sig = inspect.signature(func)

        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            # Преобразуем в неизменяемую структуру
            all_args = (
            tuple(bound_args.args), frozenset(bound_args.kwargs.items()))

            if all_args in cache:
                print("берем значение из кэша:")
                return cache[all_args]
            else:
                res = func(*bound_args.args, **bound_args.kwargs)
                if len(cache) >= max_cache_size:
                    print("удаляем первый добавленный элемент в кэш")
                    cache.popitem(last=False)
                cache[all_args] = res
                return res

        return wrapper

    return decorator

#tests
@my_cache()
def rand_sum(a, b=0):
    return a + b + random.random()

@my_cache(3)
def rand_sum1(a,b=0):
    return a + b + random.random()

@my_cache()
def rand_sum_kwargs(**kwargs):
    sum=random.random()
    for key, value in kwargs.items():
        if isinstance(value, int):
            sum+=value
    return sum

#проверка для размера кэша 5
print("\nRandsum 1-6")
print(rand_sum(1,0))
print(rand_sum(2,0))
print(rand_sum(3,0))
print(rand_sum(4,0))
print(rand_sum(5,0))
print(rand_sum(6,0))
print("Randsum 6-1")
print(rand_sum(6,0))
print(rand_sum(5,0))
print(rand_sum(4,0))
print(rand_sum(3,0))
print(rand_sum(2,0))
print(rand_sum(1,0))

#проверка для значений по умолчанию
print("\nRandsum 1")
print(rand_sum(1))

#проверка для памяти 3
print("\nRandsum1 3,0-3,3")
print(rand_sum1(3,0))
print(rand_sum1(3,1))
print(rand_sum1(3,2))
print(rand_sum1(3,3))
print("Randsum1 3,3-3,0")
print(rand_sum1(3,3))
print(rand_sum1(3,2))
print(rand_sum1(3,1))
print(rand_sum1(3,0))

#проверка для kwargs
print("\nKwargs")
print(rand_sum_kwargs(x1=1,x2=2))
print(rand_sum_kwargs(x3=1,x2=2))
print(rand_sum_kwargs(x1=1,x2=2))
