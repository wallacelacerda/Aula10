try:
   def soma(a, b):
       print(a, b)
       return a + b
 
   soma(input("Digite o primeiro numero:"), 2)
except:
    print("ERRO!")
else:
    print("Calculo feito com sucesso!")
    opiniao = input("Deixe sua opinião sobre codigo")
    print("Sua opinião é: ", opiniao)
finally:
    print("Fim do calculo")           