import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ----------------- DATOS -----------------
heroes = [
    {
        "nombre": "biron",
        "rol": [
            "top"
        ],
        "salud_max": 3508,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "mayene",
        "rol": [
            "jg"
        ],
        "salud_max": 3409,
        "mana_max": None,
        "ataque_fisico": 182,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "musashi",
        "rol": [
            "jg"
        ],
        "salud_max": 3300,
        "mana_max": None,
        "ataque_fisico": 177,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Liam po",
        "rol": [
            "supp"
        ],
        "salud_max": 3722,
        "mana_max": None,
        "ataque_fisico": 198,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "dun",
        "rol": [
            "supp"
        ],
        "salud_max": 3590,
        "mana_max": None,
        "ataque_fisico": 193,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "fuzi",
        "rol": [
            "top"
        ],
        "salud_max": 3552,
        "mana_max": None,
        "ataque_fisico": 176,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "sun ce",
        "rol": [
            "jg"
        ],
        "salud_max": 3624,
        "mana_max": None,
        "ataque_fisico": 166,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Allain",
        "rol": [
            "top"
        ],
        "salud_max": 3512,
        "mana_max": None,
        "ataque_fisico": 187,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Arthur",
        "rol": [
            "jg"
        ],
        "salud_max": 3748,
        "mana_max": None,
        "ataque_fisico": 175,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Ata",
        "rol": [
            "jg"
        ],
        "salud_max": 3722,
        "mana_max": None,
        "ataque_fisico": 191,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Augran",
        "rol": [
            "jg"
        ],
        "salud_max": 3401,
        "mana_max": None,
        "ataque_fisico": 187,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Charlotte",
        "rol": [
            "jg"
        ],
        "salud_max": 3413,
        "mana_max": None,
        "ataque_fisico": 176,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "dharma",
        "rol": [
            "jg"
        ],
        "salud_max": 3456,
        "mana_max": None,
        "ataque_fisico": 184,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Donghuang",
        "rol": [
            "supp"
        ],
        "salud_max": 3429,
        "mana_max": None,
        "ataque_fisico": 168,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "Guan yu",
        "rol": [
            "top"
        ],
        "salud_max": 3667,
        "mana_max": None,
        "ataque_fisico": 178,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Heino",
        "rol": [
            "mid"
        ],
        "salud_max": 3313,
        "mana_max": None,
        "ataque_fisico": 165,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "kaiser",
        "rol": [
            "jg"
        ],
        "salud_max": 3476,
        "mana_max": None,
        "ataque_fisico": 188,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "LI XIN",
        "rol": [
            "jg"
        ],
        "salud_max": 3512,
        "mana_max": None,
        "ataque_fisico": 190,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Bai qi",
        "rol": [
            "top"
        ],
        "salud_max": 3690,
        "mana_max": None,
        "ataque_fisico": 181,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Lui bang",
        "rol": [
            "supp"
        ],
        "salud_max": 3543,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Lu bu",
        "rol": [
            "top"
        ],
        "salud_max": 3587,
        "mana_max": None,
        "ataque_fisico": 192,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "menki",
        "rol": [
            "jg"
        ],
        "salud_max": 3369,
        "mana_max": None,
        "ataque_fisico": 171,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "mi yue",
        "rol": [
            "jg"
        ],
        "salud_max": 3251,
        "mana_max": None,
        "ataque_fisico": 160,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "mulan",
        "rol": [
            "top"
        ],
        "salud_max": 3321,
        "mana_max": None,
        "ataque_fisico": 171,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "nezha",
        "rol": [
            "top"
        ],
        "salud_max": 3526,
        "mana_max": None,
        "ataque_fisico": 175,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Ukyo tachibana",
        "rol": [
            "jg"
        ],
        "salud_max": 3250,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "wuyan",
        "rol": [
            "jg"
        ],
        "salud_max": 3702,
        "mana_max": None,
        "ataque_fisico": 178,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "yang jian",
        "rol": [
            "jg"
        ],
        "salud_max": 3407,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "yao",
        "rol": [
            "jg"
        ],
        "salud_max": 3304,
        "mana_max": None,
        "ataque_fisico": 173,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "Zhuangzi",
        "rol": [
            "supp"
        ],
        "salud_max": 3624,
        "mana_max": None,
        "ataque_fisico": 174,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "Cuerpo a cuerpo"
    },
    {
        "nombre": "angela",
        "rol": [
            "mid"
        ],
        "salud_max": 3328,
        "mana_max": None,
        "ataque_fisico": 172,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "da qiao",
        "rol": [
            "supp"
        ],
        "salud_max": 3266,
        "mana_max": None,
        "ataque_fisico": 171,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "daji",
        "rol": [
            "mid"
        ],
        "salud_max": 3295,
        "mana_max": None,
        "ataque_fisico": 172,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "diochan",
        "rol": [
            "mid"
        ],
        "salud_max": 3205,
        "mana_max": None,
        "ataque_fisico": 170,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "dr bian",
        "rol": [
            "mid"
        ],
        "salud_max": 3253,
        "mana_max": None,
        "ataque_fisico": 171,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "gan & mo",
        "rol": [
            "mid"
        ],
        "salud_max": 3251,
        "mana_max": None,
        "ataque_fisico": 165,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "gao",
        "rol": [
            "mid"
        ],
        "salud_max": 3320,
        "mana_max": None,
        "ataque_fisico": 167,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "kongming",
        "rol": [
            "jg"
        ],
        "salud_max": 3300,
        "mana_max": None,
        "ataque_fisico": 162,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "lady zhen",
        "rol": [
            "mid"
        ],
        "salud_max": 3202,
        "mana_max": None,
        "ataque_fisico": 168,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "liang",
        "rol": [
            "supp"
        ],
        "salud_max": 3204,
        "mana_max": None,
        "ataque_fisico": 171,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "mai shiranui",
        "rol": [
            "mid"
        ],
        "salud_max": 3288,
        "mana_max": None,
        "ataque_fisico": 172,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "milady",
        "rol": [
            "mid"
        ],
        "salud_max": 3213,
        "mana_max": None,
        "ataque_fisico": 168,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "mozi",
        "rol": [
            "supp"
        ],
        "salud_max": 3372,
        "mana_max": None,
        "ataque_fisico": 178,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "nuwa",
        "rol": [
            "mid"
        ],
        "salud_max": 3226,
        "mana_max": None,
        "ataque_fisico": 163,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "princesa frost",
        "rol": [
            "mid"
        ],
        "salud_max": 3206,
        "mana_max": None,
        "ataque_fisico": 166,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "shangguan",
        "rol": [
            "mid"
        ],
        "salud_max": 3389,
        "mana_max": None,
        "ataque_fisico": 161,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "shi",
        "rol": [
            "mid"
        ],
        "salud_max": 3225,
        "mana_max": None,
        "ataque_fisico": 168,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "sima yi",
        "rol": [
            "jg"
        ],
        "salud_max": 3257,
        "mana_max": None,
        "ataque_fisico": 173,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "xiao qiao",
        "rol": [
            "mid"
        ],
        "salud_max": 3200,
        "mana_max": None,
        "ataque_fisico": 163,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "yixing",
        "rol": [
            "mid"
        ],
        "salud_max": 3253,
        "mana_max": None,
        "ataque_fisico": 173,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "yuhuan",
        "rol": [
            "jg"
        ],
        "salud_max": 3202,
        "mana_max": None,
        "ataque_fisico": 166,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "zhou yu",
        "rol": [
            "mid"
        ],
        "salud_max": 3278,
        "mana_max": None,
        "ataque_fisico": 170,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "ziya",
        "rol": [
            "supp"
        ],
        "salud_max": 3222,
        "mana_max": None,
        "ataque_fisico": 172,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "agudo",
        "rol": [
            "jg"
        ],
        "salud_max": 2651,
        "mana_max": None,
        "ataque_fisico": 186,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "alessio",
        "rol": [
            "adc"
        ],
        "salud_max": 3340,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "arli",
        "rol": [
            "adc"
        ],
        "salud_max": 3219,
        "mana_max": None,
        "ataque_fisico": 175,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "chano",
        "rol": [
            "jg"
        ],
        "salud_max": 3299,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "consorte yu",
        "rol": [
            "adc"
        ],
        "salud_max": 3234,
        "mana_max": None,
        "ataque_fisico": 177,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "di renjie",
        "rol": [
            "adc"
        ],
        "salud_max": 3352,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "erin",
        "rol": [
            "adc"
        ],
        "salud_max": 3245,
        "mana_max": None,
        "ataque_fisico": 176,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "fang",
        "rol": [
            "jg"
        ],
        "salud_max": 3257,
        "mana_max": None,
        "ataque_fisico": 175,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "garo",
        "rol": [
            "adc"
        ],
        "salud_max": 3282,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "hou yi",
        "rol": [
            "adc"
        ],
        "salud_max": 3362,
        "mana_max": None,
        "ataque_fisico": 176,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "huang zhong",
        "rol": [
            "adc"
        ],
        "salud_max": 3318,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "lady sun",
        "rol": [
            "adc"
        ],
        "salud_max": 3329,
        "mana_max": None,
        "ataque_fisico": 179,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "loong",
        "rol": [
            "adc"
        ],
        "salud_max": 3256,
        "mana_max": None,
        "ataque_fisico": 175,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "luara",
        "rol": [
            "adc"
        ],
        "salud_max": 3204,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "luban n.°7",
        "rol": [
            "adc"
        ],
        "salud_max": 3366,
        "mana_max": None,
        "ataque_fisico": 184,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "marco polo",
        "rol": [
            "adc"
        ],
        "salud_max": 3207,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "meng ya",
        "rol": [
            "adc"
        ],
        "salud_max": 3331,
        "mana_max": None,
        "ataque_fisico": 175,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "shouyue",
        "rol": [
            "adc"
        ],
        "salud_max": 3275,
        "mana_max": None,
        "ataque_fisico": 188,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 10,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "arke",
        "rol": [
            "jg"
        ],
        "salud_max": 3315,
        "mana_max": None,
        "ataque_fisico": 188,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 125,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "A distancia"
    },
    {
        "nombre": "athena",
        "rol": [
            "jg"
        ],
        "salud_max": 3201,
        "mana_max": None,
        "ataque_fisico": 176,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 390,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "butterfly",
        "rol": [
            "jg"
        ],
        "salud_max": 3400,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "cirrus",
        "rol": [
            "jg"
        ],
        "salud_max": 3218,
        "mana_max": None,
        "ataque_fisico": 181,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "dian wei",
        "rol": [
            "jg"
        ],
        "salud_max": 3595,
        "mana_max": None,
        "ataque_fisico": 171,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "feyd",
        "rol": [
            "jg"
        ],
        "salud_max": 3335,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "han xin",
        "rol": [
            "jg"
        ],
        "salud_max": 3232,
        "mana_max": None,
        "ataque_fisico": 190,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "jing",
        "rol": [
            "jg"
        ],
        "salud_max": 3343,
        "mana_max": None,
        "ataque_fisico": 186,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "lam",
        "rol": [
            "jg"
        ],
        "salud_max": 3312,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "li bai",
        "rol": [
            "jg"
        ],
        "salud_max": 3257,
        "mana_max": None,
        "ataque_fisico": 181,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "liu bei",
        "rol": [
            "jg"
        ],
        "salud_max": 3402,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "luna",
        "rol": [
            "jg"
        ],
        "salud_max": 3207,
        "mana_max": None,
        "ataque_fisico": 170,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "nakoruru",
        "rol": [
            "jg"
        ],
        "salud_max": 3359,
        "mana_max": None,
        "ataque_fisico": 186,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "pei",
        "rol": [
            "jg"
        ],
        "salud_max": 3238,
        "mana_max": None,
        "ataque_fisico": 175,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "príncipe de lanling",
        "rol": [
            "jg"
        ],
        "salud_max": 3340,
        "mana_max": None,
        "ataque_fisico": 183,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 390,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "wukong",
        "rol": [
            "jg"
        ],
        "salud_max": 3334,
        "mana_max": None,
        "ataque_fisico": 183,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 20,
        "daño_critico": 150,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "xuance",
        "rol": [
            "jg"
        ],
        "salud_max": 3369,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "ying",
        "rol": [
            "jg"
        ],
        "salud_max": 3394,
        "mana_max": None,
        "ataque_fisico": 183,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 380,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "zilong",
        "rol": [
            "jg"
        ],
        "salud_max": 3468,
        "mana_max": None,
        "ataque_fisico": 185,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 385,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "cai yan",
        "rol": [
            "supp"
        ],
        "salud_max": 3314,
        "mana_max": None,
        "ataque_fisico": 167,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "dolia",
        "rol": [
            "supp"
        ],
        "salud_max": 3308,
        "mana_max": None,
        "ataque_fisico": 170,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "dyadia",
        "rol": [
            "supp"
        ],
        "salud_max": 3332,
        "mana_max": None,
        "ataque_fisico": 169,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "guiguzi",
        "rol": [
            "supp"
        ],
        "salud_max": 3394,
        "mana_max": None,
        "ataque_fisico": 166,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "kui",
        "rol": [
            "supp"
        ],
        "salud_max": 3657,
        "mana_max": None,
        "ataque_fisico": 181,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 370,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "liu shan",
        "rol": [
            "supp"
        ],
        "salud_max": 3659,
        "mana_max": None,
        "ataque_fisico": 180,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "ming",
        "rol": [
            "supp"
        ],
        "salud_max": 3330,
        "mana_max": None,
        "ataque_fisico": 168,
        "ataque_magico": 10,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "sakeer",
        "rol": [
            "supp"
        ],
        "salud_max": 3331,
        "mana_max": None,
        "ataque_fisico": 140,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "sun bin",
        "rol": [
            "supp"
        ],
        "salud_max": 3468,
        "mana_max": None,
        "ataque_fisico": 177,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 360,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "xiang yu",
        "rol": [
            "supp"
        ],
        "salud_max": 3666,
        "mana_max": None,
        "ataque_fisico": 195,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    },
    {
        "nombre": "yaria",
        "rol": [
            "supp"
        ],
        "salud_max": 2913,
        "mana_max": None,
        "ataque_fisico": 165,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 365,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 5,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "a distancia"
    },
    {
        "nombre": "Zhang fei",
        "rol": [
            "supp"
        ],
        "salud_max": 3658,
        "mana_max": None,
        "ataque_fisico": 168,
        "ataque_magico": 0,
        "defensa_fisica": 150,
        "defensa_magica": 75,
        "velocidad_movimiento": 375,
        "perforacion_fisica": 0,
        "perforacion_magica": 0,
        "velocidad_ataque_bonus": 0,
        "critico": 0,
        "daño_critico": 200,
        "robo_vida_fisico": 0,
        "robo_vida_magico": 0,
        "reduccion_enfriamiento": 0,
        "resistencia": 0,
        "regeneracion_salud": None,
        "regeneracion_mana": None,
        "alcance_ataque": "cuerpo a cuerpo"
    }
]

