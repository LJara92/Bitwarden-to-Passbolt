# JSON a CSV: Conversión de Bitwarden a Passbolt

Este script convierte un archivo JSON exportado desde **Bitwarden** a un archivo CSV compatible con **Passbolt**.

## Características

- Extrae datos esenciales del JSON de Bitwarden como:
  - Nombre del elemento
  - Nombre de usuario
  - Contraseña
  - URI(s)
  - Notas
- Genera un archivo CSV estructurado para importar directamente en Passbolt.

## Requisitos

- Python 3.x
- Módulos estándar: `json`, `csv`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/Bitwarden-to-Passbolt.git
   cd Bitwarden-to-Passbolt
   
2. Asegúrate de tener Python instalado en tu sistema.
   
## Uso
1. Exporta tu bóveda desde Bitwarden en formato JSON.
2. Define las rutas del archivo JSON de origen y del CSV de destino en el script:

`archivo_json = r"C:\\Ruta\\De\\Tu\\Archivo.json"`
`archivo_csv = r"C:\\Ruta\\De\\Tu\\Archivo.csv"`

3. Ejecuta el script:

`python json_to_csv.py`

4. Encuentra tu archivo CSV generado en la ubicación especificada

## Estructura del CSV
El archivo CSV generado contendrá las siguientes columnas:

  - name: Nombre del elemento
  - username: Nombre de usuario
  - password: Contraseña
  - uri: Enlaces asociados (si hay múltiples, estarán separados por comas)
  - description: Notas

##  Manejo de Errores
El script incluye manejo básico de errores:

  - Si una entrada del JSON no contiene algún campo esperado, el error será registrado en la consola.
  - Mensajes claros indican cualquier fallo durante la conversión.

##  Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún problema o deseas agregar funcionalidades, no dudes en abrir un issue o enviar un pull request.


*Autor*: Lautaro Jara

*Creado*: 25/11/2024


   
