from __init__ import __version__
from _gap import gap

class clash:
    def __init__(self, poles):
        self._clash = gap(poles)

    def gap(self):
        return self._clash