df = pd.DataFrame(heroes)

# ----------------- CÁLCULO DE ÍNDICE DE COMBATE -----------------
df["indice_combate"] = df["salud_max"] * 0.25 + df["ataque_fisico"] * 0.4 + df["defensa_fisica"] * 0.25 + df["velocidad_movimiento"] * 0.1

# ----------------- INTERFAZ -----------------
st.title("📊 Comparador Profesional de Héroes")

st.markdown("""
Este sistema te permite comparar héroes entre sí usando estadísticas clave para determinar ventajas competitivas.
También puedes analizar el rendimiento promedio por rol y obtener recomendaciones basadas en atributos.
""")

# Selección de héroes
col1, col2 = st.columns(2)
with col1:
    hero1 = st.selectbox("Selecciona el primer héroe", df['nombre'])
with col2:
    hero2 = st.selectbox("Selecciona el segundo héroe", df['nombre'], index=1)

hero1_data = df[df['nombre'] == hero1].iloc[0]
hero2_data = df[df['nombre'] == hero2].iloc[0]

# ----------------- VISUALIZACIÓN ESTADÍSTICAS -----------------
st.markdown("## 🔍 Estadísticas individuales")

col1, col2 = st.columns(2)
with col1:
    st.subheader(hero1)
    st.metric("Salud Máx", hero1_data["salud_max"])
    st.metric("Ataque Físico", hero1_data["ataque_fisico"])
    st.metric("Defensa Física", hero1_data["defensa_fisica"])
    st.metric("Velocidad", hero1_data["velocidad_movimiento"])
    st.metric("Índice de Combate", round(hero1_data["indice_combate"], 2))
    st.metric("Bajas", hero1_data["bajas"])
    st.metric("Muertes", hero1_data["muertes"])
