# PRESENTACIÓN WIRTH-IMPL25

## Introducción

Este proyecto es una exploración práctica de tres conceptos clave en diferentes lenguajes de programación modernos:

- **Abstracción en Scala**: Cómo el lenguaje aprovecha la orientación a objetos y la programación funcional para definir estructuras abstractas y reutilizables.
- **Anotaciones en C#**: El uso de atributos como una forma poderosa de enriquecer el código con metadatos que guían comportamientos en tiempo de compilación y ejecución.
- **Funciones Lambda en Python**: Expresiones funcionales concisas que permiten una escritura más declarativa y elegante del código.

Cada sección incluye ejemplos de código comentado y explicaciones breves, con el objetivo de comparar estilos, sintaxis y paradigmas entre lenguajes.


## Abstracción – Scala 

### Conceptos Previos

#### ¿Qué es la abstracción?
La **abstracción** consiste en definir estructuras generales que ocultan detalles de implementación y permiten trabajar con ideas más conceptuales. En programación orientada a objetos, esto se traduce en clases abstractas o interfaces.

#### Conceptos clave en Scala:
- **Abstract class**: con `abstract` declara que la clase asociada no puede instanciarse directamente. En nuestro caso la clase `PaymentMethod`define un contrato común para todos los métodos de pago y delega los detalles de pay y balance a las subclases, ocultando el cómo se hace el pago (aquí la idea de la abstracción).

- **Sealed trait**: un `trait` es como una interfaz con posible implementacion. Al usar sealed estamo cerradon la jerarquía de subtipos al archivo, favoreciendo el control del diseño. Esto nos proporciona una mejor seguridad y mantenibilidad del diseño, evitando que otros componentes definan estados no contemplados.  En nuestro caso el archivo `Common.scala` muestra este concepto. 

- **Modificadores de visibilidad**: los modificadores de visibilidad como su nombre indica cambian los permisos de visibilidad de una clase, es decir, encapsulación con diferentes grados de acceso. 
  - `private`: limita el acceso solo a la clase donde se define. En nuestro caso `creditLimit` solo lo puede usar la clase `CreditCard`.
  - `protected`: permite el acceso desde subclaes. En nuestro caso `balance` es visible en CreditCard y PayPal, pero no desde fuera
  - `public`: permite el acceso desde cualquier clase. 

- **Diferencia entre inmutable y mutable**: En nuestro ejemplo se puede diferencia entre lo inmutable (lo que no se puede cambiar), por ejemplo con `val owner: String`, usando val de lo mutable (lo que si se puede cambiar), por ejemplo `var balance`. Esta diferenciación refuerza el diseño robusto del ejemplo 

- **Type**: usando la variable `type` abstraemos un tipo , por ejemplo en `type Money = Double` para abstraer el tipo de dinero. Esto sirve para que el cliente que use un sistema parecido a esto piense en "Money" y no en "Double"

### Código de Ejemplo

```scala
package payment

class PayPal(private val email: String, private var balance: Money) extends PaymentMethod {

  val name: String = "PayPal"

  def pay(amount: Money): TransactionStatus = {
    if (amount <= balance) {
      balance -= amount
      logTransaction(amount, Success)
      Success
    } else {
      logTransaction(amount, Failure)
      Failure
    }
  }

  def recharge(amount: Money): Unit = {
    balance += amount
  }
  
  def getBalance: Money = balance
}
```
```scala
package payment

// Clase abstracta base
abstract class PaymentMethod {

  val name: String

  def pay(amount: Money): TransactionStatus

  protected def logTransaction(amount: Money, status: TransactionStatus): Unit = {
    println(s"[$name] Transacción de $amount€ => Estado: $status")
  }
}
```

```scala
package payment

class CreditCard(cardNumber: String, var creditLimit: Money) extends PaymentMethod {

  val name: String = "Tarjeta de Crédito"
  def pay(amount: Money): TransactionStatus = {
    if (amount <= creditLimit) {
      creditLimit -= amount
      logTransaction(amount, Success)
      Success
    } else {
      logTransaction(amount, Failure)
      Failure
    }
  }
}
```

```scala
package payment

type Money = Double
sealed trait TransactionStatus

case object Success extends TransactionStatus
case object Failure extends TransactionStatus
```

### Código de tests

