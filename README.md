# AutoPwnMaster

## Descripción

`AutoPwnMaster.py` es un script automatizado para realizar ataques DotDotPwn en URLs obtenidas de un dominio objetivo. El script realiza las siguientes acciones:

1. Ejecuta `paramspider` para obtener URLs relacionadas con el dominio objetivo.
2. Reemplaza la cadena "FUZZ" con "TRAVERSAL" en el archivo de resultados generado por `paramspider`.
3. Crea y ejecuta un script Bash que realiza ataques DotDotPwn en las URLs encontradas.

## Requisitos

### Librerías de Python

El script utiliza las siguientes librerías de Python que son parte de la biblioteca estándar:

- `os`
- `subprocess`
- `sys`

No se requiere instalar librerías adicionales de Python.

### Herramientas Externas

Para que el script funcione correctamente, asegúrate de tener instaladas las siguientes herramientas en tu sistema:

- **paramspider**: Utilizado para recolectar URLs. Puedes instalarlo siguiendo las instrucciones en su [repositorio oficial](https://github.com/devanshbatham/ParamSpider).

- **sed**: Utilizado para reemplazar texto en el archivo de resultados. Normalmente está disponible en sistemas Unix/Linux.

- **DotDotPwn**: Herramienta para realizar ataques de traversing. https://www.kali.org/tools/dotdotpwn/

- **timeout**: Comando para limitar el tiempo de ejecución del ataque. Normalmente está disponible en sistemas Unix/Linux.

## Uso

Ejecuta el script desde la línea de comandos proporcionando el dominio objetivo como argumento:

```bash
python3 AutoPwnMaster.py <dominio>
