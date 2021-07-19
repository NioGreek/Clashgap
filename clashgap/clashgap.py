from __init__ import __version__
from _gap import gap

class clash:
    def __init__(self, clash):
        self._gap = gap(clash)

    def gap(self):
        return self._gap

