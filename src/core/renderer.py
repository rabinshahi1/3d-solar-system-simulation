# src/core/renderer.py
import json
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
from src.objects.planet import Planet, update_light_position, setup_lighting,setup_lighting
import json
from src.objects.asteroid import AsteroidBelt
from src.core.camera import Camera
# from src.ui.speed import RotationPanel
# Load JSON from file
def load_planet_data(json_path):
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)  # Ensure the file is loaded properly
            return data  # Return the loaded dictionary
    except FileNotFoundError:
        print(f"Error: File '{json_path}' not found!")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON! {e}")
        return None
def key_callback(key, x, y):
    camera.process_keyboard(key)
    glut.glutPostRedisplay()
camera=Camera()
# rotation=RotationPanel()

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.asteroid_belt = AsteroidBelt(500)
        self.all_data=load_planet_data("assets/info/relative_data.json")
        self.planets = []  # List of Planet objects
        self.init_solar_system()
        setup_lighting()

    def init_solar_system(self):
      
        for planet in self.all_data:
            data=self.all_data[planet]
            value=data.values()
            
            self.planets.append(Planet(*value))
      
            
       

    def render(self,o_speed,r_speed):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        # Set up the camera
        
        pos, target, up = camera.get_view_matrix()
        glu.gluLookAt(pos[0], pos[1], pos[2],
                  target[0], target[1], target[2],
                  up[0], up[1], up[2])
        update_light_position()
        # speed=rotation.slider_callback()
        # Update and draw each planet
        for planet in self.planets:
            planet.update(o_speed,r_speed)
            planet.draw()
        self.asteroid_belt.render()
        gl.glFlush()
