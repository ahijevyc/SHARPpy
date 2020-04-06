<<<<<<< HEAD
from . import _sharppy_version as version
=======
#from . import _sharppy_version as version
>>>>>>> bc150d10e33555001255d0c9a8e33935c21790fc

__all__ = ['version', 'sharptab', 'viz', 'databases', 'io', 'plot']

#__version__ = version.get_version()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

