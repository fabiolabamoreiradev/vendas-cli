from typing import List, Dict
from datetime import datetime

def filter_by_date(data: List[Dict], start: str | None, end: str | None) -> List[Dict]:
    def in_range(row):
        date = datetime.fromisoformat(row["data"])
        if start and date < datetime.fromisoformat(start):
            return False
        if end and date > datetime.fromisoformat(end):
            return False
        return True
    return [row for row in data if in_range(row)]

def total_por_produto(data: List[Dict]) -> Dict[str, float]:
    result = {}
    for row in data:
        produto = row["produto"]
        valor = float(row["valor"])
        result[produto] = result.get(produto, 0) + valor
    return result

def total_vendas(data: List[Dict]) -> float:
    return sum(float(row["valor"]) for row in data)

def produto_mais_vendido(data: List[Dict]) -> str:
    counts = {}
    for row in data:
        produto = row["produto"]
        counts[produto] = counts.get(produto, 0) + 1
    return max(counts, key=counts.get) if counts else ""
