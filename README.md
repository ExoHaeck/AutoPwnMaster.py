# AutoPwnMaster

## Descripción

`AutoPwnMaster.py` es un script automatizado diseñado para detectar vulnerabilidades de Local File Inclusion (LFI) en URLs obtenidas de un dominio objetivo. Realiza las siguientes acciones:

1. Ejecuta **paramspider** para obtener URLs relacionadas con el dominio objetivo.
2. Reemplaza la cadena "FUZZ" con "TRAVERSAL" en el archivo de resultados generado por `paramspider`.
3. Crea y ejecuta un script Bash que realiza ataques DotDotPwn en las URLs encontradas.
4. Guarda las URLs vulnerables con toda la carga útil en un archivo `lfi_vulns.txt`.

## Requisitos

### Librerías de Python

El script usa las siguientes librerías de Python (incluidas en la biblioteca estándar):

- `os`
- `subprocess`
- `sys`

### Herramientas Externas

Asegúrate de tener instaladas las siguientes herramientas:

- **paramspider**: Para recolectar URLs. [Instrucciones de instalación](https://github.com/devanshbatham/ParamSpider).
- **DotDotPwn**: Para realizar ataques de traversal. [DotDotPwn](https://www.kali.org/tools/dotdotpwn/).
- **sed**: Utilizado para reemplazar texto en los archivos. Viene preinstalado en sistemas Unix/Linux.
- **timeout**: Comando para limitar el tiempo de ejecución del ataque. Viene preinstalado en sistemas Unix/Linux.

## Uso

Ejecuta el script desde la terminal proporcionando el dominio objetivo como argumento:

```bash
python3 AutoPwnMaster.py <dominio>
