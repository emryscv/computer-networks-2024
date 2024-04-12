# Seminario Final de Redes de Computadoras
### Tema: Cliente HTTP
### Equipo

1.    Angel Daniel Alonso Guevara
2.    Emrys Cruz Viera

## Sobre el Cliente

Nuestro cliente implementa un conjunto de características del protocolo HTTP versión 1.1, definido en el RFC 2616. La implementación del protocolo de capa de aplicación, está construida sobre la librería sockets de python; la cual nos permite utilizar el protocolo TCP de la capa de transporte. 

### WorkFlow del cliente

El método request recive el método, la URL, los headers y el body. Luego:ç
1. Se Parsea la URL con el método parseURL con q tiene soporte para dos posibles patrones q consideramos correctos:

```
    http://host:port/URI
    host:port/URI
```
donde URI puede ser vacio entonces se considera `/` y port tambien entonces se considera `:80`

2. Se crea el socket y se conecta al host y el puerto extraidos de la URL
3. Se construye el string del request q es el q se enviara al servidor a partir de: ***host***, ***port***, ***headers*** y ***body***
4. Se espera por la respuesta. esta se la recive y procesa el método reciveResponse:
    1. Se intenta recivir hasta el fin de la seccion de los headers marcado por `\r\n\r\n`
    2. Se extraen status code y se parsean los headers
    3. El body se recive ne dependencia de que información dispongamos en lso headers. En general hay dos maneras q son las mas comunes que exista el header `content-length` o `transfer-encoding` con el valor `chunked`, en el caso de chunked eliminamos su implementación por problemas de compatibilidad en serividors como `www.google.com`. Luego en general esperarmos siempre recibir un body hasta q obtengamos time-out, lo cual no es lo mejor pero funciona en la mayoría de casos
5. Si el status code es de tipo 3**. Se procede a la redirección, como dictamina el RFC en cada caso.

### Interfaz gráfica.

Esta está basada en ***CustomTkinter***, una librería de renderizado de gráficos de ***Python***. Disponemos de una interfaz lo más similar a ***Postman*** posible, luego tenemos control sobre el tipo método, la URL, añadir Headers y editar el Body a nuestro gusto. Así como obtenmos información del Response, digase: ***Status***, ***Headers*** y ***Response***. Igual teniamos idea de implementar cookies pero, por problemas de tiempo no se entrega.


