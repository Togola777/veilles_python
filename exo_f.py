# codiging: utf-8

print("Entrez un nombree et je vous founis son factoriel: ", end=" ")
n = int(input())
c = n
for i in range(1, n):
    n *= i
print("Le factoriel de ", c, "est: ", n)