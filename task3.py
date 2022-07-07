def appearance(intervals):
    # чтобы было три участника, урок, ученик и учитель
    # запишем в общий список кортежи в виде (время, участник, вход или выход)
    time_list = []
    for i in range(len(intervals['lesson'])):
        time_list.append((intervals['lesson'][i], 'L', 1 - 2*(i % 2)))
    for i in range(len(intervals['pupil'])):
        time_list.append((intervals['pupil'][i], 'P', 1 - 2*(i % 2)))
    for i in range(len(intervals['tutor'])):
        time_list.append((intervals['tutor'][i], 'T', 1 - 2*(i % 2)))
    time_list.sort(key=lambda x: x[0])

    total = 0
    # есть небольшая загвоздка: ученик открывает несколько окон, и интервалы начинают заканчиваться один в другом
    # поэтому всех трех участников отслеживаем отдельно
    L = 0
    P = 0
    T = 0
    sub_interval_started = False
    start = 0
    for i in time_list:
        if i[1] == 'L':
            L += i[2]
        if i[1] == 'P':
            P += i[2]
        if i[1] == 'T':
            T += i[2]
        # если наступают условия "посещения" и мы еще не начали отслеживать время - начинаем
        if (L > 0) and (P > 0) and (T > 0) and not sub_interval_started:
            sub_interval_started = True
            start = i[0]
        # если мы отслеживали время, и условия посещения пропадают - записываем время в итог
        # урок у нас закончится в любом случае, поэтому проверять крайние случаи нет смысла
        if not ((L > 0) and (P > 0) and (T > 0)) and sub_interval_started:
            sub_interval_started = False
            total += i[0] - start

    return total


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

