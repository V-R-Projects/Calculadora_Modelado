import sys
from pathlib import Path

if __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    import patron_multicapas.business
    __package__ = 'patron_multicapas.business'

from ..data.data import Data

class Business:
    def __init__(self, dataHandler_):
        self.dataHandler = dataHandler_