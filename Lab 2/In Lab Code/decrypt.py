code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''

for ch in code:
    if ch.islower():
        base = ord('a')
    elif ch.isupper():
        base = ord('A')
    else:
        plainText += ch
        continue

    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < base:
        cipherValue = base + (ordValue - base - distance) % 26
    plainText += chr(cipherValue)

print(plainText)

