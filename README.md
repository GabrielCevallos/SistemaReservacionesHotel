# Sistema Reservaciones Hotel
**Acceso Usuario:** Pancho

**Contraseña:** 123

**Integrantes:**
Gabriel Cevallos, Nathaly Camacho, Francisco Jaramillo, Jimmy Ontaneda, Ariana Sarango

**Ciclo:** Segundo "A"

**Diagrama UML:**

![image](https://github.com/GabrielCevallos/SistemaReservacionesHotel/assets/166523819/b228f6c6-e0d3-42fd-b716-f16eab245022)

# Sistema Hotelario

Nuestro hotel ofrece cómodas habitaciones, variados servicios adicionales y paquetes especiales con beneficios exclusivos. Gestionamos las reservas eficientemente, asegurando disponibilidad y organización para una experiencia satisfactoria.

# Estructura del Proyecto

1. **Contenido**: Carpeta principal del proyecto.
  - **Servicio**: Módulo para la gestión de servicios del hotel.
  - **Paquete**: Módulo para la gestión de paquetes especiales.
  - **Habitacion**: Módulo para la gestión de habitaciones.
  
2. **Enumeración**
  - **EstadoHabitacion**: Define los estados posibles de una habitación (RESERVADA, DISPONIBLE, OCUPADA).

3. **Interfaces**
  - **GestionReservaciones**: Interfaz para la gestión de reservas.

4. **Herencia**
  - **Persona**: Clase base.
    - **Cliente**: Subclase de Persona para clientes del hotel.
    - **Recepcionista**: Subclase de Persona para recepcionistas del hotel.
5. **Composiciones**
  - **OfertaHotel**: Módulo para la gestión de ofertas del hotel.
    - **OfertaServicios**: Submódulo para la gestión de ofertas de servicios.
    - **OfertaPaquete**: Submódulo para la gestión de ofertas de paquetes.
    - **OfertaHabitacion**: Submódulo para la gestión de ofertas de habitaciones.

# Ejecutar Programa

Para comenzar, ve a la terminal y navega hasta la carpeta donde deseas clonar el repositorio, luego copia este código:

    git clone https://github.com/GabrielCevallos/SistemaReservacionesHotel.git 

Una vez clonado el repositorio, sigue los pasos en el IDE que se te facilite.

# Pycharm:

1. Abre la carpeta clonada. 
2. En el caso de que no tengas instalado Django, ejecuta el siguiente comando:

            pip install django


3. Para acceder a nuestra página web, ve a la terminal de Pycharm y ejecuta el siguiente comando:


        python manage.py runserver


# Visual Studio Code:

1. Abre la carpeta clonada.
2. En "Control de código fuente" se visualizan las ramas.
3. Para ejecutar el programa, en la barra superior ir a "Run", luego ve a "Start Debugging" o presiona "F5".

