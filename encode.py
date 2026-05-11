import random

msg = input("input text to encrypt: ")
msg_bytes = list(msg.encode())
print(f"original message bytes were {msg_bytes}")
counter = 1
keys = []

def randencode(msg_bytes, counter):
    keyN = random.randrange(1, 256, 2)
    keys.append(keyN)

    print(f"Key number {counter} is {keyN}")

    result = []

    for b in msg_bytes:
        r = (b * keyN) % 256
        result.append(r)

    print(f"Result {counter} is {result}\n")

    return result


results = []

for i in range(3):
    msg_bytes = randencode(msg_bytes, counter)
    results.append(msg_bytes)
    counter += 1


result = []

msg_bytes_original = list(msg.encode())

for i in range(3):
    msg_bytes = randencode(msg_bytes_original, counter)
mixed = [results[i] + results[(i + 1) % len(results)] for i in range(len(results))]

print("mixed:", mixed)

print("final results list:")
print(results)
print(keys)