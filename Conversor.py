numero = 69

if (numero - 128) >= 0:
    bit1 = "1"
    numero = numero - 128
else:
    bit1 = "0"


if (numero - 64) >= 0:
    bit2 = "1"
    numero = numero - 64
else:
    bit2 = "0"


if (numero - 32) >= 0:
    bit3 = "1"
    numero = numero - 32
else:
    bit3 = "0"


if (numero - 16) >= 0:
    bit4 = "1"
    numero = numero - 16
else:
    bit4 = "0"


if (numero - 8) >= 0:
    bit5 = "1"
    numero = numero - 8
else:
    bit5 = "0"


if (numero - 4) >= 0:
    bit6 = "1"
    numero = numero - 4
else:
    bit6 = "0"


if (numero - 2) >= 0:
    bit7 = "1"
    numero = numero - 2
else:
    bit7 = "0"


if (numero - 1) >= 0:
    bit8 = "1"
    numero = numero - 1
else:
    bit8 = "0"

print(numero)
print(bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8)