import unittest
from herencia import *

class TestTrabajadores(unittest.TestCase):

    def test_instancias(self):
        t = Trabajador(nombre="Ana", id_empleado=1, salario_base=30000)
        d = Disenador(nombre="Luis", id_empleado=2, salario_base=35000, herramienta_preferida="Figma")
        dev = Desarrollador(nombre="María", id_empleado=3, salario_base=40000, lenguaje_principal="Python")
        acc = EspecialistaDeAccesibilidad(nombre="Carlos", id_empleado=4, salario_base=37000, normativa_referencia="WCAG")
        fs = Fullstack(nombre="Laura", id_empleado=5, salario_base=45000, lenguaje_principal="JavaScript", herramienta_preferida="Sketch", anos_experiencia=3)
        ux = UXEngineer(nombre="Pepe", id_empleado=6, salario_base=42000, herramienta_preferida="Adobe XD", normativa_referencia="ADA", especialidad_ux="UX Writing", anos_experiencia=2)

        self.assertIsInstance(d, Trabajador)
        self.assertIsInstance(dev, Trabajador)
        self.assertIsInstance(acc, Trabajador)
        self.assertIsInstance(fs, Desarrollador)
        self.assertIsInstance(fs, Disenador)
        self.assertIsInstance(fs, Trabajador)
        self.assertIsInstance(ux, Disenador)
        self.assertIsInstance(ux, EspecialistaDeAccesibilidad)
        self.assertIsInstance(ux, Trabajador)

    def test_herencia(self):
        self.assertTrue(issubclass(Disenador, Trabajador))
        self.assertTrue(issubclass(Desarrollador, Trabajador))
        self.assertTrue(issubclass(EspecialistaDeAccesibilidad, Trabajador))
        self.assertTrue(issubclass(Fullstack, Desarrollador))
        self.assertTrue(issubclass(Fullstack, Disenador))
        self.assertTrue(issubclass(UXEngineer, Disenador))
        self.assertTrue(issubclass(UXEngineer, EspecialistaDeAccesibilidad))

    def test_trabajar(self):
        dev = Desarrollador(nombre="Mario", id_empleado=7, salario_base=41000, lenguaje_principal="Java")
        self.assertEqual(dev.trabajar(), "Mario está desarrollando software en Java.")

        dis = Disenador(nombre="Julia", id_empleado=8, salario_base=36000, herramienta_preferida="Figma")
        self.assertEqual(dis.trabajar(), "Julia está diseñando interfaces con Figma.")

        acc = EspecialistaDeAccesibilidad(nombre="Sonia", id_empleado=9, salario_base=38000, normativa_referencia="WCAG")
        self.assertEqual(acc.trabajar(), "Sonia está evaluando accesibilidad según la normativa WCAG.")

        fs = Fullstack(nombre="Fran", id_empleado=10, salario_base=50000, lenguaje_principal="Python", herramienta_preferida="Figma", anos_experiencia=2)
        self.assertIn("Fran (Fullstack) está:", fs.trabajar())

        ux = UXEngineer(nombre="Leo", id_empleado=11, salario_base=43000, herramienta_preferida="Sketch", normativa_referencia="ADA", especialidad_ux="Research", anos_experiencia=4)
        self.assertIn("Leo (UX Engineer) está:", ux.trabajar())

    def test_salario_anual(self):
        d = Disenador(nombre="Luis", id_empleado=2, salario_base=35000, herramienta_preferida="Figma")
        self.assertEqual(d.calcular_salario_anual(), 35000 + 5000)

        dev = Desarrollador(nombre="María", id_empleado=3, salario_base=40000, lenguaje_principal="Python")
        self.assertEqual(dev.calcular_salario_anual(), 40000 + 8000)

        acc = EspecialistaDeAccesibilidad(nombre="Carlos", id_empleado=4, salario_base=37000, normativa_referencia="WCAG")
        self.assertEqual(acc.calcular_salario_anual(), 37000 + 6000)

        fs = Fullstack(nombre="Laura", id_empleado=5, salario_base=45000, lenguaje_principal="JavaScript", herramienta_preferida="Sketch", anos_experiencia=3)
        self.assertEqual(fs.calcular_salario_anual(), 45000 + (3 * 1000) + 10000)

        ux = UXEngineer(nombre="Pepe", id_empleado=6, salario_base=42000, herramienta_preferida="Adobe XD", normativa_referencia="ADA", especialidad_ux="UX Writing", anos_experiencia=2)
        self.assertEqual(ux.calcular_salario_anual(), 42000 + (2 * 1000) + 9000)

    def test_metodos_propios(self):
        d = Disenador(nombre="Paula", id_empleado=12, salario_base=30000, herramienta_preferida="Figma")
        self.assertEqual(d.crear_prototipo(), "Paula está creando un prototipo interactivo.")

        dev = Desarrollador(nombre="Mario", id_empleado=13, salario_base=31000, lenguaje_principal="C++")
        self.assertEqual(dev.escribir_codigo(), "Mario está escribiendo código limpio y eficiente.")

        acc = EspecialistaDeAccesibilidad(nombre="Lucía", id_empleado=14, salario_base=32000, normativa_referencia="EN301549")
        self.assertEqual(acc.auditar_interfaz(), "Lucía está auditando la interfaz para garantizar accesibilidad.")

        fs = Fullstack(nombre="Fran", id_empleado=15, salario_base=47000, lenguaje_principal="Java", herramienta_preferida="Sketch", anos_experiencia=5)
        self.assertEqual(fs.gestionar_proyecto_completo(), "Fran está gestionando un proyecto de desarrollo completo.")

        ux = UXEngineer(nombre="Leo", id_empleado=16, salario_base=41000, herramienta_preferida="Adobe XD", normativa_referencia="WCAG", especialidad_ux="Visual Design", anos_experiencia=4)
        self.assertEqual(ux.realizar_pruebas_usabilidad(), "Leo está conduciendo pruebas de usabilidad.")

if __name__ == '__main__':
    unittest.main()
