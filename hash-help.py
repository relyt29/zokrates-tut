import hashlib

preimage = bytes.fromhex('00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00\
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 10 32 f0 0a 02')

print("input: " + preimage.hex())
print("input: " + str(int(preimage.hex(),16)))

#bin(int(preimage.hex(), 16)) //binary representation of pre-image
diggory = hashlib.sha256(preimage).hexdigest()

print("hash hex:   " + diggory[0:32])
print("hash hex 2: " + diggory[32:])
print("hash decimal:   " + str(int("0x" + str(diggory[0:32]), 16)))
print("hash decimal 2: " + str(int("0x" + str(diggory[32:]), 16)))
