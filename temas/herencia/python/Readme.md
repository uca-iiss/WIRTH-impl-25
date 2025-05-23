# Herencia en Python

## Introducción
Bienvenido a este repositorio donde explicaremos y mostraremos los conceptos de Herencia y Polimorfismo en Python, mediante un ejemplo sencillo con un codigo limpio y accesible para cualquiera

## Estructura de Directorio
- `/README.md`: Archivo actual, donde explicaremos los conceptos y mostraremos los pasos a seguir para comprobar el funcionamiento del     ejemplo
- `/herencia.py`: Archivo python donde se encuentra el codigo de ejemplo.
- `/test.py`: Archivo python donde se encuentra el codigo de los test
- `/Jenkinsfile`: configuración de pipeline para la comprobación del funcionamiento del código


## Conceptos Previos
Antes de comenzar con el codigo donde se muestra los conceptos de herencia y polimorfismo, vamos a explicar algunos conceptos claves necesarios para entender el funcionamiento de la herencia y el polimorfismo en Python.

- **Herencia Básica**:
  La herencia (o herencia básica) permite que una clase (subclase) herede atributos y métodos de otra clase (superclase). En el ejemplo, las clases `Diseñador`, `Desarrollador` y `EspecialistaDeAccesibilidad` actúan como subclases de la superclase `Trabajador` la cual proporciona atributos como `nombre` o `id del empleado`y métodos básicos como `trabajar` o `calcular salario anual`, que son heredados por las otras clases.

- **Herencia Múltiple**:
  Python permite que una clase herede de múltiples clases, proporcionando una forma de combinar funcionalidades de múltiples superclases. Esto puede resultar en una situación compleja cuando diferentes clases base tienen métodos con el mismo nombre. Python utiliza el método de resolución de orden de método (MRO) para determinar el orden en el que se buscan los métodos. Este orden está definido por el algoritmo C3 linearization. En el código, la clase `FullStack` hereda tanto de la clase `Desarrollador` como de `Diseñador`, combinando sus atributos y métodos. 

- **Uso de kwargs con super().__init__()**:
    Vamos a explicar primeramente el concepto de kwargs. **kwargs sirve para aceptar una cantidad varible de argumentos nombrados en un función o método, es decir, kwargs actua como un diccionario que recoge todos los argumentos que se pasen con nombre y que no estén explícitamente definidos en los parámetros. 
    Hemos usado **kwargs porque cuando trabajamos con herencia (sobretodo la herencia multiple), **kwargs nos da una flexibilidad para pasar los argumentos entre las distintas clases evitando errores por el paso masivo de parámetros entre las distintas capas de herencia.
    Una vez explicado esto, porque lo usamos con super().__init__(*kwargs)? Bueno el uso de super() hace que se llame al constructor de la clase padre directamente, cosa que es muy importante porque se debe de seguir el MRO como hemos explicado previamente. Entonces al usar **kwargs, no necesitamos preocuparnos por cuáles parámetros son de qué clase, esto nos proporciona una mayor flexibilidad y un código mucho más limpio

- **Polimorfismo**:
  El polimorfismo permite que métodos con el mismo nombre actúen de manera diferente en diferentes clases. Por ejemplo, el método `trabajar` se define tanto en `Trabajador` como en `Diseñador`, `Desarrollador` y `EspecialistaDeAccesibilidad`, pero su implementación puede ser diferente en cada clase.

- **Composición de Clases**:
  Además de la herencia, las clases `Diseñador`, `Desarollador` y `EspecialistaDeAccesibilidad` demuestran cómo la composición puede ser utilizada para agregar diferentes capacidades a las clases. Estas clases introducen nuevos métodos como `crear_prototipo`,  `escribir_codigo` y `auditar_interfaz` que son específicos para sus respectivas funcionalidades.

