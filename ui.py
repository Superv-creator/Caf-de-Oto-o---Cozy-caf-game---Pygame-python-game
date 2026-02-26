import pygame, math, constantes as c
from idiomas import t
import sonido

def crear_texto_flotante(x, y, texto, color):
    c.textos_flotantes.append({'x': x, 'y': y, 'texto': texto, 'vida': 255, 'color': color})

rect_boton_cafe = pygame.Rect(10, 5, 44, 44)


def dibujar_boton_cafe(sup, t_ms):
    pygame.draw.rect(sup, (60, 35, 15), rect_boton_cafe, border_radius=8)
    pygame.draw.rect(sup, (120, 80, 40), rect_boton_cafe, 2, border_radius=8)
    cx = rect_boton_cafe.centerx
    cy = rect_boton_cafe.centery + 4
    pygame.draw.ellipse(sup, (160, 110, 60), (cx - 11, cy + 6, 22, 7))
    pygame.draw.rect(sup, (220, 200, 180), (cx - 8, cy - 5, 16, 12), border_radius=3)
    pygame.draw.ellipse(sup, (100, 70, 40), (cx - 6, cy - 3, 12, 7))
    pygame.draw.arc(sup, (180, 140, 80), (cx + 6, cy - 3, 7, 9), -math.pi / 2, math.pi / 2, 2)
    for i, vxo in enumerate([-2, 0, 2]):
        fase = t_ms * 0.005 + i * 1.1
        alpha = max(0, int(150 - (t_ms * 2 + i * 70) % 150))
        vs = pygame.Surface((4, 8), pygame.SRCALPHA)
        pygame.draw.line(vs, (220, 220, 220, alpha), (2, 8), (2 + int(math.sin(fase) * 1.5), 0), 1)
        sup.blit(vs, (cx + vxo - 2, cy - 13 + int(math.sin(fase) * 1.5)))


def dibujar_menu_opciones(sup, t_ms):
    overlay = pygame.Surface((c.ANCHO, c.ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 140))
    sup.blit(overlay, (0, 0))

    ventana = pygame.Rect(280, 100, 440, 470)
    pygame.draw.rect(sup, (50, 30, 20), ventana, border_radius=15)
    pygame.draw.rect(sup, (120, 80, 40), ventana, 3, border_radius=15)

    titulo = c.fuente_opciones_titulo.render(t("titulo_juego"), True, (255, 220, 100))
    sup.blit(titulo, (ventana.centerx - titulo.get_width() // 2, ventana.y + 20))

    on_str  = t("on")
    off_str = t("off")

    ttiempo = c.fuente_small.render(
        t("tiempo_jugado", c.format_tiempo(c.tiempo_jugado)), True, (200, 180, 140))
    sup.blit(ttiempo, (ventana.centerx - ttiempo.get_width() // 2, ventana.y + 55))

    # Texto del botón idioma
    idioma_label = t("idioma")   # "Idioma: Español" / "Language: English"

    rects = {}
    botones = [
        ("musica",   t("musica",  on_str if c.musica_on  else off_str), pygame.Rect(350, 190, 300, 50)),
        ("sonido",   t("sonido",  on_str if c.sonido_on  else off_str), pygame.Rect(350, 255, 300, 50)),
        ("idioma",   idioma_label,                                       pygame.Rect(350, 320, 300, 50)),
        ("reiniciar",t("reiniciar"),                                     pygame.Rect(350, 385, 300, 50)),
        ("cerrar",   t("cerrar"),                                        pygame.Rect(350, 455, 300, 40)),
    ]
    for key, texto, r in botones:
        rects[key] = r
        if key == "cerrar":
            col = (60, 80, 60)
        elif key == "idioma":
            col = (40, 60, 90)
        else:
            col = (100, 60, 40)
        pygame.draw.rect(sup, col, r, border_radius=10)
        pygame.draw.rect(sup, (150, 100, 60), r, 2, border_radius=10)
        t2 = c.fuente_opciones.render(texto, True, (255, 255, 255))
        sup.blit(t2, (r.centerx - t2.get_width() // 2, r.centery - t2.get_height() // 2))

    return rects


def dibujar_confirmacion(sup):
    overlay = pygame.Surface((c.ANCHO, c.ALTO), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 100))
    sup.blit(overlay, (0, 0))

    ventana = pygame.Rect(300, 220, 400, 200)
    pygame.draw.rect(sup, (60, 30, 20), ventana, border_radius=15)
    pygame.draw.rect(sup, (200, 80, 80), ventana, 3, border_radius=15)

    t1 = c.fuente_opciones_titulo.render(t("confirmar_titulo"), True, (255, 100, 100))
    t2 = c.fuente_small.render(t("confirmar_texto"), True, (200, 140, 140))
    sup.blit(t1, (ventana.centerx - t1.get_width() // 2, ventana.y + 20))
    sup.blit(t2, (ventana.centerx - t2.get_width() // 2, ventana.y + 60))

    r_si = pygame.Rect(350, 340, 140, 50)
    r_no = pygame.Rect(510, 340, 140, 50)
    pygame.draw.rect(sup, (180, 50, 50), r_si, border_radius=10)
    pygame.draw.rect(sup, (50, 120, 50), r_no, border_radius=10)
    sup.blit(c.fuente_opciones.render(t("si"), True, (255, 255, 255)),
             (r_si.centerx - 10, r_si.centery - 10))
    sup.blit(c.fuente_opciones.render(t("no"), True, (255, 255, 255)),
             (r_no.centerx - 10, r_no.centery - 10))
    return r_si, r_no
