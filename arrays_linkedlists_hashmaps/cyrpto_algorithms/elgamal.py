# Generates public key y
# p - large prime number
# g - integer, where 1 < g < p
# Kpriv - randomly chosen, where 1 < Kpriv < p-1
def elgamal_getpubkey(p, g, Kpriv):  #get y
  y = (g**Kpriv) % p
  print("p =", p)
  print("g =", g)
  print("y =", y)
  return y


# Encrypts message M to produce ciphertext C = (C1, C2)
# Note: k is a random number, where 1 < k < p-1
def elgamal_encrypt(M, k, p, g, y):
  C1 = (g**k) % p
  C2 = (M * (y**k)) % p
  print(f'encrypted message: (C1, C2) = ({C1}, {C2})')
  return C1, C2


# Decrypts ciphertext C = (C1, C2) to produce message M
def elgamal_decrypt(C1, C2, Kpriv, p):
  X = (C1**Kpriv) % p
  M = (C2 * (X**(p - 2))) % p

  print("decrypted message: ", M)
  return M


#####RUNNER###################################
#####################################
p = 262681
g = 1063
Kpriv = 1039
y = elgamal_getpubkey(p, g, Kpriv)  # get public key

k = 29
M = 12404 # This represents 3 letters so its supposed to be 6 digits, with 2 digits representing each letter. 
# It's just that the leading digit, in this case, was a zero
# so it was ommitted

Cs = elgamal_encrypt(M, k, p, g, y)
C1 = Cs[0]
C2 = Cs[1]

M = elgamal_decrypt(C1, C2, Kpriv, p)

converted_str = ""
val = M
while True:
  charCode = val % 100
  converted_str = chr(ord('A') + charCode) + converted_str
  val = val // 100
  if (val == 0):
    break
print(converted_str)




n = 9
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
            