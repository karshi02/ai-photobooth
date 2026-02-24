# from app.prompt_builder import build_prompt

# def build_prompt(background: str, outfit: str) -> str:
#     background_map = {
#         "sea": "beautiful tropical beach, blue sky, ocean",
#         "studio": "professional photo studio, clean background"
#     }

#     outfit_map = {
#         "casual": "casual outfit, modern style",
#         "suit": "formal suit, elegant, business style"
#     }

#     bg_desc = background_map.get(background, background)
#     outfit_desc = outfit_map.get(outfit, outfit)

#     prompt = f"""
#     ultra realistic photo of the same person,
#     wearing {outfit_desc},
#     standing in {bg_desc},
#     photobooth style,
#     studio lighting,
#     high detail,
#     sharp focus
#     """

#     return prompt.strip()
def generate_image(prompt):
    """Generate an image for the given prompt.

    This function writes a simple placeholder PNG to `output/output.png` so
    that callers receive a real file on disk. Replace this implementation
    with real model/API calls when available.
    """
    import os
    import base64

    print("Generating image with prompt:")
    print(prompt)

    out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "output.png")

    # 1x1 PNG (white) encoded in base64 — valid image file without external libs
    png_b64 = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMA"
        "ASsJTYQAAAAASUVORK5CYII="
    )

    with open(out_path, "wb") as f:
        f.write(base64.b64decode(png_b64))

    print("Saved:", out_path)
    return out_path