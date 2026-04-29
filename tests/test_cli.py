import sys
from vendas.cli import main
import tempfile

def test_cli_text_output(monkeypatch, capsys):
    content = "produto,quantidade,preco_unitario,data_venda\nA,2,10,2026-01-01\n"

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(content)
        f.flush()

        monkeypatch.setattr(sys, "argv", ["prog", f.name])

        main()

        captured = capsys.readouterr()
        assert "TOTAL" in captured.out


def test_cli_json_output(monkeypatch, capsys):
    content = "produto,quantidade,preco_unitario,data_venda\nA,2,10,2026-01-01\n"

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(content)
        f.flush()

        monkeypatch.setattr(sys, "argv", ["prog", f.name, "--format", "json"])

        main()

        captured = capsys.readouterr()
        assert "total_geral" in captured.out