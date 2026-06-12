try:
    def divisao(a, b):
        print(a / b)
        return a / b

    divisao(10, )
except ZeroDivisionError:
    print(f"Ocorreu um erro: divisão por zero")
except Exception as e:
    print(f"ocorreu um erro: {e}")
else:
    print("Calculo feito com sucesso!")
    opiniao = input("Deixe sua opinião sobre o codigo")
    print("Sua opinião é: ", opiniao)

finally:
    print("Fim do calculo")
