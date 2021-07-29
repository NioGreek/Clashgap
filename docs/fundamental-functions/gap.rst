*******************
The gap() functions
*******************

The gap function is used to combine a list with two elements into a gap object. It accepts a list with two elements as parameter, and returns another list representing the gap of the input list

.. code-block:: python

   gap(clash: list) -> list

Here is a demonstration of it's usage

.. code-block:: python

   import clasgap
   gap = clashgap.gap(["spam", "ham"])
   print(gap)

stdout:

.. code-block:: python

   [["sp", "h"], "am"]]

The gap() and fill() functions are inverse of each other. So ``fill(gap(x)) == x`` and ``gap(fill(y)) == y`` are both True, for any valid x and y

.. note::
   The gap function currently only supports input list of length two
