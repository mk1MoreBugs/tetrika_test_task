def appearance(intervals: dict[str, list[int]]) -> int:
    pupil_time = clear_list(intervals["pupil"])
    tutor_time = clear_list(intervals["tutor"])
    lesson_time = clear_list(intervals["lesson"])
    return calculate_time(pupil_time, tutor_time, lesson_time)


def clear_list(input_list: list[int]) -> list[int]:
    if len(input_list) == 2:
        return input_list

    new_list = input_list.copy()
    index = 1
    while index < len(new_list) - 1:
        if new_list[index] >= new_list[index+1]:
            new_list.pop(index+1)
            if new_list[index+1] < new_list[index]:
                new_list.pop(index+1)
            else:
                new_list.pop(index)
        else:
            index += 2

    return new_list


def calculate_time(pupil_time: list[int], tutor_time: list[int], lesson_time: list[int]) -> int:
    accumulate = 0

    pupil_index = 0
    tutor_index = 0
    while pupil_index < len(pupil_time) and tutor_index < len(tutor_time):
        start_time = pupil_time[pupil_index]
        if pupil_time[pupil_index] < tutor_time[tutor_index]:
            start_time = tutor_time[tutor_index]
        if start_time < lesson_time[0]:
            start_time = lesson_time[0]

        end_time = pupil_time[pupil_index+1]
        if tutor_time[tutor_index+1] < pupil_time[pupil_index+1]:
            end_time = tutor_time[tutor_index+1]
        if lesson_time[-1] < end_time:
            end_time = lesson_time[-1]

        if tutor_time[tutor_index+1] < pupil_time[pupil_index+1]:
            tutor_index += 2
        else:
            pupil_index += 2

        if end_time - start_time < 0:
            continue

        accumulate += end_time - start_time

    return accumulate


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'