with col2:
    st.subheader(hero2)
    st.metric("Salud Máx", hero2_data["salud_max"])
    st.metric("Ataque Físico", hero2_data["ataque_fisico"])
    st.metric("Defensa Física", hero2_data["defensa_fisica"])
    st.metric("Velocidad", hero2_data["velocidad_movimiento"])
    st.metric("Índice de Combate", round(hero2_data["indice_combate"], 2))
    st.metric("Bajas", hero2_data["bajas"])
    st.metric("Muertes", hero2_data["muertes"])

# ----------------- COMPARACIÓN -----------------
def comparar_heroes(h1, h2):
    def evaluar(campo, label):
        if h1[campo] > h2[campo]:
            return f"✅ {h1['nombre']} tiene más {label}"
        elif h1[campo] < h2[campo]:
            return f"✅ {h2['nombre']} tiene más {label}"
        else:
            return f"🔸 Ambos tienen la misma {label}"

    return [
        evaluar("salud_max", "salud máxima"),
        evaluar("ataque_fisico", "ataque físico"),
        evaluar("defensa_fisica", "defensa física"),
        evaluar("velocidad_movimiento", "velocidad de movimiento"),
        evaluar("indice_combate", "índice de combate"),
        evaluar("bajas", "bajas"),
        evaluar("muertes", "muertes"),
    ]

