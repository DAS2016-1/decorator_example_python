import os

class Draw(object):
    homedir = os.path.expanduser('~')

    def draw_clean(self):
        path = self.homedir + '/decorator.py'
        arq = open(path, 'w')
        arq.close()

    def draw_head(self):
        path = self.homedir + '/decorator.py'
        arq = open(path, 'r')
        conteudo = arq.readlines()
        texto = """import turtle
wn = turtle.Screen()
pen = turtle.Turtle()

"""
        arq = open(path, 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_end(self):
        path = self.homedir + '/decorator.py'
        arq = open(path, 'r')
        conteudo = arq.readlines()
        texto = """wn.exitonclick()

"""
        arq = open(path, 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_janela_simples(self):
        path = self.homedir + '/decorator.py'
        arq = open(path, 'r')
        conteudo = arq.readlines()
        texto = """pen.forward(250)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(200)
pen.right(90)

"""
        arq = open(path, 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_borda(self):
        path = self.homedir + '/decorator.py'
        arq = open(path, 'r')
        conteudo = arq.readlines()
        texto = """pen.pensize(3)
pen.forward(250)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.pensize(1)

"""
        arq = open(path, 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_rolagem_vertical(self):
        path = self.homedir + '/decorator.py'
        arq = open(path, 'r')
        conteudo = arq.readlines()
        texto = """pen.forward(240)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(240)
pen.right(90)
pen.forward(200)
pen.right(90)

"""
        arq = open(path, 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_rolagem_horizontal(self):
        path = self.homedir + '/decorator.py'
        arq = open(path, 'r')
        conteudo = arq.readlines()
        texto = """pen.forward(240)
pen.right(90)
pen.forward(190)
pen.right(90)
pen.forward(240)
pen.right(90)
pen.forward(190)
pen.right(90)

"""
        arq = open(path, 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()
