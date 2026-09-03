class figura:
    def __init__(self, largo):
        self.largo = largo

class cuadrado(figura):
    def areacuadrado(self):
        area = self.largo * self.largo
        return area
    def perimetrocuadrado(self):
        perimetro = self.largo * 4
        return perimetro

class circulo(figura):
    def areacirculo(self):
        area = 3.1416 * (self.largo ** 2)
        return area
    def perimetrocirculo(self):
        perimetro = 2 * 3.1416 * self.largo
        return perimetro

circulo1 = circulo(15)
print("El area del circulo es: ", circulo1.areacirculo())
print("El perimetro del circulo es: ", circulo1.perimetrocirculo())
cuadrado = cuadrado(10)
print("El area del cuadrado es: ", cuadrado.areacuadrado())
print("El perimetro del cuadrado es: ", cuadrado.perimetrocuadrado())

