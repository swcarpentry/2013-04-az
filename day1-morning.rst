Day 1 / Morning
===============

Introductions!
--------------

For more on efficiency, reproducibility, and correctness, see `this
talk Titus gave in Colorado yesterday,
<http://www.slideshare.net/c.titus.brown/2013-ucar-best-practices>`__,
as well as the paper `Best Practices in Scientific Computing <http://arxiv.org/abs/1210.0530>`__.

You might also be interested in `this blog post and the associated paper
on version control <http://blogs.biomedcentral.com/bmcblog/2013/02/28/version-control-for-scientific-research/>`__.

.. @@ upload my presentation

Using this Web site
-------------------

Reload to get the latest links!

Commenting

Here's an Etherpad that we'll paste stuff into: `the etherpad link <http://openetherpad.org/oYBcyQ6ROS>`__.

Intro technology, and Python basics
-----------------------------------

(Titus Brown)

Git quick guide:

 - to retrieve the materials for the class, do::

      git clone https://github.com/swcarpentry/2013-04-az.git
      cd 2013-04-az 

   at the shell prompt.

 - to update the materials, do::

      git pull origin master

IPython Notebook quick guide:

 - run ::

      ipython notebook --pylab=inline

   in the directory containing your notebook files.  A Web view of the
   notebook should pop up.

Python installing guide:

 - run, variously, one of ::

      pip install <packagename>

   or ::

      ~/anaconda/bin/pip install <packagename>

   or ::

      sudo pip install <packagename>

Applying Python basics to data analysis
---------------------------------------

(Rich Enbody)

`Counting birds (full of code) <https://raw.github.com/swcarpentry/2013-04-az/master/notebooks/10-introducing-bird-counting-FULL.ipynb>`__

`Counting birds (empty) - for the intrepid <https://raw.github.com/swcarpentry/2013-04-az/master/notebooks/10-introducing-bird-counting-EMPTY.ipynb>`__

`Generating the raw data -- for the interested <https://raw.github.com/swcarpentry/2013-04-az/master/notebooks/99-generate-lots-of-birds.ipynb>`__
