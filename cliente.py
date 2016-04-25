from decorator import *
from draw import *

if __name__ == "__main__":

    Draw().draw_head()

    janelasimples = JanelaSimples()
    janeladecorada = Borda()
    janeladecorada.set_janela(janelasimples)
    janeladecorada.draw()

    Draw().draw_end()
