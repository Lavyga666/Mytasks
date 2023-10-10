



numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
uniq_1 = numbers[0:4]
uniq_2 = numbers[5:21]
summ_uniq_1 = sum(uniq_1[::1])
summ_uniq_2 = sum(uniq_2[::1])
lengh = len(numbers)
numbers[4] = (summ_uniq_1 + summ_uniq_2) / lengh
print("Измененный список:", numbers)

