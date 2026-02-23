def select_background():
    options = ["sea", "studio"]
    print("เลือกฉาก:")
    for i, o in enumerate(options):
        print(f"{i+1}. {o}")
    return options[int(input("> ")) - 1]

def select_outfit():
    options = ["casual", "suit"]
    print("เลือกชุด:")
    for i, o in enumerate(options):
        print(f"{i+1}. {o}")
    return options[int(input("> ")) - 1]