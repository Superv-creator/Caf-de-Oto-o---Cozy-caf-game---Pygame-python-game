import pygame, math, random, constantes as c
from idiomas import t, nombres_mejoras

class Moneda:
    def __init__(self):
        self.x = random.randint(450, 900)
        self.y = -50
        self.rect = pygame.Rect(self.x-22, self.y-22, 44, 44)

    def actualizar(self):
        if self.y < 540: self.y += 3
        self.rect.center = (self.x, int(self.y))

    def dibujar(self, sup):
        pygame.draw.circle(sup, (218,165,32), (self.x, int(self.y)), 20)
        pygame.draw.circle(sup, (255,215,0),  (self.x, int(self.y)), 17)
        t2 = c.fuente_menu.render("¥", True, (100,70,0))
        sup.blit(t2, (self.x-t2.get_width()//2, int(self.y)-t2.get_height()//2))


def dibujar_icono_mejora(sup, id_mejora, cx, cy):
    if id_mejora == 0:
        pygame.draw.rect(sup,(160,100,40),(cx-10,cy+2,20,6),border_radius=2)
        pygame.draw.rect(sup,(100,60,20),(cx-2,cy-8,4,12))
        pygame.draw.polygon(sup,(180,130,60),[(cx-8,cy-8),(cx+8,cy-8),(cx+6,cy-14),(cx-6,cy-14)])
    elif id_mejora == 1:
        pygame.draw.ellipse(sup,(200,40,40),(cx-6,cy-14,12,20))
        pygame.draw.ellipse(sup,(230,80,80),(cx-6,cy-14,12,8))
        pygame.draw.ellipse(sup,(230,80,80),(cx-6,cy+2,12,8))
        pygame.draw.line(sup,(150,30,30),(cx,cy-14),(cx,cy-20),2)
        pygame.draw.circle(sup,(255,240,100),(cx,cy-4),3)
    elif id_mejora == 2:
        pygame.draw.ellipse(sup,(160,100,50),(cx-10,cy-14,20,8))
        pygame.draw.line(sup,(100,60,20),(cx-7,cy-10),(cx-7,cy+8),2)
        pygame.draw.line(sup,(100,60,20),(cx+7,cy-10),(cx+7,cy+8),2)
        pygame.draw.line(sup,(100,60,20),(cx-7,cy+2),(cx+7,cy+2),2)
    elif id_mejora == 3:
        pygame.draw.circle(sup,(220,220,220),(cx,cy),10)
        pygame.draw.polygon(sup,(220,220,220),[(cx-10,cy-6),(cx-6,cy-16),(cx-2,cy-6)])
        pygame.draw.polygon(sup,(220,220,220),[(cx+2,cy-6),(cx+6,cy-16),(cx+10,cy-6)])
        pygame.draw.circle(sup,(0,0,0),(cx-4,cy-2),2)
        pygame.draw.circle(sup,(0,0,0),(cx+4,cy-2),2)
        pygame.draw.polygon(sup,(255,150,160),[(cx-2,cy+3),(cx+2,cy+3),(cx,cy+6)])
    elif id_mejora == 4:
        pygame.draw.rect(sup,(80,45,20),(cx-8,cy-6,16,14),border_radius=3)
        pygame.draw.ellipse(sup,(60,35,10),(cx-8,cy-6,16,8))
        pygame.draw.arc(sup,(100,60,30),(cx+6,cy-4,8,10),-math.pi/2,math.pi/2,2)
        pygame.draw.line(sup,(200,200,200),(cx-3,cy-8),(cx-2,cy-14),1)
        pygame.draw.line(sup,(200,200,200),(cx+3,cy-8),(cx+4,cy-14),1)


class Mejora:
    def __init__(self, id, noms, pre, apt):
        self.id   = id
        self.noms = noms
        self.precio = pre
        self.apt    = apt
        self.nivel  = 0
        self.rect   = pygame.Rect(20, 115 + (id * 97), 360, 85)

    def es_max(self):
        return self.nivel >= len(self.noms)

    def dibujar(self, sup):
        mxed  = self.es_max()
        mouse = pygame.mouse.get_pos()
        cf    = (60, 45, 45)
        if self.rect.collidepoint(mouse) and not mxed:
            cf = (85, 60, 60)
        pygame.draw.rect(sup, cf, self.rect, border_radius=12)
        pygame.draw.rect(sup, (180,140,140), self.rect, 2, border_radius=12)
        dibujar_icono_mejora(sup, self.id, self.rect.x+32, self.rect.y+42)
        idx = min(self.nivel, len(self.noms)-1)
        sup.blit(c.fuente_menu.render(self.noms[idx], True, (255,255,255)),
                 (self.rect.x+68, self.rect.y+18))
        if mxed:
            sup.blit(c.fuente_menu.render(t("max"), True, (100,255,100)),
                     (self.rect.x+68, self.rect.y+48))
        else:
            color_precio = (255,215,0) if c.dinero >= self.precio else (200,80,80)
            sup.blit(c.fuente_menu.render(
                t("coste", c.format_esp(self.precio)), True, color_precio),
                (self.rect.x+68, self.rect.y+48))


# ── Decoraciones del café ──────────────────────────────────────────────────────

def dibujar_farolillo(sup, x, y, t_ms):
    glow = pygame.Surface((50,50), pygame.SRCALPHA)
    alpha = int(120 + 60*math.sin(t_ms*0.004))
    pygame.draw.circle(glow,(255,200,80,alpha),(25,25),22)
    sup.blit(glow,(x-25,y-25))
    pygame.draw.ellipse(sup,(200,40,40),(x-12,y-18,24,36))
    pygame.draw.ellipse(sup,(220,60,60),(x-10,y-14,20,28))
    for oy in [-8,0,8]: pygame.draw.line(sup,(240,100,100),(x-11,y+oy),(x+11,y+oy),1)
    pygame.draw.rect(sup,(160,20,20),(x-10,y-20,20,6),border_radius=2)
    pygame.draw.rect(sup,(160,20,20),(x-10,y+14,20,6),border_radius=2)
    pygame.draw.line(sup,(120,60,30),(x,y-20),(x,y-32),2)
    for fx in range(x-8,x+10,4): pygame.draw.line(sup,(220,100,50),(fx,y+20),(fx-1,y+28),1)
    pygame.draw.circle(sup,(255,240,150),(x,y),5)


def dibujar_vela(sup, x, y, t_ms):
    pygame.draw.ellipse(sup,(200,180,150),(x-10,y+8,20,8))
    pygame.draw.rect(sup,(255,250,240),(x-6,y-8,12,18),border_radius=2)
    pygame.draw.ellipse(sup,(240,230,210),(x-6,y-8,12,6))
    pygame.draw.line(sup,(80,60,40),(x,y-8),(x,y-12),1)
    flicker = math.sin(t_ms*0.015)*1.5
    pygame.draw.polygon(sup,(255,200,50),
        [(x-3,y-12),(x+3,y-12),(x+int(2+flicker),y-20),(x,y-22),(x-int(2+flicker),y-20)])
    pygame.draw.polygon(sup,(255,120,30),[(x-1,y-13),(x+1,y-13),(x,y-19)])
    h = pygame.Surface((20,20),pygame.SRCALPHA)
    pygame.draw.circle(h,(255,220,80,60),(10,10),10)
    sup.blit(h,(x-10,y-22))


def dibujar_guirnalda(sup, x1, y, x2, t_ms):
    puntos = 20
    colores = [(255,80,80),(255,200,50),(100,200,255),(200,100,255),(100,255,150)]
    for i in range(puntos):
        tp = i/(puntos-1)
        bx = int(x1+(x2-x1)*tp)
        by = int(y+18*math.sin(math.pi*tp))
        if i > 0:
            tpp = (i-1)/(puntos-1)
            bxp = int(x1+(x2-x1)*tpp)
            byp = int(y+18*math.sin(math.pi*tpp))
            pygame.draw.line(sup,(80,80,80),(bxp,byp),(bx,by),1)
        if i % 3 == 0:
            col = colores[(i//3) % len(colores)]
            fl  = 0.7+0.3*math.sin(t_ms*0.005+i*0.8)
            bc  = tuple(min(255,int(co*fl)) for co in col)
            g2  = pygame.Surface((14,14),pygame.SRCALPHA)
            pygame.draw.circle(g2,(*col,60),(7,7),7)
            sup.blit(g2,(bx-7,by-7))
            pygame.draw.circle(sup,bc,(bx,by),4)
            pygame.draw.circle(sup,(255,255,220),(bx-1,by-1),1)
            pygame.draw.line(sup,(120,120,120),(bx,by-4),(bx,by-7),1)


def dibujar_jarron_flores(sup, x, y, t_ms):
    pygame.draw.polygon(sup,(160,100,60),
        [(x-6,y+18),(x+6,y+18),(x+9,y+8),(x+7,y-5),(x+10,y-10),(x+10,y-18),
         (x-10,y-18),(x-10,y-10),(x-7,y-5),(x-9,y+8)])
    pygame.draw.ellipse(sup,(180,120,70),(x-10,y-20,20,6))
    pygame.draw.ellipse(sup,(140,85,50),(x-7,y+15,14,5))
    pygame.draw.line(sup,(200,140,80),(x-6,y),(x+6,y),1)
    flores = [{"ox":-8,"col":(220,60,60)},{"ox":0,"col":(255,170,40)},
              {"ox":8,"col":(200,80,160)},{"ox":-4,"col":(255,220,50)},{"ox":5,"col":(100,160,220)}]
    for i, fl in enumerate(flores):
        swing = math.sin(t_ms*0.0015+i*1.2)*3
        fx = x+fl["ox"]+int(swing); fy = y-18-i*4
        pygame.draw.line(sup,(70,140,70),(x+fl["ox"]//2,y-17),(fx,fy),1)
        for ang in range(0,360,72):
            r2 = math.radians(ang)
            pygame.draw.circle(sup,fl["col"],(fx+int(math.cos(r2)*4),fy+int(math.sin(r2)*4)),3)
        pygame.draw.circle(sup,(255,255,200),(fx,fy),2)


gato_cola_off = random.uniform(0, math.pi*2)

def dibujar_gato(sup, gx, gy, l3, t_ms, parpadeo):
    col = (240,240,240)
    cola_ang = math.sin(t_ms*0.003+gato_cola_off)*0.6
    cx_b=gx+18; cy_b=gy+8
    cx_m=cx_b+int(math.sin(cola_ang*0.5)*17); cy_m=cy_b-int(math.cos(cola_ang*0.5)*12)
    cx_t=cx_b+int(math.sin(cola_ang)*28);     cy_t=cy_b-int(math.cos(cola_ang)*19)
    pygame.draw.line(sup,col,(cx_b,cy_b),(cx_m,cy_m),5)
    pygame.draw.line(sup,col,(cx_m,cy_m),(cx_t,cy_t),4)
    pygame.draw.circle(sup,col,(cx_t,cy_t),4)
    pygame.draw.ellipse(sup,col,(gx-18,gy+15,14,10))
    pygame.draw.ellipse(sup,col,(gx+4,gy+15,14,10))
    pygame.draw.ellipse(sup,col,(gx-22,gy-10,44,38))
    pygame.draw.circle(sup,col,(gx,gy-18),18)
    pygame.draw.polygon(sup,col,[(gx-16,gy-30),(gx-8,gy-48),(gx-2,gy-30)])
    pygame.draw.polygon(sup,col,[(gx+2,gy-30),(gx+8,gy-48),(gx+16,gy-30)])
    pygame.draw.polygon(sup,(255,180,190),[(gx-13,gy-31),(gx-8,gy-43),(gx-4,gy-31)])
    pygame.draw.polygon(sup,(255,180,190),[(gx+4,gy-31),(gx+8,gy-43),(gx+13,gy-31)])
    pygame.draw.polygon(sup,(255,150,160),[(gx-3,gy-18),(gx+3,gy-18),(gx,gy-15)])
    for bx2,ex,ey in [(-4,-22,-19),(-4,-22,-14),(4,22,-19),(4,22,-14)]:
        pygame.draw.line(sup,(150,150,150),(gx+bx2,gy-15),(gx+ex,gy+ey),1)
    pygame.draw.line(sup,(180,100,120),(gx,gy-15),(gx,gy-12),1)
    pygame.draw.arc(sup,(160,80,100),(gx-7,gy-14,7,6), math.pi, 2*math.pi, 2)
    pygame.draw.arc(sup,(160,80,100),(gx,gy-14,7,6),   math.pi, 2*math.pi, 2)
    if parpadeo:
        pygame.draw.arc(sup,(50,50,50),(gx-16,gy-24,10,8),0,math.pi,2)
        pygame.draw.arc(sup,(50,50,50),(gx+6,gy-24,10,8),0,math.pi,2)
    else:
        pygame.draw.circle(sup,(60,160,60),(gx-11,gy-20),6)
        pygame.draw.circle(sup,(60,160,60),(gx+11,gy-20),6)
        pygame.draw.circle(sup,(0,0,0),(gx-11,gy-20),3)
        pygame.draw.circle(sup,(0,0,0),(gx+11,gy-20),3)
        pygame.draw.circle(sup,(255,255,255),(gx-9,gy-22),2)
        pygame.draw.circle(sup,(255,255,255),(gx+13,gy-22),2)
    pygame.draw.ellipse(sup,(255,180,180),(gx-18,gy-12,8,5))
    pygame.draw.ellipse(sup,(255,180,180),(gx+10,gy-12,8,5))
    if l3 >= 2:
        pygame.draw.polygon(sup,(200,50,50),[(gx-12,gy-4),(gx+12,gy-4),(gx,gy+8)])
        pygame.draw.line(sup,(220,70,70),(gx-12,gy-4),(gx+12,gy-4),2)
    if l3 >= 3:
        pygame.draw.rect(sup,(40,40,45),(gx-10,gy-38,20,8),border_radius=2)
        pygame.draw.rect(sup,(50,50,55),(gx-8,gy-44,16,8),border_radius=2)
        pygame.draw.line(sup,(200,180,50),(gx+6,gy-44),(gx+10,gy-52),2)
    if l3 >= 4:
        pygame.draw.polygon(sup,(220,200,180),[(gx-10,gy-4),(gx+10,gy-4),(gx+13,gy+20),(gx-13,gy+20)])
        pygame.draw.line(sup,(200,180,160),(gx-8,gy-4),(gx-8,gy-15),1)
        pygame.draw.line(sup,(200,180,160),(gx+8,gy-4),(gx+8,gy-15),1)


def dibujar_cafe(pantalla, t_ms, celebrando, gato_parpadeo_dur):
    pygame.draw.rect(pantalla,(35,20,20),(400,520,600,130))
    l0,l1,l2,l3,l4 = [m.nivel for m in c.lista_mejoras_cafe]

    if "chimenea" in c.mejoras_especiales_compradas:
        cx_ch,cy_ch = 900,380
        pygame.draw.rect(pantalla,(100,100,100),(cx_ch,cy_ch,80,140))
        pygame.draw.rect(pantalla,(40,20,10),(cx_ch+15,cy_ch+70,50,50))
        for i in range(5):
            fh = random.randint(10,25)
            pygame.draw.rect(pantalla,(255,100+random.randint(0,100),0),(cx_ch+20+i*8,cy_ch+120-fh,6,fh))
        pygame.draw.rect(pantalla,(80,80,80),(cx_ch,cy_ch,80,140),4)

    if l2 >= 5:
        pygame.draw.ellipse(pantalla,(180,100,70),(410,510,150,40))
        pygame.draw.ellipse(pantalla,(220,180,120),(415,514,140,32),3)
        for fx in range(420,550,8):
            pygame.draw.line(pantalla,(220,200,180),(fx,508),(fx-4,505),1)
            pygame.draw.line(pantalla,(220,200,180),(fx,550),(fx+4,553),1)
        for cx_r in [440,485,530]:
            pygame.draw.polygon(pantalla,(220,180,120),[(cx_r,520),(cx_r+12,530),(cx_r,540),(cx_r-12,530)])
            pygame.draw.polygon(pantalla,(150,70,50),[(cx_r,523),(cx_r+8,530),(cx_r,537),(cx_r-8,530)])

    cs = (80,80,85) if l0==0 else (101,67,33) if l0==1 else (139,90,43)
    tiene_ventana = "ventana_bosque" in c.mejoras_especiales_compradas

    pygame.draw.rect(pantalla,cs,(550,320,300,200),border_radius=10)
    if l0 >= 2: pygame.draw.rect(pantalla,(160,110,60),(550,320,300,8),border_radius=10)
    if l0 >= 3 and not tiene_ventana:
        pygame.draw.rect(pantalla,(50,30,20),(585,360,230,110),border_radius=5)
    if l0 >= 4: pantalla.blit(c.fuente_cafe.render("CAFÉ",True,(200,150,100)),(660,462))
    pygame.draw.rect(pantalla,(80,50,20),(540,310,320,30))

    if tiene_ventana:
        VX,VY,VW,VH = 590,340,210,110
        pygame.draw.rect(pantalla,(30,60,40),(VX,VY,VW,VH))
        pygame.draw.rect(pantalla,(20,80,30),(VX,VY+VH-25,VW,25))
        for ax,ay,ar,ah in [(VX+20,VY+50,18,28),(VX+60,VY+35,22,35),(VX+110,VY+45,16,25),
                             (VX+155,VY+30,24,38),(VX+190,VY+50,14,22)]:
            pygame.draw.rect(pantalla,(60,35,15),(ax,ay,6,ah))
            pygame.draw.circle(pantalla,(25,90,35),(ax+3,ay),ar)
            pygame.draw.circle(pantalla,(35,110,45),(ax+3,ay-5),ar-6)
        pygame.draw.rect(pantalla,(100,60,30),(VX,VY,VW,VH),5)
        pygame.draw.line(pantalla,(100,60,30),(VX+VW//2,VY),(VX+VW//2,VY+VH),4)
        pygame.draw.line(pantalla,(100,60,30),(VX,VY+VH//2),(VX+VW,VY+VH//2),4)

    if l1 >= 1: dibujar_farolillo(pantalla,570,330,t_ms)
    if l1 >= 2: dibujar_farolillo(pantalla,830,330,t_ms)
    if l1 >= 3: dibujar_vela(pantalla,610,458,t_ms)
    if l1 >= 4: dibujar_guirnalda(pantalla,550,322,850,t_ms)
    if l1 >= 5: dibujar_jarron_flores(pantalla,800,456,t_ms)

    if l4 >= 1:
        cx_b,cy_b = 636,462
        pygame.draw.rect(pantalla,(80,50,25),(cx_b-7,cy_b-14,14,18),border_radius=3)
        pygame.draw.rect(pantalla,(100,65,30),(cx_b-7,cy_b-14,14,6),border_radius=2)
        pygame.draw.line(pantalla,(60,35,15),(cx_b,cy_b-14),(cx_b,cy_b-20),2)
        pygame.draw.rect(pantalla,(120,80,40),(cx_b-5,cy_b-8,10,4),border_radius=1)
        tx_t,ty_t = 660,462
        pygame.draw.ellipse(pantalla,(180,130,70),(tx_t-11,ty_t+6,22,8))
        pygame.draw.rect(pantalla,(220,200,180),(tx_t-9,ty_t-6,18,14),border_radius=3)
        pygame.draw.ellipse(pantalla,(100,70,40),(tx_t-7,ty_t-4,14,8))
        pygame.draw.arc(pantalla,(180,140,80),(tx_t+7,ty_t-4,8,10),-math.pi/2,math.pi/2,2)
        for i,vxo in enumerate([-3,0,3]):
            fase = t_ms*0.004+i*1.1
            alpha = max(0,int(160-(t_ms*3+i*80)%160))
            vs = pygame.Surface((4,10),pygame.SRCALPHA)
            pygame.draw.line(vs,(220,220,220,alpha),(2,10),(2+int(math.sin(fase)*1.5),0),1)
            pantalla.blit(vs,(tx_t+vxo-2,ty_t-16+int(math.sin(fase)*2)))

    if l4 >= 2:
        pygame.draw.rect(pantalla,(90,55,25),(738,437,16,28),border_radius=2)
        pygame.draw.rect(pantalla,(110,70,35),(739,453,14,8),border_radius=1)
        pygame.draw.rect(pantalla,(80,80,85),(740,428,12,10),border_radius=2)
        pygame.draw.line(pantalla,(60,60,65),(752,433),(759,433),2)
        pygame.draw.circle(pantalla,(50,50,55),(759,433),3)

    if l4 >= 3:
        pygame.draw.rect(pantalla,(180,210,220),(762,437,18,32),border_radius=2)
        pygame.draw.rect(pantalla,(120,160,180),(762,437,18,32),1,border_radius=2)
        pygame.draw.rect(pantalla,(80,50,25),(763,454,16,9),border_radius=1)
        pygame.draw.rect(pantalla,(100,100,105),(760,435,20,4),border_radius=1)
        pygame.draw.rect(pantalla,(100,100,105),(760,468,20,4),border_radius=1)
        pygame.draw.line(pantalla,(120,120,125),(771,435),(771,425),2)
        pygame.draw.rect(pantalla,(100,100,105),(764,422,14,4),border_radius=2)

    if l3 >= 1:
        gx,gy = 700,460
        dibujar_gato(pantalla,gx,gy,l3,t_ms,gato_parpadeo_dur>0)
        if celebrando:
            pygame.draw.polygon(pantalla,(255,215,0),
                [(gx-15,gy-55),(gx-15,gy-75),(gx,gy-65),(gx+15,gy-75),(gx+15,gy-55)])

    pygame.draw.rect(pantalla,(60,35,15),(540,468,320,52),border_radius=5)
    pygame.draw.rect(pantalla,(60,35,15),(540,466,14,54),border_radius=3)
    pygame.draw.rect(pantalla,(60,35,15),(846,466,14,54),border_radius=3)
    if l0 >= 4:
        pantalla.blit(c.fuente_cafe.render("CAFÉ",True,(200,150,100)),(660,476))

    if l2 >= 1:
        if l2 < 4:
            pygame.draw.rect(pantalla,(139,69,19),(480,460,40,60))
            pygame.draw.ellipse(pantalla,(160,110,60),(476,456,48,12))
            if l2 >= 2:
                pygame.draw.rect(pantalla,(139,69,19),(430,460,40,60))
                pygame.draw.ellipse(pantalla,(160,110,60),(426,456,48,12))
            if l2 >= 3:
                pygame.draw.rect(pantalla,(200,50,50),(480,460,40,10))
                pygame.draw.rect(pantalla,(200,50,50),(430,460,40,10))
        else:
            pygame.draw.rect(pantalla,(100,60,30),(425,475,100,40),border_radius=6)
            pygame.draw.rect(pantalla,(180,70,70),(425,455,100,25),border_radius=8)
            for rx in range(435,520,15):
                pygame.draw.line(pantalla,(150,50,50),(rx,455),(rx,475),2)
            pygame.draw.rect(pantalla,(200,80,80),(420,470,110,15),border_radius=5)
            pygame.draw.rect(pantalla,(140,50,50),(415,465,15,25),border_radius=5)
            pygame.draw.rect(pantalla,(140,50,50),(520,465,15,25),border_radius=5)

    if l0 >= 5:
        for i in range(7):
            pygame.draw.rect(pantalla,
                (210,105,30) if i%2==0 else (255,240,200),(540+(i*46),280,46,45),border_radius=5)
    if l0 >= 6:
        pygame.draw.rect(pantalla,(40,40,40),(860,450,35,60))
        pygame.draw.rect(pantalla,(100,60,30),(860,450,35,60),3)
        for i in range(3):
            pygame.draw.line(pantalla,(220,220,220),(865,460+i*10),(885,462+i*10),2)
