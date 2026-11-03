ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num: int) -> str:
    if num == 0:
        return ALPHABET[0]
    out = []
    while num > 0:
        num, rem = divmod(num, 62)
        out.append(ALPHABET[rem])
    return "".join(reversed(out))

def decode(code: str) -> int:
    num = 0
    for ch in code:
        num = num * 62 + ALPHABET.index(ch)
    return num