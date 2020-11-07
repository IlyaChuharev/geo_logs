geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def sortlist(geo_log, russia):
    russia_logs = []
    for visit in geo_log:
            if list(visit.values())[0][1] == russia:
                 russia_logs.append(visit)
    return russia_logs # чтоб не зациклилось)

country = sortlist(geo_logs, 'Россия')
for s in country:
  print(s) 