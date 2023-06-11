def binary_search(array, element, left, right):
    if right <= 0:
        return False  # значит элемент отсутствует
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] < element <= array[middle+1] :  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


strnums = str(input())
anynum = int(input())
nums = [int(x) for x in strnums.split(" ")]

qsort(nums, 0, len(nums) - 1)

res = binary_search(nums, anynum, 0, len(nums) - 1)
if res is False:
    print("Не найдено")
else:
    print("Позиция:", res)

