import string

def normalize(txt: str) -> str:
    txt = txt.lower().replace("-", " ")
    translator = str.maketrans("", "", string.punctuation)
    txt = txt.translate(translator)
    txt = " ".join(txt.split())
    return txt