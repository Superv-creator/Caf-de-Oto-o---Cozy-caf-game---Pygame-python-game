import pygame, random, math, sys, constantes as c
from jardin import dibujar_item_jardin

SUELO_Y = 450

# Datos fijos para árboles variados (semilla para que sean siempre iguales)
import random as _rnd
_rnd.seed(42)
ARBOLES_RUNNER = [
    {'off': i*183, 'h': _rnd.randint(70,130), 'r': _rnd.randint(28,50),
     'col1': _rnd.choice([(200,90,20),(180,60,20),(210,130,30),(160,80,40),(220,100,50)]),
     'col2': _rnd.choice([(230,120,40),(200,80,30),(240,150,50),(180,100,50)]),
     'tronco': _rnd.choice([(80,50,25),(100,65,30),(70,45,20)]),
     'forma': _rnd.choice(['redondo','doble','triple'])
    } for i in range(7)]
_rnd.seed()  # restore random

def dibujar_gato_runner(sup, x, y, t_ms, chocado):
    """Dibuja al gato de perfil para el modo runner con detalles mejorados."""
    col = (240, 240, 240)
    # Pequeño rebote al correr
    oy = math.sin(t_ms * 0.02) * 3 if not chocado else 0
    # Patas animadas
    fase = math.sin(t_ms * 0.02) * 10
    pygame.draw.line(sup, col, (x-12, y+12+oy), (x-18-fase, y+24), 5)
    pygame.draw.line(sup, col, (x+8, y+12+oy), (x+14+fase, y+24), 5)
    
    # --- COLA MEJORADA (más gruesa y con movimiento) ---
    mov_cola = math.sin(t_ms * 0.01) * 6
    pygame.draw.line(sup, col, (x-22, y+5+oy), (x-45, y-10+oy+mov_cola), 9)
    pygame.draw.circle(sup, col, (x-45, int(y-10+oy+mov_cola)), 4)

    # Cuerpo elíptico
    pygame.draw.ellipse(sup, col, (x-28, y-12+oy, 50, 30))
    
    # Cabeza adelantada
    hx, hy = x+18, y-15+oy
    pygame.draw.circle(sup, col, (hx, hy), 16)
    
    # --- OREJAS (dobles para dar profundidad) ---
    pygame.draw.polygon(sup, (210,210,210), [(hx-8, hy-14), (hx-2, hy-28), (hx+6, hy-14)])
    pygame.draw.polygon(sup, col, [(hx-4, hy-14), (hx+4, hy-30), (hx+12, hy-14)])
    
    # Ojo y Nariz
    if chocado:
        pygame.draw.line(sup, (50,50,50), (hx+4, hy-6), (hx+12, hy+2), 2)
        pygame.draw.line(sup, (50,50,50), (hx+12, hy-6), (hx+4, hy+2), 2)
    else:
        pygame.draw.circle(sup, (60,160,60), (hx+7, hy-4), 5)
        pygame.draw.circle(sup, (0,0,0), (hx+8, hy-4), 2)
    
    # Nariz rosada
    pygame.draw.circle(sup, (255,180,190), (hx+14, hy+2), 3)

    # Bigotes
    if not chocado:
        pygame.draw.line(sup, (180,180,180), (hx+12, hy+2), (hx+25, hy), 1)
        pygame.draw.line(sup, (180,180,180), (hx+12, hy+2), (hx+25, hy+4), 1)