- **Inicialización de Superclases en Herencia Múltiple**:
  En herencia múltiple, es importante inicializar correctamente todas las superclases para asegurarse de que todos los atributos de la clase base se configuren adecuadamente. En la clase `FullStack`, por ejemplo, se llama explícitamente a los inicializadores de `Desarrollador` y `Diseñador` para asegurar una inicialización completa.

Tras esta breve explicación de ciertos conceptos claves del funcionamiento de la herencia y del polimorfismo, mostraremos a continuación el codigo que se ha usado como ejemplo

## Código de Ejemplo
A continuación, se muestra un ejemplo de cómo se pueden utilizar la herencia en Python:
[**herencia.py**](./herencia.py)

```python
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
```

Ahora vamos a explicar los métodos que se han usado en el ejemplo:

### Clase `Trabajador`:

- `__init__(self, nombre, id_empleado, salario_base, **kwargs)`: Constructor que inicializa los atributos comunes a todos los trabajadores: nombre, ID y salario base.

- `__str__(self)`: Método que devuelve una representación legible del objeto trabajador, incluyendo el nombre y el ID.

- `trabajar(self)`: Método que representa una acción genérica de trabajo. Este método muestra cómo se puede proporcionar un comportamiento básico en una superclase que otras clases pueden heredar o sobrescribir.

- `calcular_salario_anual(self)`: Método que devuelve el salario base anual del trabajador. Este método se sobrescribirá en las diferentes subclases. 

### Clase `Diseñador`:
- `__init__(self, herramienta_preferida, **kwargs)`: Constructor que inicializa al diseñador con su herramienta preferida, además de los atributos comunes heredados de Trabajador.

- `trabajar(self)`: Sobrescribe el método de Trabajador, indicando que el diseñador está trabajando con una herramienta de diseño específica.

- `crear_prototipo(self)`: Método propio de la clase Diseñador que simula la creación de un prototipo interactivo.

- `calcular_salario_anual(self)`: Sobrescribe el cálculo de salario para incluir un bonus de diseñador.

### Clase `Desarrollador`:
- `__init__(self, lenguaje_principal, **kwargs)`: Constructor que inicializa al desarrollador con su lenguaje de programación principal y los atributos comunes heredados de Trabajador

- `trabajar(self)`: Sobrescribe el método de Trabajador para reflejar que el desarrollador está escribiendo código.

- `escribir_codigo(self)`: Método propio que indica que el desarrollador está escribiendo código eficiente.

- `calcular_salario_anual(self)`: Sobrescribe el cálculo de salario para añadir un bonus de desarrollador.

#### Clase `EspecialistaDeAccesibilidad`:
- `__init__(self, normativa_referencia, **kwargs)`: Constructor que inicializa al especialista con la normativa de accesibilidad que utiliza, además de los atributos comunes hereados de la clase Trabajador

- `trabajar(self)`: Sobrescribe el método de Trabajador para indicar que el especialista está evaluando la accesibilidad.

- `auditar_interfaz(self)`: Método propio que simula una auditoría de accesibilidad.

- `calcular_salario_anual(self)`: Sobrescribe el cálculo de salario para añadir un bonus específico de accesibilidad.

### Clase `Fullstack`: 
- `__init__(self, anos_experiencia, **kwargs)`: Constructor que inicializa el número de años de experiencia y llama al constructor de sus clases padre usando super().

`trabajar(self)`: Sobrescribe el método trabajar combinando las acciones de diseñador y desarrollador, además de agregar una capa de integración.

- `gestionar_proyecto_completo(self)`: Método propio que indica que el fullstack puede encargarse de todo el proyecto.

- `calcular_salario_anual(self)`: Sobrescribe el cálculo de salario para incluir la experiencia y un bonus adicional por ser fullstack.

### Clase `UXEngineer`: 
- `__init__(self, especialidad_ux, anos_experiencia, **kwargs)`: Constructor que inicializa la especialidad UX y la experiencia, además de llamar al constructor de sus clases padre usando super().

- `trabajar(self)`: Sobrescribe el método trabajar combinando las acciones del diseñador y del especialista en accesibilidad, enfocándose en la experiencia de usuario.

