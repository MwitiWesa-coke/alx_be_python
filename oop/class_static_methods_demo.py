class Calculator:
    calculation_type = "Arithmetic Operations" # Class attribute

    @staticmethod
    def add(a, b):
        """static method to add two numbers"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multipy two numbers, prints class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
