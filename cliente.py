from Decorator import Janela, JanelaSimples, JanelaVertical, JanelaDecorator

if __name__ == "__main__":
    janelasimples = JanelaSimples()

    janelasimples.draw()

    janeladecorada = JanelaVertical(janelasimples)
    janeladecorada.draw()
