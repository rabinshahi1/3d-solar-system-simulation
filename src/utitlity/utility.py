import json
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import numpy as np
import OpenGL.GLU as glu
from PIL import Image
import sys
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
def load_texture(texture_path):
    """Load a texture image and return the OpenGL texture ID."""
    try:
        image = Image.open(texture_path)
    except IOError:
        print(f"Error: Unable to load texture '{texture_path}'")
        sys.exit(1)
    
    # Flip the image vertically so that it maps correctly to the sphere
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = np.array(image.convert("RGB"), np.uint8)
    
    tex_id = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, tex_id)
    
    # Set texture parameters
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, image.width, image.height, 0,
                    gl.GL_RGB, gl.GL_UNSIGNED_BYTE, img_data)
    
    gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    return tex_id
