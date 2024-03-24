def get_text():
    with open("../texts/text1.txt", "r") as file:
        text = " ".join(file.read().split())
        return text