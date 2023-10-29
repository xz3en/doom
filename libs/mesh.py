from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from libs.engine import Engine

import glm

from libs.node import Spatial

class Mesh(Spatial):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        
        self.vbo = self.engine.ctx.buffer(self.vertices.to_bytes())
        self.ebo = self.engine.ctx.buffer(self.indices.to_bytes())
        
        self.vao = self.engine.ctx.vertex_array(
            self.engine.shader,
            [
                (self.vbo,"3f","vertex")
            ],
            index_buffer=self.ebo
        )
    
    def render(self):
        self.engine.shader["perspective"].write(self.engine.current_camera.perspective)
        self.engine.shader["view"].write(self.engine.current_camera.view)
        self.vao.render()
        
    @property
    def vertices(self):
        return glm.array(glm.vec3())
    
    @property
    def indices(self):
        return glm.array(glm.uint32,0)

class Quad(Mesh):
    def __init__(self, engine: Engine):
        super().__init__(engine)
    
    @property
    def vertices(self):
        return glm.array(
            glm.vec3(1,1,0),
            glm.vec3(1,-1,0),
            glm.vec3(-1,-1,0),
            glm.vec3(-1,1,0)
        )
    
    @property
    def indices(self):
        return glm.array(
            glm.uint32,
            0,1,3,
            1,2,3
        )
    