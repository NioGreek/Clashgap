Getting Started with Clashgap
=============================

Clashgap is a diff/compression module in python

How it works
------------

In case if you have two strings:

    "This is a sentence..." and "This is a word..."

you could "clash" both of them together and find their gap, to get an array loking something like:

    ["This is a", ["sentence", "word"], "..."]

As you can the clashgap algorithm looks for collisions in the two strings to find the gap. The clashgaped string maybe used for compression or as the diff of the input strings

Getting Started
---------------

To start using the package you would have to install it. Have a look at the Installation guide. After that out of the way, give it a try by following the instructions at the Give it a try guide

- :doc:`Installing Clashgap <getting-started/installation>`
- :doc:`Give it a try <getting-started/give-it-a-try>`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Getting Started

   getting-started/installation
   getting-started/give-it-a-try

Fundamental Functions
---------------------

The fundamental functions of the package is ``gap()`` and ``fill()``

- :doc:`The gap() function <fundamental-functions/gap>`
- :doc:`The fill() function <fundamental-functions/fill>`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Fundamental Functions

   fundamental-functions/fill
   fundamental-functions/gap

Advanced Features
-----------------

You could also check out thre Clash class, which enables you instantiate a Clash object, with the input array.

- :doc:`The Clash class <advanced-features/clash>`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Advanced Fetures

   advanced-features/clash

About Clashgap
--------------

To find more about the project, you may head on to any of these links

- `PyPI project page <https://pypi.org/project/clashgap>`_
- `GitHub repo <https://github.com/NioGreek/Clashgap>`_
- :doc:`Changelog<about-clashgap/changelog>`
- :doc:`All Links<about-clashgap/links>`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: About Clashgap

   about-clashgap/changelog
   about-clashgap/links
