def task(array):
    # из предлагаемого примера видно, что массив представляет из себя строку из единиц и нулей
    # нам нужен первый ноль
    # встроенный метод, возвращающий индекс первого вхождения элемента
    return array.index('0')


print(task("111111111110000000000000000"))
