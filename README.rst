ln.py
=====

.. image:: http://img.shields.io/pypi/v/ln.py.png
  :target: https://pypi.python.org/pypi/ln.py

You always get ``ln`` arguments in the wrong order?

Then ``ln.py`` is for you.

Installation
-------------

``pip install ln.py`` or similar.

Usage
-----

Type `lnp A B` and lnp will ask you to choose the direction of the link
-  that way you don't have to remember tho order of the arguments :)

.. code-block:: console

   > lnp A B
   1. A -> B
   2. B -> A
   Which one? 1
   A -> B

``lnp`` will allow you to update a link:

For instance, if ``latest`` is a symlink to ``1.0``,
then you con update the link to ``2.0`` this way:

.. code-block:: console

   lnp latest 2.0
   1. latest -> 2.0
   2. 2.0 -> latest
   Which one? 1
   latest -> 1.0 already exists. Overwrite (Y/n) y
   latest -> 2.0

lnp will also refuse to replace a "real"  file with a symlink because
that's almost always a mistake. If you really want to do this, use
``rm`` to remove the problematic file first.


API
---

Since ln.py is written in Python you can also use it as a replacement
of the standard library ``os.symlink`` function:

.. code-block:: python

    from ln import ln

    ln(from_="latest", to="1.0)

