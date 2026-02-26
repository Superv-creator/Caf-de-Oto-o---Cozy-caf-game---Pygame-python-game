# idiomas.py — Traducciones del juego
# Añade aquí nuevas claves si amplías el juego

TEXTOS = {
    "es": {
        # ── HUD / General ──────────────────────────────────────────
        "moneda_recogida":      "+¥500",
        "pocas_hojas":          "Pocas hojas",
        "ya_instalado":         "Ya instalado",
        "instalado_cafe":       "Instalado en cafe",
        "sin_fondos":           "¡Sin fondos!",
        "guardado_inventario":  "Guardado en inventario",
        "colocar_cafe":         "Clic en el cafe para colocar",
        "cancelar_esc":         "Clic en el cafe para colocar  |  Esc cancela",

        # ── Menú opciones ──────────────────────────────────────────
        "titulo_juego":         "CAFÉ OTOÑAL",
        "tiempo_jugado":        "Tiempo jugado: {}",
        "musica":               "Música: {}",
        "sonido":               "Sonido: {}",
        "on":                   "ON",
        "off":                  "OFF",
        "reiniciar":            "Reiniciar partida",
        "cerrar":               "Cerrar",
        "idioma":               "Idioma: Español",
        "confirmar_titulo":     "¿Seguro?",
        "confirmar_texto":      "Se perderá todo el progreso.",
        "si":                   "Sí",
        "no":                   "No",

        # ── Panel izquierdo café ───────────────────────────────────
        "tienda_titulo":        "TIENDA OTOÑAL",
        "cafe_completado":      "¡CAFÉ COMPLETADO!",
        "decorar_cafe":         "DECORAR CAFE",
        "ir_jardin":            "IR AL JARDÍN",
        "minijuegos":           "MINIJUEGOS",
        "decorar_sub":          "Mejoras con hojas doradas",
        "jardin_sub":           "Decorar y ver visitantes",
        "mini_sub":             "Match-3, Runner, Defensa...",
        "volver":               "< Volver",
        "hojas_disp":           "Hojas: {}",

        # ── Tienda decorar café ────────────────────────────────────
        "decorar_titulo":       "DECORAR CAFE",
        "instalado":            "INSTALADO",
        "precio_hojas_cu":      "{} hojas c/u",
        "precio_hojas_fijo":    "{} hojas",
        "clic_cafe":            "{} hojas c/u  -  clic en cafe",

        # ── Submenú minijuegos ─────────────────────────────────────
        "mini_titulo":          "MINIJUEGOS",
        "mini_subtitulo":       "Gana hojas doradas",
        "match3_nombre":        "MATCH-3",
        "match3_sub":           "Combina fichas · gana hojas",
        "runner_nombre":        "RUNNER",
        "runner_sub":           "Salta obstáculos · gana hojas",
        "calabazas_nombre":     "TIRO CALABAZAS",
        "calabazas_sub":        "Apunta y dispara",
        "setas_nombre":         "COLECTA SETAS",
        "setas_sub":            "Reflejos en el bosque",
        "defensa_nombre":       "DEFENSA",
        "defensa_sub":          "Protege el café · gana hojas",

        # ── Jardín ────────────────────────────────────────────────
        "jardin_titulo":        "DECORA TU JARDÍN",
        "tab_deco":             "Decoración",
        "tab_mob":              "Mobiliario",
        "tab_juegos":           "Juegos",
        "tab_especial":         "Especial",
        "comprar_yen":          "¥{}",
        "comprar_hojas":        "{} Hojas",
        "hoja_ganada":          "+1 Hoja!",
        "max":                  "MÁXIMO",
        "coste":                "Coste: ¥{}",

        # ── Textos flotantes ──────────────────────────────────────
        "aprendiz_gano":        "Aprendiz ganó: ¥{}",
        "defensa_hojas":        "+{} hojas de defensa",
        "devuelto_hojas":       "+{} Hojas",
        "devuelto_yen":         "+¥{}",

        # ── Inauguración ──────────────────────────────────────────
        "gran_inauguracion":    "¡GRAN INAUGURACIÓN!",

        # ── Match-3 ───────────────────────────────────────────────
        "m3_hojas":             "Hojas: {}",
        "m3_record":            "Récord: {}",
        "m3_salir":             "ESC para salir",
        "m3_rebarajando":       "¡Rebarajando!",
        "m3_combo2":            "¡Combo x2!",
        "m3_combo3":            "¡Combo x3!",
        "m3_combo4":            "¡MEGA COMBO!",
        "m3_combo5":            "¡EXPLOSIÓN!",
        "m3_combo_n":           "¡Combo x{}!",

        # ── Runner ────────────────────────────────────────────────
        "run_hojas":            "Hojas: {}",
        "run_record":           "Récord: {}",
        "run_controles":        "ESC salir  |  ESPACIO saltar  |  doble salto disponible",
        "run_chocado":          "¡CHOCADO!",
        "run_reintentar":       "ESPACIO para reintentar  |  ESC para salir",

        # ── Setas ─────────────────────────────────────────────────
        "set_hojas":            "Hojas: {}",
        "set_tiempo":           "Tiempo: {}s",
        "set_record":           "Récord: {}",
        "set_fin":              "¡FIN DE LA COLECTA!",
        "set_mas10":            "+10",
        "set_genial":           "¡GENIAL! +50",
        "set_puaj":             "PUAJ! -25",

        # ── Calabazas ─────────────────────────────────────────────
        "cal_hojas":            "Hojas: {}",
        "cal_ronda":            "Ronda: {} | Tiros: {}",
        "cal_record":           "Récord: {}",
        "cal_nuevo_record":     "¡NUEVO RÉCORD!",
        "cal_sin_municion":     "SIN MUNICIÓN",
        "cal_salir":            "ESC para salir",

        # ── Defensa ───────────────────────────────────────────────
        "def_defensores":       "DEFENSORES",
        "def_volver":           "< Volver",
        "def_reiniciar":        "Reiniciar",
        "def_victoria":         "¡VICTORIA!",
        "def_victoria_sub":     "Las sombras han sido derrotadas",
        "def_premio":           "+250 hojas",
        "def_nuevo_juego":      "Haz clic para jugar de nuevo",
        "def_derrota":          "¡DERROTA!",
        "def_derrota_sub":      "Las sombras han cruzado el cafe...",
        "def_reintentar":       "Haz clic para reintentar",
        "def_oleada":           "Oleada  {}%",
        "def_oleada_final":     "¡¡ OLEADA FINAL !!",
        "def_velocidad1":       "x1",
        "def_velocidad2":       "x2",
        "def_velocidad3":       "x3",
        "def_cafe_letrero":     "CAFE",
        "def_sin_fondos":       "Sin fondos",
        # Nombres y descripciones de defensores
        "def_nombre_buho":      "Buho",
        "def_nombre_oso":       "Oso",
        "def_nombre_conejo":    "Conejo",
        "def_nombre_zorro":     "Zorro",
        "def_desc_buho":        "Genera hojas",
        "def_desc_oso":         "Tanque fuerte",
        "def_desc_conejo":      "Dispara bellas",
        "def_desc_zorro":       "Lanza fuego",
        # Cuenta atrás
        "def_cuenta_sub1":      "¡Coloca tus defensores!",
        "def_cuenta_sub2":      "¡Las sombras se acercan!",
        "def_cuenta_sub3":      "¡Defiende!",
    },

    "en": {
        # ── HUD / General ──────────────────────────────────────────
        "moneda_recogida":      "+¥500",
        "pocas_hojas":          "Not enough leaves",
        "ya_instalado":         "Already installed",
        "instalado_cafe":       "Installed in café",
        "sin_fondos":           "Not enough funds!",
        "guardado_inventario":  "Saved to inventory",
        "colocar_cafe":         "Click on the café to place",
        "cancelar_esc":         "Click on the café to place  |  Esc cancels",

        # ── Menú opciones ──────────────────────────────────────────
        "titulo_juego":         "AUTUMN CAFÉ",
        "tiempo_jugado":        "Time played: {}",
        "musica":               "Music: {}",
        "sonido":               "Sound: {}",
        "on":                   "ON",
        "off":                  "OFF",
        "reiniciar":            "Restart game",
        "cerrar":               "Close",
        "idioma":               "Language: English",
        "confirmar_titulo":     "Are you sure?",
        "confirmar_texto":      "All progress will be lost.",
        "si":                   "Yes",
        "no":                   "No",

        # ── Panel izquierdo café ───────────────────────────────────
        "tienda_titulo":        "AUTUMN SHOP",
        "cafe_completado":      "CAFÉ COMPLETE!",
        "decorar_cafe":         "DECORATE CAFÉ",
        "ir_jardin":            "GO TO GARDEN",
        "minijuegos":           "MINI-GAMES",
        "decorar_sub":          "Upgrades with golden leaves",
        "jardin_sub":           "Decorate and see visitors",
        "mini_sub":             "Match-3, Runner, Defense...",
        "volver":               "< Back",
        "hojas_disp":           "Leaves: {}",

        # ── Tienda decorar café ────────────────────────────────────
        "decorar_titulo":       "DECORATE CAFÉ",
        "instalado":            "INSTALLED",
        "precio_hojas_cu":      "{} leaves each",
        "precio_hojas_fijo":    "{} leaves",
        "clic_cafe":            "{} leaves each  -  click on café",

        # ── Submenú minijuegos ─────────────────────────────────────
        "mini_titulo":          "MINI-GAMES",
        "mini_subtitulo":       "Earn golden leaves",
        "match3_nombre":        "MATCH-3",
        "match3_sub":           "Match tiles · earn leaves",
        "runner_nombre":        "RUNNER",
        "runner_sub":           "Jump obstacles · earn leaves",
        "calabazas_nombre":     "PUMPKIN SHOT",
        "calabazas_sub":        "Aim and shoot",
        "setas_nombre":         "MUSHROOM HUNT",
        "setas_sub":            "Forest reflexes",
        "defensa_nombre":       "DEFENSE",
        "defensa_sub":          "Protect the café · earn leaves",

        # ── Jardín ────────────────────────────────────────────────
        "jardin_titulo":        "DECORATE YOUR GARDEN",
        "tab_deco":             "Decoration",
        "tab_mob":              "Furniture",
        "tab_juegos":           "Games",
        "tab_especial":         "Special",
        "comprar_yen":          "¥{}",
        "comprar_hojas":        "{} Leaves",
        "hoja_ganada":          "+1 Leaf!",
        "max":                  "MAX",
        "coste":                "Cost: ¥{}",

        # ── Textos flotantes ──────────────────────────────────────
        "aprendiz_gano":        "Apprentice earned: ¥{}",
        "defensa_hojas":        "+{} defense leaves",
        "devuelto_hojas":       "+{} Leaves",
        "devuelto_yen":         "+¥{}",

        # ── Inauguración ──────────────────────────────────────────
        "gran_inauguracion":    "GRAND OPENING!",

        # ── Match-3 ───────────────────────────────────────────────
        "m3_hojas":             "Leaves: {}",
        "m3_record":            "Record: {}",
        "m3_salir":             "ESC to exit",
        "m3_rebarajando":       "Reshuffling!",
        "m3_combo2":            "Combo x2!",
        "m3_combo3":            "Combo x3!",
        "m3_combo4":            "MEGA COMBO!",
        "m3_combo5":            "EXPLOSION!",
        "m3_combo_n":           "Combo x{}!",

        # ── Runner ────────────────────────────────────────────────
        "run_hojas":            "Leaves: {}",
        "run_record":           "Record: {}",
        "run_controles":        "ESC exit  |  SPACE jump  |  double jump available",
        "run_chocado":          "CRASHED!",
        "run_reintentar":       "SPACE to retry  |  ESC to exit",

        # ── Setas ─────────────────────────────────────────────────
        "set_hojas":            "Leaves: {}",
        "set_tiempo":           "Time: {}s",
        "set_record":           "Record: {}",
        "set_fin":              "TIME'S UP!",
        "set_mas10":            "+10",
        "set_genial":           "GREAT! +50",
        "set_puaj":             "YUCK! -25",

        # ── Calabazas ─────────────────────────────────────────────
        "cal_hojas":            "Leaves: {}",
        "cal_ronda":            "Round: {} | Shots: {}",
        "cal_record":           "Record: {}",
        "cal_nuevo_record":     "NEW RECORD!",
        "cal_sin_municion":     "OUT OF AMMO",
        "cal_salir":            "ESC to exit",

        # ── Defensa ───────────────────────────────────────────────
        "def_defensores":       "DEFENDERS",
        "def_volver":           "< Back",
        "def_reiniciar":        "Restart",
        "def_victoria":         "VICTORY!",
        "def_victoria_sub":     "The shadows have been defeated",
        "def_premio":           "+250 leaves",
        "def_nuevo_juego":      "Click to play again",
        "def_derrota":          "DEFEAT!",
        "def_derrota_sub":      "The shadows crossed the café...",
        "def_reintentar":       "Click to retry",
        "def_oleada":           "Wave  {}%",
        "def_oleada_final":     "FINAL WAVE!!",
        "def_velocidad1":       "x1",
        "def_velocidad2":       "x2",
        "def_velocidad3":       "x3",
        "def_cafe_letrero":     "CAFÉ",
        "def_sin_fondos":       "No funds",
        # Nombres y descripciones de defensores
        "def_nombre_buho":      "Owl",
        "def_nombre_oso":       "Bear",
        "def_nombre_conejo":    "Rabbit",
        "def_nombre_zorro":     "Fox",
        "def_desc_buho":        "Generates leaves",
        "def_desc_oso":         "Strong tank",
        "def_desc_conejo":      "Shoots acorns",
        "def_desc_zorro":       "Throws fire",
        # Cuenta atrás
        "def_cuenta_sub1":      "Place your defenders!",
        "def_cuenta_sub2":      "The shadows approach!",
        "def_cuenta_sub3":      "Defend!",
    },
}

