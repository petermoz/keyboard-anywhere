#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Copyright 2011 Peter Morton & Matthew Yeung
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
A simple demo showing reading data from the Kinect, and displaying
it using libQGLViewer. 

"""


from PyQt4 import QtCore, QtGui
import PyQGLViewer
import OpenGL.GL as ogl
import numpy as np
import time
import freenect


SAMPLE_STRIDE = 2          # Divide depth map resolution by this amount

# Precompute U, V coordinates (since they never change)
U, V = np.meshgrid(np.arange(0,640, SAMPLE_STRIDE), 
                   np.arange(0,480, SAMPLE_STRIDE))


def depth_to_xyz(u, v, stride, depth):
    """ Convert depth map to cartesian coordinates. 
    
    Parameters as originally determined by Zephod (? I think). Or found on
    the OpenKinect.org mailing list
    
    """
    
    depth_flipped = depth[::-stride, ::stride]
    valid = depth_flipped != 2047    # Non-return = 2047
    
    us = u[valid].flatten()
    vs = v[valid].flatten()
    ds = depth_flipped[valid]

    KinectMinDistance = -10
    KinectDepthScaleFactor = .0021
    
    zz = 100.0 / (-0.00307 * ds + 3.33)
    xx = (us - 320) * (zz + KinectMinDistance) * KinectDepthScaleFactor
    yy = (vs - 240) * (zz + KinectMinDistance) * KinectDepthScaleFactor
    zz = -(zz - 200)    # Move sensor from origin (easier for displaying)
    
    points = np.vstack((xx,yy,zz)).astype(float)
    return points                     


class Viewer(PyQGLViewer.QGLViewer):
    """ Subclass PyQGLViewer to provide additional functionality. """
    
    def __init__(self):
        PyQGLViewer.QGLViewer.__init__(self)        
        self.points = np.zeros((3,1))
    
    def init(self):
        """ For initialisation once OpenGL context is created. """
        self.setAnimationPeriod(33)
        
        ogl.glDisable(ogl.GL_LIGHTING)
        ogl.glEnableClientState(ogl.GL_VERTEX_ARRAY)
        ogl.glEnable(ogl.GL_BLEND)
        ogl.glBlendFunc(ogl.GL_SRC_ALPHA, ogl.GL_ONE_MINUS_SRC_ALPHA)
        ogl.glEnable(ogl.GL_CULL_FACE)
        ogl.glPointSize(2.0)

        self.setStateFileName('display_kinect.xml')
        if not self.restoreStateFromFile():
            self.camera().setSceneRadius(500)
        
    def animate(self):
        """ Get the latest data from the kinect, and update the state. """
        depth, timestamp = freenect.sync_get_depth()
        xyz = depth_to_xyz(U, V, SAMPLE_STRIDE, np.array(depth))
        self.points = xyz
    
    def draw(self):
        """ Draw the point cloud and keyboard. """ 
        ogl.glColor4f(0.6,0.6,0.6,1)
        ogl.glVertexPointer(3, ogl.GL_FLOAT, 0, self.points.T)
        ogl.glDrawArrays(ogl.GL_POINTS, 0, self.points.shape[1])

    def helpString(self):
        """ Text shown in help window. """
        output = "<h2>display-kinect</h2>"
        output += "<p>Press ENTER to start/stop live display of Kinect Data.</p>"
        return output
    
if __name__ == '__main__':
    app = QtGui.QApplication([])
    win = Viewer()
    win.show()
    app.exec_()
    
