keyboard-anywhere
=================

A virtual musical keyboard using the XBox Kinect, written in python and based 
on libfreenect.
Since releasing the video, we've had a lot of requests for code. I have 
held off until this point, because the dependencies are quite complex, and
getting the code running is probably more trouble than it's worth. Still,
at least now you can read the code and see how we did it.

.. note:: 

    I have no intention of making an active project out of this. This 
    repository has been created to distribute the source code used in the demo 
    video, along with some basic information about setup and usage. Hopefully
    it will be sufficient for other uses to be able to run keyboard-anywhere
    on their own computer. If not, then hopefully the code will be useful for
    people developing for the Kinect. The code may be further developed and 
    features added, but I make no guarantees.

Basic Instructions
------------------
So far, I've only attempted to make this work on GNU/Linux (or more 
specifically, Ubuntu 10.04 and 10.10). All instructions assume you have
a recent Ubuntu install. Most (all?) of the libraries I have used are
cross platform, so if you've got some skill and patience, there's no
reason you shouldn't be able to get this working on OS X or Windows.
I'm just not providing any instructions for it.

Dependencies
~~~~~~~~~~~~

The python script depends on::

    freenect
    numpy
    pyopengl
    PyQt4
    PyQGLViewer
    fluidsynth

If you have all of them working in python, you're good to go. Otherwise
skip to the "Detailed Dependencies" section below.

Usage
~~~~~

Assuming all the dependencies are working ok, running the script will produce 
a seemingly empty grey window. This window is produced by QGLViewer, so you
can press the 'h' key to access a help screen. A quick summary of that information
is provided below:

- 	Double click the middle mouse to centre the view (you should see some keys)
-   Press ENTER to start the displaying of kinect data (here's where it will crash
    if you didn't get freenect installed correctly, or your kinect isn't plugged in)
-	Left click and drag to rotate the view, right click and drag to move it
-	Scroll wheel zooms the view

Once you've figured out the view, and waved to yourself in live kinect data, 
press the 'f' key to display FPS information. If it's 30, that's great, you're
keeping up with the kinect. If it's significantly less than that (say 10), playing
the keyboard might not be much fun, and you'll need to try a faster computer. 

Now, define where you want the keyboard to be:

-	Orient the view so you can see the surface on which you want to place the keyboard
-	Press ENTER to pause the kinect data
-	Press the '1' key
-	Holding SHIFT, left click a data point to set the lower left corner of the piano
	(Note: you must actually click on a point for it to work. You'll see a confirmation
	message when it does. If you're struggling to hit a point, try zooming out).
-	Press the '2' key
-	Again holding SHIFT, left click a data point. This sets the lower right corner
-	Press the '3' key
-	SHIFT + left-click another point. This will be used to set the upper corners of
	the keyboard. If this doesn't make sense, try it out and just see where the
	keyboard appears. It won't look right until you've set all three points.
- 	To modify any of the points, just press '1', '2' or '3' and try again

Press ENTER to resume the live data. Chances are, the keyboard will intersect 
some of the data points (meaning that you'll hear notes, and the keys will 
light up green). To solve this, experiment with pressing and holding 'z' or
'SHIFT + z' to 'nudge' the keyboard away from the existing data until all the
notes are off. 

Now wave your hands / limbs / children through the areas marked out by the
virtual keys, and make some music!


Detailed Dependencies
---------------------

I got keyboard-anywhere working on a fresh Ubuntu 10.10 install with the
following steps.

1.  apt-get install the following (this is AFAIK the minimal set):

    - PyQGLViewer / PyQt4

        - build-essential
        - pyqt4-devtools
        - qt4-qmake
        - libqt4-dev
        - python-qt4-gl
        - python-qt4-dev
        - python-numpy
        - python-setuptools

    - freenect

        - cmake
        - libusb-1.0-0-dev
        - freeglut3-dev
        - libxmu-dev
        - libxi-dev

    - audio output

        - fluidsynth
        - fluid-soundfont-gm

2.  use easy_install to get cython 0.14 (``sudo easy_install cython``)

3.  compile libfreenect (with BUILD_PYTHON set to ON)
    (follow the instructions at https://github.com/OpenKinect/libfreenect)

4.  download, compile and install QGLViewer and PyQGLViewer (follow instructions in the 
    INSTALL or README files):

    - https://gforge.inria.fr/frs/download.php/28138/libQGLViewer-2.3.9-py.tgz
    - https://gforge.inria.fr/frs/download.php/28139/PyQGLViewer-0.9.0.zip





.. image:: https://d2weczhvl823v0.cloudfront.net/petermoz/keyboard-anywhere/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

