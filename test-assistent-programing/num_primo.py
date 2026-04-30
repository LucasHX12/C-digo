from typing import List, Tuple


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo usando verificações otimizadas.

    Um número primo é maior que 1 e divisível apenas por 1 e por ele mesmo.

    Args:
        numero (int): O número a ser verificado. Deve ser um inteiro não negativo.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se o input não for um inteiro.

    Exemplos:
        >>> eh_primo(2)
        True
        >>> eh_primo(4)
        False
    """
    if not isinstance(numero, int):
        raise TypeError("O número deve ser um inteiro.")

    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False

    # 2 é o único número primo par
    if numero == 2:
        return True

    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False

    # Verifica divisibilidade por números ímpares até a raiz quadrada
    limite = int(numero ** 0.5) + 1
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False

    return True


def executar_testes() -> None:
    """Executa testes automatizados da função eh_primo.
    
    Valida o funcionamento da função `eh_primo()` através de um conjunto
    abrangente de casos de teste, incluindo números primos, compostos e
    números especiais (0, 1, números negativos).
    
    Imprime o resultado de cada teste indicando se passou ou falhou,
    além de um resumo final informando o status geral dos testes.
    
    Returns:
        None
    
    Exemplo:
        >>> executar_testes()
        Executando testes da função eh_primo:
          2: PASSOU (esperado: True, obtido: True)
          ...
        Todos os testes passaram! ✅
    """
    # Casos de teste: (numero, esperado)
    casos_teste: List[Tuple[int, bool]] = [
        (2, True),   # Primo par
        (3, True),   # Primo ímpar
        (4, False),  # Composto par
        (5, True),   # Primo
        (10, False), # Composto
        (11, True),  # Primo
        (17, True),  # Primo
        (20, False), # Composto
        (23, True),  # Primo
        (29, True),  # Primo
        (1, False),  # Não primo
        (0, False),  # Não primo
        (-5, False), # Não primo
    ]

    print("Executando testes da função eh_primo:")
    todos_passaram = True

    for numero, esperado in casos_teste:
        try:
            resultado = eh_primo(numero)
            status = "PASSOU" if resultado == esperado else "FALHOU"
            print(f"  {numero}: {status} (esperado: {esperado}, obtido: {resultado})")
            if resultado != esperado:
                todos_passaram = False
        except Exception as e:
            print(f"  {numero}: ERRO - {e}")
            todos_passaram = False

    if todos_passaram:
        print("\nTodos os testes passaram! ✅")
    else:
        print("\nAlguns testes falharam. ❌")


def interacao_usuario() -> None:
    """Permite interação manual com o usuário para testar números primos.
    
    Implementa um loop interativo que solicita ao usuário a digitação de
    números inteiros e verifica se cada um é primo ou não. O loop continua
    até que o usuário digite 'sair'.
    
    O usuário receberá mensagens de erro caso digite valores inválidos
    (não-inteiros) e poderá encerrar a aplicação digitando 'sair'.
    
    Returns:
        None
    
    Exemplo:
        >>> interacao_usuario()
        Digite um número inteiro para verificar se é primo (ou 'sair' para encerrar): 7
        7 é primo? True
    """
    MENSAGEM_PROMPT = "Digite um número inteiro para verificar se é primo (ou 'sair' para encerrar): "
    MENSAGEM_ERRO = "Por favor, digite um número inteiro válido ou 'sair'."

    while True:
        entrada = input(MENSAGEM_PROMPT).strip().lower()

        if entrada == 'sair':
            print("Encerrando interação.")
            break

        try:
            numero = int(entrada)
            resultado = eh_primo(numero)
            print(f"{numero} é primo? {resultado}")
        except ValueError:
            print(MENSAGEM_ERRO)
        except TypeError as e:
            print(f"Erro: {e}")


# Ponto de entrada principal
if __name__ == "__main__":
    try:
        numero = int(input("Digite um número para verificar se é primo: "))
        resultado = eh_primo(numero)
        print(f"{numero} é primo? {resultado}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    except TypeError as e:
        print(f"Erro: {e}")
