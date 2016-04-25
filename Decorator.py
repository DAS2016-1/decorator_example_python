class Janela():
    def draw():
        pass

class JanelaSimples(Janela):
    def draw(self):
        print("Desenhando uma janela")

class JanelaDecorator(Janela):
    janelaDecorada = Janela

    def __init__(self):
        janelaDecorada = Janela

class JanelaVertical(JanelaDecorator):
    def __init__(self, janeladecorada):
        super(JanelaVertical, self).__init__()

    def drawVertical(print):
        print("Janela Vertical")

    def fazer():
        print ("afsdfasd")

    def draw(self):
        # drawVertical()
        fazer()
        janelaDecorada.draw()


