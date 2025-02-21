import random
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from src.utitlity.utility import load_texture

class AsteroidBelt:
    def __init__(self, num_asteroids=500):
        self.asteroids = []
        for _ in range(num_asteroids):
            distance = random.uniform(14.5, 15.5)  # AU distance from the Sun
            angle = random.uniform(0, 360)  # Random orbit angle
            height = random.uniform(-0.2, 0.2)  # Small vertical offset
            size = random.uniform(0.02, 0.08)  # Small asteroid sizes
            self.asteroid_texture=load_texture("assets/textures/asteroid2.jpg")  if "assets/textures/asteroid2.jpg" else None
            # Convert polar coordinates to Cartesian (x, y, z)
            x = distance * np.cos(np.radians(angle))
            z = distance * np.sin(np.radians(angle))
            y = height
            
            self.asteroids.append({"x": x, "y": y, "z": z, "size": size, "angle": angle})

    def render(self):
        glColor3f(0.32, 0.16, 0.16)  # reddish brown
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.asteroid_texture)
        for asteroid in self.asteroids:
            glPushMatrix()
            glTranslatef(asteroid["x"], asteroid["y"], asteroid["z"])
            glutSolidSphere(asteroid["size"], 8, 8)  # Small sphere for asteroid
            glPopMatrix()
        glDisable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, 0)
        
