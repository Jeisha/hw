from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 
import math as m

w,h= 750,750

def square():
    for i in range(3):
        glBegin(GL_QUADS)
        glVertex2f(5,5)
        glVertex2f(250,5)
        glVertex2f(250,250)
        glVertex2f(5,250)
        glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    square()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(500,50)
wind = glutCreateWindow("Week 7 Homework")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

