import pygame as pg
import moderngl as mgl
from sys import exit

from libs.node import Node
from libs.camera import Camera

class Engine:
    def __init__(self):
        pg.init()
        
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,pg.GL_CONTEXT_PROFILE_CORE)
        
        self.window_size: (int,int) = (1280,720)
        
        self.surface: pg.Surface = pg.display.set_mode(self.window_size,pg.OPENGL | pg.DOUBLEBUF)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.delta_time: float = 1 / 60
        self.should_close: bool = False
        
        self.nodes: list[Node] = []
        
        self.ctx: mgl.Context = mgl.create_context()
        self.ctx.gc_mode = "auto"
        
        self.current_camera = Camera(self)
        
        self.shader = self.compile_shader()
    
    def add(self,node: Node):
        self.nodes.append(node)
    
    def remove(self,node: Node):
        if node in self.nodes:
            self.nodes.pop(self.nodes.index(node))
    
    def update(self):
        for node in self.nodes:
            if not isinstance(node,Node): break
            node.update()
    
    def render(self):
        for node in self.nodes:
            if not isinstance(node,Node): break
            node.render()

    def handle_event(self,event: pg.event.Event):
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            self.should_close = True
    
    def compile_shader(self,fragment: str="default",vertex: str="default") -> mgl.Program:
        with open(f"shaders/{fragment}.frag") as file:
            fragment_shader = file.read()
        
        with open(f"shaders/{vertex}.vert") as file:
            vertex_shader = file.read()
        
        return self.ctx.program(
            fragment_shader=fragment_shader,
            vertex_shader=vertex_shader
        )
    
    def run(self):
        while 1:
            if self.should_close: break
            self.delta_time = self.clock.tick(60)
            
            for event in pg.event.get():
                self.handle_event(event)
            
            self.ctx.clear(0.2, 0.3, 0.3, 1.0)
            self.update()
            self.render()
            
            pg.display.flip()
        
        pg.quit()
        exit(0)
        
        
            
            