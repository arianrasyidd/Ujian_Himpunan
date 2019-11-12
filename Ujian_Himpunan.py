#----------------------------- Selasa, 12 November 2019 ------------------------------------------------

#SOAL 1

A = []
B = []

for ab in range(1, 21):
    if ab % 2 == 0:
        A.append(ab)
    else:
        B.append(ab)

A, B = set(A), set(B)

C = set(range(-1, -10, -1))
D = {2, 3, 5, 7, 11, 13, 17, 19}
E = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18}

# print(A, B, C, D, E)

a = A | B | C | D | E
b = (A & B) | (D & E)
c = (A | B) & (D | E)
d = (A | B) - (D | E)
e = (A | B | C) - (A & E)

print(a, b, c, d, e)