# Nombres de mejoras del café
MEJORAS_NOMBRES = {
    "es": [
        ["Arreglar Madera","Barniz","Ventana","Nombre","Marquesina","Pizarra"],
        ["Farolillo","Dúo Farolillos","Vela de Té","Guirnalda","Jarrón"],
        ["Taburete","Dos Taburetes","Cojines","Banco","Alfombra"],
        ["Aprendiz Gatuno","Pañuelo","Gorro","Gato Experto"],
        ["Grano","Molinillo","Prensa Francesa","Receta Latte"],
    ],
    "en": [
        ["Fix Wood","Varnish","Window","Name Sign","Awning","Chalkboard"],
        ["Lantern","Duo Lanterns","Tea Candle","Garland","Vase"],
        ["Stool","Two Stools","Cushions","Bench","Rug"],
        ["Cat Apprentice","Scarf","Hat","Expert Cat"],
        ["Bean","Grinder","French Press","Latte Recipe"],
    ],
}

JARDIN_NOMBRES = {
    "es": {
        "flor_roja":      "Flor Roja",      "flor_azul":   "Flor Azul",
        "seta":           "Seta Otoñal",    "piedra":      "Piedra Camino",
        "agua":           "Tramo de Río",   "taburete":    "Taburete Tronco",
        "banco":          "Banco de Parque","farola":      "Farola Clásica",
        "fuente":         "Fuente de Piedra","columpio":   "Columpio",
        "subebaja":       "Sube y Baja",    "tobogan":     "Tobogán",
        "estanque_koi":   "Estanque Koi",   "hamaca":      "Hamaca",
        "manta_picnic":   "Manta Picnic",   "pozo_deseos": "Pozo Deseos",
    },
    "en": {
        "flor_roja":      "Red Flower",     "flor_azul":   "Blue Flower",
        "seta":           "Autumn Mushroom","piedra":      "Stepping Stone",
        "agua":           "River Stretch",  "taburete":    "Log Stool",
        "banco":          "Park Bench",     "farola":      "Classic Lamp",
        "fuente":         "Stone Fountain", "columpio":    "Swing",
        "subebaja":       "Seesaw",         "tobogan":     "Slide",
        "estanque_koi":   "Koi Pond",       "hamaca":      "Hammock",
        "manta_picnic":   "Picnic Blanket", "pozo_deseos": "Wishing Well",
    },
}

