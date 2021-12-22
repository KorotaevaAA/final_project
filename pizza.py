from random import randint
from typing import Callable


class Pizza:
    def __init__(self, name: str, size: str):
        if name not in ['Margherita', 'Pepperoni', 'Hawaiian']:
            raise ValueError('Not have this pizza in menu')
        if size not in ['L', 'XL']:
            raise ValueError('Possible sizes: L, XL')

        self.size = size
        self.name = name

        if name == 'Margherita':
            self.name += ' 🧀'
            self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

        if name == 'Pepperoni':
            self.name += ' 🍕'
            self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

        if name == 'Hawaiian':
            self.name += ' 🍍'
            self.ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __str__(self):
        return f'{self.name} ({self.size})'

    def dict(self, test=False):
        """Выводит рецепт"""
        recipe = {self.name: ', '.join(ingredient for ingredient in self.ingredients)}
        if test:
            return recipe
        else:
            print(recipe)

    def __eq__(self, other):
        if self.name == other.name and self.size == other.size:
            return True
        else:
            return False


def order(pizza: str, size: str, delivery_flg: bool, test=False):
    """Готовит и доставляет пиццу"""
    if delivery_flg not in [True, False]:
        raise ValueError('Delivery: True or False?')
    ordered_pizza = Pizza(pizza, size)
    answer = ''
    if test:
        answer += ordered_pizza.__str__() + ': 👨🏻‍🍳 Приготовлено за 15 минут '
    else:
        print(ordered_pizza, ': 👨🏻‍🍳 Приготовлено за 15 минут')
    if delivery_flg:
        if test:
            answer += ordered_pizza.__str__() + ': 🛵 Доставлено за 10 минут'
        else:
            print(ordered_pizza, ': 🛵 Доставлено за 10 минут')
    if test:
        return answer


def menu(test=False):
    """Выводит меню"""
    all_pizza = [Pizza('Margherita', 'L'), Pizza('Pepperoni', 'L'), Pizza('Hawaiian', 'L')]
    answer = ''
    for pizza in all_pizza:
        if test:
            answer += f'- {pizza.name}: ' + ', '.join(ingredient for ingredient in pizza.ingredients) + ' '
        else:
            print(f'- {pizza.name}: ', ', '.join(ingredient for ingredient in pizza.ingredients))
    if test:
        return answer


def log(example: str) -> Callable:
    """Перед выполнением функции выводим по шаблону ее имя и время"""
    def outer_wrapper(function: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs):
            print(example.replace('{}', f'{randint(5, 50)}').replace('name', function.__name__))
            function(*args, **kwargs)

        return inner_wrapper

    return outer_wrapper


@log('🥧 name in {} s!')
def bake(pizza: Pizza):
    """Готовит пиццу"""


@log('🛵 name in {} s!')
def delivery(pizza: Pizza):
    """Доставляет пиццу"""


@log('🏠 name in {} s!')
def pickup(pizza: Pizza):
    """Доставляет пиццу"""


if __name__ == '__main__':
    first_pizza = Pizza('Pepperoni', 'L')
    print(first_pizza)
    first_pizza.dict()

    second_pizza = Pizza('Margherita', 'L')
    third_pizza = Pizza('Pepperoni', 'XL')
    same_pizza = Pizza('Pepperoni', 'L')

    print(first_pizza == first_pizza)
    print(first_pizza == second_pizza)
    print(first_pizza == third_pizza)
    print(first_pizza == same_pizza)

    menu()
    order('Hawaiian', 'XL', delivery_flg=True)
    bake(first_pizza)
    delivery(first_pizza)
    pickup(first_pizza)
