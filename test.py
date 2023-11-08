from datetime import date, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}
    new_users = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    
    today = date.today() 
    #today = date(year=2023, month=11, day=6)

    
    print ("today - ", today)
   
    # weekend_before_monday = today - timedelta(days = 2)
    # today_day = today.weekday()
    # тут обробляємо вхідні дані юзерів - імʼя та день народження
    for user in users:
        name = user['name']
        birthday_date = user["birthday"]
        new_birthday_date = birthday_date.replace(year=today.year)
        print ("new_birthday_date - ", new_birthday_date)
        if new_birthday_date < today:  # якщо найближчий день народження менше поточної дати...
            new_birthday_date = new_birthday_date.replace(year=today.year + 1)
        
        print ("new_birthday_date - ", new_birthday_date)
        birthday_date_day = new_birthday_date.weekday()
        # print ("day - ", birthday_date_day, name)
        
        # в цьому if логіка "сьогодні-понеділок" - додавання днів народжень з минулих вихідних та ігноруємо наступні вихідні
        # if today_day == 0:
        #     if  weekend_before_monday <= new_birthday_date < today :
        #         new_users['Monday'].append(name)
        #     elif birthday_date_day == 5 or birthday_date_day == 6:
        #         continue
        # тут збираємо словник з відповідними датами народження на привітання
        if  today <= new_birthday_date <= today + timedelta(days=6):
            if birthday_date_day == 0 or birthday_date_day == 5 or birthday_date_day == 6:
                new_users['Monday'].append(name)
            elif birthday_date_day == 1:
                new_users['Tuesday'].append(name)
            elif birthday_date_day == 2:
                new_users['Wednesday'].append(name)
            elif birthday_date_day == 3:
                new_users['Thursday'].append(name)
            else:
                new_users['Friday'].append(name)
        else:
            continue
   
    # в цьому циклі прибираємо дні з порожніми списками в значеннях
    for day, el in list(new_users.items()):
        if el == []:
            del new_users[day]
    # тут перевіряємо чи не пустий словник
    if any(new_users[day] for day in new_users):
        return new_users
    else: return {}

# def get_birthdays_per_week(users):
#     if not users:
#         return {}
#     new_users = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
#     today = date.today()

#     # тут обробляємо вхідні дані юзерів - імʼя та день народження
#     for user in users:
#         name = user['name']
#         birthday_date = user["birthday"]
#         new_birthday_date = birthday_date.replace(year=today.year)
#         if new_birthday_date < today:  # якщо найближчий день народження менше поточної дати...
#             new_birthday_date = new_birthday_date.replace(year=today.year + 1)
#         # тут збираємо словник з відповідними датами народження на привітання
#         if today <= new_birthday_date <= today + timedelta(days=6):
#             birthday_date_day = new_birthday_date.weekday()
#             if birthday_date_day == 0 or birthday_date_day == 5 or birthday_date_day == 6:
#                 new_users['Monday'].append(name)
#             elif birthday_date_day == 1:
#                 new_users['Tuesday'].append(name)
#             elif birthday_date_day == 2:
#                 new_users['Wednesday'].append(name)
#             elif birthday_date_day == 3:
#                 new_users['Thursday'].append(name)
#             else:
#                 new_users['Friday'].append(name)

#     return {key: value for key, value in new_users.items() if value}




if __name__ == "__main__":
    users = [
        
        {'name': 'previous_Friday', 'birthday': date(2023, 11, 3)},
        {'name': 'previous_Saturday', 'birthday': date(2023, 11, 4)},
        {'name': 'previous_Sunday', 'birthday': date(2023, 11, 5)},
        {'name': 'Monday', 'birthday': date(2023, 11, 6)},
        {'name': 'Tuesday', 'birthday': date(2023, 11, 7)},
        {'name': 'Wednesday', 'birthday': date(2023, 11, 8)},
        {'name': 'Thursday', 'birthday': date(2023, 11, 9)},
        {'name': 'Friday', 'birthday': date(2023, 11, 10)},
        {'name': 'Saturday', 'birthday': date(2023, 11, 11)}, 
        {'name': 'Sunday', 'birthday': date(2023, 11, 12)},
        {'name': 'next_Monday', 'birthday': date(2023, 11, 13)},
        {'name': 'next_Tuesday', 'birthday': date(2023, 11, 14)},
        {'name': 'next_Friday', 'birthday': date(2023, 11, 17)},
        {'name': 'next_next_Sunday', 'birthday': date(2023, 11, 19)},
        {'name': 'next_next_Monday', 'birthday': date(2023, 11, 20)},
        {'name': 'next_next_Tuesday', 'birthday': date(2023, 11, 21)},
        {'name': 'first_january', 'birthday': date(2024, 1, 1)},

]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