```scala
package payment

import org.scalatest.funsuite.AnyFunSuite

class PaymentMethodSpec extends AnyFunSuite {

  test("CreditCard permite pago si hay suficiente crédito") {
    val card = new CreditCard("1234", 100.0)
    val result = card.pay(50.0)
    assert(result == Success)
  }

  test("CreditCard rechaza pago si no hay suficiente crédito") {
    val card = new CreditCard("1234", 30.0)
    val result = card.pay(50.0)
    assert(result == Failure)
  }

  test("PayPal permite pago si hay saldo suficiente") {
    val paypal = new PayPal("user@example.com", 80.0)
    val result = paypal.pay(60.0)
    assert(result == Success)
  }

  test("PayPal rechaza pago si el saldo es insuficiente") {
    val paypal = new PayPal("user@example.com", 20.0)
    val result = paypal.pay(30.0)
    assert(result == Failure)
  }

  test("Paypal recarga saldo corretamente"){
    val paypal = new PayPal("user@example.com", 0.0)
    paypal.recharge(100.0)
    assert(paypal.getBalance == 100.0)
  }
}
```
## Anotaciones - C#

### Conceptos Previos

#### ¿Qué son las anotaciones?
En C#, las **anotaciones** se llaman atributos, y son metadatos que se agregan al código usando corchetes ([ ]). Estos modifican o describen cómo se comportan clases, propiedades, métodos, etc.

#### Conceptos clave en Scala:
- **Definición y Uso de Atributos**: Los atributos en C# se definen como clases que heredan del tipo `System.Attribute`. Estas clases pueden contener propiedades, campos y constructores que permiten configurar su comportamiento y datos asociados. Además, utilizando el atributo `AttributeUsage`, se puede indicar a qué elementos del código se puede aplicar el atributo (por ejemplo, clases, métodos, propiedades, etc.), y si es posible aplicar múltiples instancias del mismo atributo en un solo elemento. Esta configuración proporciona flexibilidad a la hora de utilizar atributos personalizados de forma controlada y estructurada.

- **Aplicación de Atributos**:Los atributos se aplican escribiéndolos entre corchetes `[ ]` justo antes del elemento del código al que se refieren. Esto puede incluir clases, métodos, propiedades, campos, parámetros, ensamblados y más. Al aplicar un atributo, es posible pasarle argumentos definidos en su constructor, así como establecer valores para sus propiedades públicas. Esto hace que los atributos sean altamente configurables y útiles para describir el propósito o comportamiento esperado de los elementos del programa.

- **Atributos Intrínsecos y Personalizados**: C# incluye una variedad de atributos integrados en el .NET Framework que cumplen funciones específicas. Algunos ejemplos comunes incluyen `[Obsolete]`, que marca un elemento como obsoleto y genera una advertencia en tiempo de compilación; `[Serializable]`, que indica que una clase puede ser serializada; y `[DllImport]`, que permite importar funciones de bibliotecas externas. Sin embargo, cuando los atributos estándar no son suficientes, los desarrolladores pueden definir atributos personalizados que se ajusten a necesidades específicas del dominio de la aplicación. Esta capacidad de extensión permite crear soluciones más flexibles y mantenible

- **Reflexión y Atributos**: La reflexión es una característica de C# que permite inspeccionar la estructura del programa en tiempo de ejecución. Usando reflexión, es posible acceder a los atributos aplicados a una clase, método o cualquier otro miembro, y actuar en consecuencia. Esto es especialmente útil en frameworks, bibliotecas de validación, motores de pruebas automáticas, herramientas de documentación y otros escenarios donde se requiere comportamiento dinámico basado en metadatos.

- **Atributos y Serialización**: Los atributos juegan un papel importante en la serialización de objetos, especialmente en el contexto de APIs y servicios web. En .NET, atributos como [JsonPropertyName] permiten cambiar el nombre con el que se serializa una propiedad, mientras que [JsonIgnore] evita que una propiedad sea incluida en la salida serializada. Esta capacidad de control detallado sobre la salida serializada permite que los objetos se adapten mejor a los requerimientos de comunicación externa sin modificar su estructura interna.


### Código de Ejemplo

