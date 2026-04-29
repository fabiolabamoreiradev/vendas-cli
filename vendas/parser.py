from typing import List, Dict
import csv
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

REQUIRED_FIELDS = {"produto", "quantidade", "preco_unitario", "data_venda"}

def parse_csv(path: str) -> List[Dict]:
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)

            if not data:
                raise ValueError("CSV vazio")

            # ✅ 1. valida header
            header = set(data[0].keys())
            if not REQUIRED_FIELDS.issubset(header):
                raise ValueError(
                    f"CSV inválido. Esperado: {REQUIRED_FIELDS}, encontrado: {header}"
                )

            # ✅ 2. valida conteúdo (AQUI 👇)
            for i, row in enumerate(data, start=1):
                try:
                    float(row["preco_unitario"])
                    int(row["quantidade"])
                    datetime.fromisoformat(row["data_venda"])
                except ValueError:
                    raise ValueError(f"Erro na linha {i}: dados inválidos")

            return data

    except FileNotFoundError:
        logger.error(f"Arquivo não encontrado: {path}")
        raise