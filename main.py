from utils import load_operations, get_operation_instances, get_executed_operations



def main():
    operations = load_operations("./src/data/operations.json")
    get_operation_instances(operations)
    executed_operations = get_executed_operations(operations_instances)
    sorted_operations = sort_operations(executed_operations)
    five_operations = sorted_operations[:5]
    for operation in five_operations:
        print(operation)






if __name__ == "__main__":
    main()



