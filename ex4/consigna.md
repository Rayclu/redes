Ejercicio 4: Calculadora de Promedio de Notas:
En este ejercicio, van a crear un sistema donde el cliente envía tres notas al servidor y este
calcula y devuelve el promedio. El cliente debe pedir al usuario que ingrese las tres notas
separadas por comas (por ejemplo: "7,8,9") y enviarlas al servidor. El servidor, al recibir los
datos, debe usar el método split(",") para separar las notas, convertirlas a números con float(),
calcular el promedio sumando las tres y dividiendo por 3, y finalmente devolver el resultado
formateado con dos decimales usando {promedio:.2f}.