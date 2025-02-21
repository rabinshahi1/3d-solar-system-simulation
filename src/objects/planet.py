# src/objects/planet.py
import OpenGL.GL as gl
import OpenGL.GLU as glu
from src.utitlity.utility import load_texture
# Global variable for any light animation if needed
light_angle = 0.0

def update_light_position():
  
    light_pos = [0.0, 0.0, 0.0, 1.0]  # Light at the Sun's center
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, light_pos)

def setup_lighting():
    """
    Enable OpenGL fixed-function lighting and set light properties.
    Call this once during initialization.
    """
    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glEnable(gl.GL_DEPTH_TEST)

    # Set light properties.
    # Position the light at the Sun (0, 0, 0)
    light_pos = [0.0, 0.0, 0.0, 1.0]
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, light_pos)
    
    # For a pronounced day/night effect, use low ambient light and strong diffuse
    ambient_light  = [0.05, 0.05, 0.05, 1.0]   # Very low ambient light
    diffuse_light  = [1.0, 1.0, 1.0, 1.0]       # Bright diffuse light
    specular_light = [1.0, 1.0, 1.0, 1.0]
    
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, ambient_light)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, diffuse_light)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, specular_light)


class Planet:
    def __init__(self, name, distance, rotation_speed, radius,orbit_speed, texture_path):
  
        self.name = name
        self.radius = radius
        self.distance = distance
        self.rotation_speed = rotation_speed
        self.orbit_speed = orbit_speed
        
        self.texture_id = load_texture(texture_path) if texture_path else None

        self.self_rotation = 0.0  # Planet's own rotation angle
        self.orbit_rotation = 0.0  # Orbital rotation angle around the Sun

        # Create a quadric object for drawing a smooth sphere
        self.quadric = glu.gluNewQuadric()
        glu.gluQuadricTexture(self.quadric, gl.GL_TRUE)
        glu.gluQuadricNormals(self.quadric, glu.GLU_SMOOTH)

    def update(self,o_speed,r_speed):
        
            
        self.self_rotation = (self.self_rotation + self.rotation_speed+r_speed) %360
        self.orbit_rotation = (self.orbit_rotation + self.orbit_speed+o_speed) %360
        if r_speed==0.0:
          self.self_rotation=0.0
        if o_speed==0.0:
          self.orbit_rotation=0.0
    def draw(self):
        #
        """Draw the planet with its texture."""
        gl.glPushMatrix()

        # For non-Sun bodies, apply orbital rotation and translation
        
        if self.distance > 0: 
            gl.glRotatef(self.orbit_rotation, 0, 1, 0)
            gl.glTranslatef(self.distance, 0, 0)

        # Rotate the sphere so that the texture aligns correctly.
        # Rotating -90° around X moves the poles to the proper positions.
            

            # Apply the planet's own rotation about its Z-axis
           
        gl.glRotatef(-90, 1, 0, 0)
        if self.distance > 0:
             gl.glRotatef(self.self_rotation, 0, 0, 1)
        if self.distance == 0:
        # For the Sun, set a high emissive value.
         gl.glMaterialfv(gl.GL_FRONT, gl.GL_EMISSION, [1.0, 1.0, 0.5, 1.0])
        else:
        # For other planets, reset emission to zero and set regular material properties.
            gl.glMaterialfv(gl.GL_FRONT, gl.GL_EMISSION, [0.0, 0.0, 0.0, 1.0])
            gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
            gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
            gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
            gl.glMaterialf(gl.GL_FRONT, gl.GL_SHININESS, 50.0)

        # Enable and bind texture if available
        if self.texture_id:
            gl.glEnable(gl.GL_TEXTURE_2D)
            gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)

        # Draw the sphere with the quadric
        glu.gluSphere(self.quadric, self.radius, 36, 18)

        if self.texture_id:
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
            gl.glDisable(gl.GL_TEXTURE_2D)
        if self.name=="Saturn":
            self.draw_ring()

        gl.glPopMatrix()
    def draw_ring(self):
     
        gl.glPushMatrix()
        gl.glRotatef(27, 1, 0, 0)  # Align with Saturn's equator

        gl.glColor3f(0.3, 0.4, 0.5)  # Light brownish color (like Saturn's rings)
        
        quad = glu.gluNewQuadric()
        glu.gluQuadricDrawStyle(quad, glu.GLU_FILL)

        # Draw a ring using a disk with an inner radius
        glu.gluDisk(quad, self.radius * 1.2, self.radius * 1.5, 100, 20)

        gl.glPopMatrix()

