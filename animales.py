import pygame
import math
import random
import constantes as c

TIPOS_ANIMAL = ["CONEJO","OSO","BUHO","RANA","PATO","ZORRO","PANDA"]

def color_animal(tipo):
    return {"CONEJO":(240,240,240),"OSO":(139,69,19),"BUHO":(120,100,90),
            "RANA":(100,200,100),"PATO":(255,220,50),
            "ZORRO":(230,100,30),"PANDA":(240,240,240)}[tipo]

def dibujar_animal(sup, tipo, x, y, escala=1.0, mirando_izq=False, parpadeo=False):
    def s(v): return max(1, int(v*escala))
    col = color_animal(tipo)

    sombra = pygame.Surface((int(s(50)),int(s(16))), pygame.SRCALPHA)
    pygame.draw.ellipse(sombra, (0,0,0,60), (0,0,int(s(50)),int(s(16))))
    sup.blit(sombra, (x - s(25), y + s(18)))

    if tipo == "CONEJO":
        pygame.draw.circle(sup, col, (x,y), s(25))
        for ox in [-10, 4]:
            pygame.draw.ellipse(sup, col,          (x+ox, y-s(45), s(10), s(30)))
            pygame.draw.ellipse(sup, (255,180,180),(x+ox+2, y-s(40), s(6), s(20)))
        pygame.draw.circle(sup, (255,150,150),(x, y+s(2)), s(3))
        pygame.draw.rect(sup,(255,255,255),(x-s(4),y+s(5),s(8),s(6)))
        pygame.draw.line(sup,(200,200,200),(x,y+s(5)),(x,y+s(10)),1)
    elif tipo == "OSO":
        pygame.draw.circle(sup, col,(x-s(15),y-s(20)),s(12))
        pygame.draw.circle(sup, col,(x+s(15),y-s(20)),s(12))
        pygame.draw.circle(sup, col,(x,y),s(25))
        pygame.draw.ellipse(sup,(200,150,100),(x-s(12),y-s(8),s(24),s(16)))
        pygame.draw.circle(sup,(0,0,0),(x,y-s(2)),s(3))
    elif tipo == "BUHO":
        pygame.draw.circle(sup, col,(x,y),s(25))
        pygame.draw.polygon(sup,(80,65,60),[(x-s(12),y-s(18)),(x-s(4),y-s(18)),(x-s(8),y-s(24))])
        pygame.draw.polygon(sup,(80,65,60),[(x+s(4),y-s(18)),(x+s(12),y-s(18)),(x+s(8),y-s(24))])
        pygame.draw.circle(sup,(255,255,255),(x-s(9),y-s(8)),s(9))
        pygame.draw.circle(sup,(255,255,255),(x+s(9),y-s(8)),s(9))
        pygame.draw.circle(sup,(0,0,0),(x-s(9),y-s(8)),s(4))
        pygame.draw.circle(sup,(0,0,0),(x+s(9),y-s(8)),s(4))
        pygame.draw.polygon(sup,(255,165,0),[(x-s(5),y+s(1)),(x+s(5),y+s(1)),(x,y+s(8))])
    elif tipo == "RANA":
        pygame.draw.circle(sup, col,(x,y),s(25))
        for ox in [-s(14),s(14)]:
            pygame.draw.circle(sup,col,(x+ox,y-s(20)),s(10))
            pygame.draw.circle(sup,(255,255,255),(x+ox,y-s(20)),s(7))
            pygame.draw.circle(sup,(0,0,0),(x+ox,y-s(20)),s(3))
        pygame.draw.line(sup,(0,0,0),(x-s(6),y+s(5)),(x,y+s(8)),2)
        pygame.draw.line(sup,(0,0,0),(x,y+s(8)),(x+s(6),y+s(5)),2)
    elif tipo == "PATO":
        pygame.draw.circle(sup, col,(x,y),s(25))
        pygame.draw.ellipse(sup,(255,140,0),(x-s(12),y,s(24),s(12)))
        for ox in [-s(18),s(8)]:
            pygame.draw.ellipse(sup,(200,160,20),(x+ox,y-s(8),s(12),s(22)))
    elif tipo == "ZORRO":
        pygame.draw.circle(sup, col,(x,y),s(25))
        pygame.draw.polygon(sup,col,[(x-s(16),y-s(20)),(x-s(8),y-s(42)),(x-s(2),y-s(20))])
        pygame.draw.polygon(sup,col,[(x+s(2),y-s(20)),(x+s(8),y-s(42)),(x+s(16),y-s(20))])
        pygame.draw.polygon(sup,(255,200,180),[(x-s(14),y-s(22)),(x-s(8),y-s(36)),(x-s(4),y-s(22))])
        pygame.draw.polygon(sup,(255,200,180),[(x+s(4),y-s(22)),(x+s(8),y-s(36)),(x+s(14),y-s(22))])
        pygame.draw.ellipse(sup,(255,240,220),(x-s(8),y-s(4),s(16),s(12)))
        pygame.draw.circle(sup,(200,60,20),(x,y+s(2)),s(4))
        pygame.draw.circle(sup,(50,30,10),(x-s(8),y-s(12)),s(4))
        pygame.draw.circle(sup,(50,30,10),(x+s(8),y-s(12)),s(4))
        pygame.draw.circle(sup,(255,200,50),(x-s(8),y-s(12)),s(2))
        pygame.draw.circle(sup,(255,200,50),(x+s(8),y-s(12)),s(2))
        pygame.draw.circle(sup,(0,0,0),(x-s(8),y-s(12)),s(1))
        pygame.draw.circle(sup,(0,0,0),(x+s(8),y-s(12)),s(1))
        pygame.draw.circle(sup,(255,255,255),(x-s(7),y-s(13)),max(1,s(1)))
        pygame.draw.circle(sup,(255,255,255),(x+s(9),y-s(13)),max(1,s(1)))
    elif tipo == "PANDA":
        pygame.draw.circle(sup,(240,240,240),(x,y),s(25))
        pygame.draw.ellipse(sup,(40,40,40),(x-s(14),y-s(16),s(12),s(10)))
        pygame.draw.ellipse(sup,(40,40,40),(x+s(2),y-s(16),s(12),s(10)))
        pygame.draw.circle(sup,(40,40,40),(x-s(18),y-s(24)),s(8))
        pygame.draw.circle(sup,(40,40,40),(x+s(18),y-s(24)),s(8))
        pygame.draw.circle(sup,(255,255,255),(x-s(8),y-s(12)),s(4))
        pygame.draw.circle(sup,(255,255,255),(x+s(8),y-s(12)),s(4))
        pygame.draw.circle(sup,(0,0,0),(x-s(8),y-s(12)),s(2))
        pygame.draw.circle(sup,(0,0,0),(x+s(8),y-s(12)),s(2))
        pygame.draw.circle(sup,(100,100,100),(x,y+s(4)),s(5))

    if tipo not in ["BUHO","RANA","ZORRO","PANDA"]:
        if parpadeo:
            pygame.draw.arc(sup,(50,50,50),(x-s(13),y-s(8),s(10),s(6)),0,math.pi,max(1,s(2)))
            pygame.draw.arc(sup,(50,50,50),(x+s(3),y-s(8),s(10),s(6)),0,math.pi,max(1,s(2)))
        else:
            pygame.draw.circle(sup,(0,0,0),(x-s(8),y-s(5)),s(3))
            pygame.draw.circle(sup,(0,0,0),(x+s(8),y-s(5)),s(3))
            pygame.draw.circle(sup,(255,255,255),(x-s(7),y-s(6)),s(1))
            pygame.draw.circle(sup,(255,255,255),(x+s(9),y-s(6)),s(1))
    elif tipo in ["BUHO","RANA"] and parpadeo:
        pygame.draw.arc(sup,(50,50,50),(x-s(18),y-s(13),s(18),s(10)),0,math.pi,max(1,s(2)))
        pygame.draw.arc(sup,(50,50,50),(x+s(1),y-s(13),s(18),s(10)),0,math.pi,max(1,s(2)))


