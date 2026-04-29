from typing import Dict
import json

def format_text(total_produtos: Dict, total: float, top: str) -> str:
    linhas = ["\nRelatório de Vendas\n", "-" * 30]
    for produto, valor in total_produtos.items():
        linhas.append(f"{produto:20} R$ {valor:.2f}")
    linhas.append("-" * 30)
    linhas.append(f"TOTAL: R$ {total:.2f}")
    linhas.append(f"MAIS VENDIDO: {top}")
    return "\n".join(linhas)

def format_json(total_produtos: Dict, total: float, top: str) -> str:
    return json.dumps({
        "total_por_produto": total_produtos,
        "total_geral": total,
        "produto_mais_vendido": top
    }, indent=2, ensure_ascii=False)
