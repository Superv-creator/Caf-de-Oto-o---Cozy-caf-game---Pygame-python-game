import pygame, sys, random, math
import constantes as c
import guardado as g
import ui
import sonido
from idiomas import t, nombres_mejoras, nombre_item_jardin, nombre_item_cafe_hoja
from cafe import Mejora, Moneda, dibujar_cafe
from jardin import ItemJardin, dibujar_item_jardin, actualizar_mariposas, dibujar_mariposas, cazar_mariposa
from animales import AnimalJardin, Visitante
from minijuegos.match3 import ejecutar_match3
from minijuegos.runner import ejecutar_runner
from minijuegos.calabazas import ejecutar_calabazas
from minijuegos.setas import ejecutar_setas
from minijuegos.defensa import ejecutar_defensa


def _dibujar_hoja_hud(sup, x, y, escala=1.4, color=(100, 220, 80)):
    s = escala
    pygame.draw.ellipse(sup, color,
                        (int(x - 8 * s), int(y - 5 * s), int(16 * s), int(10 * s)))
    pygame.draw.ellipse(sup, (min(255, color[0] + 40), min(255, color[1] - 20), 0),
                        (int(x - 6 * s), int(y - 3 * s), int(12 * s), int(6 * s)))
    pygame.draw.line(sup, (40, 120, 20),
                     (int(x - 7 * s), int(y)), (int(x + 7 * s), int(y)), 1)
    pygame.draw.line(sup, (100, 70, 30),
                     (int(x + 7 * s), int(y)), (int(x + 10 * s), int(y + 4 * s)), 1)


# ── Init ──────────────────────────────────────────────────────────────────────
sonido.init()

pantalla = pygame.display.set_mode((c.ANCHO, c.ALTO))
pygame.display.set_caption("Café Otoñal")
reloj = pygame.time.Clock()

# ── Mejoras café (nombres desde idiomas) ──────────────────────────────────────
def _crear_mejoras():
    noms = nombres_mejoras()
    return [
        Mejora(0, noms[0], 150,   2),
        Mejora(1, noms[1], 800,   8),
        Mejora(2, noms[2], 2500,  25),
        Mejora(3, noms[3], 12000, 80),
        Mejora(4, noms[4], 60000, 300),
    ]

c.lista_mejoras_cafe = _crear_mejoras()

# ── Tienda jardín ─────────────────────────────────────────────────────────────
c.tienda_jardin = [
    ItemJardin(0,  nombre_item_jardin("flor_roja"),     2500,   "flor_roja",    (255, 80, 80),    0),
    ItemJardin(1,  nombre_item_jardin("flor_azul"),     2500,   "flor_azul",    (80, 150, 255),   0),
    ItemJardin(2,  nombre_item_jardin("seta"),          4000,   "seta",         (200, 50, 50),    0),
    ItemJardin(3,  nombre_item_jardin("piedra"),        6000,   "piedra",       (150, 150, 150),  0),
    ItemJardin(4,  nombre_item_jardin("agua"),          15000,  "agua",         (60, 150, 200),   0),
    ItemJardin(5,  nombre_item_jardin("taburete"),      25000,  "taburete",     (160, 110, 60),   1),
    ItemJardin(6,  nombre_item_jardin("banco"),         45000,  "banco",        (101, 67, 33),    1),
    ItemJardin(7,  nombre_item_jardin("farola"),        65000,  "farola",       (40, 40, 40),     1),
    ItemJardin(8,  nombre_item_jardin("fuente"),        85000,  "fuente",       (100, 100, 100),  1),
    ItemJardin(9,  nombre_item_jardin("columpio"),      100000, "columpio",     (160, 80, 30),    2),
    ItemJardin(10, nombre_item_jardin("subebaja"),      120000, "subebaja",     (200, 100, 30),   2),
    ItemJardin(11, nombre_item_jardin("tobogan"),       150000, "tobogan",      (200, 60, 60),    2),
    ItemJardin(12, nombre_item_jardin("estanque_koi"),  200,    "estanque_koi", (60, 150, 200),   3, "hoja"),
    ItemJardin(13, nombre_item_jardin("hamaca"),        300,    "hamaca",       (160, 110, 60),   3, "hoja"),
    ItemJardin(14, nombre_item_jardin("manta_picnic"),  150,    "manta_picnic", (220, 80, 60),    3, "hoja"),
    ItemJardin(15, nombre_item_jardin("pozo_deseos"),   250,    "pozo_deseos",  (90, 78, 70),     3, "hoja"),
]

TIENDA_CAFE_HOJAS = [
    ItemJardin(20, nombre_item_cafe_hoja("chimenea"),       125, "chimenea",       (0, 0, 0), 0, "hoja"),
    ItemJardin(21, nombre_item_cafe_hoja("ventana_bosque"), 175, "ventana_bosque", (0, 0, 0), 0, "hoja"),
    ItemJardin(22, nombre_item_cafe_hoja("nube_redonda"),    60, "nube_redonda",   (0, 0, 0), 0, "hoja"),
    ItemJardin(23, nombre_item_cafe_hoja("nube_alargada"),   50, "nube_alargada",  (0, 0, 0), 0, "hoja"),
    ItemJardin(24, nombre_item_cafe_hoja("nube_corazon"),    80, "nube_corazon",   (0, 0, 0), 0, "hoja"),
    ItemJardin(25, nombre_item_cafe_hoja("nube_gatito"),     90, "nube_gatito",    (0, 0, 0), 0, "hoja"),
    ItemJardin(26, nombre_item_cafe_hoja("estrella_fugaz"), 120, "estrella_fugaz", (0, 0, 0), 0, "hoja"),
    ItemJardin(27, nombre_item_cafe_hoja("arcoiris"),       200, "arcoiris",       (0, 0, 0), 0, "hoja"),
    ItemJardin(28, nombre_item_cafe_hoja("estrella_deco"),   40, "estrella_deco",  (0, 0, 0), 0, "hoja"),
    ItemJardin(29, nombre_item_cafe_hoja("piedrecita_cafe"), 30, "piedrecita_cafe",(0, 0, 0), 0, "hoja"),
]
TIPOS_CIELO_LIBRE = {"nube_redonda","nube_alargada","nube_corazon","nube_gatito",
                     "estrella_fugaz","arcoiris","estrella_deco","piedrecita_cafe"}
TIPOS_CAFE_FIJOS  = {"chimenea","ventana_bosque"}

SUBMENU_NOMBRES_KEY = ["tab_deco","tab_mob","tab_juegos","tab_especial"]

hojas_fondo = [{'x': random.randint(0, 1000), 'y': random.randint(-650, 0),
                'vel': random.uniform(1, 2.5), 'off': random.uniform(0, 100)} for _ in range(25)]

g.cargar_partida()

# Actualizar nombres según idioma cargado del guardado
def _refrescar_nombres():
    noms = nombres_mejoras()
    for i, m in enumerate(c.lista_mejoras_cafe):
        m.noms = noms[i]
    for item in c.tienda_jardin:
        item.nombre = nombre_item_jardin(item.tipo)
    for item in TIENDA_CAFE_HOJAS:
        item.nombre = nombre_item_cafe_hoja(item.tipo)

