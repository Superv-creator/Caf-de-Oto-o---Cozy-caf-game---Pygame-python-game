import pygame, math, random, constantes as c
from animales import dibujar_animal

class ItemJardin:
    def __init__(self,id,nombre,precio,tipo,color,categoria,moneda="yen"):
        self.id=id; self.nombre=nombre; self.precio=precio
        self.tipo=tipo; self.color=color; self.categoria=categoria
        self.moneda=moneda
        self.rect=pygame.Rect(20,95+(id*58),360,50)

def dibujar_item_jardin(sup, tipo, px, py, color, escala=1.0, t_ms=0, ocupantes=None):
    def s(v): return max(1,int(v*escala))
    if ocupantes is None: ocupantes=[]

    if tipo in ('flor_roja','flor_azul'):
        swing=math.sin(t_ms*0.002+px*0.05)*2*escala
        tx=px+int(swing)
        pygame.draw.line(sup,(60,130,60),(px,py+s(4)),(tx,py-s(10)),max(1,s(2)))
        for ang in range(0,360,60):
            r2=math.radians(ang)
            pygame.draw.circle(sup,color,(tx+int(math.cos(r2)*s(6)),py-s(10)+int(math.sin(r2)*s(6))),max(2,s(4)))
        pygame.draw.circle(sup,(255,240,100),(tx,py-s(10)),max(2,s(3)))

    elif tipo=='seta':
        pygame.draw.rect(sup,(220,220,200),(px-s(4),py-s(5),s(8),s(16)),border_radius=s(3))
        pygame.draw.ellipse(sup,color,(px-s(15),py-s(15),s(30),s(20)))
        pygame.draw.circle(sup,(255,255,255),(px-s(5),py-s(10)),max(1,s(3)))
        pygame.draw.circle(sup,(255,255,255),(px+s(6),py-s(7)),max(1,s(2)))

    elif tipo=='piedra':
        pygame.draw.ellipse(sup,color,(px-s(25),py-s(12),s(50),s(24)))
        pygame.draw.ellipse(sup,(130,130,130),(px-s(25),py-s(12),s(50),s(24)),max(1,s(2)))

    elif tipo=='agua':
        pygame.draw.ellipse(sup,(30,100,150),(px-s(50),py-s(25),s(100),s(50)))
        pygame.draw.ellipse(sup,color,(px-s(50),py-s(25),s(100),s(50)))
        wave=int(math.sin(t_ms*0.004)*3)
        pygame.draw.line(sup,(100,180,220),(px-s(20),py-s(5)+wave),(px+s(20),py-s(5)+wave),max(1,s(2)))
        pygame.draw.line(sup,(100,180,220),(px-s(10),py+s(10)-wave),(px+s(30),py+s(10)-wave),max(1,s(2)))
        pygame.draw.ellipse(sup,(40,130,180),(px-s(50),py-s(25),s(100),s(50)),max(1,s(2)))

    elif tipo=='estanque_koi':
        pygame.draw.ellipse(sup,(80,80,80),(px-s(65),py-s(35),s(130),s(70)))
        for ang in range(0,360,30):
            r2=math.radians(ang)
            sx2=int(math.cos(r2)*s(62)); sy2=int(math.sin(r2)*s(32))
            pygame.draw.circle(sup,(110,110,110),(px+sx2,py+sy2),s(5))
        pygame.draw.ellipse(sup,(15,65,120),(px-s(55),py-s(28),s(110),s(56)))
        pygame.draw.ellipse(sup,(25,90,160),(px-s(50),py-s(25),s(100),s(50)))
        pygame.draw.ellipse(sup,(35,110,180),(px-s(44),py-s(22),s(88),s(44)))
        for nf_ang in [0, 2.1, 4.2]:
            nfx=px+int(math.cos(nf_ang+t_ms*0.0005)*s(18))
            nfy=py+int(math.sin(nf_ang+t_ms*0.0005)*s(9))
            pygame.draw.circle(sup,(40,130,50),(nfx,nfy),s(7))
            pygame.draw.circle(sup,(55,160,65),(nfx,nfy),s(5))
            pygame.draw.circle(sup,(220,60,100),(nfx,nfy),s(3))

        def dibujar_koi(color_cuerpo, color_mancha, ang_rad, radio_x, radio_y, ep=1.0):
            fx = px + int(math.cos(ang_rad) * s(radio_x))
            fy = py + int(math.sin(ang_rad) * s(radio_y))
            orient = ang_rad + math.pi/2
            long_c = max(2, int(s(10)*ep))
            anch_c = max(1, int(s(5)*ep))
            cos_o, sin_o = math.cos(orient), math.sin(orient)
            pts_cuerpo = []
            for i2 in range(8):
                a2 = i2/8 * math.pi*2
                ex2 = math.cos(a2)*long_c; ey2 = math.sin(a2)*anch_c
                pts_cuerpo.append((int(fx + ex2*cos_o - ey2*sin_o),
                                   int(fy + ex2*sin_o + ey2*cos_o)))
            pygame.draw.polygon(sup, color_cuerpo, pts_cuerpo)
            pygame.draw.circle(sup, color_mancha,
                               (int(fx + long_c*0.2*cos_o), int(fy + long_c*0.2*sin_o)),
                               max(1, int(s(3)*ep)))
            cbx = int(fx - long_c*0.9*cos_o); cby = int(fy - long_c*0.9*sin_o)
            cw = max(1, int(s(5)*ep))
            pygame.draw.polygon(sup, color_cuerpo, [
                (cbx, cby),
                (int(cbx - s(6)*ep*cos_o + cw*sin_o), int(cby - s(6)*ep*sin_o - cw*cos_o)),
                (int(cbx - s(6)*ep*cos_o - cw*sin_o), int(cby - s(6)*ep*sin_o + cw*cos_o)),
            ])
            pygame.draw.circle(sup, (0,0,0),
                               (int(fx + long_c*0.6*cos_o), int(fy + long_c*0.6*sin_o)),
                               max(1, int(s(2)*ep)))

        dibujar_koi((240,130,20),(255,255,255), t_ms*0.001, 22, 11)
        dibujar_koi((240,240,240),(255,140,0), t_ms*0.0013+2, 16, 8, 0.85)
        dibujar_koi((200,50,50),(30,30,30), t_ms*0.0008+4, 28, 14, 0.75)
        for bx_off,by_off in [(-s(18),-s(8)),(s(12),-s(10)),(-s(5),s(6))]:
            gs=pygame.Surface((s(10),s(4)),pygame.SRCALPHA)
            alpha=int(80+60*math.sin(t_ms*0.004+bx_off))
            pygame.draw.ellipse(gs,(200,230,255,alpha),(0,0,s(10),s(4)))
            sup.blit(gs,(px+bx_off,py+by_off))
        pygame.draw.ellipse(sup,(90,90,90),(px-s(65),py-s(35),s(130),s(70)),s(4))

    elif tipo=='hamaca':
        arbol_tronco = (90, 65, 40)
        arbol_hoja   = (30, 80, 30)
        arbol_hoja2  = (45, 110, 45)
        ay = py + s(12)
        pygame.draw.rect(sup, arbol_tronco, (px-s(52), ay-s(45), s(14), s(55)), border_radius=s(3))
        pygame.draw.ellipse(sup, arbol_hoja,  (px-s(65), ay-s(68), s(40), s(35)))
        pygame.draw.ellipse(sup, arbol_hoja2, (px-s(60), ay-s(72), s(30), s(25)))
        pygame.draw.rect(sup, arbol_tronco, (px+s(38), ay-s(45), s(14), s(55)), border_radius=s(3))
        pygame.draw.ellipse(sup, arbol_hoja,  (px+s(25), ay-s(68), s(40), s(35)))
        pygame.draw.ellipse(sup, arbol_hoja2, (px+s(30), ay-s(72), s(30), s(25)))
        pygame.draw.line(sup,(160,140,100),(px-s(45),ay-s(25)),(px-s(38),ay-s(15)),max(1,s(2)))
        pygame.draw.line(sup,(160,140,100),(px+s(45),ay-s(25)),(px+s(38),ay-s(15)),max(1,s(2)))
        curve_drop = s(22) if not ocupantes else s(30)
        PASOS = 22
        borde_sup, borde_inf = [], []
        grosor = s(14)
        for i in range(PASOS+1):
            t_ratio = i/PASOS
            hx = px - s(38) + int(t_ratio * s(76))
            hy_c = ay - s(22) + int(math.sin(t_ratio * math.pi) * curve_drop)
            borde_sup.append((hx, hy_c))
            borde_inf.append((hx, hy_c + grosor))
        poly_pts = borde_sup + list(reversed(borde_inf))
        if len(poly_pts) >= 3:
            pygame.draw.polygon(sup, (190,165,110), poly_pts)
            for stripe_i in range(4):
                t_r = (stripe_i+1)/5
                ix = int(px - s(38) + t_r * s(76))
                iy_top = int(ay - s(22) + math.sin(t_r * math.pi) * curve_drop)
                pygame.draw.line(sup,(155,120,70),(ix, iy_top),(ix, iy_top+grosor),max(1,s(2)))
            pygame.draw.lines(sup,(220,195,140),False,borde_sup,max(2,s(3)))
            pygame.draw.lines(sup,(150,120,70),False,borde_inf,max(1,s(2)))
        if ocupantes:
            cx_h = px
            cy_h = int(ay - s(22) + curve_drop//2)
            dibujar_animal(sup, ocupantes[0], cx_h, cy_h, escala*0.5, parpadeo=True)

    elif tipo=='manta_picnic':
        pm=[(px-s(55),py-s(2)),(px+s(55),py-s(5)),(px+s(50),py+s(16)),(px-s(50),py+s(18))]
        pygame.draw.polygon(sup,(220,70,55),pm)
        for i in range(1,5):
            f=i/5
            ix1=int(px-s(55)+(px+s(55)-(px-s(55)))*f); iy1=int(py-s(2)+(py-s(5)-(py-s(2)))*f)
            ix2=int(px-s(50)+(px+s(50)-(px-s(50)))*f); iy2=int(py+s(18)+(py+s(16)-py-s(18))*f)
            pygame.draw.line(sup,(190,45,35),(ix1,iy1),(ix2,iy2),max(1,s(1)))
        for i in range(1,4):
            f=i/4
            ix1=int(px-s(55)+(px-s(50)-(px-s(55)))*f); iy1=int(py-s(2)+(py+s(18)-(py-s(2)))*f)
            ix2=int(px+s(55)+(px+s(50)-(px+s(55)))*f); iy2=int(py-s(5)+(py+s(16)-(py-s(5)))*f)
            pygame.draw.line(sup,(190,45,35),(ix1,iy1),(ix2,iy2),max(1,s(1)))
        pygame.draw.polygon(sup,(240,200,80),pm,max(2,s(3)))
        pygame.draw.rect(sup,(170,120,65),(px-s(9),py-s(16),s(18),s(14)),border_radius=s(2))
        pygame.draw.ellipse(sup,(195,145,80),(px-s(9),py-s(20),s(18),s(8)))
        pygame.draw.arc(sup,(130,85,35),(px-s(7),py-s(28),s(14),s(14)),0,math.pi,max(1,s(2)))
        posiciones_manta=[(px-s(30),py+s(4)),(px+s(30),py+s(4)),(px-s(15),py+s(12)),(px+s(15),py+s(12))]
        if ocupantes:
            for i2,at in enumerate(ocupantes[:4]):
                ox3,oy3=posiciones_manta[i2]
                dibujar_animal(sup,at,ox3,oy3,escala*0.44)
                bx3=ox3+s(14); by3=oy3-s(28)
                pygame.draw.ellipse(sup,(255,255,240),(bx3,by3,s(28),s(18)))
                pygame.draw.polygon(sup,(255,255,240),[(bx3+s(4),by3+s(15)),(bx3+s(10),by3+s(15)),(bx3+s(2),by3+s(22))])
                pygame.draw.rect(sup,(210,160,90),(bx3+s(6),by3+s(8),s(12),s(7)),border_radius=max(1,s(1)))
                pygame.draw.ellipse(sup,(255,90,90),(bx3+s(8),by3+s(5),s(8),s(5)))
                pygame.draw.circle(sup,(255,210,60),(bx3+s(12),by3+s(4)),max(1,s(2)))

    elif tipo=='pozo_deseos':
        pygame.draw.ellipse(sup,(80,68,60),(px-s(30),py-s(32),s(60),s(16)))
        pygame.draw.rect(sup,(95,80,70),(px-s(30),py-s(28),s(60),s(32)))
        for i in range(4):
            fy=py-s(28)+i*s(8)
            pygame.draw.line(sup,(75,62,54),(px-s(30),fy),(px+s(30),fy),max(1,s(1)))
        for i in range(3):
            fx=px-s(15)+i*s(15)
            pygame.draw.line(sup,(75,62,54),(fx,py-s(28)),(fx,py+s(4)),max(1,s(1)))
        pygame.draw.ellipse(sup,(40,32,24),(px-s(18),py-s(31),s(36),s(10)))
        pygame.draw.ellipse(sup,(22,16,10),(px-s(14),py-s(30),s(28),s(7)))
        pygame.draw.ellipse(sup,(110,92,80),(px-s(30),py-s(32),s(60),s(16)))
        pygame.draw.ellipse(sup,(128,108,93),(px-s(27),py-s(30),s(54),s(12)))
        pygame.draw.rect(sup,(110,75,45),(px-s(28),py-s(60),s(7),s(32)))
        pygame.draw.rect(sup,(110,75,45),(px+s(21),py-s(60),s(7),s(32)))
        pygame.draw.rect(sup,(130,90,50),(px-s(30),py-s(60),s(60),s(7)),border_radius=s(2))
        pygame.draw.polygon(sup,(160,85,40),[(px-s(34),py-s(60)),(px+s(34),py-s(60)),(px,py-s(82))])
        pygame.draw.polygon(sup,(190,110,55),[(px-s(30),py-s(62)),(px+s(30),py-s(62)),(px,py-s(80))])
        pygame.draw.line(sup,(130,105,75),(px,py-s(58)),(px,py-s(38)),max(1,s(1)))
        pygame.draw.rect(sup,(140,105,70),(px-s(5),py-s(44),s(10),s(8)),border_radius=s(2))
        if ocupantes:
            entrada=ocupantes[0]
            if isinstance(entrada,tuple): animal_tipo,deseo,coin_t = entrada
            else: animal_tipo,deseo,coin_t = entrada,'corazon',0
            ax2=px+s(46); ay2=py+s(8)
            dibujar_animal(sup,animal_tipo,ax2,ay2,escala*0.46)
            ciclo=180
            fase=coin_t%ciclo
            coin_prog=fase/ciclo*math.pi
            t_coin=fase/ciclo
            coin_x=int(ax2+(px-ax2)*t_coin)
            coin_y=int(ay2-s(12)-math.sin(coin_prog)*s(22))
            coin_alpha=int(255*math.sin(coin_prog))
            if coin_alpha>20:
                cs3=pygame.Surface((s(10),s(10)),pygame.SRCALPHA)
                pygame.draw.circle(cs3,(255,215,0,coin_alpha),(s(5),s(5)),s(4))
                pygame.draw.circle(cs3,(200,160,0,coin_alpha),(s(5),s(5)),s(2))
                sup.blit(cs3,(coin_x-s(5),coin_y-s(5)))
            if t_coin>0.7:
                bx2=ax2+s(12); by2=ay2-s(50)
                pygame.draw.ellipse(sup,(255,245,250),(bx2,by2,s(30),s(22)))
                pygame.draw.polygon(sup,(255,245,250),[(bx2+s(4),by2+s(18)),(bx2+s(10),by2+s(18)),(bx2+s(2),by2+s(26))])
                cx2=bx2+s(15); cy2=by2+s(11)
                if deseo=='corazon':
                    pygame.draw.circle(sup,(255,80,120),(cx2-s(4),cy2-s(2)),s(4))
                    pygame.draw.circle(sup,(255,80,120),(cx2+s(4),cy2-s(2)),s(4))
                    pygame.draw.polygon(sup,(255,80,120),[(cx2-s(7),cy2+s(1)),(cx2+s(7),cy2+s(1)),(cx2,cy2+s(8))])
                elif deseo=='moneda':
                    pygame.draw.circle(sup,(255,215,0),(cx2,cy2),s(6))
                    pygame.draw.circle(sup,(200,160,0),(cx2,cy2),s(4))
                    pygame.draw.circle(sup,(255,240,100),(cx2,cy2),s(2))
                elif deseo=='trebol':
                    for dx3,dy3 in [(0,-s(4)),(0,s(2)),(-s(4),-s(1)),(s(4),-s(1))]:
                        pygame.draw.circle(sup,(50,190,70),(cx2+dx3,cy2+dy3),s(3))
                    pygame.draw.line(sup,(30,130,40),(cx2,cy2+s(4)),(cx2,cy2+s(8)),max(1,s(2)))

    elif tipo=='taburete':
        sombra=pygame.Surface((s(50),s(10)),pygame.SRCALPHA)
        pygame.draw.ellipse(sombra,(0,0,0,60),(0,0,s(50),s(10)))
        sup.blit(sombra,(px-s(25),py+s(18)))
        pygame.draw.ellipse(sup,(80,50,20),(px-s(20),py-s(5),s(40),s(20)))
        pygame.draw.ellipse(sup,color,(px-s(20),py-s(15),s(40),s(20)))
        for lx in [px-s(12),px+s(5)]:
            pygame.draw.line(sup,(60,35,10),(lx,py+s(5)),(lx,py+s(18)),max(1,s(2)))

    elif tipo=='banco':
        sombra=pygame.Surface((s(100),s(14)),pygame.SRCALPHA)
        pygame.draw.ellipse(sombra,(0,0,0,55),(0,0,s(100),s(14)))
        sup.blit(sombra,(px-s(50),py+s(12)))
        pygame.draw.rect(sup,(100,60,30),(px-s(45),py-s(35),s(90),s(12)),border_radius=s(3))
        pygame.draw.line(sup,(80,45,15),(px-s(35),py-s(35)),(px-s(35),py-s(10)),max(1,s(2)))
        pygame.draw.line(sup,(80,45,15),(px+s(25),py-s(35)),(px+s(25),py-s(10)),max(1,s(2)))
        pygame.draw.rect(sup,color,(px-s(45),py-s(22),s(90),s(14)),border_radius=s(3))
        pygame.draw.rect(sup,(60,40,20),(px-s(38),py-s(8),s(8),s(20)))
        pygame.draw.rect(sup,(60,40,20),(px+s(30),py-s(8),s(8),s(20)))
        if ocupantes:
            for i,at in enumerate(ocupantes[:2]):
                ox=px-s(15)+i*s(28); dibujar_animal(sup,at,ox,py-s(32),escala*0.55)

    elif tipo=='farola':
        sombra=pygame.Surface((s(30),s(10)),pygame.SRCALPHA)
        pygame.draw.ellipse(sombra,(0,0,0,60),(0,0,s(30),s(10)))
        sup.blit(sombra,(px-s(15),py+s(24)))
        if escala==1.0:
            glow=pygame.Surface((60,60),pygame.SRCALPHA)
            pygame.draw.circle(glow,(255,255,100,50),(30,30),30)
            sup.blit(glow,(px-30,py-65))
        pygame.draw.rect(sup,(60,60,60),(px-s(10),py+s(15),s(20),s(10)))
        pygame.draw.rect(sup,color,(px-s(4),py-s(25),s(8),s(40)))
        pygame.draw.polygon(sup,color,[(px-s(12),py-s(25)),(px+s(12),py-s(25)),(px+s(8),py-s(45)),(px-s(8),py-s(45))])
        pygame.draw.polygon(sup,(255,240,100),[(px-s(8),py-s(28)),(px+s(8),py-s(28)),(px+s(5),py-s(42)),(px-s(5),py-s(42))])
        pygame.draw.polygon(sup,(30,30,30),[(px-s(14),py-s(45)),(px+s(14),py-s(45)),(px,py-s(55))])

    elif tipo=='fuente':
        fy_off = s(30)
        sombra=pygame.Surface((s(120),s(22)),pygame.SRCALPHA)
        pygame.draw.ellipse(sombra,(0,0,0,55),(0,0,s(120),s(22)))
        sup.blit(sombra,(px-s(60),py+s(18)))
        pygame.draw.ellipse(sup,(90,85,80),(px-s(58),py-s(18)+fy_off,s(116),s(36)))
        for ang in range(0,360,40):
            r2=math.radians(ang)
            sx2=int(math.cos(r2)*s(54)); sy2=int(math.sin(r2)*s(16))
            pygame.draw.circle(sup,(110,105,100),(px+sx2,py+sy2+fy_off),s(4))
        pygame.draw.ellipse(sup,(30,100,160),(px-s(48),py-s(14)+fy_off,s(96),s(28)))
        pygame.draw.ellipse(sup,(50,130,200),(px-s(44),py-s(12)+fy_off,s(88),s(24)))
        pygame.draw.rect(sup,(100,95,90),(px-s(8),py-s(58)+fy_off,s(16),s(48)),border_radius=s(4))
        pygame.draw.ellipse(sup,(110,105,100),(px-s(10),py-s(60)+fy_off,s(20),s(8)))
        pygame.draw.ellipse(sup,(90,85,80),(px-s(22),py-s(72)+fy_off,s(44),s(16)))
        pygame.draw.ellipse(sup,(30,100,160),(px-s(18),py-s(70)+fy_off,s(36),s(12)))
        for i in range(4):
            ang2=i*(math.pi/2)+t_ms*0.002
            wx=px+int(math.cos(ang2)*s(14)); wy_start=py-s(62)+fy_off
            drop_progress=(t_ms//8+i*20)%30
            pygame.draw.line(sup,(100,180,255),(wx,wy_start),(wx-s(2)+int(math.sin(ang2+1)*s(5)),wy_start+drop_progress),max(1,s(2)))
        for bx_off,by_off in [(-s(15),-s(5)+fy_off),(s(20),-s(8)+fy_off),(s(5),s(8)+fy_off)]:
            gs=pygame.Surface((s(12),s(5)),pygame.SRCALPHA)
            alpha=int(100+80*math.sin(t_ms*0.004+bx_off))
            pygame.draw.ellipse(gs,(200,230,255,alpha),(0,0,s(12),s(5)))
            sup.blit(gs,(px+bx_off,py+by_off))
        if ocupantes:
            dibujar_animal(sup,ocupantes[0],px+s(30),py-s(15)+fy_off,escala*0.5)

    elif tipo=='columpio':
        sombra=pygame.Surface((s(70),s(12)),pygame.SRCALPHA)
        pygame.draw.ellipse(sombra,(0,0,0,55),(0,0,s(70),s(12)))
        sup.blit(sombra,(px-s(35),py+s(14)))
        pygame.draw.line(sup,(100,65,30),(px-s(30),py-s(55)),(px-s(20),py+s(10)),max(2,s(2)))
        pygame.draw.line(sup,(100,65,30),(px+s(30),py-s(55)),(px+s(20),py+s(10)),max(2,s(2)))
        pygame.draw.line(sup,(100,65,30),(px-s(30),py-s(55)),(px+s(30),py-s(55)),max(2,s(2)))
        swing_a=math.sin(t_ms*0.003)*0.4 if ocupantes else math.sin(t_ms*0.0015)*0.15
        sx=int(math.sin(swing_a)*s(20)); sy=int((1-math.cos(swing_a))*s(10))
        pygame.draw.line(sup,(80,50,20),(px-s(10),py-s(55)),(px-s(10)+sx,py-s(15)+sy),max(1,s(2)))
        pygame.draw.line(sup,(80,50,20),(px+s(10),py-s(55)),(px+s(10)+sx,py-s(15)+sy),max(1,s(2)))
        pygame.draw.rect(sup,color,(px-s(12)+sx,py-s(18)+sy,s(24),s(6)),border_radius=s(2))
        if ocupantes:
            dibujar_animal(sup,ocupantes[0],px+sx,py-s(32)+sy,escala*0.55)

    elif tipo=='subebaja':
        sombra=pygame.Surface((s(96),s(12)),pygame.SRCALPHA)
        pygame.draw.ellipse(sombra,(0,0,0,55),(0,0,s(96),s(12)))
        sup.blit(sombra,(px-s(48),py+s(14)))
        pygame.draw.rect(sup,(80,50,20),(px-s(5),py-s(15),s(10),s(20)),border_radius=s(3))
        pygame.draw.ellipse(sup,(60,35,10),(px-s(8),py-s(18),s(16),s(10)))
        tilt=math.sin(t_ms*0.004)*0.5 if (ocupantes and len(ocupantes)>=2) else math.sin(t_ms*0.002)*0.2
        lx2=s(42); ly2=int(math.sin(tilt)*lx2)
        pygame.draw.line(sup,color,(px-lx2,py-s(5)-ly2),(px+lx2,py-s(5)+ly2),max(3,s(5)))
        pygame.draw.circle(sup,(140,90,40),(px-lx2,py-s(5)-ly2),s(5))
        pygame.draw.circle(sup,(140,90,40),(px+lx2,py-s(5)+ly2),s(5))
        if ocupantes:
            if len(ocupantes)>=1: dibujar_animal(sup,ocupantes[0],px-lx2,py-s(5)-ly2-s(16),escala*0.55)
            if len(ocupantes)>=2: dibujar_animal(sup,ocupantes[1],px+lx2,py-s(5)+ly2-s(16),escala*0.55)

    elif tipo=='tobogan':
        sombra=pygame.Surface((s(80),s(14)),pygame.SRCALPHA)
        pygame.draw.ellipse(sombra,(0,0,0,55),(0,0,s(80),s(14)))
        sup.blit(sombra,(px-s(30),py+s(14)))
        pygame.draw.line(sup,(100,65,30),(px-s(30),py+s(10)),(px-s(10),py-s(50)),max(2,s(2)))
        pygame.draw.rect(sup,(120,80,40),(px-s(20),py-s(55),s(24),s(8)),border_radius=s(2))
        for i in range(3):
            ex2=px-s(26)+i*s(6); ey2=py-s(18)-i*s(14)
            pygame.draw.line(sup,(140,90,45),(ex2,ey2),(ex2+s(8),ey2),max(1,s(2)))
        pygame.draw.polygon(sup,(200,80,80),
            [(px-s(8),py-s(52)),(px+s(6),py-s(52)),(px+s(35),py+s(8)),(px+s(22),py+s(8))])
        pygame.draw.polygon(sup,(220,100,100),
            [(px-s(5),py-s(50)),(px+s(5),py-s(50)),(px+s(28),py+s(5)),(px+s(20),py+s(5))])
        pygame.draw.line(sup,(80,50,20),(px+s(35),py+s(8)),(px+s(35),py+s(18)),max(2,s(2)))
        if ocupantes:
            prog=((t_ms//20)%100)/100.0
            ax=int(px-s(5)+(px+s(28)-(px-s(5)))*prog)
            ay=int(py-s(48)+(py+s(3)-py+s(48))*prog)
            dibujar_animal(sup,ocupantes[0],ax,ay,escala*0.5)

    elif tipo=='estrella_deco':
        pulse=1.0+math.sin(t_ms*0.003+px*0.05)*0.15
        r_e=int(s(12)*pulse)
        pts=[]
        for k in range(10):
            ang=math.pi/2+k*math.pi*2/10
            r_k=r_e if k%2==0 else r_e//2
            pts.append((int(px+math.cos(ang)*r_k),int(py-math.sin(ang)*r_k)))
        pygame.draw.polygon(sup,(255,240,100),pts)
        pygame.draw.polygon(sup,(255,200,50),pts,max(1,s(1)))
        pygame.draw.circle(sup,(255,255,200),(px,py),max(1,s(3)))

    elif tipo=='piedrecita_cafe':
        pygame.draw.ellipse(sup,(160,150,140),(px-s(14),py-s(7),s(28),s(14)))
        pygame.draw.ellipse(sup,(140,130,120),(px-s(11),py-s(5),s(22),s(10)))
        pygame.draw.ellipse(sup,(185,175,165),(px-s(8),py-s(6),s(10),s(6)))

mariposas=[{'x':float(random.randint(420,980)),'y':float(random.randint(200,560)),
            'vx':random.uniform(-0.4,0.4),'vy':random.uniform(-0.3,0.3),
            'col':(random.randint(180,255),random.randint(80,200),random.randint(180,255)),
            'off':random.uniform(0,math.pi*2),
            'alpha':255,'muriendo':False} for _ in range(6)]

def actualizar_mariposas(t_ms):
    for b in mariposas[:]:
        if b['muriendo']:
            b['alpha'] -= 12
            b['y'] -= 1.5
            if b['alpha'] <= 0:
                mariposas.remove(b)
                mariposas.append({'x':float(random.randint(420,980)),'y':float(random.randint(200,560)),
                    'vx':random.uniform(-0.4,0.4),'vy':random.uniform(-0.3,0.3),
                    'col':(random.randint(180,255),random.randint(80,200),random.randint(180,255)),
                    'off':random.uniform(0,math.pi*2),'alpha':255,'muriendo':False})
            continue
        b['x']+=b['vx']+math.sin(t_ms*0.002+b['off'])*0.3
        b['y']+=b['vy']+math.cos(t_ms*0.003+b['off'])*0.2
        if b['x']<420: b['vx']=abs(b['vx'])
        if b['x']>990: b['vx']=-abs(b['vx'])
        if b['y']<180: b['vy']=abs(b['vy'])
        if b['y']>590: b['vy']=-abs(b['vy'])

def cazar_mariposa(mx, my):
    for b in mariposas:
        if b['muriendo']: continue
        if math.hypot(mx - b['x'], my - b['y']) < 22:
            b['muriendo'] = True
            return True
    return False

def dibujar_mariposas(sup, t_ms):
    for b in mariposas:
        x2, y2 = int(b['x']), int(b['y'])
        col = b['col']
        alpha = b.get('alpha', 255)
        col_b = (min(255,col[0]+50), min(255,col[1]+40), min(255,col[2]+50))

        # Tamaño pequeño y fijo — sin animación de alas para evitar desconexiones
        aw, ah = 10, 7   # ala superior: ancho, alto
        iw, ih =  7, 5   # ala inferior: ancho, alto

        if alpha < 255:
            surf_b = pygame.Surface((36, 26), pygame.SRCALPHA)
            bx, by = 18, 13
            col_a = (*col, alpha)
            col_bb = (*col_b, alpha)
            pygame.draw.ellipse(surf_b, col_a,  (bx - aw - 1, by - ah,         aw, ah))
            pygame.draw.ellipse(surf_b, col_a,  (bx + 1,       by - ah,         aw, ah))
            pygame.draw.ellipse(surf_b, col_bb, (bx - aw//2 - 2, by - ah + 1, aw//2, ah//2))
            pygame.draw.ellipse(surf_b, col_bb, (bx + 2,          by - ah + 1, aw//2, ah//2))
            pygame.draw.ellipse(surf_b, col_a,  (bx - iw - 1, by + 1,          iw, ih))
            pygame.draw.ellipse(surf_b, col_a,  (bx + 1,       by + 1,          iw, ih))
            pygame.draw.ellipse(surf_b, (40,30,20,alpha), (bx - 1, by - ah, 3, ah + ih))
            sup.blit(surf_b, (x2 - bx, y2 - by))
        else:
            pygame.draw.ellipse(sup, col,   (x2 - aw - 1, y2 - ah,         aw, ah))
            pygame.draw.ellipse(sup, col,   (x2 + 1,       y2 - ah,         aw, ah))
            pygame.draw.ellipse(sup, col_b, (x2 - aw//2 - 2, y2 - ah + 1, aw//2, ah//2))
            pygame.draw.ellipse(sup, col_b, (x2 + 2,          y2 - ah + 1, aw//2, ah//2))
            pygame.draw.ellipse(sup, col,   (x2 - iw - 1, y2 + 1,          iw, ih))
            pygame.draw.ellipse(sup, col,   (x2 + 1,       y2 + 1,          iw, ih))
            pygame.draw.ellipse(sup, (40,30,20), (x2 - 1, y2 - ah, 3, ah + ih))
