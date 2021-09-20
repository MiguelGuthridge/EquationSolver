"""Ensure that the comma operator is collecting correctly

Most of this is tested implicitly through other tests of functions
"""

import pytest

from .helpers import equate

from equator import EqCommaError

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
