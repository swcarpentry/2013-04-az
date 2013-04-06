Wrapping up - Day 2, afternoon
==============================

Everything is on the Web site
-----------------------------

We've tried to put everything up on the Web site.  Please ask us if
you can't find it!

Additional resources include those in :doc:`resources`, as well as
using Google to look for answers, and checking out both `StackOverflow
<http://stackoverflow.com/>`__ and `BioStars
<http://biostars.org/>`__.

You might also consider `attending office hours <http://software-carpentry.org/bootcamps/office-hours.html>`__.

Posting IPython Notebooks
-------------------------

You can post IPython Notebooks on github, and view them statically via
nbviewer.ipython.org (i.e.  without loading them into a running
IPython Notebook instance).  For example, see:

https://github.com/swcarpentry/2013-04-az/blob/master/notebooks/10-introducing-bird-counting-FULL.ipynb

which can be viewed in "raw" form here:

https://github.com/swcarpentry/2013-04-az/raw/master/notebooks/10-introducing-bird-counting-FULL.ipynb

and which can be viewed in rendered form by pasting the 'raw' URL into
http://nbviewer.ipython.org:

http://nbviewer.ipython.org/urls/github.com/swcarpentry/2013-04-az/raw/master/notebooks/10-introducing-bird-counting-FULL.ipynb

Moving around directories in the shell
--------------------------------------

Paths, directories, and file locations are a source of great confusing.
Here are a few simple rules:

1. Treat everything as a relative location.

   For example, if you're in the 2013-04-az/scripts folder and you want to
   reference a file in the 2013-04-az/data folder, use::

       ../data/filename

   where the '..' means "go up one level" and the '/data/' means "go down
   into the data directory from there."

2. pwd will tell you what directory you're in.

3. cd will change your current directory.

4. ls will list files in your current directory.

5. TAB completion is your friend.  TAB completion does two things:
   it makes you less typo-prone, AND it makes sure that the 
   file actually exists (because you can only tab-complete on files
   that are actually there).


Shell scripts and pipelines
---------------------------

In the `scripts subdirectory <https://github.com/swcarpentry/2013-04-az/blob/master/scripts>`__, we have a number of Python scripts.  Turn your attention to three of them, please:

`make-big-birdlist.py <https://github.com/swcarpentry/2013-04-az/blob/master/scripts/make-big-birdlist.py>`__ -- creates a bunch of fake bird data.  Run by giving it the name of the file that you want it to output, e.g.::

   python make-big-birdlist.py counts.csv

`make-birdcounts.py <https://github.com/swcarpentry/2013-04-az/blob/master/scripts/make-birdcounts.py>`__ -- parses the counts.csv file and converts dates into day-of-year, then produced a histogram of bird counts by day.  This is then saved into a .dat file that can be loaded by the next script.  Usage::

   python make-birdcounts.py counts.csv counts.dat

`plot-birdcounts.py <https://github.com/swcarpentry/2013-04-az/blob/master/scripts/plot-birdcounts.py>`__ -- loads in the counts.dat file, produces a plot, and then saves the plot. ::

   python plot-birdcounts.py counts.dat counts.pdf

These are three automated scripts that each do some smaller part of an overall
larger set of tasks - essentially, a data analysis pipeline.

You could run all three scripts above by hand, but that's error prone.
You could also combine all three scripts above into one -- there's no
reason why not -- but that's inflexible, especially if there are multiple
ways to use the scripts (not so in the above case, but frequently true
in real cases) or if some of the steps take a long time.

So what to do?

You can write a shell script, as in `make-plot.sh <https://github.com/swcarpentry/2013-04-az/blob/master/scripts/make-plot.sh>`__.  This can be run by typing::

   bash make-plot.sh

All this is is a list of the commands you want run at the shell --
simplicity itself, right?  No hidden tricks here.  It's that simple.

Note that a good way to get a shell script started is to run a series
of commands at the shell, then -- when done -- type 'history' to get a
list of the commands you've run.  Copy/paste from that history into
a file, and you've got a shell script of sorts!

Remember to version control your shell scripts :)

Writing shell scripts is a good way to keep track of what it is you've
actually run, as opposed to what you think you've run.  And once
they're version controlled, well, now you're really in good shape for
your methods section...

Final point: if you look at the shell script, you'll see that every
time you run it, it runs all three commands.  For large data sets,
this can get time consuming, especially if you're working to optimize
one step, or doing parameter explanation.  There's a program called
'make' that can keep track of what has changed and what needs to be run
again based on those changes, but you have to configure it a bit with
a file called 'Makefile'.

For an example from our own pipeline for the diginorm paper, see:

   https://github.com/ged-lab/2012-paper-diginorm/blob/master/pipeline/Makefile
