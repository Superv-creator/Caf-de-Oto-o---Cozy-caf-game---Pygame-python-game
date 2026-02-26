import pygame
import os

pygame.init()
ANCHO, ALTO = 1000, 650

fuente_menu    = pygame.font.SysFont("Verdana", 16, bold=True)
fuente_stats   = pygame.font.SysFont("Verdana", 24, bold=True)
fuente_titulo  = pygame.font.SysFont("Verdana", 35, bold=True)
fuente_decora  = pygame.font.SysFont("Verdana", 26, bold=True)
fuente_cafe    = pygame.font.SysFont("Verdana", 28, bold=True)
fuente_moneda_txt = pygame.font.SysFont("Verdana", 20, bold=True)
fuente_final   = pygame.font.SysFont("Verdana", 45, bold=True)
fuente_opciones       = pygame.font.SysFont("Verdana", 20, bold=True)
fuente_opciones_titulo = pygame.font.SysFont("Verdana", 24, bold=True)
fuente_small   = pygame.font.SysFont("Verdana", 13, bold=True)

# Recursos del juego
dinero           = 0
hojas_doradas    = 0
ganancia_pasiva  = 0
pantalla_actual  = "CAFE"
timer_inauguracion = 0
inauguracion_mostrada = False
tiempo_jugado    = 0
record_match3 = 0
record_runner = 0
record_calabazas = 0
record_setas = 0
menu_opciones_abierto = False
musica_on  = True
sonido_on  = True
confirmando_reinicio = False
submenu_jardin_actual = 0
item_seleccionado_jardin = None
lista_mejoras_cafe = []
mejoras_especiales_compradas = []
tienda_jardin = []
elementos_jardin_colocados = []
animales_jardin = []
monedas = []
visitantes = []
confeti = []
textos_flotantes = []
SAVE_FILE = "savegame.json"

# Idioma activo: "es" | "en"
idioma = "es"

# Inventarios para objetos especiales
inventario_jardin = []
inventario_cielo  = []

# Objetos colocados en el cielo (café)
objetos_cielo_colocados = []

# Modo decoración cielo
modo_cielo = False
objeto_seleccionado_cielo = None


def format_esp(n):
    return f"{int(n):,}".replace(",", ".")


def format_tiempo(s):
    h = int(s) // 3600
    m = (int(s) % 3600) // 60
    ss = int(s) % 60
    return f"{h}h {m:02d}m {ss:02d}s" if h > 0 else f"{m}m {ss:02d}s"


def dibujar_hoja(sup, x, y, color=(180, 220, 80), escala=1.0):
    """Dibuja una hojita otoñal con pygame puro."""
    import math
    s = max(1, int(escala))
    surf = pygame.Surface((int(16 * escala), int(12 * escala)), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, color, (0, int(2 * escala), int(16 * escala), int(8 * escala)))
    sup.blit(surf, (x - int(8 * escala), y - int(6 * escala)))
    pygame.draw.line(sup, (min(255, color[0] - 40), min(255, color[1] - 40), 0),
                     (x - int(6 * escala), y), (x + int(6 * escala), y), max(1, s))
