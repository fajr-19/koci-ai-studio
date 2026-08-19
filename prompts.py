SCENE_LIBRARY = {
    "Yoyin": {
        "Yoyin Intro": "Yoyin sits proudly and calmly, then slowly turns her head as if checking on her children.",
        "Yoyin Menatap": "Yoyin gently blinks and looks around with a firm but caring mother expression.",
    },
    "Kokow": {
        "Kokow Rebahan": "Kokow slowly blinks and gently turns his head.",
        "Kokow Bangun": "Kokow slowly opens his sleepy eyes and stretches slightly.",
        "Kokow Kaget": "Kokow slowly opens his sleepy eyes and suddenly notices something off-screen, then gently turns his head.",
    },
    "Cecep": {
        "Cecep Bawel": "Cecep meows loudly with an excited funny expression and bounces slightly.",
        "Cecep Jalan": "Cecep walks a few steps energetically while looking curious.",
    },
    "Nian": {
        "Nian Tenang": "Nian sits neatly, blinks softly, and slowly turns her head with a calm elegant expression.",
    },
    "Ompel": {
        "Ompel Penasaran": "Ompel takes a few tiny clumsy steps, tilts his head, and looks around curiously.",
    },
    "Family": {
        "Family Duduk": "The family sits together peacefully with gentle blinking and subtle head movement.",
        "Family Ending": "The whole family rests together peacefully in a warm cozy room with subtle movement.",
    },
}

BASE_DESCRIPTIONS = {
    "Yoyin": "The exact same mother cat shown in the input image. Keep her tabby fur, facial appearance, body proportions, eyes, and red collar unchanged.",
    "Kokow": "The exact same orange cat shown in the input image. Keep his orange fur, sleepy face, body proportions, eyes, and collar unchanged.",
    "Cecep": "The exact same tabby cat shown in the input image. Keep his tabby fur pattern, facial appearance, body proportions, eyes, and collar unchanged.",
    "Nian": "The exact same female tabby cat shown in the input image. Keep her fur pattern, facial appearance, body proportions, eyes, and collar unchanged.",
    "Ompel": "The exact same tiny baby kitten shown in the input image. Keep his tiny body, fur pattern, face, eyes, and proportions unchanged.",
    "Family": "Use the exact same five cat characters shown in the input image. Keep every character's fur color, markings, face, proportions, and identity unchanged.",
}

STYLE_SUFFIX = "Natural subtle movement, warm indoor lighting, cute cinematic 3D animated family film style."

def get_characters():
    return list(SCENE_LIBRARY.keys())

def get_scenes(character):
    return list(SCENE_LIBRARY.get(character, {}).keys())

def build_prompt(character, scene_name):
    base = BASE_DESCRIPTIONS.get(character, "")
    scene = SCENE_LIBRARY.get(character, {}).get(scene_name, "")
    return f"{base} {scene} {STYLE_SUFFIX}".strip()