```csharp
using System;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Collections.Generic;


// Atributo personalizado para validar el salario
[AttributeUsage(AttributeTargets.Property, AllowMultiple = false)]
public class RangoSalarioAttribute : Attribute
{
    public decimal Min { get; }
    public decimal Max { get; }

    public RangoSalarioAttribute(double min, double max)
    {
        Min = (decimal)min;
        Max = (decimal)max;
    }
}

// Clase Trabajador usando el atributo personalizado
public class Trabajador
{
    [RangoSalario(1000, 10000)] // Salario entre 1000 y 10000
    public decimal Salario { get; set; }

    public string Nombre { get; set; } = string.Empty;

    public void Validar()
    {
        var propiedades = GetType().GetProperties();
        foreach (var prop in propiedades)
        {
            var attr = Attribute.GetCustomAttribute(prop, typeof(RangoSalarioAttribute)) as RangoSalarioAttribute;
            if (attr != null)
            {
                decimal valor = (decimal)prop.GetValue(this)!;
                if (valor < attr.Min || valor > attr.Max)
                {
                    throw new ArgumentOutOfRangeException(prop.Name, $"El salario debe estar entre {attr.Min} y {attr.Max}.");
                }
            }
        }
    }
}

// Clase Empresa con control de serialización JSON
public class Empresa
{
    [JsonPropertyName("nombre_empresa")]
    public string Nombre { get; set; } = string.Empty;

    [JsonPropertyName("ubicacion")]
    public string Ubicacion { get; set; } = string.Empty;

    [JsonPropertyName("trabajadores")]
    public List<Trabajador> Empleados { get; set; } = new List<Trabajador>();
}

// Programa principal
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Ejemplo 1: Validación de Salario Correcta");
        var trabajadorValido = new Trabajador { Nombre = "Ana", Salario = 3500m };
        try
        {
            trabajadorValido.Validar();
            Console.WriteLine("Validación exitosa para Ana.");
        }
        catch (ArgumentOutOfRangeException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }

        Console.WriteLine("\nEjemplo 2: Validación de Salario Incorrecta");
        var trabajadorInvalido = new Trabajador { Nombre = "Carlos", Salario = 500m };
        try
        {
            trabajadorInvalido.Validar();
            Console.WriteLine("Validación exitosa para Carlos.");
        }
        catch (ArgumentOutOfRangeException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }

        Console.WriteLine("\nEjemplo 3: Serialización JSON de Empresa");
        var empresa = new Empresa
        {
            Nombre = "Tech Solutions",
            Ubicacion = "Madrid",
            Empleados = new List<Trabajador>
            {
                new Trabajador { Nombre = "Ana", Salario = 3500m },
                new Trabajador { Nombre = "Luis", Salario = 4200m }
            }
        };

        string json = JsonSerializer.Serialize(empresa, new JsonSerializerOptions { WriteIndented = true });
        Console.WriteLine(json);
    }
}
```

### Código de tests

```csharp
using NUnit.Framework;
using System;
using System.Text.Json;
using System.Collections.Generic;


namespace EmpresaTests
{
    [TestFixture]
    public class TrabajadorTests
    {
        [Test]
        public void ValidarSalario_Valido_NoLanzaExcepcion()
        {
            var trabajador = new Trabajador { Nombre = "Pedro", Salario = 3000m };
            Assert.DoesNotThrow(() => trabajador.Validar());
        }

        [Test]
        public void ValidarSalario_Invalido_LanzaExcepcion()
        {
            var trabajador = new Trabajador { Nombre = "Laura", Salario = 200m };
            var ex = Assert.Throws<ArgumentOutOfRangeException>(() => trabajador.Validar());
            StringAssert.Contains("Salario", ex.Message);
        }

        [Test]
        public void SerializarEmpresa_ContieneDatosCorrectos()
        {
            var empresa = new Empresa
            {
                Nombre = "Innovatech",
                Ubicacion = "Barcelona",
                Empleados = new List<Trabajador>
                {
                    new Trabajador { Nombre = "Carlos", Salario = 4000m },
                    new Trabajador { Nombre = "Elena", Salario = 5200m }
                }
            };

            string json = JsonSerializer.Serialize(empresa);

            StringAssert.Contains("Innovatech", json);
            StringAssert.Contains("Barcelona", json);
            StringAssert.Contains("Carlos", json);
            StringAssert.Contains("Elena", json);
        }

        [Test]
        public void Salario_MinimoPermitido_EsValido()
        {
            var trabajador = new Trabajador { Nombre = "Pepe", Salario = 1000m };
            Assert.DoesNotThrow(() => trabajador.Validar());
        }

        [Test]
        public void Salario_MaximoPermitido_EsValido()
        {
            var trabajador = new Trabajador { Nombre = "Lucía", Salario = 10000m };
            Assert.DoesNotThrow(() => trabajador.Validar());
        }

        [Test]
        public void Salario_JustoPorDebajoDelMinimo_LanzaExcepcion()
        {
            var trabajador = new Trabajador { Nombre = "Mario", Salario = 999.99m };
            Assert.Throws<ArgumentOutOfRangeException>(() => trabajador.Validar());
        }

        [Test]
        public void Salario_JustoPorEncimaDelMaximo_LanzaExcepcion()
        {
            var trabajador = new Trabajador { Nombre = "Ana", Salario = 10000.01m };
            Assert.Throws<ArgumentOutOfRangeException>(() => trabajador.Validar());
        }

        [Test]
        public void SerializacionEmpresa_PropiedadesJsonRenombradasCorrectamente()
        {
            var empresa = new Empresa
            {
                Nombre = "DataCorp",
                Ubicacion = "Valencia",
                Empleados = new List<Trabajador>()
            };

            string json = JsonSerializer.Serialize(empresa);
            StringAssert.Contains("\"nombre_empresa\"", json);
            StringAssert.Contains("\"ubicacion\"", json);
            StringAssert.Contains("\"trabajadores\"", json);
        }
    }
}
```
## Lambdas - Python

