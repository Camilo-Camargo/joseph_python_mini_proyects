import sympy as sp
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

def guardar_en_pdf(outputs, imagen, resultado):
    c = canvas.Canvas("resultado.pdf", pagesize=letter)
    c.setFont("Helvetica", 12)
    
    # Agregar las expresiones LaTeX al PDF
    y = 700
    for output in outputs:
        c.drawString(100, y, output)
        y -= 20
    
    # Agregar la imagen al PDF
    c.drawImage(imagen, 100, 200, width=400, height=300)
    
    # Agregar el resultado al PDF
    c.drawString(100, 100, resultado)
    
    c.save()

def main(var, fun, sup, inf):
    # Variable de integración
    variable = sp.Symbol(var)
    # Definición de la función
    funcion = sp.sympify(fun)
    # Tipo de funcion
    funcion_tipo = input('Es una funcion trigonometrica?: ')
    if funcion_tipo == 'si':
        # Intervalo de integración
        a = inf*sp.pi  # Límite inferior del intervalo
        b = sup*sp.pi # Límite superior del intervalo
    else :
        a = inf
        b = sup
    # Cálculo del área utilizando la función de SymPy
    area = sp.integrate(funcion, (variable, a, b))

    # Graficar la curva y el área bajo la curva
    x_vals = np.linspace(0, 10, 100)
    f = sp.lambdify(variable, funcion, modules='numpy')
    y_vals = f(x_vals)
    
    plt.plot(x_vals, y_vals, 'b', linewidth=1)
    plt.fill_between(x_vals, y_vals, where=((x_vals >= a) & (x_vals <= b)), color='black')
    plt.title('Area bajo la curva')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    
    # Guardar la gráfica como imagen
    imagen = 'grafica.png'
    plt.savefig(imagen)
    
    # Generar las expresiones LaTeX renderizadas en una imagen
    outputs = []
    outputs.append(f"Expresión: {sp.latex(funcion)}")

    # Guardar el resultado como una cadena de texto
    resultado = f'El área bajo la curva es: {area}'

    # Guardar en PDF
    guardar_en_pdf(outputs, imagen, resultado)

    # Mostrar el área calculada
    print(resultado)

if __name__ == "__main__":
    var = input('Digite la variable: ')
    fun = input('Digite la función: ')
    inf = int(input('Digite el valor del límite inferior: '))
    sup = int(input('Digite el valor del límite superior: '))
    main(var, fun, sup, inf)