def _dibujar_corazon(sup, cx, cy, r, alpha=255):
    """Dibuja un corazón pequeño centrado en (cx,cy) con radio r."""
    surf = pygame.Surface((r*4, r*4), pygame.SRCALPHA)
    bx, by = r*2, r*2
    col = (255, 80, 150, alpha)
    pygame.draw.circle(surf, col, (bx - r, by - r//2), r)
    pygame.draw.circle(surf, col, (bx + r, by - r//2), r)
    pygame.draw.polygon(surf, col, [
        (bx - r*2, by),
        (bx + r*2, by),
        (bx,       by + r*2 + r//2),
    ])
    sup.blit(surf, (cx - r*2, cy - r*2))


class AnimalJardin:
    def __init__(self):
        self.tipo = random.choice(TIPOS_ANIMAL)
        self.x = float(random.randint(440,980))
        self.y = float(random.randint(200,580))
        self.vx = random.uniform(-0.6,0.6)
        self.vy = random.uniform(-0.3,0.3)
        self.estado = "VAGANDO"
        self.estado_timer = random.randint(180,400)
        self.obj_target = None
        self.deseo = 'corazon'
        self.coin_t = 0
        self.mirando_izq = self.vx < 0
        self.parpadeo_timer = random.randint(150, 400)
        self.parpadeo_dur = 0
        self.parpadeo_activo = False
        self.bounce_off = random.uniform(0, math.pi*2)
        self.cabeceo_timer = 0
        self.zzz_off = random.uniform(0, math.pi*2)
        # Para besos en banco
        self.beso_timer = 0          # ticks restantes emitiendo corazones
        self.corazones = []          # lista de partículas [{x,y,vy,r,alpha,vida}]
        # Para trampolín en seta
        self.salto_fase = random.uniform(0, math.pi*2)  # fase del salto (continuo)

    def tocar(self):
        self.cabeceo_timer = 40

    def _hay_pareja_banco(self, otros_animales):
        """Devuelve True si hay otro animal de la misma especie sentado en el mismo banco."""
        if self.obj_target is None or self.obj_target.get('tipo') != 'banco':
            return False
        for otro in otros_animales:
            if otro is self:
                continue
            if (otro.tipo == self.tipo
                    and otro.estado == "SENTADO"
                    and otro.obj_target is self.obj_target):
                return True
        return False

    def actualizar(self, objetos, otros_animales):
        self.estado_timer -= 1
        if self.cabeceo_timer > 0: self.cabeceo_timer -= 1

        self.parpadeo_timer -= 1
        if self.parpadeo_timer <= 0:
            if self.parpadeo_activo:
                self.parpadeo_dur -= 1
                if self.parpadeo_dur <= 0:
                    self.parpadeo_activo = False
                    self.parpadeo_timer = random.randint(150, 400)
            else:
                self.parpadeo_activo = True
                self.parpadeo_dur = random.randint(3, 7)
                self.parpadeo_timer = self.parpadeo_dur

        # --- Actualizar partículas de corazones ---
        for p in self.corazones[:]:
            p['y'] -= p['vy']
            p['x'] += p.get('vx', 0)
            p['vida'] -= 1          # desaparecen lentamente
            p['alpha'] = max(0, p['vida'])
            if p['vida'] <= 0:
                self.corazones.remove(p)

        # --- Emitir corazones si hay pareja en banco ---
        if self.estado == "SENTADO" and self._hay_pareja_banco(otros_animales):
            self.beso_timer = 10   # mantiene activo mientras estén juntos
        if self.beso_timer > 0:
            self.beso_timer -= 1
            if random.random() < 0.04:   # ~1 corazón cada 25 frames, muy esporádico
                self.corazones.append({
                    'x': self.x + random.uniform(-8, 8),
                    'y': self.y - 28,
                    'vy': random.uniform(0.25, 0.5),   # sube despacio
                    'vx': random.uniform(-0.2, 0.2),
                    'r': random.randint(3, 5),
                    'alpha': 255,
                    'vida': 255,
                })

        if self.estado == "VAGANDO":
            TIPOS_BLOQ = {'hamaca','estanque_koi','agua','pozo_deseos'}
            RADIO_BLOQ = {'hamaca': 80, 'estanque_koi': 85, 'agua': 75, 'pozo_deseos': 80}
            for obj in objetos:
                if obj['tipo'] in TIPOS_BLOQ:
                    r = RADIO_BLOQ[obj['tipo']]
                    ddx = self.x - obj['x']; ddy = self.y - obj['y']
                    dist_obj = math.hypot(ddx, ddy)
                    if dist_obj < r and dist_obj > 1:
                        fuerza = (r - dist_obj) / r * 1.5
                        self.x += (ddx/dist_obj) * fuerza
                        self.y += (ddy/dist_obj) * fuerza
            self.x += self.vx; self.y += self.vy
            if self.vx != 0: self.mirando_izq = self.vx<0
            if self.x<420: self.vx=abs(self.vx)
            if self.x>980: self.vx=-abs(self.vx)
            if self.y<190: self.vy=abs(self.vy)
            if self.y>590: self.vy=-abs(self.vy)
            if self.estado_timer<=0:
                interactivos=[o for o in objetos if o['tipo'] in
                              ('banco','columpio','subebaja','tobogan','fuente',
                               'hamaca','manta_picnic','pozo_deseos','seta')]
                if interactivos and random.random()<0.6:
                    posible_target = random.choice(interactivos)
                    ocupantes = sum(1 for a in otros_animales if a.obj_target == posible_target)
                    tipo_pt = posible_target['tipo']
                    # La seta admite 1 animal a la vez saltando
                    limite = 4 if tipo_pt=='manta_picnic' else (
                             1 if tipo_pt in('columpio','hamaca','tobogan','pozo_deseos','seta') else 2)
                    if ocupantes < limite:
                        self.obj_target = posible_target
                        self.estado="YENDO"; self.estado_timer=300
                    else:
                        self.estado_timer=random.randint(50,150)
                else:
                    self.vx=random.uniform(-0.6,0.6); self.vy=random.uniform(-0.3,0.3)
                    self.estado_timer=random.randint(150,350)

        elif self.estado=="YENDO":
            if self.obj_target is None: self.estado="VAGANDO"; self.estado_timer=200; return
            tx,ty=self.obj_target['x'],self.obj_target['y']
            dx,dy=tx-self.x,ty-self.y; dist=math.hypot(dx,dy)
            if dist<15:
                tipo_t = self.obj_target['tipo']
                self.estado = {
                    "banco":"SENTADO","columpio":"COLUMPIO","subebaja":"SUBEBAJA",
                    "tobogan":"TOBOGAN","fuente":"FUENTE","hamaca":"SENTADO",
                    "manta_picnic":"PICNIC","pozo_deseos":"DESEO",
                    "seta":"SALTANDO",
                }.get(tipo_t, "SENTADO")
                ox_t = self.obj_target['x']; oy_t = self.obj_target['y']
                if tipo_t=='pozo_deseos': self.x=float(ox_t+46); self.y=float(oy_t+8)
                elif tipo_t=='manta_picnic': self.x=float(ox_t); self.y=float(oy_t+10)
                elif tipo_t=='seta':
                    # Se coloca encima del sombrero (py-15 es la cúpula de la seta a escala 1)
                    self.x=float(ox_t); self.y=float(oy_t-18)
                    self.salto_fase = 0.0   # reinicia fase para salto vistoso
                else: self.x=float(ox_t); self.y=float(oy_t)
                if tipo_t=='pozo_deseos':
                    self.deseo=random.choice(['corazon','moneda','trebol'])
                    self.coin_t=0; self.estado_timer=200
                elif tipo_t=='seta':
                    self.estado_timer=random.randint(180, 360)   # ~3-6 s saltando
                else:
                    self.estado_timer=random.randint(400,700)
            else:
                spd=1.2
                TIPOS_BLOQ = {'hamaca','estanque_koi','agua','pozo_deseos'}
                RADIO_BLOQ = {'hamaca': 65, 'estanque_koi': 70, 'agua': 60, 'pozo_deseos': 50}
                desvio_x, desvio_y = 0.0, 0.0
                for obj in objetos:
                    if obj is self.obj_target: continue
                    if obj['tipo'] in TIPOS_BLOQ:
                        r = RADIO_BLOQ[obj['tipo']]
                        ddx = self.x - obj['x']; ddy = self.y - obj['y']
                        d = math.hypot(ddx, ddy)
                        if d < r and d > 1:
                            desvio_x += (ddx/d) * (r-d)/r * 2
                            desvio_y += (ddy/d) * (r-d)/r * 2
                self.x += dx/dist*spd + desvio_x
                self.y += dy/dist*spd + desvio_y
                self.mirando_izq=dx<0
            if self.estado_timer<=0: self.estado="VAGANDO"; self.obj_target=None; self.estado_timer=200

        elif self.estado == "SALTANDO":
            # Avanza la fase del salto (velocidad del bote)
            self.salto_fase += 0.12
            # Mantener self.y igual que la seta para que el sort lo pinte DESPUÉS (encima)
            if self.obj_target is not None:
                self.y = float(self.obj_target['y'])
            if self.estado=='DESEO': self.coin_t+=1
            if self.estado_timer<=0:
                self.estado="VAGANDO"; self.obj_target=None
                self.vx=random.uniform(-0.6,0.6); self.vy=random.uniform(-0.3,0.3)
                self.estado_timer=random.randint(150,300)

        else:
            if self.estado=='DESEO': self.coin_t+=1
            if self.estado_timer<=0:
                self.estado="VAGANDO"; self.obj_target=None
                self.vx=random.uniform(-0.6,0.6); self.vy=random.uniform(-0.3,0.3)
                self.estado_timer=random.randint(150,300)

    def dibujar(self, sup, t_ms):
        # --- Dibujar corazones flotantes (besos en banco) ---
        for p in self.corazones:
            _dibujar_corazon(sup, int(p['x']), int(p['y']), p['r'], int(p['alpha']))

        if self.estado in ("VAGANDO","YENDO"):
            bounce_y = int(math.sin(t_ms*0.01 + self.bounce_off) * 1.5)
            cabeceo_y = int(math.sin(self.cabeceo_timer * 0.4) * 6) if self.cabeceo_timer > 0 else 0
            dibujar_animal(sup, self.tipo, int(self.x), int(self.y) + bounce_y + cabeceo_y,
                           0.52, self.mirando_izq, self.parpadeo_activo)

        elif self.estado == "SALTANDO" and self.obj_target is not None:
            # Bote sobre la seta: seno siempre positivo → el animal sube y baja
            # abs(sin) da forma de rebote, se aplana en el suelo (base de la seta)
            fase = self.salto_fase
            altura_max = 28   # píxeles de altura máxima del salto
            bote = abs(math.sin(fase))              # 0→1→0→1... forma de "bote"
            salto_y = -int(bote * altura_max)       # negativo = hacia arriba

            # Ligero aplastamiento cuando toca la seta (cerca del suelo del bote)
            squash = 1.0 - bote * 0.18             # 1.0 normal … 0.82 aplastado
            escala_salto = 0.52 * squash

            # Estrellitas de impacto en el suelo del bote
            if bote < 0.08:   # justo al "tocar"
                for _ in range(2):
                    ox = random.randint(-14, 14)
                    oy = random.randint(-4, 4)
                    r_e = random.randint(2, 4)
                    pygame.draw.circle(sup, (255, 230, 80),
                                       (int(self.x) + ox, int(self.y) + oy), r_e)

            # -18 = encima del sombrero de la seta; salto_y añade el bote hacia arriba
            dibujar_animal(sup, self.tipo,
                           int(self.x), int(self.y) - 18 + salto_y,
                           escala_salto, self.mirando_izq, self.parpadeo_activo)

        elif self.estado == "SENTADO" and self.obj_target is not None and self.obj_target.get('tipo') == 'hamaca':
            bx = self.obj_target['x']
            by = self.obj_target['y']
            for i, letra in enumerate(['z','z','Z']):
                fase = (t_ms * 0.0015 + i * 0.8 + self.zzz_off) % (math.pi * 2)
                alpha = int(max(0, min(255, 180 * math.sin(fase))))
                if alpha < 20: continue
                ox2 = int(math.sin(fase * 0.5 + i) * 8)
                oy2 = -int(20 + i*12 + math.cos(fase)*4)
                sz = 12 + i * 3
                fnt = pygame.font.SysFont("Verdana", sz, bold=True)
                tz = fnt.render(letra, True, (180, 220, 255))
                tz.set_alpha(alpha)
                sup.blit(tz, (bx + ox2 + 8, by + oy2))


class Visitante:
    def __init__(self):
        self.x = 1050; self.y = 500
        self.target_x = random.randint(600,800)
        self.dest_banco_x = 450
        self.estado = "ENTRANDO"
        self.tipo = random.choice(TIPOS_ANIMAL)
        self.rect = pygame.Rect(self.x-40, self.y-90, 120, 140)
        self.parpadeo_timer = random.randint(150,400)
        self.parpadeo_dur = 0
        self.parpadeo_activo = False
        self.timer_sentado = 0

    def actualizar(self):
        self.parpadeo_timer -= 1
        if self.parpadeo_timer <= 0:
            if self.parpadeo_activo:
                self.parpadeo_dur -= 1
                if self.parpadeo_dur <= 0:
                    self.parpadeo_activo = False
                    self.parpadeo_timer = random.randint(150, 400)
            else:
                self.parpadeo_activo = True
                self.parpadeo_dur = random.randint(3, 7)
                self.parpadeo_timer = self.parpadeo_dur

        if self.estado == "ENTRANDO":
            self.x -= 2
            if self.x <= self.target_x: self.estado = "ESPERANDO"
        elif self.estado == "YENDO_BANCO":
            self.x -= 2
            if self.x <= self.dest_banco_x:
                self.estado = "SENTADO"
                self.timer_sentado = 200
        elif self.estado == "SENTADO":
            self.timer_sentado -= 1
            if self.timer_sentado <= 0: self.estado = "SALIENDO"
        elif self.estado == "SALIENDO":
            self.x -= 3
            if self.x < 350: return True
        self.rect.x = self.x-40
        return False

    def dibujar(self, sup, t_ms=0):
        x, y = int(self.x), int(self.y)
        dy = -45 if self.estado == "SENTADO" else 0
        dibujar_animal(sup, self.tipo, x, y + dy, 0.8, parpadeo=self.parpadeo_activo)
        
        if self.estado == "ESPERANDO":
            bx, by = x + 20, y - 75
            pygame.draw.ellipse(sup, (255, 255, 255), (bx, by, 50, 42)) 
            pygame.draw.polygon(sup, (255, 255, 255), [(bx+10, by+35), (bx+20, by+35), (bx+5, by+50)])
            cx, cy = bx + 25, by + 22
            pygame.draw.ellipse(sup, (160, 110, 60), (cx-10, cy+6, 20, 5))
            pygame.draw.rect(sup, (120, 75, 45), (cx-7, cy-4, 14, 11), border_radius=2)
            pygame.draw.arc(sup, (120, 75, 45), (cx+3, cy-3, 7, 8), -math.pi/2, math.pi/2, 2)
            for i in range(3):
                fase = t_ms * 0.005 + i * 1.5
                hx = cx - 5 + (i * 5) + math.sin(fase) * 2
                pygame.draw.line(sup, (180, 180, 180), (hx, cy - 8), (hx + math.sin(fase), cy - 15), 2)
