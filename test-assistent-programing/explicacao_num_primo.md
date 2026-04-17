Aqui está uma explicação linha a linha do código Python refatorado presente no arquivo `num_primo.py`. Aplicamos técnicas de clean code, como type hints, separação de responsabilidades, constantes, validação de entrada e testes estruturados. Vou explicar de forma técnica e didática.

### 1. Importações
```python
from typing import List, Tuple
```
- **Explicação Técnica**: Importa tipos genéricos do módulo `typing` para type hints. `List` e `Tuple` permitem anotar tipos de coleções, melhorando a legibilidade e detecção de erros em IDEs.
- **Explicação Didática**: É como declarar "essa variável é uma lista de tuplas". Ajuda o Python a entender melhor o código e evita bugs.

### 2. Definição da Função com Type Hints
```python
def eh_primo(numero: int) -> bool:
```
- **Explicação Técnica**: Define a função com type hints: `numero: int` indica que o parâmetro deve ser inteiro, `-> bool` que retorna booleano. Em Python moderno, isso é clean code para clareza e verificação estática.
- **Explicação Didática**: Agora é explícito: a função recebe um int e devolve True/False. Facilita manutenção e evita confusões.

### 3. Docstring Melhorada
```python
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
```
- **Explicação Técnica**: Docstring expandida com descrição detalhada, exemplos de uso (doctests) e exceções. Segue convenções como Google style. Doctests podem ser executados com `doctest`.
- **Explicação Didática**: É um "contrato" da função: o que faz, o que espera, o que retorna e possíveis erros. Exemplos mostram como usar.

### 4. Validação de Tipo
```python
if not isinstance(numero, int):
    raise TypeError("O número deve ser um inteiro.")
```
- **Explicação Técnica**: `isinstance()` verifica o tipo em runtime. Levanta `TypeError` se não for int, seguindo princípio de fail-fast.
- **Explicação Didática**: Garante que só inteiros sejam processados. Se passar uma string, erro imediato em vez de comportamento estranho.

### 5. Verificações Iniciais (≤ 1, 2, Pares)
```python
# Números menores ou iguais a 1 não são primos
if numero <= 1:
    return False

# 2 é o único número primo par
if numero == 2:
    return True

# Números pares maiores que 2 não são primos
if numero % 2 == 0:
    return False
```
- **Explicação Técnica**: Mesmas otimizações, mas agora com validação prévia. Evita loops desnecessários.
- **Explicação Didática**: Filtros rápidos: negativos/0/1 → False; 2 → True; pares >2 → False. Reduz trabalho.

### 6. Loop Otimizado
```python
# Verifica divisibilidade por números ímpares até a raiz quadrada
limite = int(numero ** 0.5) + 1
for divisor in range(3, limite, 2):
    if numero % divisor == 0:
        return False
```
- **Explicação Técnica**: `limite` armazena o cálculo da raiz para clareza. `divisor` nome mais descritivo que `i`. Mesmo algoritmo O(√n).
- **Explicação Didática**: Testa apenas ímpares até √numero. Variável `limite` torna o código mais legível.

### 7. Retorno Final
```python
return True
```
- **Explicação Técnica**: Se passou por tudo, é primo.
- **Explicação Didática**: Sem mudanças.

### 8. Função de Testes Estruturados
```python
def executar_testes() -> None:
    """Executa testes automatizados da função eh_primo."""
    # Casos de teste: (numero, esperado)
    casos_teste: List[Tuple[int, bool]] = [
        (2, True), (3, True), (4, False), ...
    ]
```
- **Explicação Técnica**: Função separada para testes, seguindo SRP (Single Responsibility Principle). Usa lista de tuplas para casos esperados. Type hints em tudo.
- **Explicação Didática**: Testes organizados: cada tupla é "número + resultado esperado". Fácil adicionar mais casos.

### 9. Loop de Testes com Validação
```python
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
```
- **Explicação Técnica**: Itera sobre casos, compara resultado com esperado. Trata exceções. Usa f-strings para formatação.
- **Explicação Didática**: Para cada teste, diz se passou ou falhou. Mostra detalhes para debug.

### 10. Função de Interação com Usuário
```python
def interacao_usuario() -> None:
    """Permite interação manual com o usuário para testar números."""
    MENSAGEM_PROMPT = "Digite um número inteiro para verificar se é primo (ou 'sair' para encerrar): "
    MENSAGEM_ERRO = "Por favor, digite um número inteiro válido ou 'sair'."
```
- **Explicação Técnica**: Função separada para input do usuário. Constantes para mensagens (DRY principle). Loop while para múltiplas entradas.
- **Explicação Didática**: Separa lógica de testes da interação. Constantes evitam repetir strings.

### 11. Tratamento de Entrada
```python
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
```
- **Explicação Técnica**: `strip().lower()` normaliza entrada. `try/except` para ValueError (não int) e TypeError (da função). Loop infinito até 'sair'.
- **Explicação Didática**: Trata entradas ruins graciosamente. Permite sair digitando 'sair'.

### 12. Ponto de Entrada Principal (Ajustado)
```python
if __name__ == "__main__":
    try:
        numero = int(input("Digite um número para verificar se é primo: "))
        resultado = eh_primo(numero)
        print(f"{numero} é primo? {resultado}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    except TypeError as e:
        print(f"Erro: {e}")
```
- **Explicação Técnica**: Quando executado diretamente, solicita um número ao usuário via `input()`, converte para int, chama `eh_primo()` e imprime o resultado. Trata erros de conversão e tipo.
- **Explicação Didática**: O programa pede um número, verifica se é primo e mostra o resultado. Simples e direto para o usuário final.

### Resumo Geral
- **Clean Code Aplicado**: Type hints, funções pequenas, constantes, validação, testes estruturados, SRP.
- **Eficiência**: Mantida O(√n).
- **Melhorias**: Código mais robusto, legível e testável. Doctests na docstring permitem verificação automática.
- **Uso**: Execute `python num_primo.py` e digite um número para verificar se é primo.

Para executar testes automatizados, chame `executar_testes()` manualmente ou ajuste o main se necessário!