- `realizar_pruebas_usabilidad(self)`: Método propio que representa la realización de pruebas de usabilidad.

- `calcular_salario_anual(self)`: Sobrescribe el cálculo de salario para incluir años de experiencia y un bonus específico por su rol.


A continuacion mostraremos como hemos comprobado el funcionamiento del código

## Código de test
[**test.py**](./test.py)

```python

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

```

### `test_instancias`: 
Esta prueba se asegura de que las instancias creadas de diferentes clases (Disenador, Desarrollador, Fullstack, etc.) pertenezcan a las clases correctas y a sus superclases:

- Usa `assertIsInstance(obj, Clase)` para verificar que el objeto pertenece a una clase dada o a alguna clase base de ella.

- Verifica, por ejemplo, que un `Fullstack` sea también un `Desarrollador`, `Disenador` y `Trabajador`, lo cual sugiere herencia múltiple.

Esto comprueba que la jerarquía de herencia se ha definido correctamente.

### `test_herencia`: 
Aquí se verifica que las subclases heredan de las clases correctas, utilizando `issubclass(SubClase, SuperClase)`:

- Se comprueba que `Disenador`, `Desarrollador` y `EspecialistaDeAccesibilidad` heredan de `Trabajador`.

- También se verifica que `Fullstack` hereda tanto de `Desarrollador` como de `Disenador`, y que `UXEngineer` hereda de `Disenador` y `EspecialistaDeAccesibilidad`.

Esto asegura la estructura correcta del árbol de herencia.

### `test_trabajar`: 
Esta prueba evalúa el método sobrescrito `trabajar()` en diferentes clases:

- Cada clase tiene su propia implementación personalizada del método `trabajar`.

- Usa `assertEqual()` o `assertIn()` para confirmar que el método devuelve la cadena esperada.


### `test_salario_anual`: 
Aquí se comprueba que el método `calcular_salario_anual()` funciona correctamente:

- Este método calcula el salario base más una bonificación que varía según el tipo de trabajador.

Cada assertEqual verifica que el salario calculado sea correcto de acuerdo con las reglas específicas de la subclase.

### `test_metodos_propios`: 
Esta prueba verifica que cada subclase tiene métodos únicos adicionales además de los heredados:

- `Disenador` tiene `crear_prototipo`
- `Desarrollador` tiene `escribir_codigo`
- `EspecialistaDeAccesibilidad` tiene `auditar_interfaz`
- `Fullstack` tiene `gestionar_proyecto_completo`
- `UXEngineer` tiene `realizar_pruebas_usabilidad`

Cada uno de estos métodos representa una habilidad especializada de ese tipo de trabajador, y se asegura que al ser llamados devuelven el mensaje correcto.

## Ejecución Test
Para ejecutar el código y pasar los test de dicho código, realiza los siguientes pasos detallados que incluye la creación de un Jenkinsfile, creación pipeline y ejecución del pipeline

### 1. Creación Jenkinsfile
A continuación, hemos creado el Jenkinsfile necesario para realizar el pipeline, este se encuentra en la carpeta con el resto de código

```Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh './venv/bin/python temas/herencia/python/test.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
    }
}
```

### 2. Crear Pipeline
Una vez realizados los pasos anteriores, abrimos Jenkins y creamos un nuevo Pipeline. Para ello: 

 - Lo definimos como `Pipeline script from SCM` y como SCM seleccionamos `Git`.
 - Ponemos la siguiente URL: `https://github.com/uca-iiss/WIRTH-impl-25`.
 - En branch ponemos `*/feature-herencia`.
 - Por último, en Script Path añadimos `temas/herencia/Jenkinsfile`

Y con esta configuración hemos creado el pipeline necesario para la ejecución de los test

### 3. Ejecutar los Tests
Una vez creado el pipeline, ejecutamos dando a `Construir ahora` y el propion Jenkins pasará los test automaticamente.

