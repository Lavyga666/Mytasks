# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group,participants_second_group, a="|"):

    group1 = participants_first_group.split(a)
    group2 = participants_second_group.split(a)

    gr1 = set(group1)
    gr2 = set(group2)
    common = gr1.intersection(gr2)
    common = sorted(list(common))
    print(common)
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
find_common_participants(participants_first_group,participants_second_group)


