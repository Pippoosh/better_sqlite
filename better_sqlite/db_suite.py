class SuiteMeta(type):
    def __repr__(cls):
        """
        Custom string representation for the class itself.
        """
        attrs = ',\n    '.join(
            f"{key}={value}" for key, value in cls.__dict__.items() if not key.startswith('__')
        )
        return f"{cls.__name__}(\n    {attrs}\n)" if attrs else f"{cls.__name__}()"


def suite(cls):
    """
    A decorator that applies a metaclass to a class for custom __repr__.

    Args:
        cls: The class to be decorated.

    Returns:
        cls: The decorated class with a custom __repr__ method.
    """
    return cls
