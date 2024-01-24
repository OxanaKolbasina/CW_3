import json

from models.operation import Operation


def load_operations(path: str):
    print(path)
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_operation_instances(operations):
    list_ = []
    for operation in operations:
        if operation:
            list_.append(
                Operation(
                    pk=operation["id"],
                    state=operation["state"],
                    date=operation["date"],
                    operation_amount=operation["operationAmount"],
                    description=operation["description"],
                    _from=operation.get("from",""),
                    _to=operation["to"],
                )
            )
    return list_


def get_executed_operations(operations):
    operation_list = []
    for operation in operations:
        if operation.state == "EXECUTED":
            operation_list.append(operation)
    return operation_list


def sort_operations(operations):
   operations = sorted(operations, key=lambda x: x.date,reverse=True)
   return operations
