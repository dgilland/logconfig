# pylint: skip-file
"""Python 2/3 compatibility
"""

import sys


PY2 = sys.version_info[0] == 2


if PY2:  # pragma: no cover
    string_types = (str, unicode)
else:  # pragma: no cover
    string_types = (str,)
