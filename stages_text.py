# -*- coding: utf-8 -*-
""""The lab changes with the stages" section, in every language.

Stage names 2 to 5 are the game's own banners (texts.gd stage_1..stage_4);
the first stage gets its own word here.
"""
import re

GAME_CODES = ["en", "fr", "de", "es", "it", "pt_BR", "ru", "tr", "pl", "ja", "ko", "zh_CN", "zh_TW", "id", "th", "vi"]
TEXTS = "/Users/sebastienreinders/Desktop/capy_shift/scripts/game/l10n/texts.gd"

INTRO = {
    "fr": ("Le labo change avec les paliers", "Plus tu tiens, plus ça s'accélère… et plus l'ambiance s'emballe : lumière, couleurs, éclairs, alarmes, jusqu'à l'orage du palier légendaire !", "Calme"),
    "en": ("The lab changes with each stage", "The longer you last, the faster it gets… and the wilder the mood: lights, colors, lightning, alarms, up to the storm of the legendary stage!", "Calm"),
    "de": ("Das Labor verändert sich mit jeder Stufe", "Je länger du durchhältst, desto schneller wird es … und desto wilder die Stimmung: Licht, Farben, Blitze, Alarme bis zum Gewitter der legendären Stufe!", "Ruhig"),
    "es": ("El laboratorio cambia con cada nivel", "Cuanto más aguantas, más rápido va… y más loco el ambiente: luces, colores, rayos, alarmas, ¡hasta la tormenta del nivel legendario!", "Tranquilo"),
    "it": ("Il laboratorio cambia a ogni livello", "Più resisti, più accelera… e più l'atmosfera si scatena: luci, colori, fulmini, allarmi, fino alla tempesta del livello leggendario!", "Calmo"),
    "pt-BR": ("O laboratório muda a cada nível", "Quanto mais você aguenta, mais rápido fica… e mais louco o clima: luzes, cores, raios, alarmes, até a tempestade do nível lendário!", "Calmo"),
    "ru": ("Лаборатория меняется с каждым этапом", "Чем дольше держишься, тем быстрее… и тем безумнее атмосфера: свет, цвета, молнии, тревога — вплоть до грозы легендарного этапа!", "Спокойно"),
    "tr": ("Laboratuvar her seviyede değişir", "Ne kadar dayanırsan o kadar hızlanır… ve ortam çılgınlaşır: ışıklar, renkler, şimşekler, alarmlar, efsanevi seviyenin fırtınasına kadar!", "Sakin"),
    "pl": ("Laboratorium zmienia się z każdym etapem", "Im dłużej wytrzymasz, tym szybciej… i tym szaleńszy klimat: światła, kolory, błyskawice, alarmy, aż do burzy etapu legendarnego!", "Spokojnie"),
    "ja": ("ステージごとにラボが変わる", "がんばるほどスピードアップ…そして雰囲気もヒートアップ：光、色、稲妻、アラーム、伝説ステージの嵐まで！", "おだやか"),
    "ko": ("단계마다 연구소가 바뀌어요", "오래 버틸수록 빨라지고… 분위기도 달아올라요: 조명, 색, 번개, 경보, 전설 단계의 폭풍까지!", "평온"),
    "zh-CN": ("实验室随阶段变化", "坚持越久越快……气氛也越疯狂：灯光、色彩、闪电、警报，直到传奇阶段的暴风雨！", "平静"),
    "zh-TW": ("實驗室隨階段變化", "堅持越久越快……氣氛也越瘋狂：燈光、色彩、閃電、警報，直到傳奇階段的暴風雨！", "平靜"),
    "id": ("Lab berubah di setiap tahap", "Makin lama bertahan, makin cepat… dan suasananya makin heboh: lampu, warna, petir, alarm, sampai badai di tahap legendaris!", "Tenang"),
    "th": ("แล็บเปลี่ยนไปทุกด่าน", "ยิ่งอยู่ได้นาน ยิ่งเร็วขึ้น… บรรยากาศก็ยิ่งเดือด: แสง สี สายฟ้า สัญญาณเตือน ไปจนถึงพายุในด่านตำนาน!", "สงบ"),
    "vi": ("Phòng thí nghiệm đổi theo từng màn", "Trụ càng lâu càng nhanh… và không khí càng bùng nổ: ánh sáng, màu sắc, tia sét, báo động, cho tới cơn bão ở màn huyền thoại!", "Yên bình"),
}


def _game_stage_names() -> dict:
    source = open(TEXTS, encoding="utf-8").read()
    names = {}
    for k in range(1, 5):
        block = re.search(r'"stage_%d": \[(.*?)\],' % k, source, re.S).group(1)
        values = re.findall(r'"((?:[^"\\]|\\.)*)"', block)
        for code, value in zip(GAME_CODES, values):
            names.setdefault(code.replace("_", "-"), []).append(value)
    return names


STAGE_NAMES = _game_stage_names()


def section(code: str) -> dict:
    title, sub, first = INTRO[code]
    return {"title": title, "sub": sub, "names": [first] + STAGE_NAMES[code]}
