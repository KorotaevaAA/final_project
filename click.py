import click
from pizza import Pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option(' =delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    ordered_pizza = Pizza(pizza, size)
    print(ordered_pizza, ': 👨🏻‍🍳 Приготовлено за 15 минут')
    if delivery:
        print(ordered_pizza, ': 🛵 Доставлено за 10 минут')

@cli.command()
def menu():
    """Выводит меню"""
    all_pizza = [Pizza('Margherita', 'L'), Pizza('Pepperoni', 'L'), Pizza('Hawaiian', 'L')]
    for pizza in all_pizza:
        print(f'- {pizza.name}: ', ', '.join(ingredient for ingredient in pizza.ingredients))


if __name__ == '__main__':
    cli()
