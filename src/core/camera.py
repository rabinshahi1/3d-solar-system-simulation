import numpy as np
import math


class Camera:
    def __init__(self):
        # Initial camera parameters
        self.position = np.array([0.0, 2.0, 30.0], dtype=np.float32)
             # Initial pitch angle (degrees)
        self.front = np.array([0.0, 0.0, -4.0], dtype=np.float32)
        self.up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        self.right = np.cross(self.front, self.up)
          
        self.speed = 0.5        # Movement speed
  
        
        

    def process_keyboard(self, key):
        # Update camera position based on keyboard input
        print(key)
        if key == b'1':  # Top view
            self.position = np.array([0.0, 25.0, 0.0], dtype=np.float32)
            self.front = np.array([0.0, -1.0, 0.0], dtype=np.float32)
            self.up = np.array([0.0, 0.0, -1.0], dtype=np.float32)

        elif key == b'2':  # Bottom view
                self.position = np.array([0.0, -25.0, 0.0], dtype=np.float32)
                self.front = np.array([0.0, 1.0, 0.0], dtype=np.float32)
                self.up = np.array([0.0, 0.0, 1.0], dtype=np.float32)

        elif key == b'3':  # Right view
            self.position = np.array([25.0, 0.0, 0.0], dtype=np.float32)
            self.front = np.array([-1.0, 0.0, 0.0], dtype=np.float32)
            self.up = np.array([0.0, 1.0, 0.0], dtype=np.float32)

        elif key == b'4':  # Left view
            self.position = np.array([-25.0, 0.0, 0.0], dtype=np.float32)
            self.front = np.array([1.0, 0.0, 0.0], dtype=np.float32)
            self.up = np.array([0.0, 1.0, 0.0], dtype=np.float32)

        elif key == b'5':  # Front view
            self.position = np.array([0.0, 0.0, 25.0], dtype=np.float32)
            self.front = np.array([0.0, 0.0, -1.0], dtype=np.float32)
            self.up = np.array([0.0, 1.0, 0.0], dtype=np.float32)

        elif key == b'6':  # Back view
            self.position = np.array([0.0, 0.0, -25.0], dtype=np.float32)
            self.front = np.array([0.0, 0.0, 1.0], dtype=np.float32)
            self.up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        elif key == b'7':
            self.position = np.array([0.0, 2.0, 30.0], dtype=np.float32)
            self.front = np.array([0.0, 0.0, -2.0], dtype=np.float32)
            self.up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        # Move the camera position based on WASD keys
        if key == b'w':
            self.position += self.speed * self.front
        elif key == b's':
            self.position -= self.speed * self.front
        elif key == b'a':
            self.position -= self.speed * self.right
        elif key == b'd':
            self.position += self.speed * self.right
        elif key == b'q':  # Up
            self.position += self.speed * self.up
        elif key == b'e':  # Down
            self.position -= self.speed * self.up
      
   

    def get_view_matrix(self):
        # Compute the target point (position + front)
        target = self.position + self.front
        # Return the camera position, target, and up vector
        return (self.position, target, self.up)
    
