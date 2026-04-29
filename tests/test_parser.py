from vendas.parser import parse_csv
import tempfile
import pytest


def test_parse_csv_valido():
    content = "produto,quantidade,preco_unitario,data_venda\nA,2,10,2026-01-01\n"

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(content)
        f.flush()

        data = parse_csv(f.name)
        assert len(data) == 1
        assert data[0]["produto"] == "A"


def test_csv_vazio(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text("")

    with pytest.raises(ValueError):
        parse_csv(file)


def test_arquivo_inexistente():
    import pytest
    with pytest.raises(FileNotFoundError):
        parse_csv("arquivo_que_nao_existe.csv")