_refrescar_nombres()

# Iniciar música de fondo (pantalla café)
sonido.iniciar_musica()
sonido.set_volumen_musica(c.musica_on)

ultimo_pago = ultimo_spawn = ultimo_v = ultimo_autoguard = ultimo_segundo = ultimo_animal_j = pygame.time.get_ticks()
gato_parpadeo_timer = random.randint(200, 450)
gato_parpadeo_dur = 0

# Botones menú principal
btn_decorar_cafe = pygame.Rect(40, 145, 320, 55)
btn_ir_jardin    = pygame.Rect(40, 210, 320, 55)
btn_minijuegos   = pygame.Rect(40, 275, 320, 55)

# Botones submenú minijuegos
btn_ir_match3    = pygame.Rect(40, 145, 320, 50)
btn_ir_runner    = pygame.Rect(40, 205, 320, 50)
btn_ir_calabazas = pygame.Rect(40, 265, 320, 50)
btn_ir_setas     = pygame.Rect(40, 325, 320, 50)
btn_ir_defensa   = pygame.Rect(40, 385, 320, 50)
btn_volver_mini  = pygame.Rect(40, c.ALTO - 65, 320, 45)

en_tienda_cafe = False
en_submenu_minijuegos = False
scroll_tienda_cafe = 0
item_cielo_seleccionado = None
scroll_jardin = 0

# ── Flag para detener música dentro de minijuegos / jardín ────────────────────
_musica_activa_zona = True   # True = pantalla café


def _actualizar_zona_musica(nueva_pantalla):
    """Pausa/reanuda música según la pantalla."""
    global _musica_activa_zona
    if nueva_pantalla == "CAFE":
        if not _musica_activa_zona:
            sonido.reanudar_musica()
            _musica_activa_zona = True
    else:
        if _musica_activa_zona:
            sonido.pausar_musica()
            _musica_activa_zona = False


def procesar_minijuego(fn):
    sonido.detener_musica()
    t_ini = pygame.time.get_ticks()
    fn(pantalla, reloj)
    t_fin = pygame.time.get_ticks()
    secs = (t_fin - t_ini) / 1000.0
    ganancia = int(secs * (c.ganancia_pasiva * 0.5))
    c.dinero += ganancia
    c.visitantes.clear()
    c.monedas.clear()
    if ganancia > 0:
        ui.crear_texto_flotante(500, 300,
            t("aprendiz_gano", c.format_esp(ganancia)), (255, 255, 200))
    # Retomar música si volvemos al café
    sonido.iniciar_musica()
    sonido.set_volumen_musica(c.musica_on)


