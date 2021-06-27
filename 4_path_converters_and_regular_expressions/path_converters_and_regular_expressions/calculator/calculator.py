from decimal import Decimal


class Calculator:
    @staticmethod
    def add(x, y):
        return Decimal(x) + Decimal(y)

    @staticmethod
    def subtract(x, y):
        return Decimal(x) - Decimal(y)

    @staticmethod
    def multiply(x, y):
        return Decimal(x) * Decimal(y)

    @staticmethod
    def divide(x, y):
        return Decimal(x) / Decimal(y)
