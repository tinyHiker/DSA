import math


# Generate public key (e, n) using two large prime numbers p and q
def rsa_generate_Kpub(p, q):
    n = p * q
    print("n =", n)
    phi = (p - 1) * (q - 1)
    e = 2
    while (e < phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e += 1
    print("e =", e)
    return e


# Generate private key using public key (e, n)
def rsa_generate_Kpriv(e, p, q):
  phi = (p - 1) * (q - 1)

  l = []
  tmp = 1
  while len(l) <= 5:
    if (tmp * e) % phi == 1:
      l.append(tmp)
    tmp += 1

  print("5 possible d values: ", l)
  return l


# Encrypt message m using public key (e, n)
def rsa_encrypt(m, e, n):
  C = []
  for i in m:
    C.append((i**e) % n)
  print('Encrypted message: ', C)
  return C


# Decrypt ciphertext C using private key d, and n
def rsa_decrypt(c, d, n):
  M = []
  for j in c:
    M.append((j**d) % n)
  print('Decrypted message: ', M)
  return M


# Example (GIVEN)
p = 113
q = 1013
n = p * q  # n = pq -> ALWAYS

e = 31  # public key (GIVEN)
d = rsa_generate_Kpriv(e, p, q)  # private key (outputs a list)

msg = [152015, 150804, 180017, 41812, 1111]  #write each block of message
print('original message: ', msg)

# Get ciphertext C
C = rsa_encrypt(msg, e, n)

# Get decrypted message M
M = rsa_decrypt(C, d[0], n)

print(d)


