from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from libs.engine import Engine

import glm

from libs.node import Spatial

class Camera(Spatial):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        
        self.aspect_ratio = self.engine.window_size[0] / self.engine.window_size[1]
        self.fov = 90
        self.near = 0.1
        self.far = 100
        
        self.position = glm.vec3(0,0,3)
        self.rotation = glm.vec3(-90,0,0)
        
        self.forward = glm.vec3(0,0,-1)
        self.up = glm.vec3(0,1,0)
        self.right = glm.vec3(1,0,0)
    
    def update(self):
        yaw, pitch = glm.radians(self.rotation.y), glm.radians(self.rotation.x)
        
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    @property
    def perspective(self):
        return glm.perspective(glm.radians(self.fov),self.aspect_ratio,self.near,self.far)
    
    @property
    def view(self):
        return glm.lookAt(self.position,self.position + self.forward,self.up)