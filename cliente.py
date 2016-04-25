from decorator import *
from draw import *

if __name__ == "__main__":

    Draw().draw_clean()
    Draw().draw_head()

    c = JanelaSimples()
    d1 = Borda()
    d2 = RolagemVertical()
    d3 = RolagemHorizontal()

    d1.set_janela(c)
    d2.set_janela(d1)
    d3.set_janela(d2)

    d3.draw()

    Draw().draw_end()
