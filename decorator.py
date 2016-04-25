from janela import *

class JanelaDecorator(Janela):
    def __init__(self):
        self.jan = Janela()

    def set_janela(self, janela):
        self.jan = janela

    def draw(self):
        self.jan.draw()

class Borda(JanelaDecorator):
    def __init__(self):
        super(Borda, self).__init__()

    def draw(self):
        super(Borda, self).draw()
        print("Janela Vertical")
        Draw().draw_borda()
