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

class RolagemVertical(JanelaDecorator):
    def __init__(self):
        super(RolagemVertical, self).__init__()

    def draw(self):
        super(RolagemVertical, self).draw()
        print("Rolagem Vertical")
        Draw().draw_rolagem_vertical()

class RolagemHorizontal(JanelaDecorator):
    def __init__(self):
        super(RolagemHorizontal, self).__init__()

    def draw(self):
        super(RolagemHorizontal, self).draw()
        print("Rolagem Horizontal")
        Draw().draw_rolagem_horizontal()
