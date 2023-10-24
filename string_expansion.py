def string_expansion(text):
    n = 1
    text_new = ""
    i = 0
    
    while i < len(text):
        if text[i].isnumeric():
            n = int(text[i])
            i += 1
        elif text[i].isalpha():
            text_new += n * text[i]
            i += 1
        else:
            return "Entrada inválida"  # Se encontrar caracteres não numéricos nem alfabéticos

    return text_new

text = input()
text_new = string_expansion(text)
print(f"{text} = {text_new}")
