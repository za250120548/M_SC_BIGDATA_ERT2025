
# **Introducción** 
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![VSCode](https://img.shields.io/badge/VS%20Code-Editor-007ACC?logo=visual-studio-code)](https://code.visualstudio.com/)
[![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker)](https://www.docker.com/)
[![pgAdmin](https://img.shields.io/badge/pgAdmin-4-336791?logo=postgresql)](https://www.pgadmin.org/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FCC624?logo=amazon-aws&logoColor=black)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-Infrastructure-844FBA?logo=terraform)](https://www.terraform.io/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/)
[![Big Data](https://img.shields.io/badge/Big%20Data-blue?logo=databricks&logoColor=white)](https://es.wikipedia.org/wiki/Big_data)
[![Apache Hadoop](https://img.shields.io/badge/Hadoop-yellow?logo=apache-hadoop)](https://hadoop.apache.org/)
[![Apache Spark](https://img.shields.io/badge/Spark-orange?logo=apache-spark)](https://spark.apache.org/)
[![Streaming Data](https://img.shields.io/badge/Streaming-%23DD006C?logo=streamlit&logoColor=white)](https://es.wikipedia.org/wiki/Transmisi%C3%B3n_de_datos)
## Escenario
**BookstoneData** es una start-up que lanzó su nuevo método de pago hace ocho meses. Inicialmente, la empresa tenía alrededor de **750 clientes** y, desde entonces, ha sumado aproximadamente **150,000 nuevos clientes cada mes**. Este año, la proyección es alcanzar un incremento promedio de **225,000 clientes mensuales**.

BookstoneData opera mediante sprints de dos semanas, utiliza **Git** para el control de versiones y **GitHub** como plataforma central de colaboración y gestión de código para todos sus departamentos. Todos sus servicios están desplegados en la nube, usando **Amazon Web Services (AWS)** como proveedor principal.

Este escenario simula la velocidad de crecimiento y los retos tecnológicos a los que te enfrenarás como **Junior Data Engineer**. Requiere soluciones de adquisición, almacenamiento, procesamiento, modelado y visualización de datos escalables y eficientes, alineadas con metodologías ágiles y Lean.

## Actividad
Para este Sprint, tus tareas incluyen:
1. **Lee** los siguientes temas en la sección [Teoría](#teoría):  
    a. Big Data.  
    b. Ingeniero de Datos.  
    c. Computación en la Nube.  
    d. AWS.

2. **Implementa** los pasos en la sección [Práctica](#práctica) para la empresa *BookstoneData*:  
    a. Crear cuenta:  
    * i. AWS.  
    * ii. GitHub.

    b. Instalar:  
    * i. Python.  
    * ii. VS Code.  
    * iii. Docker Desktop.  
    * iv. pgAdmin4.  
    * v. AWS CLI.  
    * vi. Terraform.

    c. Práctica en Python la [manipulación de ficheros](/Unidad_1/src/manipulación_ficheros.md) 

3. **Completa** tareas para la empresa *BookstoneData*:  
    * Revisa la sección de *Escenario*, completa las etapas en la *Actividad*, y documenta tu trabajo en `work/scenario_1.md`. Guarda toda la evidencia de tu trabajo en el directorio `work`.

---

## Teoría
Las principales nociones teóricas para esta unidad junto con recursos para aprendizaje autodidacta.

### Big Data
#### Descripción
Big Data se refiere a colecciones extremadamente grandes y diversas de datos estructurados, no estructurados y semi-estructurados que continúan creciendo exponencialmente en el tiempo. Estos conjuntos de datos son tan grandes y complejos en volumen, velocidad y variedad, que los sistemas tradicionales de manejo de datos no pueden almacenarlos, procesarlos ni analizarlos.

#### Referencias
- [Google Cloud Platform - ¿Qué es Big Data?](https://cloud.google.com/learn/what-is-big-data?hl=en)
- [Oracle - ¿Qué es Big Data?](https://www.oracle.com/uk/big-data/what-is-big-data/)
- [TechTarget - ¿Qué es big data?](https://www.techtarget.com/searchdatamanagement/definition/big-data)

### Ingeniero de Datos
#### Descripción
Un ingeniero de datos integra, transforma y consolida datos de varios sistemas de datos estructurados y no estructurados en estructuras que sean adecuadas para construir soluciones analíticas. El ingeniero de datos también ayuda a diseñar y mantener pipelines y almacenes de datos que sean de alto rendimiento, eficientes, organizados y confiables, dados un conjunto específico de requisitos y restricciones de negocio.

#### Referencias
- [MongoDB - Data Engineering Explained](https://www.mongodb.com/resources/basics/data-engineering#:~:text=Data%20engineering%20is%20the%20discipline,draw%20valuable%20insights%20from%20it.)
- [dremio - Introducción a la Ingeniería de Datos](https://www.dremio.com/resources/guides/intro-data-engineering/)
- [Redpanda - Data engineering 101](https://www.redpanda.com/guides/fundamentals-of-data-engineering)

### Computación en la nube
#### Descripción
La computación en la nube y sus soluciones asociadas brindan acceso a través de la web a recursos y productos informáticos, incluidos herramientas de desarrollo, aplicaciones empresariales, servicios de computación, almacenamiento de datos y soluciones de red. Estos servicios en la nube son alojados en el centro de datos de un proveedor de software y gestionados por el proveedor de servicios de la nube o en el centro de datos del cliente.

#### Referencias
- [IBM - ¿Qué es computación en la nube?](https://www.ibm.com/topics/cloud-computing)
- [SalesForce - ¿Qué es cloud computing?](https://www.salesforce.com/ca/cloud-computing/)
- [Oracle - ¿Qué es la computación en la nube?](https://www.oracle.com/uk/cloud/what-is-cloud-computing/)

### AWS
#### Descripción
Amazon Web Service, o AWS, es una plataforma en línea que proporciona soluciones de computación en la nube económicas y escalables. Ofrece una gama de operaciones bajo demanda, como poder de cómputo, entrega de contenido, almacenamiento de base de datos y más, para ayudar a empresas y organizaciones a crecer.

#### Referencias
- [AWS - Documentación](https://docs.aws.amazon.com/?nc2=h_ql_doc_do)
- [Simplilearn - Guía de AWS (en inglés)](https://www.simplilearn.com/tutorials/aws-tutorial/what-is-aws)
- [AWS - Cloud computing con AWS](https://aws.amazon.com/what-is-aws/)

### Contraste de arquitecturas Lambda y Kappa

#### Descripción

Las arquitecturas Lambda y Kappa son enfoques modernos para el procesamiento de datos a gran escala, pero presentan diferencias fundamentales en su estructura y aplicación. Lambda combina procesamiento por lotes (batch) y en tiempo real (stream), permitiendo manejar tanto grandes volúmenes históricos como flujos instantáneos de datos. Sin embargo, su complejidad técnica es mayor, ya que requiere el desarrollo y mantenimiento de dos flujos de procesamiento paralelos. Por otro lado, la arquitectura Kappa se basa únicamente en el procesamiento en tiempo real, simplificando la gestión porque solo se mantiene un único flujo lógico; es ideal para aplicaciones donde la baja latencia y la simplicidad operacional son prioritarias, como la monitorización en IoT o plataformas de streaming. En resumen, Lambda es útil cuando es necesario un procesamiento preciso de históricos y streaming, mientras que Kappa es la elección preferida para flujos continuos de datos con menor complejidad operativa.

#### Referencias

- [ESEID - Arquitectura Lambda vs Kappa: similitudes, diferencias y usos](https://eseid.com/arquitectura-lambda-vs-kappa/)
- [Event-Driven Architecture – Lambda and Kappa](https://www.oreilly.com/library/view/mastering-apache-storm/9781784398243/ch10s04.html)
- [Medium - Lambda and Kappa Architecture: Big Data Processing](https://medium.com/@mohamedlatif2012/lambda-and-kappa-architecture-big-data-processing-9f960a7d7b67)
---

## Práctica
La implementación para la parte práctica de la unidad

### Crear cuentas
Configura cuentas para los servicios comúnmente usados por un ingeniero de datos.

#### AWS
Accede a la página del [AWS Free Tier](https://aws.amazon.com/free/?gclid=Cj0KCQjwlvW2BhDyARIsADnIe-IgwrWgVraM9DbxPuBhtXrzhDOv1RoLsFkd13_kZDe0KCPqFPb3rjAaAiKSEALw_wcB&trk=9ab5159b-247d-4917-a0ec-ec01d1af6bf9&sc_channel=ps&ef_id=Cj0KCQjwlvW2BhDyARIsADnIe-IgwrWgVraM9DbxPuBhtXrzhDOv1RoLsFkd13_kZDe0KCPqFPb3rjAaAiKSEALw_wcB:G:s&s_kwcid=AL!4422!3!645133561110!e!!g!!create%20aws%20account!19579657595!152087369744&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all) y presiona el botón `Create a Free Account` en el centro de la página.  
Si ya tienes cuenta, presiona `Sign in to an existing AWS account`.  
Puedes seguir las instrucciones de abajo o acceder a [Crear tu cuenta de AWS](https://aws.amazon.com/getting-started/guides/setup-environment/module-one/) y seguir las instrucciones allí.  
![AWS Free Tier](/Assets/image_1.1.PNG)

**Paso 1 - Seleccionar credenciales**  
1 - Ingresa una dirección de correo electrónico y un nombre para la cuenta.  
Considera cuidadosamente qué correo utilizar. Para cuentas personales, no se recomienda usar uno corporativo, ya que podrías cambiar de empleo. Para cuentas de negocios, utiliza un alias administrable.  
2 - Selecciona Verificar dirección de correo electrónico.  
Recibirás un código en tu correo. Introdúcelo y elige Verificar.  
Serás redirigido a una nueva pantalla para crear la contraseña del usuario raíz.  
![Seleccionar credenciales](/Assets/image_1.2.PNG)

**Paso 2 - Agregar información de contacto**  
1 - Elige entre cuenta personal o de negocios.  
No hay diferencia en funcionalidades, solo en la información para facturación.  
2 - Completa la información de contacto y guarda los datos en un lugar seguro.  
3 - Lee y acepta los términos del acuerdo de AWS.  
4 - Selecciona Continuar (paso 2 de 5).  
![Añadir información de contacto](/Assets/image_1.3.PNG)

**Paso 3 - Agregar método de pago**  
1 - Ingresa los datos de facturación. Se mantendrá un pequeño bloqueo en la tarjeta, la dirección debe coincidir con la registrada en la institución financiera.  
2 - Selecciona Verificar y Continuar.  
![Agregar método de pago](/Assets/image_1.4.PNG)

**Paso 4 - Confirmar identidad**  
1 - Elige cómo quieres confirmar tu identidad: por SMS o llamada. Recibe y introduce el código, luego selecciona Continuar.  
![Confirmar tu identidad](/Assets/image_1.5.PNG)

**Paso 5 - Seleccionar plan de soporte**  
1 - Elige un plan de soporte. Para este tutorial, se recomienda la opción por defecto (Basic Support, sin costo). Puedes cambiar el plan más adelante.  
2 - Para finalizar la creación, selecciona Complete sign up.  
![Seleccionar un plan de soporte](/Assets/image_1.6.PNG)

Tu cuenta se está activando. Cuando finalice, recibirás un correo de AWS para acceder con las credenciales creadas.

#### GitHub
Accede a [GitHub](https://github.com/) y presiona el botón `Sign up` en la esquina derecha.  
Si ya tienes cuenta, haz clic en `Sign in` e inicia sesión con tus credenciales.  
Puedes seguir las instrucciones aquí o en [Crear una cuenta en GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).  
![Cuenta GitHub](/Assets/image_1.7.PNG)

**Paso 1 - Seleccionar credenciales**  
Proporciona un correo electrónico que no esté en otra cuenta de GitHub.  
Crea una contraseña segura (mínimo 8 caracteres).  
Proporciona un nombre de usuario.  
Elige si quieres recibir anuncios de GitHub.  
![Seleccionar credenciales](/Assets/image_1.8.PNG)

**Paso 2 - Pasar verificación**  
Resuelve tres puzzles para comprobar que eres humano.  
![Verificación](/Assets/image_1.9.PNG)

**Paso 3 - Confirmar dirección de correo**  
Recibirás un código de 8 dígitos en el correo, ingrésalo en la página actual.  
![Confirmar correo](/Assets/image_1.10.PNG)

**Paso 4 - Elegir tu plan**  
Para uso personal la cuenta gratuita es suficiente. Presiona `Continue for free`.  
![Elegir plan](/Assets/image_1.11.PNG)

---

### Instalar software
Instala el software necesario para el trabajo diario de un ingeniero de datos.

#### Python
Accede a la [página de descargas de Python](https://www.python.org/downloads/) y presiona `Download Python 3.<version>` en el centro de la página.  
Sigue las instrucciones aquí o visita [Guía de instalación de Python](https://realpython.com/installing-python/).  
![Sitio Python](/Assets/image_1.12.PNG)

Al descargar el instalador, ve a la carpeta `Downloads`, identifica el instalador y haz doble clic. Elige `Customize installation` y marca ambas casillas: `Install launcher for all users` y `Add Python to PATH`.  
![Ventana Python](/Assets/image_1.13.PNG)

Se recomienda instalar todas las características opcionales.  
![Características opcionales](/Assets/image_1.14.PNG)

Tras la instalación, verifica con el comando:

>python --version

Deberías ver la versión instalada.  
![Versión Python](/Assets/image_1.15.PNG)

#### VS Code
Accede a la [página de VS Code](https://code.visualstudio.com/) y presiona `Download for <OS>`.  
Puedes seguir las instrucciones para instalar localmente o usar [VS Code online](https://vscode.dev/).  
![Sitio VS Code](/Assets/image_1.16.PNG)

Ejecuta el instalador, selecciona las opciones necesarias y al finalizar presiona `Finish` para lanzar VS Code.  
![VS Code](/Assets/image_1.18.PNG)

#### Docker
Accede a la [página de Docker](https://www.docker.com/products/docker-desktop/) y pulsa `Download for <OS>`.  
Puedes consultar [Instalación de Docker Desktop](https://docs.docker.com/desktop/install/windows-install/).  
![Sitio Docker](/Assets/image_1.19.PNG)

Ejecuta el instalador, sigue los pasos y elige opciones de backend (WSL2 o Hyper-V según tu equipo).  
Al terminar, inicia Docker Desktop.  
Opcionalmente, usa [Docker Hub](https://www.docker.com/products/docker-hub/).  
![Docker Hub](/Assets/image_1.21.PNG)

#### pgAdmin 4
Para trabajar con bases de datos localmente, instala PostgreSQL y pgAdmin4.  
Accede a [PostgreSQL](https://www.postgresql.org/download/) para descargar la versión más reciente para tu OS. Instala siguiendo instrucciones del asistente.  
Descarga [pgAdmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/) y sigue el asistente de instalación.  
![Sitio pgAdmin](/Assets/image_1.22.PNG)

#### AWS CLI
Accede al [instalador de AWS CLI](https://awscli.amazonaws.com/AWSCLIV2.msi), se descargará automáticamente.  
Consulta [Instalación de AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) para más detalles.

Para actualizar en Windows, descarga el instalador cada vez y sobreescribe versiones previas. Ejecuta el instalador o usa:


>C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi



Para modo silencioso:


>C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi /qn


Verifica la instalación con:


>C:\> aws --version


Debería mostrar la versión instalada.  
![AWS CLI](/Assets/image_1.23.PNG)

#### Terraform
Visita [Terraform](https://www.terraform.io/downloads.html) y pulsa `Download Terraform`.  
Descargarás un zip; crea una carpeta en `C:/terraform`, coloca allí los archivos y descomprime el `.exe`.  
Abre el menú Inicio, busca `Variables de entorno`, edita la variable `Path` agregando la carpeta de Terraform.  
Haz clic en OK para guardar y reinicia el sistema de ser necesario.  
En la terminal ejecuta:

>terraform --version

Debería aparecer la versión instalada.  
![Terminal Terraform](/Assets/image_1.28.PNG)

