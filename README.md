# Nombre del proyecto:
# Urban Routes

# Descripción del Proyecto:

El proyecto Urban Routes prueba de manera automatizada el flujo completo en la solicitud de un servicio de taxi en línea,
contemplando todos y cada uno de los pasos necesarios para poder tener un servicio de taxi.
El objetivo del presente proyecto es validar el correcto funcionamiento de una solicitud del servicio, validando
digitación de direcciones, oprimir botones, selección de tarifas, ingreso de datos de contacto, envío de mensajes
al conductor para solicitud de servicios adicionales (aperitivos y comodidades),métodos de pago, confirmación de
reservas del servicio, etc

### Archivos y directorios:

- **data.py**: Contiene datos exactos que se utilizan en las pruebas.
-**locators.py**: Contiene los localizadores de cada uno de los elementos de la página utilizados en la presente prueba.
-**helpers.py**: Contiene un código que devuelve un número de confirmación de teléfono y lo devuelve como un string.
-**methods.py**: Contiene los métodos utilizados en las pruebas.
-**test_main.py**: Contiene la lista de comprobación para cada uno de las pruebas.

## Tecnologías Utilizadas

-**Python**: Es un lenguaje de programación principal del proyecto.
-**Pytest**: Entorno de pruebas utilizado para automatizar y gestionar las pruebas.
-**Selenium**: Es una herramienta para simular la interacción del usuario con la pagina web de Urban Routes.
-**Devtools**: Utilizado para identificar los localizadores desde Chrome.

## Ejecución de pruebas

* Ruta del archivo: C:/Users/Paola Andrade/PycharmProjects/projects/qa-project-Urban-Routes-es-main
* Necesitas tener instalados los paquetes pytest y Selenium para ejecutar las pruebas.
* Las pruebas utilizarán el navegador Chrome, así que asegúrate de tenerlo instalado.
* Para ejecutar las pruebas asegúrate de estar en el directorio "test_main.py", donde se encuentran las pruebas.
* Al finalizar las pruebas, pytest mostrará un resumen de los resultados en la terminal.

## Funcionalidad de las pruebas:

Las pruebas automatizadas cubren los siguientes pasos incurridos en la solicitud de un taxi en linea:

 1. Configurar la dirección.
 2. Seleccionar la tarifa Comfort.
 3. Rellenar el número de teléfono.
 4. Agregar una tarjeta de crédito.
 5. Escribir un mensaje para el conductor.
 6. Solicitar una manta y pañuelos.
 7. Pedir 2 helados.
 8. Esperar la búsqueda de un taxi
