# 2 final solution
subj1_all_students = {'A': {'Eden': 65, 'Omri': 53, "Yael": 66, "Shaked": 77, 'Yafit': 87, 'Rotem': 67},
                      'B': {'Eden': 98, 'Omri': 99, "Yael": 100, "Haim": 55, "Shaked": 77, 'Peleg': 77}}
subj2_all_students = {'A': {'Eden': 30, "Yael": 99, "Noa": 56, "Shaked": 14, 'May': 100},
                      'B': {'Rotem': 97, 'Eden': 56, "Yael": 78, "Shaked": 78, "Haim": 66, 'Peleg': 100}}


def compare_subjects_within_student(subj1_all_students: dict, subj2_all_students: dict) -> dict:
    new_d = {}
    n_students = {*list(subj1_all_students['A'].keys()), *list(subj1_all_students['B'].keys()),
                  *list(subj2_all_students['A'].keys()), *list(subj2_all_students['B'].keys())}
    for student in n_students:
        # Replace all missing grades with -1
        if student not in subj1_all_students['A'].keys():
            subj1_all_students['A'][student] = -1
        if student not in subj1_all_students['B'].keys():
            subj1_all_students['B'][student] = -1
        if student not in subj2_all_students['A'].keys():
            subj2_all_students['A'][student] = -1
        if student not in subj2_all_students['B'].keys():
            subj2_all_students['B'][student] = -1
        sub1 = [subj1_all_students['A'][student], subj1_all_students['B'][student]]
        sub2 = [subj2_all_students['A'][student], subj2_all_students['B'][student]]
        m_sub1 = max(sub1)
        m_sub2 = max(sub2)
        if m_sub1 == -1 or m_sub2 == -1:
            continue
        elif m_sub1 > m_sub2:
            new_d[student] = 'Subject1'
        else:
            new_d[student] = 'Subject2'
    for item in new_d:
        print(item, ":", new_d[item])

    return new_d


a = compare_subjects_within_student(subj1_all_students, subj2_all_students)

