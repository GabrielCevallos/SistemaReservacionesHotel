# SistemaReservacionesHotel
Acceso
Usuario: Pancho
Contraseña:123

Integrantes:
Gabriel Cevallos, Nathaly Camacho, Francisco Jaramillo, Jimmy Ontaneda, Ariana Sarango

Ciclo: Segundo

Diagrama UML:

![image](https://github.com/GabrielCevallos/SistemaReservacionesHotel/assets/166523819/b228f6c6-e0d3-42fd-b716-f16eab245022)

# Sistema Hotelario

Nuestro hotel ofrece cómodas habitaciones, variados servicios adicionales y paquetes especiales con beneficios exclusivos. Gestionamos las reservas eficientemente, asegurando disponibilidad y organización para una experiencia satisfactoria.

# Estructura del Proyecto

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




