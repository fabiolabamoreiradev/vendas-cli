from vendas.core import total_vendas, produto_mais_vendido, total_por_produto, filter_by_date

def test_total_vendas():
    data = [
        {"produto": "A", "quantidade": "2", "preco_unitario": "10", "data_venda": "2026-01-01"},
        {"produto": "B", "quantidade": "1", "preco_unitario": "20", "data_venda": "2026-03-01"},
    ]
    assert total_vendas(data) == 40


def test_produto_mais_vendido():
    data = [
        {"produto": "A", "quantidade": "2"},
        {"produto": "B", "quantidade": "1"},
    ]
    assert produto_mais_vendido(data) == "A"


def test_total_por_produto():
    data = [
        {"produto": "A", "quantidade": "2", "preco_unitario": "10"},
        {"produto": "A", "quantidade": "1", "preco_unitario": "10"},
    ]
    result = total_por_produto(data)
    assert result["A"] == 30



def test_filter_by_date_sem_data():
    data = [{"produto": "A"}]
    result = filter_by_date(data, None, None)
    assert len(result) == 1


def test_filter_by_date_com_data():
    data = [
        {"produto": "A", "data_venda": "2025-01-01"},
        {"produto": "B", "data_venda": "2025-03-01"},
    ]

    result = filter_by_date(data, "2025-02-01", "2025-12-01")

    assert len(result) == 1
    assert result[0]["produto"] == "B"

def test_filter_by_date():
    data = [
        {"produto": "A", "data_venda": "2025-01-01"},
        {"produto": "B", "data_venda": "2025-03-01"},
    ]

    result = filter_by_date(data, "2025-02-01", "2025-12-01")

    assert len(result) == 1
    assert result[0]["produto"] == "B"