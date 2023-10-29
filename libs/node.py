from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from libs.engine import Engine

import glm

class Node:
    def __init__(self,engine: Engine):
        engine.add(self)
        self.engine: Engine = engine
    def update(self): ...
    def render(self): ...
    def destroy(self):
        self.engine.remove(self)

class Spatial(Node):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.position: glm.vec3 = glm.vec3()
        self.rotation: glm.vec3 = glm.vec3()
        self.scale: glm.vec3 = glm.vec3(1,1,1)