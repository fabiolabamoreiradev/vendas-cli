import argparse
import logging

from vendas.parser import parse_csv
from vendas.core import filter_by_date, total_por_produto, total_vendas, produto_mais_vendido
from vendas.output import format_text, format_json

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--start")
    parser.add_argument("--end")

    args = parser.parse_args()

    data = parse_csv(args.file)
    data = filter_by_date(data, args.start, args.end)

    total_produtos = total_por_produto(data)
    total = total_vendas(data)
    top = produto_mais_vendido(data)

    if args.format == "json":
        print(format_json(total_produtos, total, top))
    else:
        print(format_text(total_produtos, total, top))

if __name__ == "__main__":
    main()
