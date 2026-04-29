from typing import List, Dict
import csv
import logging

logger = logging.getLogger(__name__)

def parse_csv(path: str) -> List[Dict]:
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        logger.error(f"Arquivo não encontrado: {path}")
        raise
