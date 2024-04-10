class Dishes():
    """Создаем класс блюд

    """
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __repr__(self):
        return f'{self.name}'

class Recipe():
    """Создаем класс рецептов, который содержит:
    - название ингредиента
    - его количество
    - единицу измерения

    """
    def __init__(self, ingredient_name, quantity, measure):
        self.ingredient_name = ingredient_name
        self.quantity = quantity
        self.measure = measure

    def __repr__(self):
        return f'{self.ingredient_name}, {self.quantity}, {self.measure}'


#Задача №1:
def read_file():
    """Функция чтения файла с рецептами, которая прочитывает файл и создает словарь cook_book

    """
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = ingredients
            f.readline()

        return cook_book


# print(read_file())

#Задача №2:
def get_shop_list_by_dishes(dishes, person_count):
    """Функция, которая принимает на вход список блюд из cook_book (если их нет - сообщит об этом)
    и количество персон для кого будем готовить
    """
    cook_book = read_file()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
        else:
            print(f'Блюда {dish} нет в книге рецептов')

    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2))
print(get_shop_list_by_dishes(['Фахитос', 'Селедка под шубой'], 4))