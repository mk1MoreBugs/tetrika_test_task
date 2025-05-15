def strict(func):
    annotations = func.__annotations__
    annotations_keys = list(annotations.keys())

    def wrapper(*args):
        print(args)
        for index, arg in enumerate(args):
            required_argument_type = annotations[annotations_keys[index]]
            if not isinstance(arg, required_argument_type):
                error_message = f"Argument {annotations_keys[index]} must be {required_argument_type}, got {type(arg)}"
                raise TypeError(error_message)
        return func(*args)

    return wrapper
