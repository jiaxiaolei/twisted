# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import pdb; pdb.set_trace()
if __name__ == '__main__':
    from pkg_resources import load_entry_point
    import sys

    sys.exit(
        load_entry_point('Twisted', 'console_scripts', 'trial')()
    )
