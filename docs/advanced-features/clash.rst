*********************
Using the Clash class
*********************

Clash is a name given to the combination of multiple strings which is used to find the gap of the strings. Think it of a object between gap and fill

You could make use of the Clash class implemented in the clashgap module to Clash two strings and find it's gap and fill. The Clash can be initialized by passing the input strings as a list. Here is a demonstration

.. code-block:: python

   clash = Clash(["spam", "ham"])

.. note::
   The Clash class currently only supports input list of length two

Constituent Methods
===================

+----------------------+----------------------------------------------------------------------+
| Name                 | Description                                                          |
+======================+======================================================================+
| :ref:`gap()<gap>`    | use this method to find the gap of the clash                         |
+----------------------+----------------------------------------------------------------------+
| :ref:`fill()<fill>`  | this methods returns the filled gap                                  |
+----------------------+----------------------------------------------------------------------+

.. _gap:

gap
---

Clash.gap() method returns the gap of the clash as a list

.. code-block:: python

   def gap(self: Clash) -> list

Here is a demonstration on how you can call the function

.. code-block:: python

   >>> clash = Clash(["spam", "ham"])
   >>> clash.gap()
   [["sp", "h"], "am"]

.. _fill:

fill
----

Clash.fill() method returns the clash itself as a list

.. code-block:: python

   def fill(self: Clash) -> list

Here is a demonstration on how you can call the function

.. code-block:: python

   >>> clash = Clash(["spam", "ham"])
   >>> clash.fill()
   ["spam", "ham"]

As you see, the fill() just returns the clash as a list. ``Clash(x).fill() == x`` is True for any valid ``x``

Using in-built function on Clash objects
========================================

+--------------------------+----------------------------------------------------------------------+
| In-built functions       | Description                                                          |
+==========================+======================================================================+
| :ref:`str()<str>`        | str(clash) returns the gap of Clash as a string                      |
+--------------------------+----------------------------------------------------------------------+
| :ref:`repr()<repr>`      | repr(clash) returns the gap of Clash as a string                     |
+--------------------------+----------------------------------------------------------------------+

.. _str:

__str__
-------

.. code-block:: python

   def __str__(self: Clash) -> str

The __str__ is a magic method used to define the behaviour on using the in-built str() function on a Clash object. Passing a Clash object on the str function will return the gap of the Clash object as a string

Here is a demonstration

.. code-block:: python

   >>> clash = Clash(["spam", "ham"])
   >>> str(clash)
   "[['sp', 'h'], 'am']"
   >>> type(str(clash))
   <class 'str'>

As per the demonstration, ``str(x) == str(x.gap())`` is True, for any valid Clash ``x``

.. _repr:

__repr__
--------

.. code-block:: python

   def __repr__(self: Clash) -> str

The __repr__ is a magic method used to define the behaviour on using the in-built repr() function on a Clash object. Passing a Clash object on the repr function will return the gap of the Clash object as a string

Here is a demonstration

.. code-block:: python

   >>> clash = Clash(["spam", "ham"])
   >>> repr(clash)
   "[['sp', 'h'], 'am']"
   >>> type(repr(clash))
   <class 'str'>

As per the demonstration, ``repr(x) == str(x.gap())`` is True, for any valid Clash ``x``
