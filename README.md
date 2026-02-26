# Cafe de-Otono---Cozy-cafe-game---Pygame-python-game
 Acogedor juego idle clicker, decoración y minijuegos, hecho con Pygame/python (IA 100%). Cozy café game - clicker, decor and mini-games  - Pygame/python game (AI100%) - 
🍂 Café Otoñal
Un juego de gestión de café con jardín, animales y minijuegos, hecho completamente con pygame y gráficos 100% en código (sin imágenes externas). 100% codificado por las IAS bajo mi dirección. 
📁 Estructura del proyecto
cafe_otonal/
├── main.py              # Bucle principal del juego
├── constantes.py        # Variables globales, fuentes, configuración
├── guardado.py          # Guardar / cargar / reiniciar partida (JSON)
├── cafe.py              # Dibujo y lógica del café
├── jardin.py            # Items del jardín, mariposas
├── animales.py          # Animales del jardín y visitantes del café
├── ui.py                # Menú de opciones, botones, textos flotantes
├── idiomas.py           # Sistema de traducción ES / EN
├── sonido.py            # Gestión centralizada de audio
│
├── minijuegos/
│   ├── match3.py        # Minijuego Match-3
│   ├── runner.py        # Minijuego Runner
│   ├── calabazas.py     # Minijuego Tiro de Calabazas
│   ├── setas.py         # Minijuego Colecta de Setas
│   ├── defensa.py       # Minijuego Torre de Defensa
│   └── pesca.py         # Minijuego Pesca (extra)
│
├── assets/
│   └── sounds/
│       ├── background.mp3   # Música de fondo (café principal)
│       ├── win_coin.wav     # Recoger moneda dorada
│       ├── menu_button.wav  # Clic en botones de menú
│       ├── kiss.wav         # Animales besándose en el banco
│       ├── jump.wav         # Animal saltando en la seta
│       ├── win.wav          # Victoria en minijuego
│       └── loose.wav        # Derrota en minijuego
│
└── savegame.json        # Partida guardada (se genera automáticamente)

🚀 Requisitos e instalación
pip install pygame

Python 3.8+ recomendado.
▶️ Cómo jugar
python main.py

🎮 Controles
Acción	Control
Comprar / interactuar	Clic izquierdo
Devolver objeto al inventario	Clic derecho
Abrir menú de opciones	Botón de la taza (esquina superior izquierda)
Cerrar / cancelar	Esc
Scroll en tiendas	Rueda del ratón
Saltar (Runner)	Espacio / Flecha arriba

🌐 Idiomas
El juego soporta español e inglés. Cambia el idioma en el menú de opciones (botón de la taza ☕). La preferencia se guarda automáticamente.
Para añadir un nuevo idioma edita idiomas.py y añade una nueva clave (ej. "fr") con todas las traducciones.
🔊 Audio
Los sonidos se cargan desde assets/sounds/. Si falta algún archivo simplemente no sonará ese efecto (el juego sigue funcionando). Volúmenes ajustables en sonido.py.
💾 Guardado
La partida se guarda automáticamente cada 30 segundos en savegame.json. También se guarda al cerrar la ventana.
🌱 Progresión
1.	Café — Mejora el stand comprando 5 líneas de mejoras con yenes (¥)
2.	Inauguración — Al completar todas las mejoras se celebra la gran inauguración
3.	Jardín — Decora con flores, mobiliario y juegos usando yenes y hojas doradas (🍃)
4.	Minijuegos — Gana hojas doradas en Match-3, Runner, Defensa, Setas y Calabazas
5.	Decoración especial — Usa hojas para añadir chimenea, nubes, arcoíris y más al café
6.	
📝 Licencia
Proyecto personal / libre. Sin assets externos: todo el arte es código pygame puro.







