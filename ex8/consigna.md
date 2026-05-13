Van a hacer un servidor que tenga una lista de frases guardadas.
 El cliente puede pedir una frase al azar, agregar una frase nueva, contar cuántas frases hay o listar todas.
Los comandos son: 
    "frase" para recibir una aleatoria.
    "agregar,texto" para sumar una nueva (el texto va después de la coma).
    "contar" para ver la cantidad.
    "listar" para ver todas con número.
    "salir" para cerrar.

Usan random.choice() para elegir frases y startswith() para detectar el comando agregar. Tienen que validar que cuando se agregue una frase, el texto no esté vacío. El cliente
tiene que mostrar los comandos disponibles cuando arranca.