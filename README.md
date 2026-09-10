# Scripts Casio FX-CG100 — Ingeniería civil

Colección de programas en Python para la calculadora **Casio FX-CG100**, pensados para cálculos de carrera: hidráulica, canales, estructuras y demás asignaturas.

Cada script pide los datos por consola, calcula y muestra el resultado en pantalla. El objetivo es tener en la calculadora las mismas herramientas que se usan en clase y en exámenes, sin depender de hojas de cálculo.

## Cómo pasar un script a la calculadora

1. Conecta la FX-CG100 al PC por USB. En la pantalla de la calculadora elige el modo **USB Flash Drive** (memoria de almacenamiento); aparecerá como una unidad extraíble de unos 4,5 MB.
2. Copia el archivo `.py` **a la raíz** de esa unidad. La app Python solo lista los archivos de la raíz: si lo dejas dentro de una carpeta, no lo verás.

   En Linux, con la calculadora montada en `/media/$USER/disk`:

   ```bash
   cp "DISEÑO DE CANALES/froude.py" /media/$USER/disk/
   rm -rf /media/$USER/disk/.Trash-1000   # el gestor de archivos deja basura al borrar
   sync && gio mount -u /media/$USER/disk # expulsar de forma segura
   ```

3. Desconecta el USB y sal del modo memoria en la calculadora.
4. Abre el menú **Python**, sitúate sobre el archivo y pulsa `tools` --> `file` --> `open` para seleccionar el archivo y abrirlo, luego `tools` --> `Run` para ejecutarlo.
5. Introduce los datos cuando se pidan y lee los resultados en pantalla.

### Requisitos para que el script funcione en la calculadora

Estas cuatro reglas son la causa habitual de que un script "no se ejecute":

- **Solo ASCII.** Nada de tildes ni `ñ`, tampoco en los comentarios. El intérprete de Casio es MicroPython y falla al abrir archivos con caracteres acentuados. Escribe `Calculos`, `seccion`, `regimen`.
- **Nombre corto.** Máximo 8 caracteres antes del `.py`, sin espacios ni acentos (`froude.py`, no `froude_casio_v2.py`).
- **En la raíz** de la memoria de almacenamiento, nunca en subcarpetas.
- **Archivo guardado.** Comprueba que no pesa 0 bytes (`ls -l`); un buffer sin guardar en el editor copia un archivo vacío.

Otras notas de uso:

- Usa punto decimal (`1.6`, no `1,6`).
- Unidades del SI: m, m³/s, m/s. (se recomienda para que todos los scripts concuerden)
- Los scripts son independientes: puedes llevar solo los que necesites.

## Organización

Los archivos se agrupan por tema, no por número de práctica. Así se pueden añadir scripts sin reestructurar el repositorio:

```text
scripts/
├── README.md
├── DISEÑO DE CANALES/
│   └── froude.py
├── HIDRÁULICA/
│   └── (próximos)
└── ESTRUCTURAS/
    └── (próximos)
```

Para publicar uno nuevo:

1. Colócalo en la carpeta del tema (crea la carpeta si no existe).
2. Añade una fila en la tabla de [Catálogo](#catálogo).
3. Si hace falta, escribe un párrafo corto en [Descripción de scripts](#descripción-de-scripts).

Nombres de archivo en `snake_case`, en minúsculas, con extensión `.py`.

## Catálogo

| Tema | Script | Qué calcula |
|------|--------|-------------|
| Diseño de canales | [`froude.py`](DISEÑO%20DE%20CANALES/froude.py) | Número de Froude y régimen del flujo (subcrítico / crítico / supercrítico) para sección rectangular, trapezoidal, triangular o circular |

## Descripción de scripts

### `froude.py` — Régimen de flujo (Froude)

Determina si el flujo en un canal es **subcrítico** (`Fr < 1`), **crítico** (`Fr = 1`) o **supercrítico** (`Fr > 1`).

Los canales son tipicos, osea simetricos. No usar si por ejemplo el objetivo es un trapezoidal o triangular con dos pendientes(z) diferentes.

**Datos según la sección**

| Sección | Datos que pide |
|---------|----------------|
| Rectangular | Caudal `Q`, tirante `y`, ancho de solera `b` |
| Trapezoidal | `Q`, `y`, `b`, talud `z` (horizontal:vertical) |
| Triangular | `Q`, `y`, talud `z` |
| Circular | `Q`, `y`, diámetro `d0` |

**Salida:** área `A`, ancho superficial `T`, profundidad hidráulica `D = A/T`, velocidad `V = Q/A` y número de Froude `Fr = V / √(gD)` con `g = 9.81 m/s²`.

Si en sección circular el tirante supera el diámetro, avisa de flujo a presión y termina.

---

Al añadir el siguiente script, copia el formato de la fila del catálogo y, si el uso no es obvio, un apartado como el de arriba.
