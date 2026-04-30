## Mudanças feitas na refatoração

### 1. Extração de lógica em função reutilizável
- O cálculo das estatísticas foi movido para a função `calcular_estatisticas(numbers: List[float])`.
- Isso torna o código reutilizável em outros módulos e facilita testes.

### 2. Tipagem explícita
- Foram adicionados tipos:
  - `List[float]` para o parâmetro `numbers`
  - `Tuple[float, float, float, float]` para o retorno
- Isso melhora a legibilidade e ajuda ferramentas de análise estática a detectar erros.

### 3. Documentação clara com docstring
- Incluiu-se uma docstring explicando:
  - o que a função faz
  - o parâmetro esperado
  - o valor retornado
  - a exceção lançada
- Isso facilita o entendimento do código sem precisar ler a implementação.

### 4. Validação de entrada
- Agora o código verifica se a lista está vazia:
  - `if not numbers: raise ValueError("A lista não pode estar vazia.")`
- Essa proteção evita divisão por zero e resultados inválidos.

### 5. Uso de funções built-in para cálculo
- A refatoração usa:
  - `sum(numbers)` para soma
  - `len(numbers)` para quantidade
  - `max(numbers)` para maior valor
  - `min(numbers)` para menor valor
- Isso simplifica o código e evita loops manuais.

### 6. Separação de exemplo de uso
- O exemplo de execução foi colocado dentro de:
  - `if __name__ == "__main__":`
- Assim, quando o arquivo for importado como módulo, não executa o bloco de demonstração automaticamente.

### 7. Formatação de saída
- A saída do valor médio é exibida com duas casas decimais:
  - `print(f"Média: {media:.2f}")`
- Isso melhora a apresentação do resultado.

---

## Resultado do código refatorado
- Código mais organizado
- Função isolada e reutilizável
- Melhor documentação
- Comportamento seguro para lista vazia
- Uso idiomático de Python
- Separação clara entre lógica e demonstração de uso
