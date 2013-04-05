Day 1 / Afternoon
=================

Doing data analysis
-------------------

(Karen Cranston)

See `the IPython Notebook, numpy-and-graphing.ipynb <http://nbviewer.ipython.org/urls/raw.github.com/swcarpentry/2013-04-az/master/notebooks/numpy-and-graphing.ipynb>`__.

A bit more IPython Notebook and matplotlib
------------------------------------------

`The whole IPython Notebook gallery <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`__

See: http://ged.msu.edu/papers/2012-diginorm/ for an example of a paper
where all the figures were generated with ipynb.

Matplotlib gallery: http://matplotlib.org/gallery.html

Note that you can use ::

   %loadpy http://matplotlib.org/mpl_examples/api/bbox_intersect.py

on the source code in the gallery links to load the code into ipynb
and execute it.

Testing
-------

(Titus Brown)

See `the IPython Notebook, testing-with-nose.ipynb <http://nbviewer.ipython.org/urls/raw.github.com/swcarpentry/2013-04-az/master/notebooks/testing-with-nose.ipynb>`__.


When we say "testing" we really mean *automated testing*.
The central problems addressed by testing are *correctness* and
*reproducibility*.  (While these are linked, they are not the
same!)

I don't want to depart from the *efficiency* argument, though --
being able to make sure your old code *stays* working is very
important to moving forward with 

There are two basic kinds of tests that I'd like to briefly
discuss.  One kind of test is a *unit test*.  The other kind
of test is a *regression test*.  (There are also many more.)

Unit tests address *small units of code*, like functions.  They
are used to isolate and nail down and prove the functionality
of potentially complicated little functions.

Regression tests address *the overall function of code*, and
they are used to make sure that your code is doing the same
thing *today* as it was *yesterday*.

I'll show you examples of both.

Writing tests
~~~~~~~~~~~~~

We're going to be using the nose testing framework, which is
just a framework that makes it easy to find and execute
tests.

Basically, 'nose' creates a command 'nosetests' that finds and
runs tests.  The idea is that you won't need to register new tests.

A test function looks like this::

   def test_something():
      # run some code
      # fail loudly or succeed silently

.. @@ See `testing-with-nose.ipynb <http://nbviewer.ipython.org/urls/raw.github.com/swcarpentry/2012-11-scripps/master/python/testing-with-nose.ipynb>`__.

More reading
~~~~~~~~~~~~

For more reading, see:

   http://software-carpentry.org/4_0/test/

and

   http://ivory.idyll.org/articles/nose-intro.html

and also

   http://ivory.idyll.org/blog/software-quality-death-spiral.html


Installing Python packages; useful Python packages
--------------------------------------------------

Using pip, which is an interface to `PyPi <https://pypi.python.org/pypi>`__

See :doc:`day1-python-packages`

Also see `the IPython Notebook, using-screed.ipynb <http://nbviewer.ipython.org/urls/raw.github.com/swcarpentry/2013-04-az/master/notebooks/using-screed.ipynb>`__.

----

Done!
