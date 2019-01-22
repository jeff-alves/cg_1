from math import floor
from OpenGL.GL import *
from OpenGL.GLUT import *

name = 'Primeiro Programa'
LARGURA = 500
ALTURA = 500
    
def linhas():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.9, 0.9, 0.9)
    glVertex2i(130, 180)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(400, 400)
    glEnd()
    glBegin(GL_LINES)
    glVertex2i(400, 400)
    glColor3f(0.7, 0.0, 0.0)
    glVertex2i(250, 0)
    glEnd()

def triangulo():
    glBegin(GL_TRIANGLES) # Desenha um triângulo na cor corrente
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(0, 250)
    glVertex2i(250, 500)
    glVertex2i(500, 250)
    glEnd()

def losango():
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(0, 250)
    glVertex2i(250, 500)
    glVertex2i(500, 250)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(250, 0)
    glEnd()

def quadrado():
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(250, 250)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2i(250, 500)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(500, 500)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(500, 250)
    glEnd()

def limpar_e_ativar(area, cor=(0,0,0,0)):
    glScissor(*area)
    glEnable(GL_SCISSOR_TEST)
    glClearColor(*cor)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)
    glViewport(*area)

def update_screen():
    w = glutGet(GLUT_WINDOW_WIDTH)
    h = glutGet(GLUT_WINDOW_HEIGHT)
    q_w = floor(w/2)
    q_h = floor(h/2)

    limpar_e_ativar(area=(0, q_h, q_w, q_h), cor=(1.0, 0.0, 0.0, 1.0))
    triangulo()

    limpar_e_ativar(area=(q_w, q_h, q_w, q_h), cor=(1.0, 0.0, 0.0, 1.0))
    losango()

    limpar_e_ativar(area=(0, 0, q_w, q_h), cor=(0.0, 1.0, 0.0, 1.0))
    linhas()

    limpar_e_ativar(area=(q_w, 0, q_w, q_h), cor=(1.0, 1.0, 1.0, 1.0))
    quadrado()

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(LARGURA, ALTURA)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(name)
    glOrtho(0, LARGURA, 0, ALTURA, -1 ,1) # Modo de projecao ortogonal
    
    glutDisplayFunc(update_screen)
    glutMainLoop()

if __name__ == '__main__': main()