CAFE_HOJAS_NOMBRES = {
    "es": {
        "chimenea":        "Chimenea",       "ventana_bosque": "Ventana Bosque",
        "nube_redonda":    "Nube Redonda",   "nube_alargada":  "Nube Alargada",
        "nube_corazon":    "Nube Corazon",   "nube_gatito":    "Nube Gatito",
        "estrella_fugaz":  "Estrella Fugaz", "arcoiris":       "Arcoiris",
        "estrella_deco":   "Estrella Deco",  "piedrecita_cafe":"Piedrecita",
    },
    "en": {
        "chimenea":        "Fireplace",      "ventana_bosque": "Forest Window",
        "nube_redonda":    "Round Cloud",    "nube_alargada":  "Long Cloud",
        "nube_corazon":    "Heart Cloud",    "nube_gatito":    "Kitty Cloud",
        "estrella_fugaz":  "Shooting Star",  "arcoiris":       "Rainbow",
        "estrella_deco":   "Deco Star",      "piedrecita_cafe":"Pebble",
    },
}


def t(clave, *args):
    """Devuelve el texto en el idioma activo. Usa {} para formatear."""
    import constantes as c
    texto = TEXTOS.get(c.idioma, TEXTOS["es"]).get(clave, clave)
    if args:
        return texto.format(*args)
    return texto


def nombres_mejoras():
    import constantes as c
    return MEJORAS_NOMBRES.get(c.idioma, MEJORAS_NOMBRES["es"])


def nombre_item_jardin(tipo):
    import constantes as c
    return JARDIN_NOMBRES.get(c.idioma, JARDIN_NOMBRES["es"]).get(tipo, tipo)


def nombre_item_cafe_hoja(tipo):
    import constantes as c
    return CAFE_HOJAS_NOMBRES.get(c.idioma, CAFE_HOJAS_NOMBRES["es"]).get(tipo, tipo)
