## Descripción del Proyecto de Gestión Hotelera
El tema de este proyecto se centra en el diseño y desarrollo de un sistema de gestión para un establecimiento hotelero utilizando la arquitectura hexagonal (también conocida como arquitectura de puertos y adaptadores). El objetivo principal es crear una aplicación que maneje eficientemente las operaciones clave relacionadas con la gestión de habitaciones, reservas y clientes de un hotel.

# Dominio del Hotel
El núcleo del sistema incluye entidades como:

- Habitacion: Representa una habitación en el hotel, con propiedades como número, tipo y comodidades.
- Comodidad: Características adicionales que puede tener una habitación (ej., Wi-Fi, aire acondicionado).
- Reserva: Gestiona las reservas de las habitaciones, vinculando fechas, clientes y habitaciones.
- Cliente: Mantiene información de contacto e identificación de los huéspedes.

Estas entidades forman el corazón del negocio hotelero, donde cada habitación puede tener comodidades específicas, las reservas se asocian con clientes y habitaciones, y los clientes tienen datos de contacto e identificación.

# Arquitectura Hexagonal
# Puertos
Se definen interfaces para la interacción con el dominio:

- HabitacionRepository: Permite operaciones CRUD sobre las habitaciones.
- ReservaRepository: Maneja operaciones CRUD para reservas.
- ClienteRepository: Gestiona las operaciones CRUD para los clientes.

Estas interfaces permiten que la lógica de negocio no dependa de cómo se almacenan o recuperan los datos.

# Adaptadores
Estas interfaces son implementadas por adaptadores que podrían interactuar con:

- Bases de datos para persistencia de datos.
- APIs externas para servicios adicionales.
- Cualquier otro sistema de comunicación o almacenamiento.

# Ejemplos incluyen:

- HabitacionDatabaseAdapter
- ReservaDatabaseAdapter
- ClienteDatabaseAdapter

# Servicios de Aplicación
Los servicios encapsulan la lógica de negocio de alto nivel:

- GestionHabitaciones: Administra la creación, modificación y eliminación de habitaciones.
- GestionReservas: Procesa la creación, cancelar y consulta de disponibilidad de reservas.
- GestionClientes: Gestiona la información de los clientes, incluyendo registro, actualización y eliminación.

# Pruebas y Mantenibilidad
La estructura de la arquitectura hexagonal facilita:

- Prueba unitaria: Al desacoplar el dominio del cómo se manejan los datos.
- Integración de sistemas: Permite cambiar cómo se implementan las interacciones sin afectar el núcleo del negocio.

# Escalabilidad y Flexibilidad
Esta arquitectura permite que el sistema sea:

- Escalable: Capaz de gestionar un aumento en la carga de trabajo.
- Flexible: Adaptable a cambios futuros en la tecnología o en los requisitos del negocio.

El proyecto no solo automatiza las operaciones diarias de un hotel sino que lo hace de una manera que permite un desarrollo ágil, pruebas efectivas y una adaptabilidad a futuros cambios tecnológicos o de negocio.

