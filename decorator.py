from janela import *

class JanelaDecorator(Janela):
    def __init__(self):
        self.jan = Janela()

    def set_janela(self, janela):
        self.jan = janela

    def draw(self):
        self.jan.draw()

class JanelaVertical(JanelaDecorator):
    def __init__(self):
        super(JanelaVertical, self).__init__()

    def draw(self):
        super(JanelaVertical, self).draw()
        print("Janela Vertical")
