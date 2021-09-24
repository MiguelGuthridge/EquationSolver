"""Ensure that the comma operator is collecting correctly

Most of this is tested implicitly through other tests of functions
"""

import pytest

from .helpers import equate

from equator import EqCommaError, EqParserException, EqRangeError

#
# Comma operator
################################################################################

def testCollect():
    """Collect comma-separated items. Raise exception because must be sent to
    a function
    """
    with pytest.raises(EqCommaError):
        equate("1, 2, 3, 4, 5")

def testComplexCollect():
    """Collecting comma-separated items except amongst other stuff
    """
    with pytest.raises(EqCommaError):
        equate("2 * (2, 5, x) - 4 + (2 * 3, 1, 3 / 2)")

def testMissingBefore():
    """Missing item before a comma
    """
    with pytest.raises(EqParserException):
        equate("max(, 2, 3, 4)")

def testMissingAfter():
    """Missing item after a comma
    """
    with pytest.raises(EqParserException):
        equate("max(2, 3, 4, )")

def testMissingMiddle():
    """Missing item between two commas
    """
    with pytest.raises(EqParserException):
        equate("max(2, 3, 4, , 6)")

#
# Range operator
################################################################################

def test_range_operator():
    with pytest.raises(EqRangeError):
        equate("1..5")

def test_range_operator_bad_args():
    # TODO: Is this a good exception type to use?
    with pytest.raises(EqRangeError):
        equate("1..5..5")
    with pytest.raises(EqRangeError):
        equate("x..(1, 2, 3)")
