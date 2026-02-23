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
    print("Generating image with prompt:")
    print(prompt)
    return "output.png"