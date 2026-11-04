"""SHA-256 theory (often mistyped as SHA-258).

SHA-256 is a cryptographic hash function in the SHA-2 family. It accepts data
of any length and produces a fixed 256-bit (32-byte) digest, commonly
represented as 64 hexadecimal characters. The same input always yields the
same digest; even a tiny input change typically changes the digest greatly.

The algorithm pads the input and processes it in 512-bit blocks. Each block
updates an internal 256-bit state through 64 rounds of bitwise operations,
rotations, and modular addition. SHA-256 is designed to be one-way and to make
finding two distinct inputs with the same digest computationally infeasible.

Uses include checking data integrity and supporting digital signatures.
Hashing is not encryption: a hash cannot be decrypted. Do not store passwords
as plain SHA-256 hashes; use a password-hashing algorithm such as Argon2,
scrypt, or bcrypt with a unique salt.

Example with Python's standard library:

	import hashlib
	digest = hashlib.sha256(b"hello").hexdigest()
"""

'''import hashlib

def compute_sha256(data: bytes) -> str:
	return hashlib.sha256(data).hexdigest()

print(compute_sha256(b"hello"))
print(compute_sha256(b"hello"))
print(compute_sha256(b"hello world"))'''

"""import hashlib
def compute_sha256(data: bytes) ->str:
    return hashlib.sha256(data).hexdigest()

print(compute_sha256(b"hello"))
print(compute_sha256(b"hello"))
print(compute_sha256(b"hello world"))

"""
