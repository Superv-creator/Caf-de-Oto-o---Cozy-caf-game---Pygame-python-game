# sonido.py — Gestión centralizada de audio
import pygame
import os

# Rutas
_BASE = os.path.join(os.path.dirname(__file__), "assets", "sounds")

# Volúmenes predeterminados (0.0 – 1.0)
VOL_MUSICA  = 0.35
VOL_SFX     = 0.45   # efectos de sonido generales
VOL_COIN    = 0.40
VOL_BTN     = 0.30
VOL_KISS    = 0.40
VOL_JUMP    = 0.45
VOL_WIN     = 0.50
VOL_LOOSE   = 0.45

_musica_cargada = False
_sfx = {}   # cache de sonidos


def _ruta(nombre):
    return os.path.join(_BASE, nombre)


def init():
    """Inicializa el mixer. Llama esto UNA vez al arrancar (constantes.py ya llama pygame.init)."""
    if not pygame.mixer.get_init():
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)


# ── Música de fondo ──────────────────────────────────────────────────────────

def iniciar_musica():
    """Empieza la música de fondo en bucle si no está ya sonando."""
    global _musica_cargada
    try:
        ruta = _ruta("background.mp3")
        if not os.path.exists(ruta):
            return
        if not _musica_cargada or not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(VOL_MUSICA)
            pygame.mixer.music.play(-1)  # -1 = bucle infinito
            _musica_cargada = True
    except Exception:
        pass


def pausar_musica():
    try:
        pygame.mixer.music.pause()
    except Exception:
        pass


def reanudar_musica():
    try:
        pygame.mixer.music.unpause()
    except Exception:
        pass


def detener_musica():
    try:
        pygame.mixer.music.stop()
    except Exception:
        pass


def set_volumen_musica(activo: bool):
    try:
        pygame.mixer.music.set_volume(VOL_MUSICA if activo else 0.0)
    except Exception:
        pass


# ── Efectos de sonido ────────────────────────────────────────────────────────

def _cargar_sfx(nombre_archivo):
    """Carga y cachea un sonido. Devuelve None si no existe."""
    if nombre_archivo in _sfx:
        return _sfx[nombre_archivo]
    ruta = _ruta(nombre_archivo)
    if not os.path.exists(ruta):
        return None
    try:
        snd = pygame.mixer.Sound(ruta)
        _sfx[nombre_archivo] = snd
        return snd
    except Exception:
        return None


def _play(nombre_archivo, volumen):
    import constantes as c
    if not c.sonido_on:
        return
    snd = _cargar_sfx(nombre_archivo)
    if snd:
        snd.set_volume(volumen)
        snd.play()


# Funciones públicas para cada sonido

def play_coin():
    """Moneda recogida (pantalla café antes de inaugurar)."""
    _play("win_coin.wav", VOL_COIN)


def play_menu_button():
    """Clic en cualquier botón de menú."""
    _play("menu_button.wav", VOL_BTN)


def play_kiss():
    """Dos animales se besan en el banco del jardín."""
    _play("kiss.wav", VOL_KISS)


def play_jump():
    """Animal salta en la seta del jardín."""
    _play("jump.wav", VOL_JUMP)


def play_win():
    """Victoria en un minijuego."""
    _play("win.wav", VOL_WIN)


def play_loose():
    """Derrota en un minijuego."""
    _play("loose.wav", VOL_LOOSE)
