"""Basic functions and stuff
"""

import sympy
from decimal import Decimal

from .unary_function import UnaryFunction

from .. import tokens
from ..segment import Segment

class SqrtFunction(UnaryFunction):
    """Square root function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("sqrt"), on, sympy.sqrt)

class SinFunction(UnaryFunction):
    """Sine function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("sin"), on, sympy.sin)

class CosFunction(UnaryFunction):
    """Cosine function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("cos"), on, sympy.cos)

class TanFunction(UnaryFunction):
    """Tan function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("tan"), on, sympy.tan)

class AsinFunction(UnaryFunction):
    """Inverse sine function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("asin"), on, sympy.asin)

class AcosFunction(UnaryFunction):
    """Inverse cosine function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("acos"), on, sympy.acos)

class AtanFunction(UnaryFunction):
    """Inverse tan function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("atan"), on, sympy.atan)

class AbsFunction(UnaryFunction):
    """Abs function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("abs"), on, sympy.Abs)

class DegFunction(UnaryFunction):
    """Degrees function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("deg"), on, sympy.deg)

class RadFunction(UnaryFunction):
    """Radians function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("rad"), on, sympy.rad)

class ExpFunction(UnaryFunction):
    """Exponent function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("exp"), on, sympy.exp)

class LnFunction(UnaryFunction):
    """Natural logarithm function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("ln"), on, sympy.log)

class LogFunction(UnaryFunction):
    """Base 10 logarithm function"""
    def __init__(self, on: Segment):
        super().__init__(tokens.Symbol("log"), on, sympy.log, 10)

class LogBaseFunction(UnaryFunction):
    """Logarithm function of any base"""
    def __init__(self, on: Segment, base: Decimal):
        super().__init__(tokens.Symbol("tan"), on, sympy.log, base)