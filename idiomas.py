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

# Nombres de ítems de tienda jardín
JARDIN_NOMBRES = {
    "es": {
        "flor_roja":        "Flor Roja",
        "flor_azul":        "Flor Azul",
        "seta":             "Seta Otoñal",
        "piedra":           "Piedra Camino",
        "agua":             "Tramo de Río",
        "taburete":         "Taburete Tronco",
        "banco":            "Banco de Parque",
        "farola":           "Farola Clásica",
        "fuente":           "Fuente de Piedra",
        "columpio":         "Columpio",
        "subebaja":         "Sube y Baja",
        "tobogan":          "Tobogán",
        "estanque_koi":     "Estanque Koi",
        "hamaca":           "Hamaca",
        "manta_picnic":     "Manta Picnic",
        "pozo_deseos":      "Pozo Deseos",
    },
    "en": {
        "flor_roja":        "Red Flower",
        "flor_azul":        "Blue Flower",
        "seta":             "Autumn Mushroom",
        "piedra":           "Stepping Stone",
        "agua":             "River Stretch",
        "taburete":         "Log Stool",
        "banco":            "Park Bench",
        "farola":           "Classic Lamp",
        "fuente":           "Stone Fountain",
        "columpio":         "Swing",
        "subebaja":         "Seesaw",
        "tobogan":          "Slide",
        "estanque_koi":     "Koi Pond",
        "hamaca":           "Hammock",
        "manta_picnic":     "Picnic Blanket",
        "pozo_deseos":      "Wishing Well",
    },
}

# Nombres de ítems tienda café (hojas)
CAFE_HOJAS_NOMBRES = {
    "es": {
        "chimenea":         "Chimenea",
        "ventana_bosque":   "Ventana Bosque",
        "nube_redonda":     "Nube Redonda",
        "nube_alargada":    "Nube Alargada",
        "nube_corazon":     "Nube Corazon",
        "nube_gatito":      "Nube Gatito",
        "estrella_fugaz":   "Estrella Fugaz",
        "arcoiris":         "Arcoiris",
        "estrella_deco":    "Estrella Deco",
        "piedrecita_cafe":  "Piedrecita",
    },
    "en": {
        "chimenea":         "Fireplace",
        "ventana_bosque":   "Forest Window",
        "nube_redonda":     "Round Cloud",
        "nube_alargada":    "Long Cloud",
        "nube_corazon":     "Heart Cloud",
        "nube_gatito":      "Kitty Cloud",
        "estrella_fugaz":   "Shooting Star",
        "arcoiris":         "Rainbow",
        "estrella_deco":    "Deco Star",
        "piedrecita_cafe":  "Pebble",
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
