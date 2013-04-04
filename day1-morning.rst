Day 1 / Morning
===============

Introductions!
--------------

`Introductory talk <http://www.slideshare.net/c.titus.brown/2013-arizonaswc>`__

For more on efficiency, reproducibility, and correctness, see `this
talk Titus gave in Colorado yesterday,
<http://www.slideshare.net/c.titus.brown/2013-ucar-best-practices>`__,
as well as the paper `Best Practices in Scientific Computing <http://arxiv.org/abs/1210.0530>`__.

You might also be interested in `this blog post and the associated paper
on version control <http://blogs.biomedcentral.com/bmcblog/2013/02/28/version-control-for-scientific-research/>`__.

Using this Web site
-------------------

Reload to get the latest links!

Commenting

Here's a `Google Doc that we'll paste stuff into: <https://docs.google.com/document/d/180QIKxhtM4bbbYAdUbO6_dSWMoSFACe3dxrzwh7emjE/edit?usp=sharing>`__.

Intro technology, and Python basics
-----------------------------------

(Titus Brown)

Git quick guide:

 - to retrieve the materials for the class, do::

      git clone https://github.com/swcarpentry/2013-04-az.git
      cd 2013-04-az/notebooks

   at the shell prompt.  On Windows, you may need to use Git Bash
   to create the directory, and then cmd.exe to run ipython notebook (see
   below).

 - to update the materials, do::

      git pull origin master

IPython Notebook quick guide:

 - run ::

      ipython notebook --pylab=inline

   in the directory containing your notebook files.  A Web view of the
   notebook should pop up.

   If you're using Anaconda, you can type::

      c:\anaconda\scripts\ipython notebook --pylab=inline

   The trick will be running this in the correct directory, but you have
   a little bit of time to figure this out because we won't start with
   a preexisting notebook.

 - executing code ::

      shift-ENTER -- to execute current "code cell" and move to next
      ctrl-ENTER -- to execute current "code cell" and stay

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

`Counting birds (full of code) <http://nbviewer.ipython.org/urls/raw.github.com/swcarpentry/2013-04-az/master/notebooks/10-introducing-bird-counting-FULL.ipynb>`__

`Generating the raw data -- for the interested <http://nbviewer.ipython.org/urls/raw.github.com/swcarpentry/2013-04-az/master/notebooks/99-generate-lots-of-birds.ipynb>`__

