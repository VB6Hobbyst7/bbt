#!/usr/bin/env python3

# Copyright (C) 2017-2020 The btclib developers
#
# This file is part of btclib. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution.
#
# No part of btclib including this file, may be copied, modified, propagated,
# or distributed except according to the terms contained in the LICENSE file.

from hashlib import sha256

from btclib.curvemult import mult
from btclib.curves import secp256k1 as ec
from btclib.ssa import sign, verify

print("\n*** EC:")
print(ec)

q = 0x18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725
q = q % ec.n
print("\n*** Key Generation:")
print(f"prvkey: {hex(q).upper()}")

Q = mult(q, ec.G)[0]
print(f"PubKey: {hex(Q).upper()}")

print("\n*** Message to be signed")
orig_msg = "Paolo is afraid of ephemeral random numbers"
msg = sha256(orig_msg.encode()).digest()
print(msg.hex().upper())

print("\n*** Sign Message")
r, s = sign(msg, q)
print(f"    r: {hex(r).upper()}")
print(f"    s: {hex(s).upper()}")

print("*** Verify Signature")
print(verify(msg, Q, (r, s)))

print("\n*** Malleated Signature")
sm = ec.n - s
print(f"    r: {hex(r).upper()}")
print(f"   sm: {hex(sm).upper()}")

print("*** Verify Malleated Signature")
print(verify(msg, Q, (r, sm)))

print("\n*** Another message to sign")
orig_msg2 = "and Paolo is right to be afraid"
msg2 = sha256(orig_msg2.encode()).digest()
print(msg2.hex().upper())

print("\n*** Sign Message")
r2, s2 = sign(msg2, q)
print(f"   r2: {hex(r2).upper()}")
print(f"   s2: {hex(s2).upper()}")

print("*** Verify Signature")
print(verify(msg2, Q, (r2, s2)))
