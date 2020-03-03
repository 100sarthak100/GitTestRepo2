list1 = [1, 2, 3, 4, 5]
print(list(map(lambda x: (x) ** 0.5, list1)))


def decorator_function(orig_func):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {orig_func.__name__}")
        return orig_func(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


display()

