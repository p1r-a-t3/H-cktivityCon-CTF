#!/usr/bin/env python

import base64
import binascii

h = binascii.hexlify
b = base64.b64encode

c = b'37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067'
print("input: {}".format(c))
def enc(f):
    # f is a byte
    b64_encode = base64.b64encode(f)
    z = []
    i = 0
    print("b64_encode", b64_encode)
    while i < len(b64_encode):
        x = [chr(ord(b64_encode[i]) ^ ord(b64_encode[((i + 1) % len(b64_encode))]))]
        # print(x)
        z += x
        i = i + 1
    print(z)
    c = h(bytearray(z))
    return c


# print(enc(b"helllllo world"))
print(enc(c))

