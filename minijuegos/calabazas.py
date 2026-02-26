import pygame
import math
import random
import constantes as c

class Particula:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.vida = 255
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vida -= 8
        return self.vida > 0

def dibujar_calabaza_realista(sup, x, y, tipo, hit):
    if hit: return
    if tipo == "n": col = (230, 90, 20); col_l = (255, 120, 30)
    elif tipo == "d": col = (255, 180, 0); col_l = (255, 210, 50)
    else: col = (100, 80, 40); col_l = (130, 110, 60)

    pygame.draw.rect(sup, (40, 80, 20), (x-4, y-28, 8, 12), border_radius=2)
    pygame.draw.ellipse(sup, col, (x-26, y-18, 20, 35))
    pygame.draw.ellipse(sup, col, (x+6, y-18, 20, 35))
    pygame.draw.ellipse(sup, col_l, (x-15, y-20, 30, 40))
    pygame.draw.arc(sup, (20, 10, 0), (x-15, y-20, 30, 40), 0, 3.14, 1)

def ejecutar_calabazas(pantalla, reloj):
    ox, oy = (c.ANCHO - 800)//2, (c.ALTO - 500)//2
    ronda = 1
    puntos = 0
    nuevo_record = False
    particulas = []
    piedra = {"pos": [150, 400], "vel": [0,0], "activa": False}
    arrastrando = False

    def generar_ronda(n_ronda):
        cantidad = min(4 + (n_ronda // 2), 9)
        nuevas = [{"x": random.randint(350, 750), "y": random.randint(150, 420), 
                   "tipo": random.choice(["n", "n", "n", "d", "e"]), "hit": False} for _ in range(cantidad)]
        
        # TABLA EQUILIBRADA: 4:4, 5:4, 6:5, 7:5, 8:6, 9:6
        tabla_tiros = {4: 4, 5: 4, 6: 5, 7: 5, 8: 6, 9: 6}
        tiros_nuevos = tabla_tiros.get(cantidad, 4) 
        return nuevas, tiros_nuevos

    calabazas, tiros = generar_ronda(ronda)

    ejecutando = True
    while ejecutando:
        mx, my = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: ejecutando = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: ejecutando = False
            
            if e.type == pygame.MOUSEBUTTONDOWN and not piedra["activa"] and tiros > 0:
                if math.hypot(mx - (ox + 150), my - (oy + 400)) < 45:
                    arrastrando = True
            
            if e.type == pygame.MOUSEBUTTONUP and arrastrando:
                arrastrando = False
                dx, dy = (ox + 150) - mx, (oy + 400) - my
                piedra["vel"] = [dx * 0.16, dy * 0.16]
                piedra["activa"] = True
                tiros -= 1

        # --- FÍSICA CON REBOTES ---
        if piedra["activa"]:
            piedra["pos"][0] += piedra["vel"][0]
            piedra["pos"][1] += piedra["vel"][1]
            piedra["vel"][1] += 0.45 # Gravedad

            # Rebote en paredes laterales del panel (ox a ox+800)
            if piedra["pos"][0] < 15 or piedra["pos"][0] > 785:
                piedra["vel"][0] *= -0.7 # Rebota y pierde un poco de fuerza
                # Ajustar posición para que no se quede pegado
                piedra["pos"][0] = 16 if piedra["pos"][0] < 15 else 784

            # Rebote en el techo (oy)
            if piedra["pos"][1] < 15:
                piedra["vel"][1] *= -0.7
                piedra["pos"][1] = 16

            for cala in calabazas:
                if not cala["hit"] and math.hypot(piedra["pos"][0] - cala["x"], piedra["pos"][1] - cala["y"]) < 30:
                    cala["hit"] = True
                    puntos += 20 if cala["tipo"] == "d" else 10
                    if cala["tipo"] == "e": puntos += 2
                    col_p = (255, 150, 0) if cala["tipo"] != "e" else (80, 60, 30)
                    for _ in range(12): particulas.append(Particula(ox+cala["x"], oy+cala["y"], col_p))
            
            # Solo desaparece si cae por debajo del suelo o sale muy lejos por los lados
            if piedra["pos"][1] > 550 or piedra["pos"][0] < -100 or piedra["pos"][0] > 900:
                piedra["activa"] = False
                piedra["pos"] = [150, 400]
        
        if all(c["hit"] for c in calabazas):
            ronda += 1
            calabazas, tiros = generar_ronda(ronda)
            piedra["activa"] = False
            piedra["pos"] = [150, 400]

        particulas = [p for p in particulas if p.update()]
        if puntos > c.record_calabazas:
            c.record_calabazas = puntos
            nuevo_record = True

        # --- DIBUJO ---
        pantalla.fill((45, 25, 25))
        pygame.draw.rect(pantalla, (55, 35, 35), (ox, oy, 800, 500), border_radius=15)
        pygame.draw.rect(pantalla, (80, 50, 40), (ox, oy, 800, 500), 3, border_radius=15)
        pygame.draw.rect(pantalla, (35, 20, 10), (ox, oy+450, 800, 50), border_radius=10)
        
        pygame.draw.line(pantalla, (100, 60, 30), (ox+150, oy+400), (ox+150, oy+460), 10)
        pygame.draw.line(pantalla, (120, 80, 50), (ox+130, oy+380), (ox+150, oy+400), 8)
        pygame.draw.line(pantalla, (120, 80, 50), (ox+170, oy+380), (ox+150, oy+400), 8)

        if arrastrando:
            dx, dy = (ox + 150) - mx, (oy + 400) - my
            for i in range(1, 15): # Guía más larga
                tx, ty = 150 + dx*0.16*i, 400 + dy*0.16*i + 0.5*0.45*(i**2)
                if 0 < tx < 800 and 0 < ty < 500: # Solo dibujar guía dentro del panel
                    pygame.draw.circle(pantalla, (200, 200, 200), (ox+int(tx), oy+int(ty)), 2)

        for cala in calabazas:
            dibujar_calabaza_realista(pantalla, ox+cala["x"], oy+cala["y"], cala["tipo"], cala["hit"])

        for p in particulas:
            pygame.draw.circle(pantalla, p.color, (int(p.x), int(p.y)), 3)

        p_pos = (ox+int(piedra["pos"][0]), oy+int(piedra["pos"][1]))
        if arrastrando: 
            p_pos = (mx, my)
            pygame.draw.line(pantalla, (220, 200, 180), (ox+130, oy+380), (mx, my), 3)
            pygame.draw.line(pantalla, (220, 200, 180), (ox+170, oy+380), (mx, my), 3)
        pygame.draw.circle(pantalla, (130, 130, 130), p_pos, 12)

        t_puntos = c.fuente_stats.render(f"Hojas: {puntos}", True, (255, 220, 100))
        t_tiros = c.fuente_menu.render(f"Ronda: {ronda} | Tiros: {tiros}", True, (200, 255, 200))
        t_record = c.fuente_menu.render(f"Récord: {c.record_calabazas}", True, (150, 255, 150))
        pantalla.blit(t_puntos, (ox+20, oy+20)); pantalla.blit(t_tiros, (ox+20, oy+55)); pantalla.blit(t_record, (ox+600, oy+20))

        if tiros <= 0 and not piedra["activa"]:
            msg = "¡NUEVO RÉCORD!" if nuevo_record else "SIN MUNICIÓN"
            txt_fin = c.fuente_final.render(msg, True, (255, 100, 100))
            txt_esc = c.fuente_opciones.render("ESC para salir", True, (255, 255, 255))
            pantalla.blit(txt_fin, (c.ANCHO//2 - txt_fin.get_width()//2, c.ALTO//2 - 40))
            pantalla.blit(txt_esc, (c.ANCHO//2 - txt_esc.get_width()//2, c.ALTO//2 + 30))

        pygame.display.flip()
        reloj.tick(60)
    c.hojas_doradas += puntos