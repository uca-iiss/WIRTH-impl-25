# Clase base
class Trabajador:
    def __init__(self, nombre, id_empleado, salario_base, **kwargs):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_empleado}"

    def trabajar(self):
        return f"{self.nombre} está realizando tareas generales."

    def calcular_salario_anual(self):
        return self.salario_base

# Herencia Simple

class Disenador(Trabajador):
    def __init__(self, herramienta_preferida, **kwargs):
        super().__init__(**kwargs)
        self.herramienta_preferida = herramienta_preferida
        self.bonus_disenador = 5000

    def trabajar(self):
        return f"{self.nombre} está diseñando interfaces con {self.herramienta_preferida}."

    def crear_prototipo(self):
        return f"{self.nombre} está creando un prototipo interactivo."

    def calcular_salario_anual(self):
        return self.salario_base + self.bonus_disenador

class Desarrollador(Trabajador):
    def __init__(self, lenguaje_principal, **kwargs):
        super().__init__(**kwargs)
        self.lenguaje_principal = lenguaje_principal
        self.bonus_desarrollador = 8000

    def trabajar(self):
        return f"{self.nombre} está desarrollando software en {self.lenguaje_principal}."

    def escribir_codigo(self):
        return f"{self.nombre} está escribiendo código limpio y eficiente."

    def calcular_salario_anual(self):
        return self.salario_base + self.bonus_desarrollador

class EspecialistaDeAccesibilidad(Trabajador):
    def __init__(self, normativa_referencia, **kwargs):
        super().__init__(**kwargs)
        self.normativa_referencia = normativa_referencia
        self.bonus_accesibilidad = 6000

    def trabajar(self):
        return f"{self.nombre} está evaluando accesibilidad según la normativa {self.normativa_referencia}."

    def auditar_interfaz(self):
        return f"{self.nombre} está auditando la interfaz para garantizar accesibilidad."

    def calcular_salario_anual(self):
        return self.salario_base + self.bonus_accesibilidad

# Herencia Múltiple

class Fullstack(Desarrollador, Disenador):
    def __init__(self, anos_experiencia, **kwargs):
        super().__init__(**kwargs)
        self.anos_experiencia = anos_experiencia
        self.bonus_fullstack = 10000

    def trabajar(self):
        trabajo_dev = Desarrollador.trabajar(self)
        trabajo_dis = Disenador.trabajar(self)
        return f"{self.nombre} (Fullstack) está:\n  - {trabajo_dev}\n  - {trabajo_dis}\n  - Integrando frontend y backend."

    def gestionar_proyecto_completo(self):
        return f"{self.nombre} está gestionando un proyecto de desarrollo completo."

    def calcular_salario_anual(self):
        return self.salario_base + (self.anos_experiencia * 1000) + self.bonus_fullstack

class UXEngineer(Disenador, EspecialistaDeAccesibilidad):
    def __init__(self, especialidad_ux, anos_experiencia, **kwargs):
        super().__init__(**kwargs)
        self.especialidad_ux = especialidad_ux
        self.anos_experiencia = anos_experiencia
        self.bonus_ux = 9000

    def trabajar(self):
        trabajo_dis = Disenador.trabajar(self)
        trabajo_acc = EspecialistaDeAccesibilidad.trabajar(self)
        return f"{self.nombre} (UX Engineer) está:\n  - {trabajo_dis}\n  - {trabajo_acc}\n  - Diseñando experiencias centradas en el usuario ({self.especialidad_ux})."

    def realizar_pruebas_usabilidad(self):
        return f"{self.nombre} está conduciendo pruebas de usabilidad."

    def calcular_salario_anual(self):
        return self.salario_base + (self.anos_experiencia * 1000) + self.bonus_ux