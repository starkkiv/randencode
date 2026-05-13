def mod_inverse(a, mod=256):
    for x in range(mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"no inverse for {a}")


def decrypt_layer(data, key):
    inv = mod_inverse(key)
    return [(b * inv) % 256 for b in data]


print("=== INTERACTIVE DECODER ===")
print("enter ciphertext bytes separated by spaces")
print("example: 145 242 83\n")

cipher = list(map(int, input("Ciphertext: ").split()))

steps = int(input("How many keys? "))

for i in range(steps):
    key = int(input(f"Key {i + 1}: "))
    cipher = decrypt_layer(cipher, key)
    print(f"After key {i + 1}: {cipher}")

print("\nFINAL RESULT:")
print("bytes:", cipher)

try:
    print("text:", bytes(cipher).decode())
except:
    print("text: <decode failed>")
