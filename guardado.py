import json, os, constantes as c

def guardar_partida():
    data = {
        "dinero": c.dinero,
        "hojas_doradas": c.hojas_doradas,
        "ganancia_pasiva": c.ganancia_pasiva,
        "niveles": [m.nivel for m in c.lista_mejoras_cafe],
        "precios": [m.precio for m in c.lista_mejoras_cafe],
        "elementos_jardin": c.elementos_jardin_colocados,
        "mejoras_especiales": c.mejoras_especiales_compradas,
        "objetos_cielo": c.objetos_cielo_colocados,
        "timer_inauguracion": c.timer_inauguracion,
        "tiempo_jugado": c.tiempo_jugado,
        "record_match3": c.record_match3,
        "record_runner": c.record_runner,
        "record_calabazas": c.record_calabazas,
        "record_setas": c.record_setas,
        "idioma": c.idioma,
    }
    with open(c.SAVE_FILE, "w") as f:
        json.dump(data, f)


def cargar_partida():
    if not os.path.exists(c.SAVE_FILE):
        return False
    try:
        with open(c.SAVE_FILE) as f:
            data = json.load(f)
        c.dinero = data.get("dinero", 800000)
        c.hojas_doradas = data.get("hojas_doradas", 0)
        c.ganancia_pasiva = data.get("ganancia_pasiva", 0)
        niveles = data.get("niveles", [0] * 5)
        precios = data.get("precios", None)
        for i, m in enumerate(c.lista_mejoras_cafe):
            if i < len(niveles): m.nivel = niveles[i]
        if precios:
            for i, m in enumerate(c.lista_mejoras_cafe):
                if i < len(precios): m.precio = precios[i]
        c.elementos_jardin_colocados = data.get("elementos_jardin", [])
        c.mejoras_especiales_compradas = data.get("mejoras_especiales", [])
        c.objetos_cielo_colocados = data.get("objetos_cielo", [])
        saved_timer = data.get("timer_inauguracion", 0)
        if saved_timer != 0:
            c.timer_inauguracion = 1
            c.inauguracion_mostrada = True
        c.tiempo_jugado = data.get("tiempo_jugado", 0)
        c.record_match3 = data.get("record_match3", 0)
        c.record_runner = data.get("record_runner", 0)
        c.record_calabazas = data.get("record_calabazas", 0)
        c.record_setas = data.get("record_setas", 0)
        c.idioma = data.get("idioma", "es")
        return True
    except:
        return False


def reiniciar_partida():
    c.dinero = 800000
    c.hojas_doradas = 0
    c.ganancia_pasiva = 0
    precios_orig = [150, 800, 2500, 12000, 60000]
    for i, m in enumerate(c.lista_mejoras_cafe):
        m.nivel = 0
        m.precio = precios_orig[i]
    c.elementos_jardin_colocados.clear()
    c.mejoras_especiales_compradas.clear()
    c.objetos_cielo_colocados.clear()
    c.timer_inauguracion = 0
    c.tiempo_jugado = 0
    c.inauguracion_mostrada = False
    c.record_match3 = 0
    c.record_runner = 0
    c.record_calabazas = 0
    c.record_setas = 0
    # El idioma se conserva al reiniciar (es preferencia del usuario)
    c.pantalla_actual = "CAFE"
    c.item_seleccionado_jardin = None
    c.monedas.clear()
    c.visitantes.clear()
    c.confeti.clear()
    c.textos_flotantes.clear()
    c.animales_jardin.clear()
    if os.path.exists(c.SAVE_FILE):
        os.remove(c.SAVE_FILE)
