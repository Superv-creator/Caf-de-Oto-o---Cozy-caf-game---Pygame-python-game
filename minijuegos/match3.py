import pygame, random, math, sys, constantes as c
from animales import TIPOS_ANIMAL, dibujar_animal

COLS, FILAS = 6, 6
CELDA = 70

def ejecutar_match3(pantalla, reloj):
    ox = c.ANCHO//2 - (CELDA*COLS)//2
    oy = c.ALTO//2  - (CELDA*FILAS)//2 + 20

    def nuevo_tablero():
        t = [[random.choice(TIPOS_ANIMAL) for _ in range(COLS)] for _ in range(FILAS)]
        for _ in range(10): t = eliminar_matches_iniciales(t)
        while not hay_movimientos(t):
            t = [[random.choice(TIPOS_ANIMAL) for _ in range(COLS)] for _ in range(FILAS)]
            for _ in range(10): t = eliminar_matches_iniciales(t)
        return t

    def hay_movimientos(t):
        for fy in range(FILAS):
            for fx in range(COLS):
                if fx+1 < COLS:
                    t[fy][fx], t[fy][fx+1] = t[fy][fx+1], t[fy][fx]
                    if buscar_matches(t): t[fy][fx], t[fy][fx+1] = t[fy][fx+1], t[fy][fx]; return True
                    t[fy][fx], t[fy][fx+1] = t[fy][fx+1], t[fy][fx]
                if fy+1 < FILAS:
                    t[fy][fx], t[fy+1][fx] = t[fy+1][fx], t[fy][fx]
                    if buscar_matches(t): t[fy][fx], t[fy+1][fx] = t[fy+1][fx], t[fy][fx]; return True
                    t[fy][fx], t[fy+1][fx] = t[fy+1][fx], t[fy][fx]
        return False

    def encontrar_hint(t):
        for fy in range(FILAS):
            for fx in range(COLS):
                if fx+1 < COLS:
                    t[fy][fx], t[fy][fx+1] = t[fy][fx+1], t[fy][fx]
                    if buscar_matches(t):
                        t[fy][fx], t[fy][fx+1] = t[fy][fx+1], t[fy][fx]
                        return (fx,fy),(fx+1,fy)
                    t[fy][fx], t[fy][fx+1] = t[fy][fx+1], t[fy][fx]
                if fy+1 < FILAS:
                    t[fy][fx], t[fy+1][fx] = t[fy+1][fx], t[fy][fx]
                    if buscar_matches(t):
                        t[fy][fx], t[fy+1][fx] = t[fy+1][fx], t[fy][fx]
                        return (fx,fy),(fx,fy+1)
                    t[fy][fx], t[fy+1][fx] = t[fy+1][fx], t[fy][fx]
        return None

    def eliminar_matches_iniciales(t):
        for fy in range(FILAS):
            for fx in range(COLS):
                while True:
                    if fx >= 2 and t[fy][fx] == t[fy][fx-1] == t[fy][fx-2]:
                        t[fy][fx] = random.choice(TIPOS_ANIMAL)
                    elif fy >= 2 and t[fy][fx] == t[fy-1][fx] == t[fy-2][fx]:
                        t[fy][fx] = random.choice(TIPOS_ANIMAL)
                    else: break
        return t

    def buscar_matches(t):
        matches = set()
        for fy in range(FILAS):
            for fx in range(COLS-2):
                if t[fy][fx] == t[fy][fx+1] == t[fy][fx+2]:
                    run = [fx, fx+1, fx+2]; k = fx+3
                    while k < COLS and t[fy][k] == t[fy][fx]: run.append(k); k += 1
                    for r in run: matches.add((fy, r))
        for fx in range(COLS):
            for fy in range(FILAS-2):
                if t[fy][fx] == t[fy+1][fx] == t[fy+2][fx]:
                    run = [fy, fy+1, fy+2]; k = fy+3
                    while k < FILAS and t[k][fx] == t[fy][fx]: run.append(k); k += 1
                    for r in run: matches.add((r, fx))
        return matches

    def hacer_caer(t):
        for fx in range(COLS):
            col = [t[fy][fx] for fy in range(FILAS) if t[fy][fx] is not None]
            vacios = FILAS - len(col)
            nueva_col = [random.choice(TIPOS_ANIMAL) for _ in range(vacios)] + col
            for fy in range(FILAS): t[fy][fx] = nueva_col[fy]
        return t

    tablero = nuevo_tablero()
    sel = None
    puntos = 0
    hojas_ganadas = 0
    jugando = True
    anim_matches = []
    anim_timer = 0
    estado = "JUGANDO"
    textos_flotantes_m3 = []
    cadena_combo = 0
    ultimo_movimiento = pygame.time.get_ticks()
    hint_celdas = None

    fuente_med = c.fuente_stats
    fuente_peq = c.fuente_menu

    while jugando:
        t_ms = pygame.time.get_ticks()
        pantalla.fill((35, 20, 20))

        # Panel fondo
        panel_r = pygame.Rect(ox-16, oy-16, CELDA*COLS+32, CELDA*FILAS+32)
        pygame.draw.rect(pantalla,(55,35,35),panel_r,border_radius=14)
        pygame.draw.rect(pantalla,(100,70,50),panel_r,3,border_radius=14)

        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                c.hojas_doradas += hojas_ganadas
                if hojas_ganadas > c.record_match3: c.record_match3 = hojas_ganadas
                jugando = False

            if e.type == pygame.MOUSEBUTTONDOWN and estado == "JUGANDO":
                mx, my = e.pos
                if ox <= mx < ox+CELDA*COLS and oy <= my < oy+CELDA*FILAS:
                    fx, fy = (mx - ox) // CELDA, (my - oy) // CELDA
                    if sel is None:
                        sel = (fx, fy); ultimo_movimiento = t_ms; hint_celdas = None
                    else:
                        sx, sy = sel
                        if abs(sx-fx) + abs(sy-fy) == 1:
                            tablero[sy][sx], tablero[fy][fx] = tablero[fy][fx], tablero[sy][sx]
                            matches = buscar_matches(tablero)
                            if matches:
                                anim_matches = list(matches); anim_timer = t_ms; estado = "ANIMANDO"
                                # Puntuación mejorada
                                base_h = 10 + (len(matches) - 3) * 5
                                hojas_ganadas += base_h
                                puntos += len(matches); cadena_combo = 1
                                ultimo_movimiento = t_ms
                            else:
                                tablero[sy][sx], tablero[fy][fx] = tablero[fy][fx], tablero[sy][sx]
                        sel = None; ultimo_movimiento = t_ms

        # Resolver matches en cadena (Cascada)
        if estado == "ANIMANDO" and t_ms - anim_timer > 400:
            # Guardamos pos para texto antes de borrar
            pos_match = anim_matches[0] if anim_matches else (0,0)
            for (my2, mx2) in anim_matches: tablero[my2][mx2] = None
            tablero = hacer_caer(tablero)
            anim_matches = []
            nuevos = buscar_matches(tablero)
            if nuevos:
                anim_matches = list(nuevos); anim_timer = t_ms
                cadena_combo += 1
                base_n = 10 + (len(nuevos) - 3) * 5
                hojas_ganadas += (base_n * cadena_combo)
                puntos += len(nuevos)
                # Texto de combo
                mensajes = {2:"¡Combo x2!", 3:"¡Combo x3!", 4:"¡MEGA COMBO!", 5:"¡EXPLOSIÓN!"}
                msg = mensajes.get(cadena_combo, f"¡Combo x{cadena_combo}!")
                tx = ox + pos_match[1]*CELDA + random.randint(0,20)
                ty = oy + pos_match[0]*CELDA - 20
                textos_flotantes_m3.append({'x': tx, 'y': ty, 'texto': msg, 'vida': 255, 'color': (100,255,180)})
            else:
                estado = "JUGANDO"; cadena_combo = 0; hint_celdas = None; ultimo_movimiento = t_ms
                if not hay_movimientos(tablero):
                    tablero = nuevo_tablero()
                    textos_flotantes_m3.append({'x': ox+CELDA*COLS//2, 'y': oy+20, 'texto': "¡Rebarajando!", 'vida': 300, 'color': (200,200,100)})

        # Hint a los 8 segundos
        if estado == "JUGANDO" and t_ms - ultimo_movimiento > 8000:
            if hint_celdas is None: hint_celdas = encontrar_hint(tablero)

        # 1. Dibujar Tablero (Celdas y Animales)
        for fy in range(FILAS):
            for fx in range(COLS):
                cx, cy = ox + fx*CELDA + CELDA//2, oy + fy*CELDA + CELDA//2
                animal = tablero[fy][fx]
                if animal is None: continue
                en_match = (fy, fx) in [(m[0], m[1]) for m in anim_matches]
                es_sel = sel == (fx, fy)
                fondo_col = (75,50,50)
                if es_sel: fondo_col = (100,140,80)
                elif en_match: fondo_col = (140,100,40)
                r_cel = pygame.Rect(ox+fx*CELDA+2, oy+fy*CELDA+2, CELDA-4, CELDA-4)
                pygame.draw.rect(pantalla, fondo_col, r_cel, border_radius=8)
                escala = 0.8
                if en_match:
                    prog = min(1.0, (t_ms - anim_timer) / 400)
                    escala = 0.8 + math.sin(prog*math.pi)*0.3
                dibujar_animal(pantalla, animal, cx, cy, escala*0.7)
                if es_sel: pygame.draw.rect(pantalla,(150,255,150),r_cel,3,border_radius=8)

        # 2. Dibujar Hint (ENCIMA del tablero)
        if hint_celdas and estado == "JUGANDO":
            if (t_ms // 400) % 2 == 0:
                for hfx, hfy in hint_celdas:
                    r_h = pygame.Rect(ox+hfx*CELDA+2, oy+hfy*CELDA+2, CELDA-4, CELDA-4)
                    pygame.draw.rect(pantalla, (255, 255, 150), r_h, 4, border_radius=8)

        # 3. HUD e Información
        pantalla.blit(fuente_med.render(f"Hojas: {hojas_ganadas}", True, (100,255,100)), (ox+20, oy-55))
        pantalla.blit(fuente_peq.render(f"Record: {c.record_match3}", True, (200,200,200)), (ox+CELDA*COLS-110, oy-45))
        pantalla.blit(fuente_peq.render("ESC para salir", True, (180,180,180)), (ox+CELDA*COLS//2-50, oy+CELDA*FILAS+20))

        # Textos flotantes
        for tf in textos_flotantes_m3[:]:
            tf['y'] -= 1.5; tf['vida'] -= 4
            if tf['vida'] <= 0: textos_flotantes_m3.remove(tf)
            else:
                s_txt = fuente_med.render(tf['texto'], True, tf['color'])
                s_txt.set_alpha(tf['vida'])
                pantalla.blit(s_txt, (int(tf['x']) - s_txt.get_width()//2, int(tf['y'])))

        pygame.display.flip()
        reloj.tick(60)