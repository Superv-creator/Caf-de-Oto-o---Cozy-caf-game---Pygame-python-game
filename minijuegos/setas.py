import pygame, random, math, constantes as c

class ParticulaSeta:
    def __init__(self, x, y, col):
        self.x, self.y = x, y
        self.vx, self.vy = random.uniform(-4, 4), random.uniform(-4, 4)
        self.vida = 255
        self.col = col
    def update(self):
        self.x += self.vx; self.y += self.vy; self.vida -= 12
        return self.vida > 0

class TextoPop:
    def __init__(self, x, y, txt, col):
        self.x, self.y, self.txt, self.col = x, y, txt, col
        self.vida = 255
    def update(self):
        self.y -= 1.2; self.vida -= 6
        return self.vida > 0

class SetaJuego:
    def __init__(self, ox, oy):
        self.tipo = random.choices(["roja", "veneno", "oro"], weights=[72, 20, 8])[0]
        self.x = random.randint(ox + 80, ox + 720)
        self.y = random.randint(oy + 80, oy + 420)
        self.nacimiento = pygame.time.get_ticks()
        self.vida = 1900 if self.tipo != "oro" else 850
        self.escala = 0.0
        self.hit = False
    def update(self, t):
        if self.escala < 1.0: self.escala += 0.15
        return t - self.nacimiento < self.vida

def dibujar_seta_pro(sup, s, t):
    if s.hit: return
    x, y, e = s.x, s.y, s.escala
    if s.tipo == "roja": col, col_m = (210, 60, 60), (255, 255, 255)
    elif s.tipo == "oro":
        col, col_m = (255, 210, 50), (255, 255, 255)
        for i in range(4):
            ang = t * 0.01 + i * (math.pi/2)
            dx, dy = x + math.cos(ang) * 45 * e, y + math.sin(ang) * 30 * e
            pygame.draw.line(sup, (255, 255, 200), (dx-5, dy), (dx+5, dy), 2)
            pygame.draw.line(sup, (255, 255, 200), (dx, dy-5), (dx, dy+5), 2)
    else: # VENENOSA
        col, col_m = (100, 30, 140), (120, 255, 120)
        for i in range(3):
            bx = x + math.sin(t*0.005 + i)*20*e
            by = y - 30*e + math.cos(t*0.005 + i)*10*e
            pygame.draw.circle(sup, (120, 255, 120), (int(bx), int(by)), int(4*e))

    pygame.draw.rect(sup, (220, 220, 200), (x-10*e, y-5*e, 20*e, 35*e), border_radius=int(6*e))
    pygame.draw.ellipse(sup, col, (x-35*e, y-25*e, 70*e, 45*e))
    if s.tipo == "oro": pygame.draw.ellipse(sup, (255, 255, 230), (x-25*e, y-18*e, 25*e, 12*e))

    # TUS 5 PUNTOS BLANCOS
    puntos_pos = [(-15, -12, 7), (18, -8, 6), (-2, -18, 5), (5, -2, 5), (-22, -3, 4)]
    for ox_m, oy_m, r_m in puntos_pos:
        pygame.draw.circle(sup, col_m, (int(x + ox_m*e), int(y + oy_m*e)), int(r_m*e))

def ejecutar_setas(pantalla, reloj):
    ox, oy = (c.ANCHO - 800)//2, (c.ALTO - 500)//2
    setas, particulas, textos = [], [], []
    puntos, shake = 0, 0
    tiempo_fin = pygame.time.get_ticks() + 30000
    ultimo_spawn, spawn_rate = 0, 1000

    ejecutando = True
    while ejecutando:
        t = pygame.time.get_ticks()
        restante = max(0, (tiempo_fin - t) // 1000)
        for e in pygame.event.get():
            if e.type == pygame.QUIT: ejecutando = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: ejecutando = False
            if e.type == pygame.MOUSEBUTTONDOWN and restante > 0:
                mx, my = e.pos
                for s in setas:
                    if not s.hit and math.hypot(mx-s.x, my-s.y) < 45:
                        s.hit = True
                        if s.tipo == "roja": 
                            puntos += 10; textos.append(TextoPop(s.x, s.y, "+10", (100,255,100)))
                            for _ in range(12): particulas.append(ParticulaSeta(s.x, s.y, (255,50,50)))
                        elif s.tipo == "oro": 
                            puntos += 50; textos.append(TextoPop(s.x, s.y, "¡GENIAL! +50", (255,215,0)))
                            for _ in range(25): particulas.append(ParticulaSeta(s.x, s.y, (255,255,150)))
                        else: 
                            puntos = max(0, puntos-25); shake = 15
                            textos.append(TextoPop(s.x, s.y, "PUAJ! -25", (200,50,255)))
                            for _ in range(15): particulas.append(ParticulaSeta(s.x, s.y, (120,255,100)))
                        spawn_rate = max(300, spawn_rate - 25); break

        if t - ultimo_spawn > spawn_rate and restante > 0:
            setas.append(SetaJuego(ox, oy)); ultimo_spawn = t
        
        setas = [s for s in setas if s.update(t) and not s.hit]
        particulas = [p for p in particulas if p.update()]
        textos = [tx for tx in textos if tx.update()]
        if puntos > c.record_setas: c.record_setas = puntos

        # DIBUJO
        sx, sy = (random.randint(-shake, shake), random.randint(-shake, shake)) if shake > 0 else (0,0)
        if shake > 0: shake -= 1
        pantalla.fill((45, 25, 25))
        pygame.draw.rect(pantalla, (55, 35, 35), (ox+sx, oy+sy, 800, 500), border_radius=15)
        pygame.draw.rect(pantalla, (80, 60, 45), (ox+sx, oy+sy, 800, 500), 4, border_radius=15)
        
        for s in setas: dibujar_seta_pro(pantalla, s, t)
        for p in particulas: pygame.draw.circle(pantalla, p.col, (int(p.x), int(p.y)), 3)
        for tx in textos:
            img = c.fuente_moneda_txt.render(tx.txt, True, tx.col)
            img.set_alpha(tx.vida); pantalla.blit(img, (tx.x - img.get_width()//2, tx.y))

        pantalla.blit(c.fuente_stats.render(f"Hojas: {puntos}", True, (255, 220, 100)), (ox+20, oy+20))
        pantalla.blit(c.fuente_stats.render(f"Tiempo: {restante}s", True, (255, 255, 255)), (ox+320, oy+20))
        pantalla.blit(c.fuente_menu.render(f"Récord: {c.record_setas}", True, (150, 255, 150)), (ox+600, oy+20))
        
        if restante <= 0:
            t1 = c.fuente_final.render("¡FIN DE LA COLECTA!", True, (255, 100, 100))
            pantalla.blit(t1, (c.ANCHO//2 - t1.get_width()//2, c.ALTO//2 - 40))

        pygame.display.flip(); reloj.tick(60)
    c.hojas_doradas += puntos