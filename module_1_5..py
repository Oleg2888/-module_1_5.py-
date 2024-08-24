
immutable_var = (1, 2, 'a', 'b')

print("Immutable tuple:", immutable_var)

try: immutable_var[0] = 10
except TypeError as e:
    print("Error:", e)
    print("Кортеж является неизменяемым объектом, поэтому его элементы нельзя изменять.")

mutable_list = [1, 2, 'a', 'b']  # Список из разных типов данных

mutable_list[0] = 10
mutable_list.append('Modified')
print("Mutable list:", mutable_list)