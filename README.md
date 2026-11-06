# <img src="https://media.tenor.com/GvP5WfH4AKgAAAAj/bee-minecraft.gif" width="50" style="vertical-align: middle;" alt="Abeja"> Ejercicio 3: Hilos con Lock - Depósito en Celda de Miel <img src="https://minecraft.wiki/images/Honey_Bottle_JE1_BE2.png?78afc" width="40" style="vertical-align: middle;" alt="Abeja">



## Descripción
Este proyecto demuestra el control de **condiciones de carrera (Race Conditions)** utilizando `threading.Lock()` en Python.

Tres abejas obreras intentan depositar miel simultáneamente (3, 4 y 2 unidades) en una celda compartida con capacidad máxima de **5 unidades** (`espacio_celda = 5`). El uso de `Lock` sincroniza el acceso para que solo una abeja verifique y deposite miel a la vez, evitando desbordamientos o saldos negativos.

## Requisitos
- Docker y Docker Compose instalados.

## Ejecución con Docker Compose

1. Clonar el repositorio y acceder al directorio:
   ```bash
   git clone https://github.com/talos0412/panal-ejercicio3-lock.git
   cd ejercicio3-lock
  
2. Iniciar el contenedor:
   ```
   docker compose up

3. Detener y eliminar el contenedor al finalizar:
   ```
   docker compose down

## Salida esperada en el contenedor:

```
Iniciando la deposición de miel en la celda...
Abeja Obrera #1 está intentando depositar 3 de miel en la celda.
Abeja Obrera #1 ha depositado 3 de miel. Espacio restante en la celda: 2.
Abeja Obrera #2 está intentando depositar 4 de miel en la celda.
Abeja Obrera #2 no puede depositar 4 de miel. Espacio insuficiente en la celda: 2.
Abeja Obrera #3 está intentando depositar 2 de miel en la celda.
Abeja Obrera #3 ha depositado 2 de miel. Espacio restante en la celda: 0.
Tiempo total de recolección: 3.00 segundos.
