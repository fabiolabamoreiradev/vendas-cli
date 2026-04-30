from typing import List, Dict
from datetime import datetime

def filter_by_date(data, start, end):
    if not start and not end:
        return data

    def in_range(row):
        date = datetime.fromisoformat(row["data_venda"])

        if start and date < datetime.fromisoformat(start):
            return False
        if end and date > datetime.fromisoformat(end):
            return False
        return True

    return [row for row in data if in_range(row)]


def total_por_produto(data):
    result = {}
    for row in data:
        produto = row["produto"]
        valor = float(row["quantidade"]) * float(row["preco_unitario"])
        result[produto] = result.get(produto, 0) + valor
    return result

def total_vendas(data):
    return sum(
        float(row["quantidade"]) * float(row["preco_unitario"])
        for row in data
    )

def produto_mais_vendido(data):
    counts = {}
    for row in data:
        produto = row["produto"]
        quantidade = int(row["quantidade"])
        counts[produto] = counts.get(produto, 0) + quantidade

    if not counts:
        return ""

    max_value = max(counts.values())

    # retorna todos que têm o valor máximo
    result = [k for k, v in counts.items() if v == max_value]

    return result
    # return max(counts, key=counts.get) if counts else ""
