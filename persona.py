from datetime import date, datetime

class Persona:
    def __init__(self, nombres, apellidos, ci, fechaNacimiento, direccion, celular, genero) -> None:
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.fechaNacimiento = fechaNacimiento
        self.direccion = direccion
        self.celular = celular
        self.genero = genero
        return
    
    def obtener_persona(self):
        print("La persona se llama: ", self.nombres, " ", self.apellidos)

    def calcular_edad(self):
        fnac=datetime.strptime(self.fechaNacimiento, "%d/%m/%Y")
        hoy = date.today()
        if(hoy.month<fnac.month):
            mes = fnac.month - hoy.month
        edad = hoy.year - int(fnac.year) - ((hoy.month, hoy.day) < (int(fnac.month), int(fnac.day)))
        print(edad)

per = Persona("Ruben", "_cito", 1234, "26/11/2020", "Siempre viva s/n", 1234567, "dudoso")
per.calcular_edad()

    #     fecha_nacimiento = datetime.strptime(self.fechaNacimiento, "%d/%m/%Y")
    #     edad = relativedelta(datetime.now(), fecha_nacimiento)
    #     print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        
    # def 

