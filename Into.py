class animal: 
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def pasear(self): 
        pass

    def alimentar(self):
        pass

    def dar_info(self):
        return self.nombre + " de raza: " + self.raza

class Mascota(animal):
    def __init__(self, nombre, raza, propietario):
        self.propietario = propietario
        super (Mascota, self).__init__(nombre,raza)
       
class Gato(Mascota):
    def pasear(self):
        print("paseando al gato" + self.dar_info() + " " + self.propietario)
    
    def alimentar(self): 
        print("alimentando al gato" + self.dar_info())

class Perro(Mascota):
    def pasear(self):
        print("Paseando al perro" + self.dar_info())

    def alimentar(self):
        print("Alimentando al perro" + self.dar_info())

class Lagartos(Mascota):
    def pasear(self):
        print("Paseando al lagarto" + self.dar_info())

    def alimentar(self):
        print("Alimentando al lagarto" + self.dar_info())

if __name__ == "__main__":
    mascotas = [Perro("Marcos", "Bulldog", "Juan"), Gato("Figara", "Angora", "Maria"), Lagartos("pedro", "sakura", "sebastian")]  
    for m in mascotas:
        m.pasear()
        m.alimentar()