*******************
The fill() function
*******************

The fill function is used to combine a gap object, to get the clash. It accepts a list representing the gap as parameter, and returns another list representing the clash

.. code-block:: python

   fill(clash: list) -> list

Here is a demonstration of it's usage

.. code-block:: python

   import clasgap
   gap = clashgap.fill([["sp", "h"], "am"])
   print(gap)

stdout:

.. code-block:: python

   ["spam", "ham"]

The gap() and fill() functions are inverse of each other. So ``gap(fill(x)) == x`` and ``fill(gap(y)) == y`` are both True, for any valid ``x`` and ``y``

.. note::
   The fill function currently only supports input list of length two
