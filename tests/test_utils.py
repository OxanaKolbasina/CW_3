from src.utils import load_operations


def test_load_operations():
    path = "./test_operation.json"
    operations = load_operations(path)
    assert len(operations) == 5
    assert operations[0]["id"] == 441945886

    path = "sdfghhjjk,gfghjkkk"
    with pytest. raises(FileExistsError):
        test_load_operations(path)


def test_get_opertion_instances():
    test_operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
            "amount": "31957.58",
            "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
    }
        ]
    operation_instances = get_opertion_instances(test_operations)
    assert isinstance(operation_instances, list)
    assert isinstance(operation_instances[0], Operation)
    assert operation_instances[0].pk == 441945886

    test_operations =[]
    operation_instances = get_opertion_instances(test_operations)
    assert operation_instances == []

    test_operations = [{}]
    operation_instances = get_operation_instances(test_operations)
    assert operation_instances == []





