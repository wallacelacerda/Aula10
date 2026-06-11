try:
   def soma(a, b):
       print(a, b)
       return a + b
 
   soma(input("Digite o primeiro numero:"), 2)
except:
    print("ERRO!")
else:
    print("Calculo feito com sucesso!")

finally:
    print("Fim do calculo")           