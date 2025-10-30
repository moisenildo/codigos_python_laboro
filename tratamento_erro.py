

try:
   valor = int(input("Informe um valor númerico: "))
   print(f"O número digitado foi {valor}")
   
except Exception as erro:
    print(f"Coisa feia, tentando colocar texto em lugar de números. O erro foi : {erro}")        
