values_list = ['Apple', 23, [9, 4, False]]
values_dict = {'a': 111011, 'b': 'Ведьмак', 'c': [3.4, 5, 6]}
values_list_2 = [54.32, 'Строка']

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('--------1---------')
print_params()
print_params(b = 25)
print_params(c = [4, 2, 3])
print_params(a = 2,  b = 'Яблоко', c = False)
print('--------2---------')
print_params(*values_list)
print_params(**values_dict)
print('--------3---------')
print_params(*values_list_2, 42)