from vendas.output import format_text, format_json

def test_format_text():
    result = format_text({"A": 30}, 30, "A")
    assert "TOTAL" in result
    assert "A" in result


def test_format_json():
    result = format_json({"A": 30}, 30, "A")
    assert '"total_geral": 30' in result