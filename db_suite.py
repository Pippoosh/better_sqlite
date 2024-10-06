def suite(cls):
    """
    A decorator that adds a custom __repr__ method to a class.

    Args:
        cls: The class to be decorated.

    Returns:
        cls: The decorated class with a custom __repr__ method.
    """

    # Define a custom __repr__ method for the class
    def class_repr(self):
        """
        Custom string representation for class instances.

        Returns:
            str: A formatted string representing the class instance's attributes.
        """
        # Join the attribute names and values into a string
        attrs = ', '.join(f'{key}={value}' for key, value in self.__dict__.items() if not key.startswith('__'))
        # Return the formatted representation
        return f"{self.__class__.__name__}({attrs})" if attrs else f"{self.__class__.__name__}()"

    # Attach the custom __repr__ to the class
    cls.__repr__ = class_repr
    return cls
