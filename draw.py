class Draw(object):

    def draw_head(self):
        arq = open('/home/wilton/decorator.py', 'r')
        conteudo = arq.readlines()
        texto = """import turtle
wn = turtle.Screen()
pen = turtle.Turtle()

"""
        arq = open('/home/wilton/decorator.py', 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_end(self):
        arq = open('/home/wilton/decorator.py', 'r')
        conteudo = arq.readlines()
        texto = """wn.exitonclick()

"""
        arq = open('/home/wilton/decorator.py', 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_janela_simples(self):
        arq = open('/home/wilton/decorator.py', 'r')
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
        arq = open('/home/wilton/decorator.py', 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()

    def draw_borda(self):
        arq = open('/home/wilton/decorator.py', 'r')
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

"""
        arq = open('/home/wilton/decorator.py', 'w')
        conteudo.append(texto)
        arq.writelines(conteudo)
        arq.close()