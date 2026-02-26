import pygame, random, math

# ─── CONFIG ────────────────────────────────────────────────────────────────────
# ANCHO y ALTO se calculan dinámicamente según la pantalla recibida (ver ejecutar_defensa)
CELDA_W, CELDA_H = 74, 85
FILAS, COLUMNAS    = 5, 9

C_ORO = (255, 215, 0)

# Estos se inicializan en ejecutar_defensa() según el tamaño de pantalla
ANCHO, ALTO = 1000, 600
INICIO_X, INICIO_Y = 300, 100

# ─── ANIMALES (copiado / compatible con el juego principal) ───────────────────
def dibujar_animal(sup, tipo, x, y, escala=1.0, mirando_izq=False, parpadeo=False):
    def s(v): return max(1, int(v*escala))
    colores = {
        "CONEJO":(240,240,240),"OSO":(139,69,19),"BUHO":(120,100,90),
        "RANA":(100,200,100),"PATO":(255,220,50),"ZORRO":(230,100,30),"PANDA":(240,240,240)
    }
    col = colores.get(tipo, (200,200,200))

    # Sombra suave bajo el animal
    sombra = pygame.Surface((int(s(50)),int(s(16))), pygame.SRCALPHA)
    pygame.draw.ellipse(sombra,(0,0,0,55),(0,0,int(s(50)),int(s(16))))
    sup.blit(sombra,(x-s(25), y+s(18)))

    if tipo == "CONEJO":
        # Orejas primero (detrás de la cabeza)
        for ox in [-10,4]:
            pygame.draw.ellipse(sup,col,(x+ox,y-s(45),s(10),s(30)))
            pygame.draw.ellipse(sup,(255,180,180),(x+ox+s(2),y-s(40),s(6),s(20)))
        # Cabeza
        pygame.draw.circle(sup,col,(x,y),s(25))
        # Nariz
        pygame.draw.polygon(sup,(255,150,160),[(x-s(3),y-s(5)),(x+s(3),y-s(5)),(x,y-s(2))])
        # Bigotes a los lados de la nariz (en la cara, no en las orejas)
        for bx2,ex2,ey2 in [(-3,-20,-3),(-3,-20,3),(3,20,-3),(3,20,3)]:
            pygame.draw.line(sup,(180,180,180),(x+bx2,y+ey2),(x+ex2,y+ey2),1)
    elif tipo == "OSO":
        pygame.draw.circle(sup,col,(x-s(15),y-s(20)),s(12))
        pygame.draw.circle(sup,col,(x+s(15),y-s(20)),s(12))
        pygame.draw.circle(sup,col,(x,y),s(25))
        pygame.draw.ellipse(sup,(200,150,100),(x-s(12),y-s(8),s(24),s(16)))
        pygame.draw.circle(sup,(0,0,0),(x,y-s(2)),s(3))
    elif tipo == "BUHO":
        pygame.draw.circle(sup,col,(x,y),s(25))
        pygame.draw.polygon(sup,(80,65,60),[(x-s(12),y-s(18)),(x-s(4),y-s(18)),(x-s(8),y-s(24))])
        pygame.draw.polygon(sup,(80,65,60),[(x+s(4),y-s(18)),(x+s(12),y-s(18)),(x+s(8),y-s(24))])
        for ox in [-9,9]:
            pygame.draw.circle(sup,(255,255,255),(x+ox,y-s(8)),s(9))
            pygame.draw.circle(sup,(0,0,0),(x+ox,y-s(8)),s(4))
            pygame.draw.circle(sup,(255,255,200),(x+ox-1,y-s(9)),s(1))
        pygame.draw.polygon(sup,(255,165,0),[(x-s(5),y+s(1)),(x+s(5),y+s(1)),(x,y+s(8))])
    elif tipo == "ZORRO":
        pygame.draw.circle(sup,col,(x,y),s(25))
        pygame.draw.polygon(sup,col,[(x-s(16),y-s(20)),(x-s(8),y-s(42)),(x-s(2),y-s(20))])
        pygame.draw.polygon(sup,col,[(x+s(2),y-s(20)),(x+s(8),y-s(42)),(x+s(16),y-s(20))])
        pygame.draw.polygon(sup,(255,200,180),[(x-s(14),y-s(22)),(x-s(8),y-s(36)),(x-s(4),y-s(22))])
        pygame.draw.polygon(sup,(255,200,180),[(x+s(4),y-s(22)),(x+s(8),y-s(36)),(x+s(14),y-s(22))])
        pygame.draw.ellipse(sup,(255,240,220),(x-s(8),y-s(4),s(16),s(12)))
        pygame.draw.circle(sup,(200,60,20),(x,y+s(2)),s(4))
        # Ojos del zorro (más visibles, con blanco del ojo)
        for ox in [-9,9]:
            pygame.draw.circle(sup,(255,255,255),(x+ox,y-s(8)),s(5))
            pygame.draw.circle(sup,(50,30,10),(x+ox,y-s(8)),s(4))
            pygame.draw.circle(sup,(255,200,50),(x+ox,y-s(8)),s(2))
            pygame.draw.circle(sup,(0,0,0),(x+ox,y-s(8)),s(1))
    elif tipo == "PANDA":
        pygame.draw.circle(sup,(240,240,240),(x,y),s(25))
        pygame.draw.ellipse(sup,(40,40,40),(x-s(14),y-s(16),s(12),s(10)))
        pygame.draw.ellipse(sup,(40,40,40),(x+s(2),y-s(16),s(12),s(10)))
        pygame.draw.circle(sup,(40,40,40),(x-s(18),y-s(24)),s(8))
        pygame.draw.circle(sup,(40,40,40),(x+s(18),y-s(24)),s(8))
        for ox in [-8,8]:
            pygame.draw.circle(sup,(255,255,255),(x+ox,y-s(12)),s(4))
            pygame.draw.circle(sup,(0,0,0),(x+ox,y-s(12)),s(2))
        pygame.draw.circle(sup,(100,100,100),(x,y+s(4)),s(5))

    # Ojos genéricos para los que no tienen arriba
    if tipo in ("CONEJO","OSO","PANDA") and not parpadeo:
        for ox in [-8,8]:
            pygame.draw.circle(sup,(0,0,0),(x+ox,y-s(5)),s(3))
            pygame.draw.circle(sup,(255,255,255),(x+ox+1,y-s(6)),s(1))
    if parpadeo and tipo not in ("BUHO","ZORRO"):
        for ox in [-8,8]:
            pygame.draw.arc(sup,(50,50,50),(x+ox-s(5),y-s(9),s(10),s(6)),0,math.pi,max(1,s(2)))

    # Mejillas
    if tipo in ("CONEJO","PANDA"):
        pygame.draw.ellipse(sup,(255,180,180),(x-s(18),y-s(5),s(8),s(5)))
        pygame.draw.ellipse(sup,(255,180,180),(x+s(10),y-s(5),s(8),s(5)))


