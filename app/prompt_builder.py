# app/prompt_builder.py

def build_prompt(background, outfit):
    return f"""
    ultra realistic photo of the same person,
    wearing {outfit},
    standing in a {background} environment,
    photobooth style,
    studio lighting
    """.strip()