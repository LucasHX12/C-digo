from typing import List, Tuple


def calcular_estatisticas(numbers: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numbers (List[float]): Lista de números para análise.

    Returns:
        Tuple[float, float, float, float]: Uma tupla contendo:
            - total: Soma de todos os números
            - media: Média aritmética
            - maior: Maior valor
            - menor: Menor valor

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numbers)
    media = total / len(numbers)
    maior = max(numbers)
    menor = min(numbers)

    return total, media, maior, menor


# Exemplo de uso
if __name__ == "__main__":
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(numbers)

    print(f"Total: {total}")
    print(f"Média: {media:.2f}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