def dibujar_fondo_runner(pantalla, scroll, t_ms):
    # Cielo azul degradado
    for y in range(SUELO_Y):
        ratio = y / SUELO_Y
        r = int(100 - ratio*30); g = int(160 - ratio*40); b = int(220 - ratio*50)
        pygame.draw.line(pantalla,(r,g,b),(0,y),(c.ANCHO,y))

    # Nubes blancas esponjosas
    for i in range(5):
        cx = (int(scroll*0.25) + i*230) % (c.ANCHO+150) - 75
        cy = 40 + (i%3)*35
        for ox,oy2,rw,rh in [(0,0,70,28),(25,-12,55,26),(-20,-8,45,22),(45,2,40,20)]:
            pygame.draw.ellipse(pantalla,(245,248,252),(cx+ox,cy+oy2,rw,rh))

    # Árboles otoñales variados en fondo (capa lejana)
    for arb in ARBOLES_RUNNER:
        tx = (int(scroll*0.45) + arb['off']) % (c.ANCHO+120) - 60
        ty = SUELO_Y - arb['h']
        trunk_h = arb['h'] - arb['r'] + 10
        pygame.draw.rect(pantalla, arb['tronco'], (tx+arb['r']//2-6, ty, 12, trunk_h))
        if arb['forma'] == 'redondo':
            pygame.draw.circle(pantalla, arb['col1'], (tx+arb['r']//2, ty-5), arb['r'])
            pygame.draw.circle(pantalla, arb['col2'], (tx+arb['r']//2, ty-8), arb['r']-8)
        elif arb['forma'] == 'doble':
            pygame.draw.circle(pantalla, arb['col1'], (tx+arb['r']//2-10, ty), arb['r']-5)
            pygame.draw.circle(pantalla, arb['col1'], (tx+arb['r']//2+10, ty-10), arb['r']-8)
            pygame.draw.circle(pantalla, arb['col2'], (tx+arb['r']//2, ty-5), arb['r']-14)
        else:  # triple
            pygame.draw.circle(pantalla, arb['col1'], (tx+arb['r']//2, ty-10), arb['r'])
            pygame.draw.circle(pantalla, arb['col1'], (tx+arb['r']//2-15, ty+5), arb['r']-10)
            pygame.draw.circle(pantalla, arb['col1'], (tx+arb['r']//2+15, ty+5), arb['r']-10)
            pygame.draw.circle(pantalla, arb['col2'], (tx+arb['r']//2, ty-15), arb['r']-12)

    # Suelo con hierba
    pygame.draw.rect(pantalla,(80,120,50),(0,SUELO_Y,c.ANCHO,c.ALTO-SUELO_Y))
    pygame.draw.rect(pantalla,(100,150,60),(0,SUELO_Y,c.ANCHO,12))

    # VALLA (capa más cercana, scroll normal)
    scroll_valla = int(scroll) % 200
    poste_col = (120,80,40)
    travesano_col = (160,110,60)
    for px_v in range(-scroll_valla, c.ANCHO+10, 80):
        pygame.draw.rect(pantalla,poste_col,(px_v, SUELO_Y-60, 10, 70),border_radius=2)
        pygame.draw.rect(pantalla,(140,95,50),(px_v, SUELO_Y-62, 10, 8),border_radius=2)
    for px_v in range(-scroll_valla+40, c.ANCHO+10, 80):
        pygame.draw.rect(pantalla,travesano_col,(px_v-36, SUELO_Y-50, 76, 7),border_radius=3)
        pygame.draw.rect(pantalla,travesano_col,(px_v-36, SUELO_Y-35, 76, 7),border_radius=3)

    # Hojas caídas decorativas
    for i in range(8):
        lx = (int(scroll*1.5) + i*140) % (c.ANCHO+30) - 15
        ly = SUELO_Y + 5 + (i%3)*4
        pygame.draw.ellipse(pantalla,(180,90,30),(lx,ly,12,7))

def ejecutar_runner(pantalla, reloj):
    gato_y = float(SUELO_Y - 20)
    vel_y = 0.0
    saltando = False
    doble_salto = True
    obstaculos = []
    hojas_ganadas = 0
    frames = 0
    velocidad = 6.0
    scroll = 0.0
    timer_spawn = 220
    estado = "JUGANDO"

    tipos_obs = [
        ('seta',    (200,50,50),  24, 30),
        ('piedra',  (150,150,150),30, 20),
        ('taburete',(160,110,60), 24, 35),
    ]

    t_ms_inicio = pygame.time.get_ticks()

    while True:
        t_ms = pygame.time.get_ticks()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                c.hojas_doradas += hojas_ganadas
                if hojas_ganadas > c.record_runner: c.record_runner = hojas_ganadas
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    c.hojas_doradas += hojas_ganadas
                    if hojas_ganadas > c.record_runner: c.record_runner = hojas_ganadas
                    return
                if e.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                    if estado == "JUGANDO":
                        if not saltando:
                            vel_y = -15; saltando = True; doble_salto = True
                        elif doble_salto:
                            vel_y = -13; doble_salto = False
                    elif estado == "GAMEOVER":
                        if e.key in (pygame.K_SPACE, pygame.K_RETURN):
                            # Sumar las hojas ganadas antes de reiniciar
                            c.hojas_doradas += hojas_ganadas
                            if hojas_ganadas > c.record_runner: c.record_runner = hojas_ganadas
                            gato_y = float(SUELO_Y-20); vel_y=0; saltando=False; doble_salto=True
                            obstaculos.clear(); hojas_ganadas=0; frames=0; velocidad=6.0
                            scroll=0; timer_spawn=220; estado="JUGANDO"
            if e.type == pygame.MOUSEBUTTONDOWN and estado == "GAMEOVER":
                c.hojas_doradas += hojas_ganadas
                if hojas_ganadas > c.record_runner: c.record_runner = hojas_ganadas
                gato_y=float(SUELO_Y-20); vel_y=0; saltando=False; doble_salto=True
                obstaculos.clear(); hojas_ganadas=0; frames=0; velocidad=6.0
                scroll=0; timer_spawn=220; estado="JUGANDO"

        if estado == "JUGANDO":
            scroll += velocidad * 0.8
            vel_y += 0.7
            gato_y += vel_y
            if gato_y >= SUELO_Y - 20:
                gato_y = SUELO_Y - 20; vel_y = 0; saltando = False; doble_salto = True

            frames += 1
            if frames % 90 == 0:
                hojas_ganadas += 1
                velocidad = min(14.0, 6.0 + frames/900)

            timer_spawn -= 1
            if timer_spawn <= 0:
                tipo_o, col_o, w_o, h_o = random.choice(tipos_obs)
                # Espaciado generoso al principio, se reduce con la velocidad
                # Mínimo 90 frames (~1.5s) al inicio, baja hasta 45 frames al máximo
                espacio_base = max(45, int(220 - frames * 0.08))
                variacion = random.randint(-15, 15)
                timer_spawn = max(45, espacio_base + variacion)
                obstaculos.append({
                    'rect': pygame.Rect(c.ANCHO+20, SUELO_Y-h_o, w_o, h_o),
                    'tipo': tipo_o, 'color': col_o
                })

        # Dibujar fondo
        dibujar_fondo_runner(pantalla, scroll, t_ms)

        # Obstáculos
        r_jugador = pygame.Rect(85, int(gato_y)-40, 50, 65)
        for obs in obstaculos[:]:
            if estado == "JUGANDO":
                obs['rect'].x -= int(velocidad)
            dibujar_item_jardin(pantalla, obs['tipo'], obs['rect'].centerx,
                                SUELO_Y - 5, obs['color'], 1.0, t_ms)
            if estado == "JUGANDO" and r_jugador.colliderect(obs['rect']):
                estado = "GAMEOVER"
                if hojas_ganadas > c.record_runner: c.record_runner = hojas_ganadas
            if obs['rect'].right < -10:
                if estado == "JUGANDO": hojas_ganadas += 10
                obstaculos.remove(obs)

        # Gato
        dibujar_gato_runner(pantalla, 115, int(gato_y), t_ms, estado=="GAMEOVER")

        # HUD
        t_h = c.fuente_stats.render(f"Hojas: {hojas_ganadas}", True, (255,215,0))
        t_r = c.fuente_menu.render(f"Récord: {c.record_runner}", True, (220,220,220))
        t_esc2 = c.fuente_small.render("ESC para salir  |  ESPACIO para saltar  |  doble salto disponible", True, (200,200,200))
        pygame.draw.ellipse(pantalla,(100,220,80),(20, 22, 16, 10))
        pygame.draw.line(pantalla,(40,120,20),(20,27),(34,27),1)
        pantalla.blit(t_h, (40, 20))
        pantalla.blit(t_r, (c.ANCHO-t_r.get_width()-20, 20))
        pantalla.blit(t_esc2, (c.ANCHO//2-t_esc2.get_width()//2, c.ALTO-28))

        if estado == "GAMEOVER":
            overlay = pygame.Surface((c.ANCHO,c.ALTO),pygame.SRCALPHA)
            overlay.fill((0,0,0,120)); pantalla.blit(overlay,(0,0))
            r_panel = pygame.Rect(300,180,400,250)
            pygame.draw.rect(pantalla,(55,30,15),r_panel,border_radius=15)
            pygame.draw.rect(pantalla,(200,100,50),r_panel,3,border_radius=15)
            t1 = c.fuente_titulo.render("¡CHOCADO!", True, (255,100,100))
            t2 = c.fuente_stats.render(f"Hojas: {hojas_ganadas}", True, (100,255,100))
            t3 = c.fuente_menu.render("ESPACIO para reintentar  |  ESC para salir", True, (220,220,180))
            pantalla.blit(t1,(r_panel.centerx-t1.get_width()//2, r_panel.y+30))
            pantalla.blit(t2,(r_panel.centerx-t2.get_width()//2, r_panel.y+100))
            pantalla.blit(t3,(r_panel.centerx-t3.get_width()//2, r_panel.y+160))

        pygame.display.flip()
        reloj.tick(60)