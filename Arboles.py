class Nodo:
    def __init__(self, izquierda, derecha=None, valor=None):
        if valor != None:
            self.valor = valor
            self.izquierda = izquierda
            self.derecha = derecha
        else:
            self.valor = izquierda
            self.izquierda = valor
            self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return ''
    elif arbol.valor in ['+', '-', '*', '/']:
        return "(" + en_orden(arbol.izquierda) + str(arbol.valor) + en_orden(arbol.derecha) + ")"
    else:
        return str(arbol.valor)



def evaluar(arbol):
    if arbol == None:
        pass
    else:
        if arbol.valor == '+':
            return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
        if arbol.valor == '-':
            return evaluar(arbol.izquierda) - evaluar(arbol.derecha)
        if arbol.valor == '*':
            return evaluar(arbol.izquierda) * evaluar(arbol.derecha)
        if arbol.valor == '/':
            return evaluar(arbol.izquierda) // evaluar(arbol.derecha)
        return int(arbol.valor)


def comprobar (op):
        if op[len(op)-1] in ['+', '-', '*', '/','+\n','-\n','*\n', '/\n']:
            valor=op.pop();
            if valor[1:]=='\n':
                valor=valor[0];
            return Nodo(comprobar(op[0:len(op)-1]),comprobar(op),valor);
        else:
            return Nodo(op[len(op)-1]);


pila = [];

handler = open('operaciones.txt')
for linea in handler:
    pila.append(linea);

while pila != []:
    operacion=pila.pop();
    operadores=operacion.split(' ');
    expresion=comprobar(operadores);
    print(en_orden(expresion)+'='+str(evaluar(expresion)))


