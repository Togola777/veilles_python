# codiging: utf-8

print("Entrez deux entier puis + pour leur addition, - pour leur soustaction; * pour leur multiplication et / pour leur division:")
a = int(input())
b = int(input())
op = input()
if op == "+":
    print("La somme est: ", a+b)
if op == "-":
    print("La différence est: ", a-b)
if op == "*":
    print("Le produit est: ", a*b)
if op == "/":
    print("Le quotient est: ", a/b)
