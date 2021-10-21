from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 
import math as m

w,h= 750,750

def background():
    glColor3f(0.7, 0.9, 0.8)
    glBegin(GL_QUADS)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glVertex2f(-1, -1)
    glVertex2f(1,-1 )
    glEnd()

def serverBooth():

    glColor3f(0,0,0.5) 
    glBegin(GL_QUADS)
    glVertex2f(-0.9, 0.1)
    glVertex2f(-0.95, 0)
    glVertex2f(-0.95, -0.2)
    glVertex2f(-0.9, -0.1)
    glEnd()

    glColor3f(0,0,0.9) 
    glBegin(GL_QUADS)
    glVertex2f(-0.9, 0.1)
    glVertex2f(-0.9, -0.1)
    glVertex2f(-0.7, -0.1)
    glVertex2f(-0.7, 0.1)
    glEnd()

    glColor3f(0,0,1) 
    glBegin(GL_QUADS)
    glVertex2f(-0.95, 0)
    glVertex2f(-0.95, -0.2)
    glVertex2f(-0.75, -0.2)
    glVertex2f(-0.75, 0)
    glEnd()

    glColor3f(0,0,0.5) 
    glBegin(GL_QUADS)
    glVertex2f(-0.7, -0.1)
    glVertex2f(-0.75, -0.2)
    glVertex2f(-0.75, 0 )
    glVertex2f(-0.7, 0.1)
    glEnd()

    glColor3f(0,0,0) 
    glBegin(GL_LINES)
    glVertex2f(-0.95, 0)
    glVertex2f(-0.9, 0.1)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-0.7, -0.1)
    glVertex2f(-0.75, -0.2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-0.7, 0.1)
    glVertex2f(-0.75, 0 )
    glEnd()

def queueLine():
    
    glLineWidth(2)
    glColor3f(0,0,0) 
    glBegin(GL_LINES)
    glVertex2f(-0.25, 0.25)
    glVertex2f(0.9, 0.25)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.25, -0.25)
    glVertex2f(0.9, -0.25)
    glEnd()

    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(-0.25, -0.25)
    glVertex2f(-0.25, 0.25)
    glEnd()

def customer():
    triangleAmount = 200
    twoPi = m.pi * 2
    x = -0.45
    y = 0
    radius = 0.15
    glColor3f(0,0.8,0) 
    for i in range(4):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for i in range(triangleAmount+1):
            glVertex2f( x + (radius * m.cos(i * twoPi / triangleAmount)) , y + (radius * m.sin(i * twoPi / triangleAmount)) )
        glEnd()
        x = x + 0.4
        glColor3f(0.8,0,0) 

def info():
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glVertex2f(-1, 0.5)
    glVertex2f(1,0.5)
    glEnd()
    glColor3f(0,0,0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glVertex2f(-1, 0.5)
    glVertex2f(1,0.5)
    glEnd()

    glRasterPos2f(-0.2, 0.9)
    for c in "Information":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(-0.2, 0.89)
    glVertex2f(0.12, 0.89)
    glEnd()

    glColor3f( 0, 0, 0 )
    glRasterPos2f(-0.8, 0.8)
    for c in "Server":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
    glColor3f(0,0,0.9) 
    glBegin(GL_QUADS)
    glVertex2f(-0.81, 0.75)
    glVertex2f(-0.61, 0.75)
    glVertex2f(-0.61, 0.55)
    glVertex2f(-0.81, 0.55)
    glEnd()

    glColor3f( 0, 0, 0 )
    glRasterPos2f(-0.3, 0.8)
    for c in "Customer in service":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
    triangleAmount = 200
    twoPi = m.pi * 2
    x = -0.05
    y = 0.65
    radius = 0.1
    glColor3f(0,0.8,0) 
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(triangleAmount+1):
        glVertex2f( x + (radius * m.cos(i * twoPi / triangleAmount)) , y + (radius * m.sin(i * twoPi / triangleAmount)) )
    glEnd()
    x = x + 0.4

    glColor3f( 0, 0, 0 )
    glRasterPos2f(0.4, 0.8)
    for c in "Customer in queue":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
    x = 0.65
    y = 0.65
    radius = 0.1
    glColor3f(0.8,0,0) 
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(triangleAmount+1):
        glVertex2f( x + (radius * m.cos(i * twoPi / triangleAmount)) , y + (radius * m.sin(i * twoPi / triangleAmount)) )
    glEnd()
    x = x + 0.4

def show2d():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    background()
    info()
    serverBooth()
    queueLine()
    customer()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(500,50)
wind = glutCreateWindow("Week 6 Homework")
glutDisplayFunc(show2d)
glutIdleFunc(show2d)
glutMainLoop()

