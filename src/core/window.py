# src/core/window.py
import OpenGL.GLUT as glut

def init_window(width, height, title):
    """
    Initialize the GLUT window.
    Returns the window handle.
    """
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(width, height)
    window = glut.glutCreateWindow(title)
    return window
