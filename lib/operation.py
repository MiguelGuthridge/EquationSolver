import math
import sympy as sym
from decimal import Decimal
from fractions import Fraction

from . import consts

FUNCTION_OPERATOR_PRECEDENCE = 10
NO_OPERATION_PRECEDENCE = 10

def operatorPrecedence(op: str):
    if   op in ['^']: return 3
    elif op in ['*', '/']: return 2
    elif op in ['+', '-']: return 1
    elif op in ['=']: return 0

def conditionalDecimal(a):
    return Decimal(str(float(a))) if isinstance(a, Fraction) else a

def conditionalFraction(a):
    if isinstance(a, Decimal):
        fract = Fraction(a)
        if len(str(fract)) < 10:
            return fract
        else:
            return a
    else:
        return a

def zeroRound(num):
    """Replaces values close to zero with zero
    And values close(ish) to infinity with infinity

    Args:
        num (Decimal | Any): value to check (will only round 
                             if can be converted to decimal)

    Returns:
        Decimal | Any: value, rounded if necessary
    """
    try:
        num = Decimal(float(num))
        if abs(num) < 10**(-consts.MAX_PRECISION):
            num = Decimal(0)
        elif abs(num) > 10**consts.MAX_PRECISION:
            num = Decimal("inf")
    except Exception:
        pass
    return num

def doOperation(operator: str, a, b):
    a = conditionalDecimal(a)
    b = conditionalDecimal(b)
    if operator == '^':
        res = a ** b
    elif operator == '*':
        res = a * b
    elif operator == '/':
        res = a / b
    elif operator == '+':
        res = a + b
    elif operator == '-':
        res = a - b
    elif operator == '=':
        res = sym.Eq(a, b)
    else:
        raise ValueError("Unrecognised operation: " + operator)
    return conditionalFraction(res)

def doFunction(func: str, a):
    if func == "sqrt":
        return sym.sqrt(a)
    elif func == "sin":
        return zeroRound(sym.sin(a))
    elif func == "cos":
        return zeroRound(sym.cos(a))
    elif func == "tan":
        return zeroRound(sym.tan(a))
    elif func == "asin":
        return zeroRound(sym.asin(a))
    elif func == "acos":
        return zeroRound(sym.acos(a))
    elif func == "atan":
        return zeroRound(sym.atan(a))
    elif func == "abs":
        return sym.Abs(a)
    elif func == "deg":
        return a * 180 / consts.CONSTANTS["pi"]
    elif func == "rad":
        return a / 180 * consts.CONSTANTS["pi"]
    elif func == consts.NEGATE:
        return -a
    elif func == "exp":
        return sym.exp(a)
    elif func == "log":
        return sym.log(a, 10.0)
    elif func == "ln":
        return sym.log(a)
    elif func.startswith("log_"):
        base = Decimal(func.replace("log_", ""))
        return sym.log(a, base)

def getConstant(const: str):
    if const in consts.CONSTANTS:
        return str(consts.CONSTANTS[const])
    else:
        return const

def _doReduceSqrt(num: int):
    # Generate a list of all perfect squares up to num
    iterator = range(2, int(math.sqrt(num)) + 1)
    squares = [i**2 for i in iterator]
    roots = [i for i in iterator]
    multiple = 1
    for rt, sq in zip(roots, squares):
        if num % sq == 0:
            multiple *= rt
            num //= sq
    return multiple, num

def reduceSqrt(sq: Fraction):
    """Returns a reduced equivalent of a square root

    Args:
        sq (Decimal): input decimal (squared)

    Returns:
        tuple: (a [Fraction], b [Fractions]) representing a*sqrt(b)
    """
    # Operate on numerator and denominator seperately
    
    numerator, denominator = sq.numerator, sq.denominator
    
    num_a, num_b = _doReduceSqrt(numerator)
    den_a, den_b = _doReduceSqrt(denominator)
    
    return Fraction(num_a, den_a), Fraction(num_b, den_b)
