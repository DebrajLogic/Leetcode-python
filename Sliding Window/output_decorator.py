def output(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(result)
    return wrapper
