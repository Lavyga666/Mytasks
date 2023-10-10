# TODO Найдите количество книг, которое можно разместить на дискете
size = 1.44
number_of_characters = 25
number_of_pages = 100
number_of_rows = 50

weight = 4 * number_of_rows * number_of_pages * number_of_characters
kbite = weight / 1024
mbite = kbite / 1024
number_of_book = int(size // mbite)

print("Количество книг, помещающихся на дискету:", number_of_book)
