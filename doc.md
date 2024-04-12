# Seminario Final de Redes de Computadoras
### Tema: Cliente HTTP
### Equipo

1. Ángel Daniel Alonso Guevara
2. Emrys Cruz Viera

## Sobre el Cliente

Nuestro cliente implementa un conjunto de características del protocolo HTTP versión 1.1, definido en el RFC 2616. La implementación del protocolo de capa de aplicación está construida sobre la librería sockets de Python; la cual nos permite utilizar el protocolo TCP de la capa de transporte.

### Workflow del Cliente

El método request recibe el método, la URL, los headers y el body. Luego:
1. Se parsea la URL con el método parseURL que tiene soporte para dos posibles patrones que consideramos correctos:

    http://host:port/URI
    host:port/URI
donde URI puede ser vacío, entonces se considera / y port también, entonces se considera :80

2. Se crea el socket y se conecta al host y el puerto extraídos de la URL.
3. Se construye el string del request que es el que se enviará al servidor a partir de: host, port, headers y body.
4. Se espera por la respuesta. Esta se recibe y procesa con el método receiveResponse:
    1. Se intenta recibir hasta el fin de la sección de los headers marcado por \r\n\r\n.
    2. Se extraen status code y se parsean los headers.
    3. El body se recibe en dependencia de qué información dispongamos en los headers. En general, hay dos maneras que son las más comunes: que exista el header content-length o transfer-encoding con el valor chunked, en el caso de chunked eliminamos su implementación por problemas de compatibilidad en servidores como www.google.com. Luego, en general esperamos siempre recibir un body hasta que obtengamos time-out, lo cual no es lo mejor pero funciona en la mayoría de casos.
5. Si el status code es de tipo 3xx, se procede a la redirección, como dictamina el RFC en cada caso.

### Interfaz Gráfica

Esta está basada en CustomTkinter, una librería de renderizado de gráficos de Python. Disponemos de una interfaz lo más similar a Postman posible, luego tenemos control sobre el tipo de método, la URL, añadir Headers y editar el Body a nuestro gusto. Así como obtenemos información del Response, digase: Status, Headers y Response. Igual teníamos idea de implementar cookies pero, por problemas de tiempo no se entrega.
