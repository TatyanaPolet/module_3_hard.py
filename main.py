
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((),
    [{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum (ds):
    pirog = []
    for i in ds:
        if isinstance(i, int):
            pirog.append(i)
        elif isinstance(i, str):
            pirog.append(len(i))
        elif isinstance(i, dict):
            if len(i) > 0:
                pirog.append(calculate_structure_sum(list(i.keys())))
                pirog.append(calculate_structure_sum(list(i.values())))
        else:
            if len(i) > 0:
                pirog.append(calculate_structure_sum(i))
    else:
        return sum(pirog)

result = calculate_structure_sum(data_structure)
print(result)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
