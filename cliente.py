from decorator import *

if __name__ == "__main__":

    janelasimples = JanelaSimples()
    janeladecorada = JanelaVertical()
    janeladecorada.set_janela(janelasimples)
    janeladecorada.draw()
