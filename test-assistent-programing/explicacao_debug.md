# Explicação do Debug

## 1. Identificação dos erros
- `item1 = float(input(Preço do item 1? ))` estava sem aspas no prompt de `input`, gerando `SyntaxError`.
- `desconto_cupom` era lido como string e, depois, utilizado em cálculo numérico com `/` e comparação `> 0`, o que geraria `TypeError`.
- A linha `print(" Item 2:        R$ {total_item2:.2f}")` estava usando aspas normais em vez de `f-string`, então o valor não era interpolado.
- O bloco `if desconto_cupom > 0:` não tinha indentação no `print` interno, causando `IndentationError`.

## 2. Causa dos erros
- O prompt de `input` precisa estar entre aspas para ser uma string válida.
- O valor retornado por `input()` é sempre texto; para operá-lo como número, é preciso convertê-lo para `int` ou `float`.
- Strings comuns não interpretam expressões como `{total_item2:.2f}`; apenas `f-string` faz a interpolação.
- Em Python, o corpo de uma estrutura de controle precisa estar indentado em relação à linha `if`.

## 3. Correção aplicada
- Corrigido o prompt de `input` para `item1` com aspas: `float(input("Preço do item 1? "))`.
- Convertido `desconto_cupom` para float: `desconto_cupom = float(input(...))`.
- Ajustado `print` de `Item 2` para usar `f-string`:
  - `print(f" Item 2:        R$ {total_item2:.2f}")`
- Corrigida a indentação do bloco `if desconto_cupom > 0:`:
  - `if desconto_cupom > 0:`
  - `    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`
- Também simplificado o cálculo final para exibir `total` diretamente com formatação numérica.

## 4. Resultado final
- O código agora aceita corretamente os valores de preço e desconto.
- O desconto é calculado apenas quando há percentual maior que zero.
- A fatura é exibida com formatação adequada e sem erros de sintaxe ou tipo.
