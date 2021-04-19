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
            if op[len(op)-1] in ['+', '-', '*', '/','+\n','-\n','*\n', '/\n']and len(op)>3: 
                return Nodo(comprobar(op[0:len(op)-3]),comprobar(op),valor);
            else:
                return Nodo(comprobar(op[0:len(op)-1]),comprobar(op),valor);
        else:
            return Nodo(op[len(op)-1]);


pila = [];

handler = open('operaciones.txt')
for linea in handler:
    pila.append(linea);

while pila != []:
    izquierda=0;
    derecha=0;
    operacion=pila.pop();
    operadores=operacion.split(' ');
    expresion=comprobar(operadores);
    aux=expresion;
    while aux.izquierda != None:
        aux=aux.izquierda;
        izquierda=izquierda+1;
    aux=expresion;
    while aux.derecha != None:
        aux=aux.derecha;
        derecha=derecha+1;
    if izquierda==derecha:
        print(en_orden(expresion)+'='+str(evaluar(expresion)))
    if izquierda>derecha:
        print(en_orden(expresion)+')='+str(evaluar(expresion)))
    if izquierda<derecha:
        print('('+en_orden(expresion)+'='+str(evaluar(expresion)))
