# codiging: utf-8

print("Saisissez les trios notes")
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
moy = (n_1 + n_2 + n_3)/3
print("la moyenne est: ", moy, "avec mention", end=" ")
if moy >= 16 :
    print("Très bien")
if moy <= 14 and moy < 16:
    print("Bien")
if moy <= 12 and moy < 14:
    print("Assez bien")
if moy <= 10 and moy < 12:
    print("Insuffisant")
