from libs.engine import Engine

from libs.mesh import Quad

if __name__ == "__main__":
    game = Engine()
    
    quad = Quad(game)
    
    game.run()