# ─── CLASE SOMBRA ENEMIGA (mucho mejor visualmente) ───────────────────────────
class Sombra:
    TIPOS = ["SOMBRA_A","SOMBRA_B","SOMBRA_C"]
    def __init__(self, fila):
        self.fila = fila
        self.x    = float(ANCHO + 60)
        self.y    = float(INICIO_Y + fila*CELDA_H + CELDA_H//2)
        self.vida_max = random.choice([80, 130, 200])
        self.vida = self.vida_max
        self.vel  = 0.55 + random.uniform(-0.12, 0.12)
        self.off  = random.uniform(0, math.pi*2)
        # Variante visual
        self.variant = random.randint(0,2)
        self.col_base = [(80,60,130),(100,40,120),(60,50,140)][self.variant]
        self.particulas = []  # trail de sombra
        self.impactos   = []  # chispas al recibir daño

    def dibujar(self, sup, t):
        x = int(self.x)
        y = int(self.y + math.sin(t*0.004 + self.off)*4)

        # Trail de niebla
        for i, (px,py,palpha) in enumerate(self.particulas):
            a_clamped = max(0, min(255, int(palpha)))
            if a_clamped <= 0: continue
            ps = pygame.Surface((20,20), pygame.SRCALPHA)
            pygame.draw.circle(ps,(80,50,120,a_clamped),(10,10),10)
            sup.blit(ps,(int(px)-10,int(py)-10))

        # Aura exterior pulsante
        aura_r = int(28 + math.sin(t*0.006+self.off)*4)
        aura = pygame.Surface((aura_r*2+4, aura_r*2+4), pygame.SRCALPHA)
        pygame.draw.circle(aura,(100,60,180,50),(aura_r+2,aura_r+2),aura_r)
        sup.blit(aura,(x-aura_r-2, y-aura_r-2))

        # Cuerpo según variante
        if self.variant == 0:  # Sombra básica
            pygame.draw.circle(sup,(60,45,110),(x,y),22)
            pygame.draw.circle(sup,self.col_base,(x,y),18)
            # Ojos amenazantes
            for ox in [-7,7]:
                pygame.draw.ellipse(sup,(255,50,50),(x+ox-4,y-5,8,10))
                pygame.draw.circle(sup,(200,0,0),(x+ox,y-2),3)
                pygame.draw.circle(sup,(255,100,100),(x+ox-1,y-4),1)
            # Boca irregular
            pts = [(x-8,y+6),(x-4,y+10),(x,y+8),(x+4,y+10),(x+8,y+6)]
            pygame.draw.lines(sup,(255,80,80),False,pts,2)
        elif self.variant == 1:  # Sombra espectral (más grande)
            pygame.draw.ellipse(sup,(50,35,100),(x-18,y-24,36,48))
            pygame.draw.ellipse(sup,self.col_base,(x-14,y-20,28,38))
            # Tentáculos inferiores
            for i in range(3):
                tx = x - 10 + i*10
                ty_base = y + 14
                wave = int(math.sin(t*0.008+i*1.2+self.off)*5)
                pygame.draw.line(sup,(80,50,150),(tx,ty_base),(tx+wave,ty_base+12),3)
            for ox in [-6,6]:
                pygame.draw.circle(sup,(255,200,50),(x+ox,y-8),4)
                pygame.draw.circle(sup,(255,100,0),(x+ox,y-8),2)
        else:  # Sombra veloz (más pequeña y rápida)
            pygame.draw.circle(sup,(70,50,120),(x,y),16)
            pygame.draw.circle(sup,self.col_base,(x,y),12)
            # Rastro de velocidad
            for i in range(3):
                tr_x = x + (i+1)*12
                tr_alpha = 80 - i*25
                ts = pygame.Surface((16,16), pygame.SRCALPHA)
                pygame.draw.circle(ts,(*self.col_base, max(0,min(255,tr_alpha))),(8,8),max(1,8-i*2))
                sup.blit(ts,(tr_x-8,y-8))
            pygame.draw.circle(sup,(255,255,100),(x,y),5)

        # Chispas de impacto
        for imp in self.impactos[:]:
            ix2,iy2,ivx,ivy,ialpha,icol = imp
            imp[0] += ivx; imp[1] += ivy; imp[4] -= 18
            if imp[4] <= 0:
                self.impactos.remove(imp)
                continue
            a2 = max(0, min(255, int(imp[4])))
            is2 = pygame.Surface((8,8), pygame.SRCALPHA)
            pygame.draw.circle(is2, (*icol, a2), (4,4), 3)
            sup.blit(is2, (int(imp[0])-4, int(imp[1])-4))

        # Barra de vida solo si está dañada
        if self.vida < self.vida_max:
            bw = 36
            pygame.draw.rect(sup,(40,0,0),(x-bw//2, y-32, bw, 5),border_radius=2)
            vw = int(bw * self.vida/self.vida_max)
            col_vida = (255,80,80) if self.vida/self.vida_max < 0.35 else (200,80,200)
            pygame.draw.rect(sup,col_vida,(x-bw//2, y-32, vw, 5),border_radius=2)

    def recibir_danio(self, dmg):
        self.vida -= dmg
        # Generar chispas de impacto
        cols_chispa = [(255,255,100),(255,180,50),(200,100,255),(255,80,80)]
        for _ in range(5):
            ang = random.uniform(0, math.pi*2)
            spd = random.uniform(1.5, 4.0)
            col_c = random.choice(cols_chispa)
            self.impactos.append([
                self.x + random.randint(-8,8),
                self.y + random.randint(-8,8),
                math.cos(ang)*spd, math.sin(ang)*spd,
                220, col_c
            ])

    def actualizar(self):
        # Añadir partícula de trail
        if random.random() < 0.3:
            self.particulas.append([self.x+random.randint(-5,5), self.y+random.randint(-5,5), 60])
        # Desvanecer partículas
        self.particulas = [[px,py,a-8] for px,py,a in self.particulas if a>8]


# ─── CLASE DEFENSOR ────────────────────────────────────────────────────────────
class Defender:
    STATS = {
        "BUHO":   {"vida":150,"precio":50,  "desc":"Genera hojas"},  # PRECIO FIJO: 50
        "OSO":    {"vida":800,"precio":50,  "desc":"Tanque fuerte"},  # PRECIO FIJO: 50
        "CONEJO": {"vida":180,"precio":100,"desc":"Dispara rápido"},  # PRECIO FIJO: 100
        "ZORRO":  {"vida":200,"precio":200,"desc":"Fuego potente"},  # PRECIO FIJO: 200
    }
    def __init__(self, tipo, x, y, fila):
        self.tipo, self.x, self.y, self.fila = tipo, x, y, fila
        stats = self.STATS[tipo]
        self.vida = self.vida_max = stats["vida"]
        self.timer = random.randint(0,60)  # offset para que no disparen todos a la vez
        self.parpadeo = False
        self.parpadeo_t = 0
        self.hit_flash = 0  # flash rojo al recibir daño

    def recibir_danio(self, d):
        self.vida -= d
        self.hit_flash = 8

    def dibujar(self, sup, t):
        bob = math.sin(t*0.005 + self.x*0.01)*2.5
        ax, ay = int(self.x), int(self.y + bob)

        # Flash al recibir daño
        if self.hit_flash > 0:
            flash = pygame.Surface((60,60), pygame.SRCALPHA)
            pygame.draw.circle(flash,(255,80,80,100),(30,30),30)
            sup.blit(flash,(ax-30,ay-30))
            self.hit_flash -= 1

        # Glow del búho cuando está cargado
        if self.tipo == "BUHO" and self.timer > 200:
            g = pygame.Surface((80,80), pygame.SRCALPHA)
            alpha = int(60 + 40*math.sin(t*0.01))
            pygame.draw.circle(g,(255,240,80,alpha),(40,40),36)
            sup.blit(g,(ax-40,ay-40))

        self.parpadeo = (t - self.parpadeo_t) % 350 < 10
        dibujar_animal(sup, self.tipo, ax, ay, 0.52, parpadeo=self.parpadeo)

        # Barra de vida
        if self.vida < self.vida_max:
            bw = 44
            pygame.draw.rect(sup,(40,0,0),(ax-bw//2, ay+30, bw, 6),border_radius=3)
            vw = max(0, int(bw * self.vida/self.vida_max))
            c = (80,255,80) if self.vida/self.vida_max > 0.5 else (255,180,30) if self.vida/self.vida_max > 0.25 else (255,60,60)
            pygame.draw.rect(sup,c,(ax-bw//2, ay+30, vw, 6),border_radius=3)


# ─── PROYECTILES ───────────────────────────────────────────────────────────────
class Proyectil:
    def __init__(self, x, y, tipo, fila):
        self.x, self.y, self.tipo, self.fila = float(x), float(y), tipo, fila
        self.trail = []
    def mover(self, spd=1):
        self.trail.append((self.x, self.y))
        if len(self.trail) > 8: self.trail.pop(0)
        self.x += (9 if self.tipo == "BELLOTA" else 7) * spd
    def dibujar(self, sup):
        if self.tipo == "BELLOTA":
            # Trail de hoja
            for i,(tx,ty) in enumerate(self.trail):
                alpha = int(40 + i*20)
                ts = pygame.Surface((10,10),pygame.SRCALPHA)
                pygame.draw.circle(ts,(160,120,60,alpha),(5,5),4-i//3)
                sup.blit(ts,(int(tx)-5,int(ty)-5))
            # Bellota con capucho
            x,y = int(self.x), int(self.y)
            pygame.draw.ellipse(sup,(139,80,25),(x-5,y-2,10,14))
            pygame.draw.ellipse(sup,(101,55,20),(x-7,y-4,14,8))
            pygame.draw.line(sup,(80,50,20),(x,y-4),(x+2,y-10),2)
        else:  # FUEGO
            for i,(tx,ty) in enumerate(self.trail):
                alpha = int(30+i*25)
                ts = pygame.Surface((20,20),pygame.SRCALPHA)
                r = 8-i//2
                pygame.draw.circle(ts,(255,140,0,alpha),(10,10),r)
                sup.blit(ts,(int(tx)-10,int(ty)-10))
            x,y = int(self.x), int(self.y)
            pygame.draw.circle(sup,(255,80,0),(x,y),10)
            pygame.draw.circle(sup,(255,220,50),(x,y),6)
            pygame.draw.circle(sup,(255,255,200),(x,y),3)


# ─── HOJA FLOTANTE ─────────────────────────────────────────────────────────────
class HojaFlotante:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)
        self.target_x, self.target_y = 58.0, 42.0
        self.rot = random.uniform(0, math.pi*2)
        self.wobble = random.uniform(0, math.pi*2)
    def mover_y_dibujar(self, sup, t):
        self.x += (self.target_x - self.x) * 0.07
        self.y += (self.target_y - self.y) * 0.07
        self.rot += 0.04
        # Dibuja hoja de otoño rotada
        lx, ly = int(self.x), int(self.y)
        pts = []
        for a in range(0,360,40):
            r2 = math.radians(a)
            r  = 12 if a%80==0 else 7
            pts.append((lx + int(math.cos(r2+self.rot)*r),
                        ly + int(math.sin(r2+self.rot)*r)))
        pygame.draw.polygon(sup, C_ORO, pts)
        pygame.draw.polygon(sup, (255,255,100), pts, 1)
        return math.hypot(self.x-self.target_x, self.y-self.target_y) < 12


# ─── FONDO OTOÑAL ──────────────────────────────────────────────────────────────
# Árboles de fondo precalculados
import random as _rnd; _rnd.seed(77)
ARBOLES_FONDO = [{'x':_rnd.randint(255,980),'y':_rnd.randint(40,100),
                  'r':_rnd.randint(22,40),'col':_rnd.choice([(190,80,20),(210,120,30),(180,60,20),(220,140,40)])}
                 for _ in range(12)]
_rnd.seed()

def dibujar_cafe_defensa(pantalla, t, vida_cafe, vida_cafe_max):
    """El café que hay que defender — fachada vertical en el borde izquierdo del campo."""
    # El café ocupa la franja x=255-295 a lo largo de toda la altura del campo
    CX = 256   # borde izquierdo del campo (panel termina en 255)
    CW = 42    # ancho del café (llega hasta ~298, grid empieza en 300)
    CY = INICIO_Y - 8
    CH = FILAS * CELDA_H + 16

    # Pulso de daño si vida baja
    vida_ratio = vida_cafe / vida_cafe_max
    if vida_ratio < 0.5:
        pulso = int(abs(math.sin(t*0.008)) * 40)
    else:
        pulso = 0

    # Pared trasera (madera oscura)
    pygame.draw.rect(pantalla, (80, 50, 28), (CX, CY, CW, CH))

    # Tejadillo superior del stand con listones
    teja_col = (160, 90, 35)
    for i in range(5):
        ty = CY - 12 + i*3
        pygame.draw.rect(pantalla, teja_col, (CX-4, ty, CW+8, 5))
    pygame.draw.rect(pantalla, (120, 65, 25), (CX-6, CY-14, CW+12, 6))

    # Mostrador (franja más oscura en el borde derecho)
    pygame.draw.rect(pantalla, (100, 62, 30), (CX + CW - 10, CY, 10, CH))

    # Ventanitas a lo largo del café (una por fila)
    for f in range(FILAS):
        wy = CY + f * CELDA_H + 15
        wh = 30
        ww = 20
        wx = CX + 5
        # Marco ventana
        pygame.draw.rect(pantalla, (60, 35, 15), (wx-1, wy-1, ww+2, wh+2), border_radius=3)
        # Cristal con efecto de luz interior cálida
        brillo = int(180 + 40*math.sin(t*0.002 + f*0.8))
        pygame.draw.rect(pantalla, (min(255,brillo), min(255,int(brillo*0.7)), 60), (wx, wy, ww, wh), border_radius=2)
        # Reflejo
        pygame.draw.line(pantalla, (255,255,200), (wx+3, wy+3), (wx+3, wy+wh-4), 1)
        pygame.draw.line(pantalla, (255,255,200), (wx+3, wy+3), (wx+ww-4, wy+3), 1)

    # Letrero "CAFE" vertical
    fnt_letrero = pygame.font.SysFont("Georgia", 11, True)
    letras = "CAFE"
    for li, letra in enumerate(letras):
        tl = fnt_letrero.render(letra, True, C_ORO)
        ly2 = CY + CH//2 - 30 + li*16
        pantalla.blit(tl, (CX + CW//2 - tl.get_width()//2 + 8, ly2))

    # Sin barra de vida: un enemigo que llega = derrota inmediata

    # Flash rojo si el café recibe daño (vida baja)
    if pulso > 0:
        flash = pygame.Surface((CW+8, CH+20), pygame.SRCALPHA)
        flash.fill((255, 50, 50, pulso))
        pantalla.blit(flash, (CX-4, CY-8))

    # Borde del mostrador
    pygame.draw.rect(pantalla, (130, 80, 35), (CX, CY, CW, CH), 2)


def dibujar_botones(pantalla, t, velocidad=1):
    """Botones Volver, Reiniciar y Velocidad — dibujados ENCIMA de todo lo demás."""
    fnt_btn = pygame.font.SysFont("Georgia", 14, True)
    # Fondo del area de botones (tapa cualquier carta que sobresalga)
    pygame.draw.rect(pantalla, (50,32,15), (0, ALTO-100, 254, 100))
    pygame.draw.line(pantalla, (110,70,30), (8, ALTO-102), (246, ALTO-102), 1)

    pygame.draw.line(pantalla, (80,55,25), (8, ALTO-97), (246, ALTO-97), 1)

    # ── Botón VOLVER ─────────────────────────────────────────────────────────
    bv = pygame.Rect(8, ALTO-90, 112, 36)
    hover_v = pygame.mouse.get_pos()[0] < 120 and pygame.mouse.get_pos()[1] > ALTO-90
    pygame.draw.rect(pantalla, (110,60,25) if hover_v else (80,45,18), bv, border_radius=8)
    pygame.draw.rect(pantalla, (200,140,60) if hover_v else (150,100,40), bv, 2, border_radius=8)
    tv = fnt_btn.render("< Volver", True, (240,200,130) if hover_v else (200,160,90))
    pantalla.blit(tv, (bv.centerx - tv.get_width()//2, bv.centery - tv.get_height()//2))

    # ── Botón REINICIAR ───────────────────────────────────────────────────────
    br = pygame.Rect(130, ALTO-90, 114, 36)
    hover_r = 130 < pygame.mouse.get_pos()[0] < 244 and pygame.mouse.get_pos()[1] > ALTO-90
    pygame.draw.rect(pantalla, (50,100,40) if hover_r else (38,72,28), br, border_radius=8)
    pygame.draw.rect(pantalla, (140,210,90) if hover_r else (100,160,60), br, 2, border_radius=8)
    tr2 = fnt_btn.render("Reiniciar", True, (200,240,150) if hover_r else (160,210,110))
    pantalla.blit(tr2, (br.centerx - tr2.get_width()//2, br.centery - tr2.get_height()//2))


def dibujar_fondo(pantalla, t):
    # Cielo crepuscular degradado
    for y in range(100):
        ratio = y/100
        r = int(80+ratio*40); g = int(50+ratio*20); b = int(60+ratio*10)
        pygame.draw.line(pantalla,(r,g,b),(255,y),(ANCHO,y))
    # Tierra otoñal
    for y in range(100, ALTO):
        ratio = (y-100)/(ALTO-100)
        r = int(55+ratio*10); g = int(38+ratio*5); b = int(25)
        pygame.draw.line(pantalla,(r,g,b),(255,y),(ANCHO,y))

    # Árboles de fondo
    for arb in ARBOLES_FONDO:
        pygame.draw.rect(pantalla,(60,35,15),(arb['x'],arb['y'],8,60))
        pygame.draw.circle(pantalla,arb['col'],(arb['x']+4,arb['y']),arb['r'])
        lighter = tuple(min(255,c+25) for c in arb['col'])
        pygame.draw.circle(pantalla,lighter,(arb['x']+4,arb['y']-8),arb['r']//2)
        # Hojitas caídas bajo el árbol (posición fija basada en índice)
        hoja_ox = (arb['x'] * 7 + arb['r'] * 3) % 40 - 20
        hoja_oy = (arb['x'] * 3 + arb['r']) % 38
        pygame.draw.ellipse(pantalla,arb['col'],(arb['x']+hoja_ox,arb['y']+arb['r']+hoja_oy,9,5))

    # Niebla suave en el horizonte
    niebla = pygame.Surface((ANCHO-255, 30), pygame.SRCALPHA)
    for ny in range(30):
        alpha = int(25*(1-ny/30))
        pygame.draw.line(niebla,(200,180,160,alpha),(0,ny),(ANCHO-255,ny))
    pantalla.blit(niebla,(255,85))


def dibujar_panel(pantalla, t):
    # Panel lateral de madera otoñal
    for y in range(ALTO):
        ratio = y/ALTO
        r = int(55+ratio*15); g = int(35+ratio*10); b = int(20+ratio*5)
        pygame.draw.line(pantalla,(r,g,b),(0,y),(250,y))

    # Vetas de madera
    for i in range(0,250,28):
        pygame.draw.line(pantalla,(70,48,28),(i,0),(i+8,ALTO),1)

    # Borde derecho del panel
    for bx in range(8):
        alpha = int(120*(1-bx/8))
        bs = pygame.Surface((1,ALTO),pygame.SRCALPHA)
        bs.fill((0,0,0,alpha))
        pantalla.blit(bs,(250+bx,0))

    # Decoración superior — banner colgante
    pygame.draw.rect(pantalla,(100,60,25),(10,0,230,65),border_radius=8)
    pygame.draw.rect(pantalla,(130,80,35),(10,0,230,65),2,border_radius=8)
    # Título "DEFENSORES" limpio
    fnt_banner = pygame.font.SysFont("Georgia",15,True)
    tb = fnt_banner.render("DEFENSORES", True, C_ORO)
    pantalla.blit(tb,(125-tb.get_width()//2, 8))
    # Línea decorativa
    pygame.draw.line(pantalla,C_ORO,(20,28),(230,28),1)
    # Hojitas dibujadas en las esquinas (no Unicode)
    for bx,by in [(22,14),(218,14),(22,48),(218,48)]:
        pts_h = []
        for a in range(0,360,90):
            r2 = math.radians(a)
            r  = 5 if a%180==0 else 3
            pts_h.append((bx+int(math.cos(r2)*r), by+int(math.sin(r2)*r)))
        pygame.draw.polygon(pantalla,C_ORO,pts_h)



def dibujar_cuadricula(pantalla, t):
    for f in range(FILAS):
        for c in range(COLUMNAS):
            rx = INICIO_X + c*CELDA_W
            ry = INICIO_Y + f*CELDA_H
            # Alternancia de hierba otoñal
            if (f+c)%2 == 0:
                col1 = (88,125,70); col2 = (78,115,62)
            else:
                col1 = (80,118,64); col2 = (72,110,58)
            pygame.draw.rect(pantalla,col1,(rx,ry,CELDA_W-2,CELDA_H-2),border_radius=6)
            # Briznas de hierba
            pygame.draw.rect(pantalla,col2,(rx+2,ry+2,CELDA_W-6,4),border_radius=2)
        # Hojas caídas decorativas en celdas (posiciones fijas)
        for f in range(FILAS):
            for c in range(COLUMNAS):
                rx = INICIO_X + c*CELDA_W
                ry = INICIO_Y + f*CELDA_H
                if (f+c*3+7) % 5 == 0:
                    pygame.draw.ellipse(pantalla,(140,80,25),(rx+10+c%5*3,ry+CELDA_H-14,10,6))
                if (f*3+c+2) % 7 == 0:
                    pygame.draw.ellipse(pantalla,(170,100,35),(rx+28+f%4*5,ry+CELDA_H-18,8,5))


# ─── COUNTER UI ────────────────────────────────────────────────────────────────
def dibujar_contador_hojas(pantalla, hojas, t):
    # Fondo sólido bien visible
    panel = pygame.Surface((200,56),pygame.SRCALPHA)
    pygame.draw.rect(panel,(20,12,5,230),(0,0,200,56),border_radius=10)
    pygame.draw.rect(panel,(180,140,40,180),(0,0,200,56),2,border_radius=10)
    pantalla.blit(panel,(5,5))

    # Hoja animada dibujada (no emoji)
    lx,ly = 30,33
    rot = math.sin(t*0.003)*0.4
    pts = []
    for a in range(0,360,45):
        r2 = math.radians(a)
        r  = 14 if a%90==0 else 9
        pts.append((lx+int(math.cos(r2+rot)*r), ly+int(math.sin(r2+rot)*r)))
    pygame.draw.polygon(pantalla,C_ORO,pts)
    pygame.draw.polygon(pantalla,(255,255,150),pts,1)
    # Nervio central de la hoja
    pygame.draw.line(pantalla,(200,160,30),
                     (lx+int(math.cos(rot+math.pi)*10), ly+int(math.sin(rot+math.pi)*10)),
                     (lx+int(math.cos(rot)*10), ly+int(math.sin(rot)*10)), 2)

    # Número con sombra para legibilidad
    fnt_num = pygame.font.SysFont("Georgia",34,True)
    snum = str(int(hojas))
    # Sombra oscura primero
    ts = fnt_num.render(snum, True, (30,15,5))
    pantalla.blit(ts,(52,13))
    # Texto dorado encima
    tt = fnt_num.render(snum, True, C_ORO)
    pantalla.blit(tt,(50,11))


def dibujar_barra_progreso(pantalla, progreso, estado):
    bx, by, bw, bh = INICIO_X+10, 10, COLUMNAS*CELDA_W-20, 22
    # Fondo
    pygame.draw.rect(pantalla,(25,15,8),(bx,by,bw,bh),border_radius=8)
    # Relleno de progreso
    fill_w = max(0, int(bw * progreso/100))
    if fill_w > 4:
        col_prog = (220,80,80) if estado.startswith("oleada") else (200,120,40)
        pygame.draw.rect(pantalla,col_prog,(bx+2,by+2,fill_w-4,bh-4),border_radius=6)
        # Brillo interior
        pygame.draw.rect(pantalla,tuple(min(255,c+60) for c in col_prog),(bx+2,by+2,fill_w-4,4),border_radius=4)
    # Borde dorado
    pygame.draw.rect(pantalla,C_ORO,(bx,by,bw,bh),2,border_radius=8)
    # Texto
    fnt_prog = pygame.font.SysFont("Georgia",13,True)
    if estado == "oleada_final_aviso":
        lbl = fnt_prog.render("¡¡ OLEADA FINAL !!", True,(255,100,100))
    else:
        lbl = fnt_prog.render(f"Oleada  {int(progreso)}%", True,(220,190,120))
    pantalla.blit(lbl,(bx+bw//2-lbl.get_width()//2, by+3))


def dibujar_tienda(pantalla, sel, hojas, t):
    TIPOS   = ["BUHO","OSO","CONEJO","ZORRO"]
    PRECIOS = {"BUHO":50,"OSO":50,"CONEJO":100,"ZORRO":200}  # PRECIOS FIJOS
    hojas_ganadas_final = 0
    velocidad = 1  # 1=normal, 2=x2, 3=x3
    NOMBRES = {"BUHO":"Buho","OSO":"Oso","CONEJO":"Conejo","ZORRO":"Zorro"}
    DESCS   = {"BUHO":"Genera hojas","OSO":"Tanque fuerte","CONEJO":"Dispara bellas","ZORRO":"Lanza fuego"}

    fnt_nom  = pygame.font.SysFont("Georgia", 16, True)
    fnt_desc = pygame.font.SysFont("Georgia", 12, False)
    fnt_prec = pygame.font.SysFont("Georgia", 15, True)

    carta_h = 100
    carta_gap = 6

    for i, tipo in enumerate(TIPOS):
        ry = 70 + i*(carta_h + carta_gap)
        rect = pygame.Rect(6, ry, 242, carta_h)
        precio = PRECIOS[tipo]
        puede  = hojas >= precio
        sel_   = (sel == tipo)

        # Fondo carta
        if sel_:
            pygame.draw.rect(pantalla,(125,88,42),rect,border_radius=10)
            # Glow dorado pulsante
            glow_a = int(50 + 30*math.sin(t*0.008))
            gsurf  = pygame.Surface((rect.w+10,rect.h+10), pygame.SRCALPHA)
            pygame.draw.rect(gsurf,(255,215,0,glow_a),(0,0,rect.w+10,rect.h+10),border_radius=12)
            pantalla.blit(gsurf,(rect.x-5,rect.y-5))
        else:
            bg = (72,48,25) if puede else (48,33,16)
            pygame.draw.rect(pantalla,bg,rect,border_radius=10)

        # Borde
        border_c = C_ORO if sel_ else ((150,110,55) if puede else (75,55,30))
        pygame.draw.rect(pantalla,border_c,rect,2,border_radius=10)

        # ── Animal centrado en mitad izquierda de la carta ──────────────────
        anim_cx = rect.x + 62
        anim_cy = rect.centery + (int(math.sin(t*0.005+i)*3) if sel_ else 0)
        dibujar_animal(pantalla, tipo, anim_cx, anim_cy, 0.52)

        # Separador vertical ligero
        pygame.draw.line(pantalla,(90,65,35),(rect.x+108,ry+10),(rect.x+108,ry+carta_h-10),1)

        # ── Texto en mitad derecha ──────────────────────────────────────────
        tx = rect.x + 120
        col_nom = (60,35,10) if sel_ else (C_ORO if puede else (130,95,55))

        # Nombre
        tn = fnt_nom.render(NOMBRES[tipo], True, col_nom)
        pantalla.blit(tn,(tx, ry+14))

        # Descripción
        td = fnt_desc.render(DESCS[tipo], True, (40,25,8) if sel_ else (175,145,95))
        pantalla.blit(td,(tx, ry+34))

        # Precio — hoja dibujada + número
        leaf_x, leaf_y = tx, ry+54
        # Dibujamos hoja pequeña
        rot_l = math.sin(t*0.003)*0.2
        lpts = []
        for a in range(0,360,60):
            r2 = math.radians(a)
            r  = 9 if a%120==0 else 6
            lpts.append((leaf_x+7+int(math.cos(r2+rot_l)*r), leaf_y+7+int(math.sin(r2+rot_l)*r)))
        leaf_col = C_ORO if puede else (130,100,50)
        pygame.draw.polygon(pantalla,leaf_col,lpts)

        tpr = fnt_prec.render(str(precio), True, leaf_col)
        pantalla.blit(tpr,(leaf_x+19, leaf_y-1))

        # "SIN FONDOS" si no puede pagar
        if not puede:
            tno = fnt_desc.render("Sin fondos", True,(200,80,80))
            pantalla.blit(tno,(tx, ry+85))


# ─── CUENTA ATRÁS ──────────────────────────────────────────────────────────────
def dibujar_cuenta_atras(pantalla, elapsed, t):
    # Overlay semitransparente
    overlay = pygame.Surface((ANCHO-255,ALTO),pygame.SRCALPHA)
    overlay.fill((0,0,0,100))
    pantalla.blit(overlay,(255,0))

    fnt_big = pygame.font.SysFont("Georgia",90,True)
    fnt_sub = pygame.font.SysFont("Georgia",28,True)

    if elapsed < 1000:
        num,sub_txt = "3","¡Coloca tus defensores!"
        col_num = (255,220,80)
    elif elapsed < 2000:
        num,sub_txt = "2","¡Las sombras se acercan!"
        col_num = (255,160,60)
    else:
        num,sub_txt = "1","¡Defiende!"
        col_num = (255,80,80)

    # Escala de aparición (bounce)
    frac = (elapsed % 1000) / 1000
    scale_f = 1.0 + math.sin(frac*math.pi)*0.15

    txt_s = fnt_big.render(num, True, col_num)
    # Sombra
    sombra_s = fnt_big.render(num, True, (0,0,0))
    cx,cy = 255 + (ANCHO-255)//2, ALTO//2
    pantalla.blit(sombra_s,(cx - txt_s.get_width()//2 + 3, cy - txt_s.get_height()//2 + 3))
    pantalla.blit(txt_s,  (cx - txt_s.get_width()//2,     cy - txt_s.get_height()//2))

    if sub_txt:
        ts = fnt_sub.render(sub_txt, True, (220,200,180))
        pantalla.blit(ts,(cx-ts.get_width()//2, cy+55))


# ─── PANTALLA FINAL ────────────────────────────────────────────────────────────
def dibujar_fin(pantalla, estado, t):
    # Overlay opaco completo - tapa TODO
    pantalla.fill((18, 12, 6))

    cx = ANCHO // 2
    cy = ALTO // 2

    if estado == "victoria":
        # Fondo suave dorado centrado
        glow = pygame.Surface((600, 320), pygame.SRCALPHA)
        pygame.draw.rect(glow, (60, 45, 10, 180), (0, 0, 600, 320), border_radius=24)
        pygame.draw.rect(glow, (180, 140, 30, 120), (0, 0, 600, 320), 2, border_radius=24)
        pantalla.blit(glow, (cx-300, cy-160))

        # Título
        fnt_titulo = pygame.font.SysFont("Georgia", 80, True)
        titulo = fnt_titulo.render("¡VICTORIA!", True, (120, 255, 160))
        sombra = fnt_titulo.render("¡VICTORIA!", True, (0, 60, 20))
        pantalla.blit(sombra, (cx - titulo.get_width()//2 + 3, cy - 120 + 3))
        pantalla.blit(titulo, (cx - titulo.get_width()//2,     cy - 120))

        # Línea separadora
        pygame.draw.line(pantalla, (100, 180, 80), (cx-200, cy-28), (cx+200, cy-28), 1)

        # Subtítulo
        fnt_sub = pygame.font.SysFont("Georgia", 22, False)
        sub = fnt_sub.render("Las sombras han sido derrotadas", True, (180, 220, 170))
        pantalla.blit(sub, (cx - sub.get_width()//2, cy - 10))

        # Premio
        fnt_premio = pygame.font.SysFont("Georgia", 30, True)
        # Hoja dibujada inline
        pygame.draw.polygon(pantalla, C_ORO, [
            (cx-95, cy+42),(cx-88, cy+32),(cx-80, cy+42),(cx-88, cy+52)])
        premio = fnt_premio.render("+250 hojas", True, C_ORO)
        pantalla.blit(premio, (cx - premio.get_width()//2 + 8, cy + 28))

        # Botón clic parpadeante
        if (t//500) % 2 == 0:
            fnt_btn = pygame.font.SysFont("Georgia", 18, True)
            btn_r = pygame.Rect(cx-140, cy+88, 280, 36)
            pygame.draw.rect(pantalla, (40, 80, 40), btn_r, border_radius=10)
            pygame.draw.rect(pantalla, (100, 200, 80), btn_r, 2, border_radius=10)
            tb = fnt_btn.render("Haz clic para jugar de nuevo", True, (160, 240, 130))
            pantalla.blit(tb, (btn_r.centerx - tb.get_width()//2, btn_r.centery - tb.get_height()//2))

    else:  # derrota
        # Fondo rojizo
        glow = pygame.Surface((560, 280), pygame.SRCALPHA)
        pygame.draw.rect(glow, (50, 10, 10, 180), (0, 0, 560, 280), border_radius=20)
        pygame.draw.rect(glow, (150, 40, 40, 120), (0, 0, 560, 280), 2, border_radius=20)
        pantalla.blit(glow, (cx-280, cy-140))

        fnt_titulo = pygame.font.SysFont("Georgia", 72, True)
        titulo = fnt_titulo.render("¡DERROTA!", True, (255, 90, 90))
        sombra = fnt_titulo.render("¡DERROTA!", True, (80, 0, 0))
        pantalla.blit(sombra, (cx - titulo.get_width()//2 + 3, cy - 100 + 3))
        pantalla.blit(titulo, (cx - titulo.get_width()//2,     cy - 100))

        pygame.draw.line(pantalla, (180, 60, 60), (cx-180, cy-18), (cx+180, cy-18), 1)

        fnt_sub = pygame.font.SysFont("Georgia", 22, False)
        sub = fnt_sub.render("Las sombras han cruzado el cafe...", True, (200, 150, 150))
        pantalla.blit(sub, (cx - sub.get_width()//2, cy + 2))

        if (t//500) % 2 == 0:
            fnt_btn = pygame.font.SysFont("Georgia", 18, True)
            btn_r = pygame.Rect(cx-120, cy+60, 240, 36)
            pygame.draw.rect(pantalla, (60, 20, 20), btn_r, border_radius=10)
            pygame.draw.rect(pantalla, (180, 60, 60), btn_r, 2, border_radius=10)
            tb = fnt_btn.render("Haz clic para reintentar", True, (240, 150, 150))
            pantalla.blit(tb, (btn_r.centerx - tb.get_width()//2, btn_r.centery - tb.get_height()//2))


# ─── RESET ─────────────────────────────────────────────────────────────────────
def reset_game(t_actual):
    return 200, [], [], [], [], "BUHO", 600, "cuenta_atras", 0.0, t_actual, 500, 500


# ─── MAIN ──────────────────────────────────────────────────────────────────────
def ejecutar_defensa(pantalla, reloj):
    """Minijuego de defensa. Devuelve hojas ganadas (250 si victoria, 0 si derrota)."""
    pygame.display.set_caption("Torre de Defensa del Bosque")
    # Adaptar al tamaño real de la pantalla
    global ANCHO, ALTO, INICIO_X, INICIO_Y
    ANCHO, ALTO = pantalla.get_size()
    INICIO_X = 300
    INICIO_Y = max(80, (ALTO - FILAS * CELDA_H) // 2)

    (hojas, defensores, enemigos, proyectiles,
     hojas_flotantes, sel, spawn_timer,
     estado, progreso, t_inicio_cuenta,
     vida_cafe, vida_cafe_max) = reset_game(pygame.time.get_ticks())

    PRECIOS = {"BUHO":50,"OSO":50,"CONEJO":100,"ZORRO":200}  # PRECIOS FIJOS
    hojas_ganadas_final = 0
    velocidad = 1  # 1=normal, 2=x2, 3=x3

    while True:
        t = pygame.time.get_ticks()
        mx, my = pygame.mouse.get_pos()

        for e in pygame.event.get():
            if e.type == pygame.QUIT: return
            if e.type == pygame.MOUSEBUTTONDOWN:
                # Botón velocidad (zona negra bajo el campo)
                campo_bottom = INICIO_Y + FILAS*CELDA_H
                if pygame.Rect(INICIO_X+10, campo_bottom+15, 130, 34).collidepoint(e.pos):
                    velocidad = (velocidad % 3) + 1

                # Botón Volver — siempre disponible
                if pygame.Rect(8, ALTO-90, 112, 36).collidepoint(e.pos):
                    return 0  # volver sin premio

                # Botón Reiniciar — siempre disponible
                if pygame.Rect(126, ALTO-90, 116, 36).collidepoint(e.pos):
                    (hojas, defensores, enemigos, proyectiles,
                     hojas_flotantes, sel, spawn_timer,
                     estado, progreso, t_inicio_cuenta,
                     vida_cafe, vida_cafe_max) = reset_game(t)
                    continue

                if estado in ("derrota","victoria"):
                    return hojas_ganadas_final
                if estado == "jugando":
                    if mx < 250:
                        # Clic en tienda
                        TIPOS = ["BUHO","OSO","CONEJO","ZORRO"]
                        for i, tipo in enumerate(TIPOS):
                            carta_sz = 100+6  # carta_h + carta_gap
                            if 70+i*carta_sz < my < 70+i*carta_sz+100:
                                sel = tipo; break
                    elif mx >= INICIO_X:
                        # Colocar defensor
                        col_idx = (mx-INICIO_X)//CELDA_W
                        fil_idx = (my-INICIO_Y)//CELDA_H
                        if 0<=fil_idx<FILAS and 0<=col_idx<COLUMNAS:
                            px2 = INICIO_X + col_idx*CELDA_W + CELDA_W//2
                            py2 = INICIO_Y + fil_idx*CELDA_H + CELDA_H//2
                            precio_sel = PRECIOS[sel]
                            if hojas >= precio_sel and not any(d.fila==fil_idx and d.x==px2 for d in defensores):
                                hojas -= precio_sel
                                defensores.append(Defender(sel, px2, py2, fil_idx))

        # ── LÓGICA ──────────────────────────────────────────────────────────────
        if estado in ("derrota","victoria"):
            pass  # juego parado, esperar clic
        elif estado == "cuenta_atras":
            if t - t_inicio_cuenta > 3000:
                estado = "jugando"

        elif estado in ("jugando","oleada_final_activa","oleada_final_aviso"):
            progreso = min(100.0, progreso + 0.012)
            spawn_timer -= velocidad
            if spawn_timer <= 0 and estado == "jugando":
                enemigos.append(Sombra(random.randint(0,FILAS-1)))
                spawn_timer = max(80, int(380 - progreso*1.8))
            if progreso >= 100 and estado == "jugando":
                estado = "oleada_final_activa"
                for _ in range(12):
                    enemigos.append(Sombra(random.randint(0,FILAS-1)))

            # Mover proyectiles y colisiones
            for p in proyectiles[:]:
                p.mover(velocidad)
                if p.x > ANCHO+20:
                    proyectiles.remove(p); continue
                for ene in enemigos[:]:
                    if ene.fila == p.fila and abs(p.x - ene.x) < 28:
                        dmg = 35 if p.tipo == "BELLOTA" else 70
                        ene.recibir_danio(dmg)
                        if p in proyectiles: proyectiles.remove(p)
                        if ene.vida <= 0 and ene in enemigos: enemigos.remove(ene)
                        break

            # Defensores actúan
            for d in defensores[:]:
                d.timer += 1
                if d.tipo == "BUHO" and d.timer >= 300:
                    hojas_flotantes.append(HojaFlotante(d.x, d.y))
                    d.timer = 0
                elif d.tipo in ("CONEJO","ZORRO"):
                    cd = 65 if d.tipo=="CONEJO" else 120
                    if d.timer >= cd:
                        if any(ene.fila==d.fila and d.x < ene.x < INICIO_X + COLUMNAS*CELDA_W for ene in enemigos):
                            tipo_p = "BELLOTA" if d.tipo=="CONEJO" else "FUEGO"
                            proyectiles.append(Proyectil(d.x+22, d.y, tipo_p, d.fila))
                            d.timer = 0

            # Enemigos avanzan o muerden
            for ene in enemigos[:]:
                ene.actualizar()
                mordiendo = False
                for d in defensores[:]:
                    if d.fila==ene.fila and abs(d.x-ene.x) < 38:
                        mordiendo = True
                        d.recibir_danio(0.6)
                        if d.vida <= 0 and d in defensores:
                            defensores.remove(d)
                        break
                if not mordiendo:
                    ene.x -= ene.vel * velocidad
                if ene.x < INICIO_X - 2:
                    if ene in enemigos: enemigos.remove(ene)
                    estado = "derrota"
                    break  # salir del bucle inmediatamente

            # Victoria: solo si no hay derrota Y oleada final terminó
            if estado == "oleada_final_activa" and len(enemigos) == 0:
                estado = "victoria"
                hojas += 250  # recompensa por ganar
                hojas_ganadas_final = 250

        # ── DIBUJADO ────────────────────────────────────────────────────────────
        pantalla.fill((40,28,18))

        # Fondo
        dibujar_fondo(pantalla, t)
        dibujar_panel(pantalla, t)
        dibujar_cuadricula(pantalla, t)
        dibujar_cafe_defensa(pantalla, t, vida_cafe, vida_cafe_max)

        # Objetos de juego
        for p in proyectiles: p.dibujar(pantalla)
        for ene in enemigos:  ene.dibujar(pantalla, t)
        for d in defensores:  d.dibujar(pantalla, t)
        for h in hojas_flotantes[:]:
            if h.mover_y_dibujar(pantalla, t):
                hojas += 25
                hojas_flotantes.remove(h)

        # Preview al colocar
        if (INICIO_X < mx < INICIO_X + COLUMNAS*CELDA_W and
                INICIO_Y < my < INICIO_Y + FILAS*CELDA_H and
                estado == "jugando"):
            c2 = (mx-INICIO_X)//CELDA_W; f2 = (my-INICIO_Y)//CELDA_H
            px3 = INICIO_X + c2*CELDA_W + CELDA_W//2
            py3 = INICIO_Y + f2*CELDA_H + CELDA_H//2
            prev = pygame.Surface((110,110),pygame.SRCALPHA)
            dibujar_animal(prev, sel, 55, 55, 0.52)
            prev.set_alpha(140)
            pantalla.blit(prev,(px3-55,py3-55))
            # Highlight de celda
            pygame.draw.rect(pantalla,(255,255,150,80) if False else (255,255,150),
                             (INICIO_X+c2*CELDA_W, INICIO_Y+f2*CELDA_H, CELDA_W-2, CELDA_H-2),
                             2, border_radius=6)

        # UI
        dibujar_tienda(pantalla, sel, hojas, t)
        dibujar_contador_hojas(pantalla, hojas, t)
        dibujar_barra_progreso(pantalla, progreso, estado)

        # Cuenta atrás
        if estado == "cuenta_atras":
            dibujar_cuenta_atras(pantalla, t - t_inicio_cuenta, t)

        # Pantalla final
        if estado in ("derrota","victoria"):
            dibujar_fin(pantalla, estado, t)

        # Botón velocidad en zona negra bajo el campo
        campo_bottom = INICIO_Y + FILAS*CELDA_H
        bspd2 = pygame.Rect(INICIO_X+10, campo_bottom+15, 130, 34)
        spd_cols2   = {1:(30,30,60), 2:(55,55,15), 3:(80,25,10)}
        spd_border2 = {1:(100,100,200), 2:(200,200,40), 3:(255,120,40)}
        spd_labels2 = {1:"x1", 2:"x2", 3:"x3"}
        pygame.draw.rect(pantalla, spd_cols2[velocidad], bspd2, border_radius=10)
        pygame.draw.rect(pantalla, spd_border2[velocidad], bspd2, 2, border_radius=10)
        # Icono rayo
        rx2 = bspd2.x+16; ry2 = bspd2.centery
        pygame.draw.polygon(pantalla, spd_border2[velocidad],
            [(rx2,ry2-9),(rx2-4,ry2+1),(rx2+1,ry2+1),(rx2-2,ry2+10),(rx2+6,ry2-1),(rx2+1,ry2-1)])
        fnt_spd2 = pygame.font.SysFont("Georgia", 18, True)
        ts_spd = fnt_spd2.render(spd_labels2[velocidad], True, spd_border2[velocidad])
        pantalla.blit(ts_spd, (bspd2.x+32, bspd2.centery - ts_spd.get_height()//2))

        dibujar_botones(pantalla, t, velocidad)
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    pygame.init()
    _pantalla = pygame.display.set_mode((ANCHO, ALTO))
    _reloj = pygame.time.Clock()
    resultado = ejecutar_defensa(_pantalla, _reloj)
    print(f"Hojas ganadas: {resultado}")
