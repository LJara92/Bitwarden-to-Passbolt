import json
import csv

#Este script convierte un archivo JSON exportado desde Bitwarden a un CSV compatible con Passbolt

def parse_json_to_csv(archivo_json, archivo_csv):
    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            datos_bitwarden = json.load(f)

        with open(archivo_csv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            
            # Cabeceras del CSV
            writer.writerow(["name", "username", "password", "uri", "description"])

            # Procesar cada entrada del JSON de Bitwarden
            for entrada in datos_bitwarden["items"]:
                try:
                    name = entrada.get("name", "")
                    username = entrada.get("login", {}).get("username", "")
                    password = entrada.get("login", {}).get("password", "")
                    uri = ", ".join(u["uri"] for u in entrada.get("login", {}).get("uris", [])) if entrada.get("login", {}).get("uris") else ""
                    description = entrada.get("notes", "")

                    # Escribir la fila en el CSV
                    writer.writerow([name, username, password, uri, description])

                except Exception as e:
                    print(f"Error en el registro: {entrada.get('name', 'Sin nombre')}. Detalle: {e}")

        print(f"Conversión completada. Archivo CSV guardado en: {archivo_csv}")

    except Exception as e:
        print(f"Error durante la conversión: {e}")


# Ruta del archivo JSON exportado desde Bitwarden
archivo_json = r"C:\\Ubicacion_De_Archivo.json"

# Ruta donde se guardara el archivo CSV para importar en Passbolt
archivo_csv = r"C:\\Ubicacion_Destino_Archivo.csv"

# Llamar a la función para realizar la conversión
parse_json_to_csv(archivo_json, archivo_csv)
