# Só existem duas estrutura de repetição em python( para e )

"""
for (etapa1; etapa2; etapa3){
     
}
"""
# EXEMPLO 01
# range() não conta o valor final, ele ignora. Se eu quiser exibir o valor final devo colocar ele + 1

for contador in range(1,10):
    print(contador, end=" ")

print("\n")    
print("*" * 60)   
# EXEMPLO 02

# o -1 indica que o intervalo irá de -1 em -1, isto é o passo a passo do valor inocial até o valor final

for contador in range(10, 0, -1):
    print(contador, end=" ")   
    
    
# EXEMPLO 03   

for contador in range(0,21, 2):
    print(contador, end=". ") 
    