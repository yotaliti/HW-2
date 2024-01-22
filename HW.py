
cook_book = {}

with open('recipes.txt', encoding='UTF-8') as f:
    lines = [i.strip() for i in f.readlines()]

    while (len(lines)) > 0:
        cook_book.update({lines[0]: []})

        for i in range(int(lines[1].strip())):
            cook_book[lines[0]] += {'ingredient_name': lines[i + 2].split('|')[0].strip(),
                                    'quantity': lines[i + 2].split('|')[1].strip(),
                                    'measure': lines[i + 2].split('|')[2].strip()},
        lines = lines[int(lines[1].strip()) + 3:]


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': int(ingredient['quantity']) * person_count}

    return shop_list
