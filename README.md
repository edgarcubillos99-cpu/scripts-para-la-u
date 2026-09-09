# Scripts Casio FX-CG100 — Ingeniería civil

Colección de programas en Python para la calculadora **Casio FX-CG100**, pensados para cálculos de carrera: hidráulica, canales, estructuras y demás asignaturas.

Cada script pide los datos por consola, calcula y muestra el resultado en pantalla. El objetivo es tener en la calculadora las mismas herramientas que se usan en clase y en exámenes, sin depender de hojas de cálculo.

## Cómo usar los scripts

1. Copia el archivo `.py` a la calculadora (USB o software de transferencia de Casio).
2. En la FX-CG100 abre **Python** y ejecuta el script.
3. Elige la opción del menú (si la hay) e introduce los datos cuando se pidan.
4. Lee los resultados en pantalla. Las unidades coinciden con las del enunciado (SI: m, m³/s, etc.).

Notas:

- Usa punto decimal (`1.6`, no `1,6`).
- Si un dato no aplica a esa geometría, el script no lo pide.
- Los scripts son independientes: puedes llevar solo los que necesites.

## Organización

Los archivos se agrupan por tema, no por número de práctica. Así se pueden añadir scripts sin reestructurar el repositorio:

```text
scripts/
├── README.md
├── DISEÑO DE CANALES/
│   └── froude_casio.py
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
| Diseño de canales | [`froude_casio.py`](DISEÑO%20DE%20CANALES/froude_casio.py) | Número de Froude y régimen del flujo (subcrítico / crítico / supercrítico) para sección rectangular, trapezoidal, triangular o circular |

## Descripción de scripts

### `froude_casio.py` — Régimen de flujo (Froude)

Determina si el flujo en un canal es **subcrítico** (`Fr < 1`), **crítico** (`Fr = 1`) o **supercrítico** (`Fr > 1`).

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