st.markdown("## ⚔️ Comparación directa")
for item in comparar_heroes(hero1_data, hero2_data):
    st.write("- " + item)

# ----------------- GRÁFICO DE COMPARACIÓN -----------------
st.markdown("## 📈 Comparación gráfica")

metrics = ['salud_max', 'ataque_fisico', 'defensa_fisica', 'velocidad_movimiento', 'bajas', 'muertes']
df_plot = df[df["nombre"].isin([hero1, hero2])].set_index("nombre")[metrics]

st.bar_chart(df_plot.T)

# ----------------- ANÁLISIS POR ROL -----------------
st.markdown("## 🧠 Análisis promedio por rol")
roles_unicos = sorted(set([rol for sublist in df["rol"] for rol in sublist]))
rol_seleccionado = st.selectbox("Selecciona un rol", roles_unicos)

df_filtrado = df[df['rol'].apply(lambda x: rol_seleccionado in x)]
if not df_filtrado.empty:
    promedio_rol = df_filtrado[metrics].mean()
    st.write(f"Promedio para el rol **{rol_seleccionado.upper()}**:")
    st.write(promedio_rol)

    fig = px.bar(promedio_rol, title=f"Promedio de estadísticas para rol {rol_seleccionado.upper()}")
    st.plotly_chart(fig)
