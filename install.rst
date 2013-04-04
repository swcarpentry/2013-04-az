Software Installation
=====================

Please follow the instructions below.  If you have trouble installing
things, that's OK -- we can help. Just be sure to download the files,
because some of them are quite large.

Quick guide
-----------

1. Download and install `VirtualBox <https://www.virtualbox.org/>`__

2. Download `this BIG file <http://is.gd/MosNIh>`__ and import it into
   VirtualBox.

3. Download and install `Anaconda CE <http://continuum.io/anacondace.html>`__.

4. If on Windows, `install Git Bash <https://openhatch.org/missions/windows-setup/install-git-bash>`__

5. If on Mac OS X, either `install XCode <https://developer.apple.com/xcode/>`__ and the command line tools, OR (easier!) `just install Git <http://code.google.com/p/git-osx-installer/downloads/list?can=3>`__.

5. Choose a code editor, below, and install that.

Links and more details
----------------------

Virtual Machine
~~~~~~~~~~~~~~~

To give everyone a consistent, pre-configured environment we provide a
Linux virtual machine. Install `VirtualBox
<https://www.virtualbox.org/>`__ and download `this virtual machine
image <http://is.gd/MosNIh>`__.

Load the VM into VirtualBox by doing Import Appliance and loading the
.ova file.

Other Options than the virtual machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To complete the entire workshop you need several things: a Bash shell,
git, a code editor (though any plain text editor will work in a
pinch), and a scientific Python installation that includes the IPython
Notebook, NumPy, and matplotlib.

Even if you plan to install things yourself please download VirtualBox
and the virtual machine as a backup. It can be extremely difficult to
get everything set up correctly, and the virtual machine almost always
works.

Bash
~~~~

Mac:

No installation needed; the default shell in Mac OS X is bash.

Windows:

Install `Git Bash <http://msysgit.github.com/>`__ following the instructions
`here <https://openhatch.org/missions/windows-setup/install-git-bash>`__.

Linux:

The default shell is usually bash but if not you can get to bash by
opening a terminal and typing "bash".

Git
~~~

Mac:

Install `Xcode <https://developer.apple.com/xcode/>`__ and the command line tools (from the Download preferences pane) or install `just git <http://code.google.com/p/git-osx-installer/downloads/list?can=3>`__.

Windows:

Install `Git Bash <http://msysgit.github.com/>`__ following the instructions
`here <https://openhatch.org/missions/windows-setup/install-git-bash>`__.

Linux:

If git is not already available on your machine you can try to install
it via your distro's package manager (e.g. apt-get).  We can help you with
this at the workshop.

Code Editor
~~~~~~~~~~~

Mac:

We recommend `Text Wrangler <http://www.barebones.com/products/textwrangler/>`__, `Sublime Text <http://www.sublimetext.com/>`__, or `Text Mate 2 <https://github.com/textmate/textmate>`__.

Windows:

`Notepad++ <http://notepad-plus-plus.org/>`__ is a popular free code
editor for Windows.

Linux:

`Kate <http://kate-editor.org/>`__ and `gedit <http://projects.gnome.org/gedit/>`__ are options for Linux users.

Python
~~~~~~

We recommend the all-in-one scientific Python installer `Anaconda CE
<http://continuum.io/anacondace.html>`__. Installation on Mac and
Linux requires using the shell and if you aren't comfortable doing the
installation yourself just download the installer and we'll help you
at the boot camp.

For other options check the Python4Astronomers page on `installing
scientific Python
<http://python4astronomers.github.com/installation/python_install.html>`__.

Technical details
-----------------

See: http://software-carpentry.org/setup/
