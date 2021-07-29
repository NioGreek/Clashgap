*********************
Using the Clash class
*********************

Clash is a name given to the combination of multiple strings which is used to find the gap of the strings. Think it of a object between gap and fill()

You could make use of the Clash class implemented in the clashgap module to Clash two strings and find their gap and fill. The Clash can be initialized by passing the input strings as a list. Here is a demonstration

.. code-block:: python

   clash = Clash(["spam", "ham"])

.. note::
   The Clash class currently only supports input list of length two

Constituent Methods
===================

+-------------+----------------------------------------------------------------------+
| Name        | Description                                                          |
+=============+======================================================================+
| gap         | use this method to find the gap of the clash                         |
+-------------+----------------------------------------------------------------------+
| fill        | this methods returns the filled gap                                  |
+-------------+----------------------------------------------------------------------+
| __str__     | using the in-built str() on clash returns the gaped clash as string  |
+-------------+----------------------------------------------------------------------+
| __repr__    | using the in-built repr() on clash returns the gaped clash as string |
+-------------+----------------------------------------------------------------------+

gap
---
