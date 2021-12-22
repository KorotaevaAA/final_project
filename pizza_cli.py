import click
from pizza import Pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery_flg', default=False, is_flag=True)
@click.option('--size', default='L', type=str)
@click.argument('pizza', nargs=1)
def order(pizza: str, size: str, delivery_flg: bool, test=False):
    """Готовит и доставляет пиццу"""
    if delivery_flg not in [True, False]:
        raise ValueError('Delivery: True or False?')
    ordered_pizza = Pizza(pizza, size)
    answer: str = ''
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


@cli.command()
def menu(test=False):
    """Выводит меню"""
    all_pizza = [Pizza('Margherita', 'L'), Pizza('Pepperoni', 'L'), Pizza('Hawaiian', 'L')]
    answer: str = ''
    for pizza in all_pizza:
        if test:
            answer += f'- {pizza.name}: ' + ', '.join(ingredient for ingredient in pizza.ingredients) + ' '
        else:
            print(f'- {pizza.name}: ', ', '.join(ingredient for ingredient in pizza.ingredients))
    if test:
        return answer


if __name__ == '__main__':
    cli()
