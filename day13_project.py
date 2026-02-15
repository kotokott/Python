import csv

def read_and_clean_csv():
    with open('files/users_data.csv', newline='', encoding='utf-8') as f:
        d_reader = csv.DictReader(f)
        udata_fieldnames = d_reader.fieldnames

        clean_users_data = []
        for row in d_reader:
            try:
                row['age'] = int(row['age'])
                row['score'] = int(row['score'])
                row['id'] = int(row['id'])
            except (ValueError, TypeError):
                continue
            if row['city'] == '':
                continue

            clean_users_data.append(row)

        print(clean_users_data)
        return clean_users_data, udata_fieldnames

def analyze_users_data(user_data: list):
    # защита от пустого списка
    if not user_data:
        print('No clean user data')
        return
    user_data_len = len(user_data)
    print('total:', user_data_len)
    print('average age:', sum([u['age'] for u in user_data]) / user_data_len)
    print('average score:', sum([u['score'] for u in user_data]) / user_data_len)
    print('max score:', max(user_data, key=lambda u: u['score'])) # надо было юзера выводить
    print('Berlin high score users:', [u for u in user_data if u['city'] == 'Berlin' and u['score'] >= 85])

def create_top_users_file(fieldnames, user_data: list):
    with open('files/top_users.csv', 'w+', newline='', encoding='utf-8') as top_f:
        d_writer = csv.DictWriter(top_f, fieldnames=fieldnames)
        d_writer.writeheader()

        d_writer.writerows([u for u in user_data if u['score'] >= 85])

def analyze_scores_by_city(user_data: list):
    # херня за O^2
    # city_scores = []
    # cities = []
    # for u in user_data:
    #     if u['city'] not in cities:
    #         city_scores.append({'city':u['city'], 'score': u['score'], 'count': 1})
    #         cities.append(u['city'])
    #     else:
    #         curr_record = city_scores[cities.index(u['city'])]
    #         curr_record = {'city': u['city'],
    #                        'score': curr_record['score'] + u['score'],
    #                        'count': curr_record['count'] + 1}
    #         city_scores[cities.index(u['city'])] = curr_record
    #
    # print({v['city']:(v['score'] / v['count']) for v in city_scores})
    stats = {}
    for u in user_data:
        city = u['city']
        if city not in stats:
            stats[city] = [0, 0]
        stats[city][0] += u['score']
        stats[city][1] += 1

    avg_by_city = {city: s/c for city, (s, c) in stats.items()}
    print(avg_by_city)


clean_users_data, udata_fieldnames = read_and_clean_csv()
analyze_users_data(clean_users_data)
create_top_users_file(udata_fieldnames, clean_users_data)
analyze_scores_by_city(clean_users_data)