### Conceptos Previos

#### ¿Qué es una función lambda?
Una **lambda** en Python es una función anónima y breve, definida con la palabra clave `lambda`. Son muy usadas en programación funcional, especialmente con funciones como `map`, `filter` y `reduce`.

#### Conceptos clave en Scala:
- **Funciones Lambda para Operaciones Simples**:Las funciones lambda se emplean comúnmente para realizar operaciones sencillas, como sumar dos valores. Son una forma compacta de escribir funciones que solo requieren una línea de código.

- **Uso de Lambda con `map()`**: La función `map()` aplica una función a cada elemento de un iterable y devuelve un nuevo iterable. Usar funciones lambda con `map()` permite aplicar operaciones complejas de manera concisa sin necesidad de definir una nueva función.

- **Uso de Lambda con `filter()`**: La función `filter()` construye un iterador a partir de aquellos elementos de un iterable para los que una función devuelve verdadero. Las funciones lambda son útiles aquí para definir rápidamente la función de filtrado sin separar la definición de la función.

- **Funciones Lambda para Condiciones Ternarias**: Las funciones lambda también pueden ser utilizadas para ejecutar expresiones condicionales, lo cual permite integrar lógica condicional dentro de una definición funcional breve y directa.

- **Uso de Lambda con `reduce()`**: La función `reduce()` de la biblioteca `functools` se utiliza para aplicar una función de dos argumentos acumulativamente a los elementos de una secuencia, de manera que se reduzca la secuencia a un único valor. Las funciones lambda son ideales para definir la función de reducción de forma rápida y en el mismo lugar donde se utiliza.


### Código de Ejemplo

```python
from functools import reduce

def operacion_basica():
  #Multiplicamos dos números
  multiplicar = lambda a, b: a * b
  return multiplicar(7, 4)

def transformar_lista():
  #Conviertimos una lista de cadenas a mayúsculas
  palabras = ["manzana", "banana", "cereza"]
  return list(map(lambda palabra: palabra.upper(), palabras)) 

def filtrar_numeros():
  #Filtramos una lista de números para obtener solo los mayores de 10
  numeros = [5, 12, 8, 21, 15, 3]
  return list(filter(lambda num: num > 10, numeros)) 

def evaluacion_condicional():
  #Determinamos si un número es positivo, negativo o cero 
  clasificar_numero = lambda x: "Positivo" if x > 0 else ("Negativo" if x < 0 else "Cero")
  return clasificar_numero(-5)

def concatenar_cadenas():
  #Concatena una lista de cadenas
  fragmentos = ["Python", " ", "es", " ", "genial"]
  return reduce(lambda acumulador, elemento: acumulador + elemento, fragmentos)
```

### Código de tests

```python
import unittest
from lambdas import *

class TestLambdas(unittest.TestCase):

    def test_operacion_basica(self):
        resultado = operacion_basica()
        self.assertEqual(resultado, 28)

    def test_transformar_lista(self):
        resultado = transformar_lista()
        self.assertEqual(resultado, ["MANZANA", "BANANA", "CEREZA"])

    def test_filtrar_numeros(self):
        resultado = filtrar_numeros()
        self.assertEqual(resultado, [12, 21, 15])

    def test_evaluacion_condicional(self):
        resultado_neg = evaluacion_condicional()
        self.assertEqual(resultado_neg, "Negativo")

        clasificar = lambda x: "Positivo" if x > 0 else ("Negativo" if x < 0 else "Cero")
        self.assertEqual(clasificar(10), "Positivo")
        self.assertEqual(clasificar(0), "Cero")

    def test_concatenar_cadenas(self):
        resultado = concatenar_cadenas()
        self.assertEqual(resultado, "Python es genial")

if __name__ == "__main__":
    unittest.main()
```