else:
    st.warning("No hay héroes para ese rol.")

# ----------------- RANKING POR ESTADÍSTICAS -----------------
st.markdown("## 🏅 Ranking de héroes por estadísticas")
stat_to_rank = st.selectbox("Selecciona la estadística para ver el Top 5", metrics + ["indice_combate"])
st.dataframe(df.sort_values(stat_to_rank, ascending=False).reset_index(drop=True).head(5))

# ----------------- BÚSQUEDA AVANZADA -----------------
st.markdown("## 🔍 Búsqueda por atributos mínimos")
col1, col2 = st.columns(2)
with col1:
    min_ataque = st.slider("Ataque físico mínimo", 100, 300, 180)
    min_salud = st.slider("Salud máxima mínima", 2000, 4000, 3000)
with col2:
    min_defensa = st.slider("Defensa física mínima", 100, 200, 150)
    min_velocidad = st.slider("Velocidad mínima", 300, 400, 370)

filtro = (df["ataque_fisico"] >= min_ataque) & (df["salud_max"] >= min_salud) & \
         (df["defensa_fisica"] >= min_defensa) & (df["velocidad_movimiento"] >= min_velocidad)

st.write("### Resultados que cumplen los criterios:")
st.dataframe(df[filtro])

# ----------------- SISTEMA DE RECOMENDACIONES -----------------
st.markdown("## 🤖 Recomendaciones de sinergia o counter")
recomendaciones = []
if hero1_data['ataque_fisico'] > 190:
    recomendaciones.append("🔹 Este héroe tiene mucho daño físico, considera acompañarlo con un soporte que lo proteja.")
if hero1_data['salud_max'] < 3300:
    recomendaciones.append("🔸 Tiene poca salud. Evita emparejarlo con héroes frágiles.")
if hero1_data['velocidad_movimiento'] >= 380:
    recomendaciones.append("🚀 Alta movilidad. Útil para flanqueos o emboscadas.")
if hero1_data['bajas'] > hero1_data['muertes']:
    recomendaciones.append("🔸 Este héroe es eficiente en peleas. Tiene un buen ratio de bajas a muertes.")
else:
    recomendaciones.append("⚠️ Este héroe tiene un alto número de muertes en comparación con sus bajas.")

if recomendaciones:
    for rec in recomendaciones:
        st.write(rec)
else:
    st.info("Este héroe tiene estadísticas equilibradas. No se detectaron recomendaciones particulares.")
