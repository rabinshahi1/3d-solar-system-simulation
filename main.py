# src/main.py
from src.core.window import init_window
from src.core.renderer import Renderer,key_callback
import OpenGL.GLUT as glut
import OpenGL.GL as gl
import OpenGL.GLU as glu
from src.ui.ui import UIPanel
from src.utitlity.utility import load_planet_data
import dearpygui.dearpygui as dpg
from src.ui.speed import RotationPanel


planet_info=load_planet_data("assets/info/data.json")
WIDTH, HEIGHT = 1200, 800
renderer = None  # Will be initialized in main()
# ui = UIPanel(planet_info)
rotation=RotationPanel()
def display():
    global renderer
    ospeed=rotation.get_ospeed()
    rspeed=rotation.get_rspeed()
    # print(speed)
    renderer.render(ospeed,rspeed)
    # ui.render()
    rotation.render()
    
    
    glut.glutSwapBuffers()

def reshape(w, h):
    gl.glViewport(0, 0, w, h)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45.0, float(w) / float(h), 0.1, 100.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

def timer(value):
    glut.glutPostRedisplay()
    
    glut.glutTimerFunc(16, timer, 0)  # Approximately 60 FPS

def main():
    global renderer
    
    init_window(WIDTH, HEIGHT, b"Solar System Simulation")
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    renderer = Renderer(WIDTH, HEIGHT)

    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutTimerFunc(16, timer, 0)
    glut.glutKeyboardFunc(key_callback)
    glut.glutMainLoop()
   

if __name__ == "__main__":
    main()
