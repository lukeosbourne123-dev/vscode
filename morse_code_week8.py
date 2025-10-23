morsecode = {'A':'.-', 'B': '-...', 'C':'-.-.', 'D':'=..', 'E':'.',
             'F':'..=.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
             'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O': '---', 'P':'.--.',
             'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
             'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', " ":" ", ',':',' }

text = "Hello, how are you?"
for ch in text:
    if(morsecode.get(ch.upper())==None):
        print(morsecode[' '], end=" ")
    else:
        print(morsecode[ch.upper()], sep=" ", end=" ")
