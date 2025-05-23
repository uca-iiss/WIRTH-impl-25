error id: file://<WORKSPACE>/abstraccion-pagos/src/main/scala/payment/common.scala:`<none>`.
file://<WORKSPACE>/abstraccion-pagos/src/main/scala/payment/common.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
empty definition using fallback
non-local guesses:

offset: 198
uri: file://<WORKSPACE>/abstraccion-pagos/src/main/scala/payment/common.scala
text:
```scala
package payment

// Alias de tipo: Money representa un Double, pero mejora la legibilidad
type Money = Double

// Estado de la transacción
sealed trait TransactionStatus

case object Success extends@@ TransactionStatus
case object Failure extends TransactionStatus

```


#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.