# ── Bucle principal ───────────────────────────────────────────────────────────
while True:
    pantalla.fill((45, 25, 25))
    t_ms = pygame.time.get_ticks()

    inaugurado = all(m.es_max() for m in c.lista_mejoras_cafe)
    if inaugurado and c.timer_inauguracion == 0 and not c.menu_opciones_abierto:
        c.timer_inauguracion = t_ms
    celebrando = inaugurado and not c.inauguracion_mostrada and c.timer_inauguracion > 0
    if celebrando and t_ms - c.timer_inauguracion >= 5000:
        c.inauguracion_mostrada = True
        c.confeti.clear()

    for h in hojas_fondo:
        h['y'] += h['vel']
        h['x'] += math.sin(t_ms * 0.02 + h['off']) * 0.5
        if h['y'] > c.ALTO: h['y'] = -20
        pygame.draw.ellipse(pantalla, (180, 90, 40), (h['x'], h['y'], 12, 8))

    if not c.menu_opciones_abierto:
        if t_ms - ultimo_segundo >= 1000:
            c.tiempo_jugado += 1
            ultimo_segundo = t_ms
        if t_ms - ultimo_pago >= 1000:
            if not inaugurado: c.dinero += c.ganancia_pasiva
            ultimo_pago = t_ms
        if inaugurado: c.monedas.clear()
        else:
            if t_ms - ultimo_spawn >= 2500:
                c.monedas.append(Moneda())
                ultimo_spawn = t_ms
        if inaugurado and t_ms - ultimo_v >= 7500 and len(c.visitantes) < 5:
            c.visitantes.append(Visitante())
            ultimo_v = t_ms
        if c.pantalla_actual == "JARDIN" and t_ms - ultimo_animal_j >= 4000 and len(c.animales_jardin) < 10:
            c.animales_jardin.append(AnimalJardin())
            ultimo_animal_j = t_ms
        gato_parpadeo_timer -= 1
        if gato_parpadeo_timer <= 0:
            if gato_parpadeo_dur > 0:
                gato_parpadeo_dur -= 1
                if gato_parpadeo_dur <= 0:
                    gato_parpadeo_timer = random.randint(200, 500)
            else:
                gato_parpadeo_dur = random.randint(3, 6)
        if t_ms - ultimo_autoguard >= 30000:
            g.guardar_partida()
            ultimo_autoguard = t_ms

    items_submenu = [item for item in c.tienda_jardin if item.categoria == c.submenu_jardin_actual]
    for i, item in enumerate(items_submenu):
        item.rect = pygame.Rect(20, 135 + (i * 58) - scroll_jardin, 360, 50)

    for i, item in enumerate(TIENDA_CAFE_HOJAS):
        item.rect = pygame.Rect(20, 95 + (i * 54) - scroll_tienda_cafe, 360, 48)

    # ── Eventos ───────────────────────────────────────────────────────────────
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            g.guardar_partida()
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            if c.confirmando_reinicio:      c.confirmando_reinicio = False
            elif item_cielo_seleccionado:   item_cielo_seleccionado = None
            elif c.menu_opciones_abierto:   c.menu_opciones_abierto = False
            elif en_tienda_cafe:            en_tienda_cafe = False; item_cielo_seleccionado = None
            elif en_submenu_minijuegos:     en_submenu_minijuegos = False
            elif c.item_seleccionado_jardin is not None: c.item_seleccionado_jardin = None

        if e.type == pygame.MOUSEBUTTONDOWN:

            # ── Menú opciones ────────────────────────────────────────────────
            if c.menu_opciones_abierto:
                ventana_r = pygame.Rect(280, 100, 440, 470)
                if c.confirmando_reinicio:
                    r_si, r_no = ui.dibujar_confirmacion(pantalla)
                    if r_si.collidepoint(e.pos):
                        sonido.play_menu_button()
                        g.reiniciar_partida()
                        _refrescar_nombres()
                        c.menu_opciones_abierto = False
                        c.confirmando_reinicio = False
                        en_tienda_cafe = False
                        en_submenu_minijuegos = False
                    elif r_no.collidepoint(e.pos):
                        sonido.play_menu_button()
                        c.confirmando_reinicio = False
                else:
                    rects_m = ui.dibujar_menu_opciones(pantalla, t_ms)
                    if rects_m["musica"].collidepoint(e.pos):
                        sonido.play_menu_button()
                        c.musica_on = not c.musica_on
                        sonido.set_volumen_musica(c.musica_on)
                    elif rects_m["sonido"].collidepoint(e.pos):
                        sonido.play_menu_button()
                        c.sonido_on = not c.sonido_on
                    elif rects_m["idioma"].collidepoint(e.pos):
                        sonido.play_menu_button()
                        c.idioma = "en" if c.idioma == "es" else "es"
                        _refrescar_nombres()
                    elif rects_m["reiniciar"].collidepoint(e.pos):
                        sonido.play_menu_button()
                        c.confirmando_reinicio = True
                    elif rects_m["cerrar"].collidepoint(e.pos):
                        sonido.play_menu_button()
                        c.menu_opciones_abierto = False
                    elif not ventana_r.collidepoint(e.pos):
                        c.menu_opciones_abierto = False
                        c.confirmando_reinicio = False
                continue

            # Botón café (abre opciones)
            if e.button == 1 and ui.rect_boton_cafe.collidepoint(e.pos):
                sonido.play_menu_button()
                c.menu_opciones_abierto = True
                continue

            if e.button == 1:
                if c.pantalla_actual == "CAFE":

                    # Visitantes esperando
                    for v in c.visitantes:
                        if v.rect.collidepoint(e.pos) and v.estado == "ESPERANDO":
                            p = 5000 + c.ganancia_pasiva * 2
                            c.dinero += p
                            ui.crear_texto_flotante(v.x, v.y, f"+¥{c.format_esp(p)}", (255, 215, 0))
                            tiene_banco = c.lista_mejoras_cafe[2].nivel >= 4
                            banco_ocupado = any(
                                ov.estado in ("YENDO_BANCO","SENTADO")
                                for ov in c.visitantes if ov != v)
                            v.estado = "YENDO_BANCO" if (tiene_banco and not banco_ocupado) else "SALIENDO"

                    # ── Tienda decorar café ──────────────────────────────────
                    if en_tienda_cafe:
                        btn_volver = pygame.Rect(20, c.ALTO - 60, 160, 40)
                        if btn_volver.collidepoint(e.pos):
                            sonido.play_menu_button()
                            en_tienda_cafe = False
                            item_cielo_seleccionado = None
                            continue
                        if item_cielo_seleccionado and e.pos[0] > 400:
                            item_sel = next((x for x in TIENDA_CAFE_HOJAS if x.tipo == item_cielo_seleccionado), None)
                            if item_sel and c.hojas_doradas >= item_sel.precio:
                                c.hojas_doradas -= item_sel.precio
                                c.objetos_cielo_colocados.append(
                                    {'tipo': item_cielo_seleccionado, 'x': e.pos[0], 'y': e.pos[1]})
                                ui.crear_texto_flotante(e.pos[0], e.pos[1],
                                    f"-{item_sel.precio} {t('tab_especial') if False else ('hojas' if c.idioma=='es' else 'leaves')}",
                                    (255, 180, 80))
                            elif item_sel:
                                ui.crear_texto_flotante(e.pos[0], e.pos[1], t("pocas_hojas"), (255, 80, 80))
                            continue
                        for item in TIENDA_CAFE_HOJAS:
                            if item.rect.collidepoint(e.pos):
                                sonido.play_menu_button()
                                if item.tipo in TIPOS_CIELO_LIBRE:
                                    item_cielo_seleccionado = (
                                        item.tipo if item_cielo_seleccionado != item.tipo else None)
                                    if item_cielo_seleccionado:
                                        ui.crear_texto_flotante(200, 300, t("colocar_cafe"), (200, 255, 200))
                                else:
                                    ya = item.tipo in c.mejoras_especiales_compradas
                                    if ya:
                                        ui.crear_texto_flotante(200, 300, t("ya_instalado"), (200, 200, 255))
                                    elif c.hojas_doradas >= item.precio:
                                        c.hojas_doradas -= item.precio
                                        c.mejoras_especiales_compradas.append(item.tipo)
                                        ui.crear_texto_flotante(200, 300, t("instalado_cafe"), (100, 255, 100))
                                    else:
                                        ui.crear_texto_flotante(200, 300, t("pocas_hojas"), (255, 100, 100))
                                break
                        continue

                    # ── Submenú minijuegos ───────────────────────────────────
                    if en_submenu_minijuegos:
                        if btn_volver_mini.collidepoint(e.pos):
                            sonido.play_menu_button()
                            en_submenu_minijuegos = False
                            continue
                        if btn_ir_match3.collidepoint(e.pos):
                            sonido.play_menu_button()
                            procesar_minijuego(ejecutar_match3)
                            continue
                        if btn_ir_runner.collidepoint(e.pos):
                            sonido.play_menu_button()
                            procesar_minijuego(ejecutar_runner)
                            continue
                        if btn_ir_calabazas.collidepoint(e.pos):
                            sonido.play_menu_button()
                            sonido.detener_musica()
                            ejecutar_calabazas(pantalla, reloj)
                            c.visitantes.clear(); c.monedas.clear()
                            sonido.iniciar_musica()
                            sonido.set_volumen_musica(c.musica_on)
                            continue
                        if btn_ir_setas.collidepoint(e.pos):
                            sonido.play_menu_button()
                            sonido.detener_musica()
                            ejecutar_setas(pantalla, reloj)
                            c.visitantes.clear(); c.monedas.clear()
                            sonido.iniciar_musica()
                            sonido.set_volumen_musica(c.musica_on)
                            continue
                        if btn_ir_defensa.collidepoint(e.pos):
                            sonido.play_menu_button()
                            sonido.detener_musica()
                            hojas_ganadas = ejecutar_defensa(pantalla, reloj)
                            c.hojas_doradas += hojas_ganadas
                            c.visitantes.clear(); c.monedas.clear()
                            sonido.iniciar_musica()
                            sonido.set_volumen_musica(c.musica_on)
                            if hojas_ganadas > 0:
                                ui.crear_texto_flotante(500, 300,
                                    t("defensa_hojas", hojas_ganadas), (100, 255, 150))
                            continue
                        continue

                    # ── Mejoras café ─────────────────────────────────────────
                    for m in c.lista_mejoras_cafe:
                        if m.rect.collidepoint(e.pos) and c.dinero >= m.precio and not m.es_max():
                            sonido.play_menu_button()
                            c.dinero -= m.precio
                            m.nivel += 1
                            c.ganancia_pasiva += m.apt
                            m.precio = int(m.precio * 1.7)

                    # Monedas
                    for mnd in c.monedas[:]:
                        if mnd.rect.collidepoint(e.pos):
                            c.dinero += 500
                            c.monedas.remove(mnd)
                            sonido.play_coin()
                            ui.crear_texto_flotante(mnd.x, mnd.y, "+¥500", (255, 215, 0))

                    if inaugurado:
                        if btn_decorar_cafe.collidepoint(e.pos):
                            sonido.play_menu_button()
                            en_tienda_cafe = True
                        elif btn_ir_jardin.collidepoint(e.pos) or e.pos[0] > 940:
                            sonido.play_menu_button()
                            c.pantalla_actual = "JARDIN"
                            c.item_seleccionado_jardin = None
                            en_tienda_cafe = False
                            en_submenu_minijuegos = False
                            _actualizar_zona_musica("JARDIN")
                        elif btn_minijuegos.collidepoint(e.pos):
                            sonido.play_menu_button()
                            en_submenu_minijuegos = True

                    if not inaugurado and e.pos[0] > 400:
                        vc = 10 + sum(m.nivel for m in c.lista_mejoras_cafe) * 5
                        c.dinero += vc
                        ui.crear_texto_flotante(e.pos[0], e.pos[1],
                            f"+¥{c.format_esp(vc)}", (255, 255, 255))

                elif c.pantalla_actual == "JARDIN":
                    if 400 < e.pos[0] < 460 and 300 < e.pos[1] < 350:
                        c.pantalla_actual = "CAFE"
                        _actualizar_zona_musica("CAFE")
                    elif e.pos[0] <= 400:
                        btn_volver_j = pygame.Rect(20, c.ALTO - 60, 160, 40)
                        if btn_volver_j.collidepoint(e.pos):
                            sonido.play_menu_button()
                            c.pantalla_actual = "CAFE"
                            c.item_seleccionado_jardin = None
                            _actualizar_zona_musica("CAFE")
                            continue
                        tab_clicked = False
                        for ti in range(4):
                            tab_r = pygame.Rect(20 + ti * 95, 95, 85, 32)
                            if tab_r.collidepoint(e.pos):
                                sonido.play_menu_button()
                                c.submenu_jardin_actual = ti
                                c.item_seleccionado_jardin = None
                                scroll_jardin = 0
                                tab_clicked = True
                                break
                        if not tab_clicked:
                            c.item_seleccionado_jardin = None
                            for item in items_submenu:
                                if item.rect.collidepoint(e.pos):
                                    c.item_seleccionado_jardin = (
                                        None if c.item_seleccionado_jardin == item.id else item.id)
                                    break
                    elif e.pos[0] > 400 and c.item_seleccionado_jardin is not None:
                        ia = next((x for x in c.tienda_jardin if x.id == c.item_seleccionado_jardin), None)
                        if ia is None:
                            c.item_seleccionado_jardin = None
                            continue
                        puede = (c.dinero >= ia.precio if ia.moneda == "yen" else c.hojas_doradas >= ia.precio)
                        if puede:
                            if ia.moneda == "yen": c.dinero -= ia.precio
                            else:                  c.hojas_doradas -= ia.precio
                            c.elementos_jardin_colocados.append(
                                {'tipo': ia.tipo, 'x': e.pos[0], 'y': e.pos[1],
                                 'precio': ia.precio, 'color': ia.color})
                            sufijo = t("comprar_hojas", "").replace("{}", "").strip() if ia.moneda == "hoja" else ""
                            if ia.moneda == "hoja":
                                ui.crear_texto_flotante(e.pos[0], e.pos[1],
                                    f"-{c.format_esp(ia.precio)} {'Hojas' if c.idioma=='es' else 'Leaves'}",
                                    (255, 100, 100))
                            else:
                                ui.crear_texto_flotante(e.pos[0], e.pos[1],
                                    f"-¥{c.format_esp(ia.precio)}", (255, 100, 100))
                        else:
                            ui.crear_texto_flotante(e.pos[0], e.pos[1], t("sin_fondos"), (255, 50, 50))
                    elif e.pos[0] > 400 and c.item_seleccionado_jardin is None:
                        if cazar_mariposa(e.pos[0], e.pos[1]):
                            c.hojas_doradas += 1
                            ui.crear_texto_flotante(e.pos[0], e.pos[1] - 10, t("hoja_ganada"), (180, 240, 100))
                        else:
                            for aj in c.animales_jardin:
                                if math.hypot(aj.x - e.pos[0], aj.y - e.pos[1]) < 30:
                                    aj.tocar()
                                    for _ in range(3):
                                        ui.crear_texto_flotante(
                                            int(aj.x) + random.randint(-12, 12),
                                            int(aj.y) - random.randint(5, 20),
                                            "corazon", (255, random.randint(80, 180), 150))
                                    break

            elif e.button == 3:
                if c.pantalla_actual == "CAFE" and en_tienda_cafe and e.pos[0] > 400:
                    mejor = -1; mejor_dist = 55
                    for i, obj in enumerate(c.objetos_cielo_colocados):
                        d = math.hypot(obj['x'] - e.pos[0], obj['y'] - e.pos[1])
                        if d < mejor_dist: mejor_dist = d; mejor = i
                    if mejor >= 0:
                        obj = c.objetos_cielo_colocados.pop(mejor)
                        item_orig = next((x for x in TIENDA_CAFE_HOJAS if x.tipo == obj['tipo']), None)
                        if item_orig: c.hojas_doradas += item_orig.precio
                        ui.crear_texto_flotante(e.pos[0], e.pos[1],
                            t("devuelto_hojas", item_orig.precio if item_orig else 0), (100, 255, 200))
                    else:
                        item_cielo_seleccionado = None

                elif c.pantalla_actual == "JARDIN" and e.pos[0] > 400:
                    for i, obj in enumerate(reversed(c.elementos_jardin_colocados)):
                        if math.hypot(obj['x'] - e.pos[0], obj['y'] - e.pos[1]) <= 45:
                            item_original = next((x for x in c.tienda_jardin if x.tipo == obj['tipo']), None)
                            if item_original and item_original.precio == 0:
                                c.inventario_jardin.append(obj['tipo'])
                                c.elementos_jardin_colocados.pop(len(c.elementos_jardin_colocados) - 1 - i)
                                ui.crear_texto_flotante(e.pos[0], e.pos[1],
                                    t("guardado_inventario"), (100, 255, 255))
                                break
                            elif item_original:
                                if item_original.moneda == "hoja":
                                    c.hojas_doradas += item_original.precio
                                    ui.crear_texto_flotante(e.pos[0], e.pos[1],
                                        t("devuelto_hojas", item_original.precio), (100, 255, 100))
                                else:
                                    c.dinero += item_original.precio
                                    ui.crear_texto_flotante(e.pos[0], e.pos[1],
                                        t("devuelto_yen", c.format_esp(item_original.precio)), (100, 255, 100))
                                c.elementos_jardin_colocados.pop(len(c.elementos_jardin_colocados) - 1 - i)
                                break
                    else:
                        c.item_seleccionado_jardin = None

        if e.type == pygame.MOUSEWHEEL:
            mx_w, my_w = pygame.mouse.get_pos()
            if mx_w <= 400:
                if en_tienda_cafe:
                    scroll_tienda_cafe = max(0, min(
                        scroll_tienda_cafe - e.y * 30,
                        max(0, 95 + len(TIENDA_CAFE_HOJAS) * 54 - (c.ALTO - 70))))
                elif c.pantalla_actual == "JARDIN":
                    n_items = len([x for x in c.tienda_jardin if x.categoria == c.submenu_jardin_actual])
                    scroll_jardin = max(0, min(scroll_jardin - e.y * 30, max(0, n_items * 58 - 400)))

    # ── Sonido de beso en banco (jardín) ─────────────────────────────────────
    # Se detecta mirando partículas de corazón recién añadidas en animales
    for aj in c.animales_jardin:
        if aj.beso_timer == 10:   # recién activado este frame
            sonido.play_kiss()

    # ── Sonido de salto en seta ────────────────────────────────────────────
    for aj in c.animales_jardin:
        if aj.estado == "SALTANDO":
            import math as _math
            bote = abs(_math.sin(aj.salto_fase))
            if bote < 0.08:   # toca el suelo → sonido cada rebote
                if not getattr(aj, '_sonido_salto_lanzado', False):
                    sonido.play_jump()
                    aj._sonido_salto_lanzado = True
            else:
                aj._sonido_salto_lanzado = False

    # ── Dibujado de pantallas ─────────────────────────────────────────────────
    if c.pantalla_actual == "CAFE":
        dibujar_cafe(pantalla, t_ms, celebrando, gato_parpadeo_dur)

        # --- ESTE ES EL CÓDIGO AÑADIDO ---
        if not inaugurado:
            texto_ganancia = c.fuente_stats.render(
                f"{c.format_esp(c.ganancia_pasiva)} ¥/s",
                True,
                (255, 230, 150)
            )
            rect_ganancia = texto_ganancia.get_rect(bottomright=(c.ANCHO - 60, c.ALTO - 100))
            pantalla.blit(texto_ganancia, rect_ganancia)
        # --- FIN DEL CÓDIGO AÑADIDO ---

        # Objetos cielo colocados
        for obj in c.objetos_cielo_colocados:
            ox, oy = obj['x'], obj['y']
            if obj['tipo'] == "nube_redonda":
                drift = math.sin(t_ms * 0.0004 + ox * 0.01) * 6
                for dx2, dy2, r2 in [(-18,4,14),(0,0,18),(18,4,13),(-9,-8,12),(9,-7,11)]:
                    pygame.draw.circle(pantalla, (255,255,255),
                                       (int(ox+dx2+drift), int(oy+dy2)), r2)
            elif obj['tipo'] == "nube_alargada":
                drift = math.sin(t_ms * 0.0003 + ox * 0.008) * 4
                for dx2,dy2,rw,rh in [(-30,0,22,9),(0,-3,28,10),(30,2,20,8),(-15,5,16,7),(15,4,16,7)]:
                    pygame.draw.ellipse(pantalla, (250,250,255),
                                        (int(ox+dx2+drift-rw), int(oy+dy2-rh), rw*2, rh*2))
            elif obj['tipo'] == "nube_corazon":
                drift = math.sin(t_ms * 0.0005 + oy * 0.01) * 5
                pulse = 1.0 + math.sin(t_ms * 0.002) * 0.05
                r2 = int(16 * pulse)
                pygame.draw.circle(pantalla, (255,220,230), (int(ox-r2//2+drift), int(oy-2)), r2)
                pygame.draw.circle(pantalla, (255,220,230), (int(ox+r2//2+drift), int(oy-2)), r2)
                pygame.draw.polygon(pantalla, (255,220,230),
                    [(int(ox-r2+drift),int(oy+6)),(int(ox+r2+drift),int(oy+6)),(int(ox+drift),int(oy+r2+10))])
            elif obj['tipo'] == "nube_gatito":
                drift = math.sin(t_ms * 0.00035 + ox * 0.009) * 5
                for dx2,dy2,r2 in [(-15,3,13),(0,0,16),(15,3,12),(-7,-9,10),(7,-9,10)]:
                    pygame.draw.circle(pantalla, (255,255,255), (int(ox+dx2+drift), int(oy+dy2)), r2)
                for sx2 in [-1,1]:
                    pygame.draw.polygon(pantalla, (255,255,255),
                        [(int(ox+sx2*8+drift),int(oy-18)),(int(ox+sx2*18+drift),int(oy-18)),
                         (int(ox+sx2*13+drift),int(oy-30))])
                pygame.draw.circle(pantalla,(200,160,190),(int(ox-6+drift),int(oy-2)),3)
                pygame.draw.circle(pantalla,(200,160,190),(int(ox+6+drift),int(oy-2)),3)
                pygame.draw.circle(pantalla,(255,160,180),(int(ox+drift),int(oy+4)),2)
            elif obj['tipo'] == "estrella_fugaz":
                prog = (t_ms * 0.0008 + ox * 0.001) % 8
                ex = int(ox + 150 - prog * 45); ey = int(oy - prog * 18)
                for i in range(12):
                    alpha = int(255 * (1 - i/12))
                    ts = pygame.Surface((6,6), pygame.SRCALPHA)
                    pygame.draw.circle(ts,(255,255,180,alpha),(3,3),max(1,3-i//5))
                    pantalla.blit(ts,(ex+i*4, ey+i*2))
                pts_star = []
                for k in range(10):
                    ang = math.pi/2 + k * math.pi*2/10
                    r_k = 7 if k%2==0 else 3
                    pts_star.append((ex+math.cos(ang)*r_k, ey-math.sin(ang)*r_k))
                pygame.draw.polygon(pantalla,(255,255,220), pts_star)
                pygame.draw.polygon(pantalla,(255,255,255), pts_star, 1)
            elif obj['tipo'] == "arcoiris":
                colores_arco = [(255,50,50),(255,140,0),(255,230,0),(60,200,60),(50,150,255),(100,50,220),(200,50,180)]
                for i, col in enumerate(colores_arco):
                    radio = 55 + i*9
                    pygame.draw.arc(pantalla, col, (int(ox-radio),int(oy-radio//2),radio*2,radio), 0, math.pi, 5)
            elif obj['tipo'] == "estrella_deco":
                pulse = 1.0 + math.sin(t_ms * 0.003 + ox * 0.05) * 0.2
                r_e = int(12 * pulse)
                pts = []
                for k in range(10):
                    ang = math.pi/2 + k*math.pi*2/10
                    r_k = r_e if k%2==0 else r_e//2
                    pts.append((int(ox+math.cos(ang)*r_k), int(oy-math.sin(ang)*r_k)))
                pygame.draw.polygon(pantalla,(255,240,100), pts)
                pygame.draw.polygon(pantalla,(255,200,50), pts, 1)
            elif obj['tipo'] == "piedrecita_cafe":
                pygame.draw.ellipse(pantalla,(160,150,140),(int(ox-10),int(oy-6),20,12))
                pygame.draw.ellipse(pantalla,(140,130,120),(int(ox-8),int(oy-4),16,9))
                pygame.draw.ellipse(pantalla,(180,170,160),(int(ox-5),int(oy-5),8,5))

        # Preview objeto cielo al arrastrar
        if en_tienda_cafe and item_cielo_seleccionado:
            mx2, my2 = pygame.mouse.get_pos()
            if mx2 > 400:
                tp = item_cielo_seleccionado
                if tp == "nube_redonda":
                    for dx2,dy2,r2 in [(-18,4,14),(0,0,18),(18,4,13),(-9,-8,12),(9,-7,11)]:
                        pygame.draw.circle(pantalla,(200,200,200),(mx2+dx2,my2+dy2),r2)
                elif tp == "nube_alargada":
                    for dx2,dy2,rw,rh in [(-30,0,22,9),(0,-3,28,10),(30,2,20,8),(-15,5,16,7),(15,4,16,7)]:
                        pygame.draw.ellipse(pantalla,(200,200,210),(mx2+dx2-rw,my2+dy2-rh,rw*2,rh*2))
                elif tp == "nube_corazon":
                    r2 = 16
                    pygame.draw.circle(pantalla,(220,180,190),(mx2-r2//2,my2-2),r2)
                    pygame.draw.circle(pantalla,(220,180,190),(mx2+r2//2,my2-2),r2)
                    pygame.draw.polygon(pantalla,(220,180,190),[(mx2-r2,my2+6),(mx2+r2,my2+6),(mx2,my2+r2+10)])
                elif tp == "nube_gatito":
                    for dx2,dy2,r2 in [(-15,3,13),(0,0,16),(15,3,12),(-7,-9,10),(7,-9,10)]:
                        pygame.draw.circle(pantalla,(200,200,200),(mx2+dx2,my2+dy2),r2)
                    for sx2 in [-1,1]:
                        pygame.draw.polygon(pantalla,(200,200,200),
                            [(mx2+sx2*8,my2-18),(mx2+sx2*18,my2-18),(mx2+sx2*13,my2-30)])
                    pygame.draw.circle(pantalla,(180,140,170),(mx2-6,my2-2),3)
                    pygame.draw.circle(pantalla,(180,140,170),(mx2+6,my2-2),3)
                    pygame.draw.circle(pantalla,(230,140,160),(mx2,my2+4),2)
                elif tp == "estrella_fugaz":
                    for i in range(8):
                        pygame.draw.circle(pantalla,(220,220,150),(mx2+i*4,my2+i*2),max(1,3-i//4))
                    pts_p = []
                    for k in range(10):
                        ang = math.pi/2 + k*math.pi*2/10
                        r_k = 6 if k%2==0 else 3
                        pts_p.append((mx2+math.cos(ang)*r_k, my2-math.sin(ang)*r_k))
                    pygame.draw.polygon(pantalla,(255,255,200),pts_p)
                elif tp == "arcoiris":
                    for i,col in enumerate([(220,80,80),(220,160,60),(220,210,80),(80,180,80),(80,130,220),(120,80,200),(180,80,160)]):
                        radio = 30+i*5
                        pygame.draw.arc(pantalla,col,(mx2-radio,my2-radio//2,radio*2,radio),0,math.pi,3)
                elif tp == "estrella_deco":
                    pts=[]
                    for k in range(10):
                        ang=math.pi/2+k*math.pi*2/10
                        r_k=14 if k%2==0 else 7
                        pts.append((int(mx2+math.cos(ang)*r_k),int(my2-math.sin(ang)*r_k)))
                    pygame.draw.polygon(pantalla,(230,215,80),pts)
                elif tp == "piedrecita_cafe":
                    pygame.draw.ellipse(pantalla,(150,140,130),(mx2-10,my2-6,20,12))
                    pygame.draw.ellipse(pantalla,(170,160,150),(mx2-5,my2-5,8,5))

        if celebrando:
            txt4 = c.fuente_final.render(t("gran_inauguracion"), True, (255, 240, 0))
            pantalla.blit(txt4, txt4.get_rect(center=(700, 220)))
        if inaugurado:
            pygame.draw.polygon(pantalla, (255,255,255), [(950,300),(980,325),(950,350)])

    elif c.pantalla_actual == "JARDIN":
        pygame.draw.rect(pantalla, (34,139,34), (400, 0, 600, c.ALTO))
        for i in range(420, 1000, 50):
            for j in range(180, c.ALTO, 60):
                pygame.draw.line(pantalla,(25,110,25),(i,j),(i-5,j-10),2)
                pygame.draw.line(pantalla,(25,110,25),(i,j),(i+5,j-10),2)
        pygame.draw.rect(pantalla,(139,69,19),(400,120,600,10))
        pygame.draw.rect(pantalla,(139,69,19),(400,160,600,10))
        for i in range(410, 1000, 45):
            pygame.draw.rect(pantalla,(120,60,15),(i,100,15,90),border_radius=3)
        for tx,ty,r1,r2,r3,col1,col2 in [
                (450,40,50,40,40,(210,100,30),(230,120,40)),
                (880,20,60,50,50,(200,90,20),(220,110,35))]:
            pygame.draw.rect(pantalla,(100,65,30),(tx-5,ty,20,120))
            pygame.draw.circle(pantalla,col2,(tx+5,ty),r1)
            pygame.draw.circle(pantalla,col1,(tx-15,ty-20),r2)
            pygame.draw.circle(pantalla,col2,(tx+15,ty-10),r3)

        uso_obj = {}
        for aj in c.animales_jardin:
            if aj.estado in ("SENTADO","COLUMPIO","SUBEBAJA","TOBOGAN","FUENTE","PICNIC","DESEO") \
                    and aj.obj_target is not None:
                try:
                    idx2 = c.elementos_jardin_colocados.index(aj.obj_target)
                    ocups = uso_obj.setdefault(idx2, [])
                    tipo_obj = aj.obj_target.get('tipo','')
                    limite = 4 if tipo_obj=='manta_picnic' else (
                             1 if tipo_obj in('columpio','hamaca','tobogan','pozo_deseos') else 2)
                    if len(ocups) < limite:
                        if tipo_obj == 'pozo_deseos': ocups.append((aj.tipo, aj.deseo, aj.coin_t))
                        else:                          ocups.append(aj.tipo)
                except ValueError:
                    pass

        TIPOS_SUELO = {'agua','estanque_koi','piedra','manta_picnic'}
        for idx2, obj in enumerate(c.elementos_jardin_colocados):
            if obj['tipo'] in TIPOS_SUELO:
                ocup = uso_obj.get(idx2, [])
                dibujar_item_jardin(pantalla, obj['tipo'], obj['x'], obj['y'],
                                    obj['color'], 1.0, t_ms, ocup)

        objetos_altos = [o for o in enumerate(c.elementos_jardin_colocados) if o[1]['tipo'] not in TIPOS_SUELO]
        objetos_ord   = sorted(objetos_altos, key=lambda x: x[1]['y'])
        animales_ord  = sorted(c.animales_jardin, key=lambda a: a.y)

        obj_it = iter(objetos_ord); anim_it = iter(animales_ord)
        obj_cur = next(obj_it, None); anim_cur = next(anim_it, None)
        while obj_cur is not None or anim_cur is not None:
            obj_y  = obj_cur[1]['y']  if obj_cur  else float('inf')
            anim_y = anim_cur.y       if anim_cur else float('inf')
            if obj_y <= anim_y:
                idx2, obj = obj_cur
                ocup = uso_obj.get(idx2, [])
                dibujar_item_jardin(pantalla, obj['tipo'], obj['x'], obj['y'],
                                    obj['color'], 1.0, t_ms, ocup)
                obj_cur = next(obj_it, None)
            else:
                if not c.menu_opciones_abierto:
                    anim_cur.actualizar(c.elementos_jardin_colocados, c.animales_jardin)
                anim_cur.dibujar(pantalla, t_ms)
                anim_cur = next(anim_it, None)

        actualizar_mariposas(t_ms)
        dibujar_mariposas(pantalla, t_ms)
        pygame.draw.polygon(pantalla, (255,255,255), [(450,300),(420,325),(450,350)])

        mx2, my2 = pygame.mouse.get_pos()
        if mx2 > 400 and c.item_seleccionado_jardin is not None:
            it = next((x for x in c.tienda_jardin if x.id == c.item_seleccionado_jardin), None)
            if it:
                dibujar_item_jardin(pantalla, it.tipo, mx2, my2, it.color, 1.0, t_ms)

    # ── Visitantes ────────────────────────────────────────────────────────────
    for v in c.visitantes[:]:
        if v.actualizar():
            c.visitantes.remove(v)
        elif c.pantalla_actual == "CAFE":
            v.dibujar(pantalla, t_ms)

    if c.pantalla_actual == "CAFE" and not inaugurado:
        for mnd in c.monedas:
            mnd.actualizar()
            mnd.dibujar(pantalla)

    if celebrando:
        if len(c.confeti) < 60:
            c.confeti.append([random.randint(400, 1000), random.randint(-100, 0),
                               random.choice([(255,0,0),(0,255,0),(0,0,255)]),
                               random.uniform(2, 6)])
        for conf in c.confeti:
            conf[1] += conf[3]
            pygame.draw.rect(pantalla, conf[2], (conf[0], conf[1], 7, 7))
            if conf[1] > c.ALTO: conf[1] = -10

    pygame.draw.rect(pantalla, (30, 15, 15), (0, 0, 400, c.ALTO))

    # ── Panel izquierdo ───────────────────────────────────────────────────────
    if inaugurado and c.pantalla_actual == "CAFE":
        if en_tienda_cafe:
            t_tit = c.fuente_decora.render(t("decorar_titulo"), True, (100, 255, 100))
            tx_tit = 200 - t_tit.get_width() // 2
            pantalla.blit(t_tit, (tx_tit, 20))
            _dibujar_hoja_hud(pantalla, tx_tit - 16, 32, 1.2)
            t_hojas_disp = c.fuente_menu.render(
                t("hojas_disp", c.format_esp(c.hojas_doradas)), True, (100, 255, 100))
            pantalla.blit(t_hojas_disp, (200 - t_hojas_disp.get_width() // 2, 52))
            if item_cielo_seleccionado:
                inst = c.fuente_small.render(t("cancelar_esc"), True, (255, 255, 150))
                pantalla.blit(inst, (200 - inst.get_width() // 2, 72))
            area_lista = pygame.Rect(0, 90, 400, c.ALTO - 70)
            clip_ant = pantalla.get_clip()
            pantalla.set_clip(area_lista)
            mouse = pygame.mouse.get_pos()
            for item in TIENDA_CAFE_HOJAS:
                if item.rect.bottom < 90 or item.rect.top > c.ALTO - 70: continue
                ya_comprado = item.tipo in c.mejoras_especiales_compradas
                es_sel = (item_cielo_seleccionado == item.tipo)
                if es_sel:                                          cf = (20, 80, 100)
                elif ya_comprado and item.tipo in TIPOS_CAFE_FIJOS: cf = (40, 80, 40)
                elif item.rect.collidepoint(mouse):                 cf = (85, 60, 60)
                else:                                               cf = (60, 45, 45)
                pygame.draw.rect(pantalla, cf, item.rect, border_radius=10)
                bord = ((100,220,255) if es_sel else
                        ((100,255,100) if (ya_comprado and item.tipo in TIPOS_CAFE_FIJOS)
                         else (180,140,140)))
                pygame.draw.rect(pantalla, bord, item.rect, 2, border_radius=10)
                nombre_t = c.fuente_menu.render(item.nombre, True, (255,255,255))
                pantalla.blit(nombre_t, (item.rect.x+12, item.rect.y+6))
                if item.tipo in TIPOS_CAFE_FIJOS:
                    if ya_comprado:
                        t_comp = c.fuente_small.render(t("instalado"), True, (100,255,100))
                        pantalla.blit(t_comp, (item.rect.x+12, item.rect.y+28))
                    else:
                        pcol = (100,255,100) if c.hojas_doradas >= item.precio else (200,80,80)
                        pantalla.blit(c.fuente_menu.render(
                            t("precio_hojas_fijo", item.precio), True, pcol),
                            (item.rect.x+12, item.rect.y+26))
                else:
                    pcol = (100,255,100) if c.hojas_doradas >= item.precio else (200,80,80)
                    if es_sel:
                        pantalla.blit(c.fuente_small.render(
                            t("clic_cafe", item.precio), True, (100,220,255)),
                            (item.rect.x+12, item.rect.y+28))
                    else:
                        pantalla.blit(c.fuente_menu.render(
                            t("precio_hojas_cu", item.precio), True, pcol),
                            (item.rect.x+12, item.rect.y+26))
            pantalla.set_clip(clip_ant)
            total_h = len(TIENDA_CAFE_HOJAS) * 54
            if total_h > area_lista.height:
                bh = max(30, int(area_lista.height ** 2 // total_h))
                by2 = int(area_lista.y + scroll_tienda_cafe /
                          max(1, total_h - area_lista.height) * (area_lista.height - bh))
                pygame.draw.rect(pantalla,(80,80,60),(395,by2,5,bh),border_radius=3)
            btn_volver = pygame.Rect(20, c.ALTO-60, 160, 40)
            pygame.draw.rect(pantalla,(80,50,30),btn_volver,border_radius=10)
            pygame.draw.rect(pantalla,(140,100,60),btn_volver,2,border_radius=10)
            t_v = c.fuente_menu.render(t("volver"), True, (255,255,255))
            pantalla.blit(t_v,(btn_volver.centerx-t_v.get_width()//2,
                               btn_volver.centery-t_v.get_height()//2))

        elif en_submenu_minijuegos:
            t_tit = c.fuente_decora.render(t("mini_titulo"), True, (255,200,80))
            pantalla.blit(t_tit,(200-t_tit.get_width()//2,20))
            t_sub = c.fuente_small.render(t("mini_subtitulo"), True, (200,180,120))
            pantalla.blit(t_sub,(200-t_sub.get_width()//2,55))
            mp = pygame.mouse.get_pos()
            mini_btns = [
                (btn_ir_match3,    t("match3_nombre"),    t("match3_sub")),
                (btn_ir_runner,    t("runner_nombre"),    t("runner_sub")),
                (btn_ir_calabazas, t("calabazas_nombre"), t("calabazas_sub")),
                (btn_ir_setas,     t("setas_nombre"),     t("setas_sub")),
                (btn_ir_defensa,   t("defensa_nombre"),   t("defensa_sub")),
            ]
            for btn, txt, subt in mini_btns:
                hc = (80,100,140) if btn.collidepoint(mp) else (55,70,105)
                pygame.draw.rect(pantalla,hc,btn,border_radius=12)
                pygame.draw.rect(pantalla,(120,160,220),btn,2,border_radius=12)
                t_n = c.fuente_menu.render(txt,True,(255,255,255))
                pantalla.blit(t_n,(btn.centerx-t_n.get_width()//2,btn.y+7))
                t_s = c.fuente_small.render(subt,True,(180,210,255))
                pantalla.blit(t_s,(btn.centerx-t_s.get_width()//2,btn.y+27))
            hc = (90,60,40) if btn_volver_mini.collidepoint(mp) else (70,45,30)
            pygame.draw.rect(pantalla,hc,btn_volver_mini,border_radius=12)
            pygame.draw.rect(pantalla,(160,120,70),btn_volver_mini,2,border_radius=12)
            t_v = c.fuente_menu.render(t("volver"),True,(255,255,255))
            pantalla.blit(t_v,(btn_volver_mini.centerx-t_v.get_width()//2,
                               btn_volver_mini.centery-t_v.get_height()//2))

        else:
            t2b = c.fuente_cafe.render(t("cafe_completado"), True, (255,215,0))
            pantalla.blit(t2b,(200-t2b.get_width()//2,85))
            mp = pygame.mouse.get_pos()
            menu_btns = [
                (btn_decorar_cafe, t("decorar_cafe"), t("decorar_sub")),
                (btn_ir_jardin,    t("ir_jardin"),    t("jardin_sub")),
                (btn_minijuegos,   t("minijuegos"),   t("mini_sub")),
            ]
            for btn, txt, subt in menu_btns:
                hc = (80,120,80) if btn.collidepoint(mp) else (60,100,60)
                pygame.draw.rect(pantalla,hc,btn,border_radius=15)
                pygame.draw.rect(pantalla,(100,200,100),btn,3,border_radius=15)
                t_n = c.fuente_menu.render(txt,True,(255,255,255))
                pantalla.blit(t_n,(btn.centerx-t_n.get_width()//2,btn.y+9))
                t_s = c.fuente_small.render(subt,True,(200,255,200))
                pantalla.blit(t_s,(btn.centerx-t_s.get_width()//2,btn.y+30))

    elif c.pantalla_actual == "CAFE":
        pantalla.blit(c.fuente_titulo.render(t("tienda_titulo"), True, (255,255,255)), (40,55))
        for m in c.lista_mejoras_cafe:
            m.dibujar(pantalla)

    elif c.pantalla_actual == "JARDIN":
        pantalla.blit(c.fuente_decora.render(t("jardin_titulo"), True, (255,255,255)), (40,55))
        tab_names = [t("tab_deco"), t("tab_mob"), t("tab_juegos"), t("tab_especial")]
        for ti, tnombre in enumerate(tab_names):
            tab_r = pygame.Rect(20+ti*95, 95, 85, 32)
            activo = (ti == c.submenu_jardin_actual)
            pygame.draw.rect(pantalla,(100,140,80) if activo else (60,80,60),tab_r,border_radius=8)
            tlab = c.fuente_small.render(tnombre, True, (255,255,255))
            pantalla.blit(tlab,(tab_r.centerx-tlab.get_width()//2, tab_r.centery-6))
        area_j = pygame.Rect(0, 133, 400, c.ALTO-68)
        clip_ant_j = pantalla.get_clip()
        pantalla.set_clip(area_j)
        for item in items_submenu:
            if item.rect.bottom < 133 or item.rect.top > c.ALTO-68: continue
            mouse = pygame.mouse.get_pos()
            cf = (60,100,60) if c.item_seleccionado_jardin==item.id else (60,45,45)
            if item.rect.collidepoint(mouse) and c.item_seleccionado_jardin!=item.id: cf=(85,60,60)
            pygame.draw.rect(pantalla,cf,item.rect,border_radius=10)
            pygame.draw.rect(pantalla,
                (180,140,140) if c.item_seleccionado_jardin!=item.id else (150,255,150),
                item.rect,2,border_radius=10)
            clip_ant2 = pantalla.get_clip()
            pantalla.set_clip(item.rect)
            dibujar_item_jardin(pantalla,item.tipo,item.rect.x+32,item.rect.y+25,item.color,0.4,t_ms)
            pantalla.set_clip(clip_ant2)
            pantalla.blit(c.fuente_menu.render(item.nombre,True,(255,255,255)),
                          (item.rect.x+72,item.rect.y+8))
            txt_p = t("comprar_yen",c.format_esp(item.precio)) if item.moneda=="yen" \
                    else t("comprar_hojas",c.format_esp(item.precio))
            pantalla.blit(c.fuente_menu.render(txt_p,True,(255,215,0)),
                          (item.rect.x+72,item.rect.y+26))
        pantalla.set_clip(clip_ant_j)
        total_j = len(items_submenu) * 58
        if total_j > area_j.height:
            bh = max(30,int(area_j.height**2//total_j))
            by2 = int(area_j.y+scroll_jardin/max(1,total_j-area_j.height)*(area_j.height-bh))
            pygame.draw.rect(pantalla,(80,80,60),(395,by2,5,bh),border_radius=3)
        btn_volver_j = pygame.Rect(20, c.ALTO-60, 160, 40)
        pygame.draw.rect(pantalla,(80,50,30),btn_volver_j,border_radius=10)
        pygame.draw.rect(pantalla,(140,100,60),btn_volver_j,2,border_radius=10)
        t_vj = c.fuente_menu.render(t("volver"),True,(255,255,255))
        pantalla.blit(t_vj,(btn_volver_j.centerx-t_vj.get_width()//2,
                            btn_volver_j.centery-t_vj.get_height()//2))

    # ── HUD global ────────────────────────────────────────────────────────────
    ui.dibujar_boton_cafe(pantalla, t_ms)
    pantalla.blit(c.fuente_stats.render(f"¥ {c.format_esp(c.dinero)}", True, (255,215,0)), (430,40))
    pantalla.blit(c.fuente_stats.render(f" {c.format_esp(c.hojas_doradas)}", True, (100,255,100)), (780,40))
    _dibujar_hoja_hud(pantalla, 768, 52)

    # Textos flotantes
    for tf in c.textos_flotantes[:]:
        tf['y'] -= 2
        tf['vida'] -= 5
        if tf['vida'] <= 0:
            c.textos_flotantes.remove(tf)
        else:
            if tf['texto'] == "corazon":
                hx, hy = int(tf['x']), int(tf['y'])
                hs = pygame.Surface((18,16),pygame.SRCALPHA)
                col_h = (*tf['color'],tf['vida'])
                pygame.draw.circle(hs,col_h,(5,5),5)
                pygame.draw.circle(hs,col_h,(13,5),5)
                pygame.draw.polygon(hs,col_h,[(0,7),(9,16),(18,7)])
                pantalla.blit(hs,(hx-9,hy-8))
            else:
                img = c.fuente_moneda_txt.render(tf['texto'], True, tf['color'])
                img.set_alpha(tf['vida'])
                pantalla.blit(img,(tf['x'],tf['y']))

    # Menú opciones encima de todo
    if c.menu_opciones_abierto:
        ui.dibujar_menu_opciones(pantalla, t_ms)
        if c.confirmando_reinicio:
            ui.dibujar_confirmacion(pantalla)

    pygame.display.flip()
    reloj.tick(60)