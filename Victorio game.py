def prem(i) :
    count = 0
    for j in range(1, i + 1) :
        if i % j == 0 : count +=1
    if count == 2 : return 1
    else : return 0


print("\nHello World")
limite = 0
i = 0
while i == 0: 
    limite = input("\nEntrez la limite : ")
    if limite.isdigit() == 0 : print("\nVeuillez entrer un entier.")
    else : i = 1

limite = int(limite)
for i in range(limite) : 
    if prem(i) == 1 : print(f"\n{i} est premier.")

