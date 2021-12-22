from pizza import Pizza
import unittest
from pizza import order
from pizza import menu


class TestTF(unittest.TestCase):
    def test_1(self):
        """Тест на вывод объекта"""
        actual = Pizza('Pepperoni', 'L').__str__()
        expected = 'Pepperoni 🍕 (L)'
        self.assertEqual(actual, expected)

    def test_2(self):
        """Тест на вывод объекта"""
        actual = Pizza('Margherita', 'XL').__str__()
        expected = 'Margherita 🧀 (XL)'
        self.assertEqual(actual, expected)

    def test_3(self):
        """Тест на вывод рецепта"""
        actual = Pizza('Margherita', 'XL').dict(test=True)
        expected = {'Margherita 🧀': 'tomato sauce, mozzarella, tomatoes'}
        self.assertEqual(actual, expected)

    def test_4(self):
        """Тест на сравнение одинаковых объектов"""
        self.assertTrue(Pizza('Hawaiian', 'XL') == Pizza('Hawaiian', 'XL'))

    def test_5(self):
        """Тест на сравнение объектов с разными размерами"""
        self.assertFalse(Pizza('Hawaiian', 'L') == Pizza('Hawaiian', 'XL'))

    def test_6(self):
        """Тест на вывод меню"""
        actual = menu(test=True)
        expected = '- Margherita 🧀: tomato sauce, mozzarella, tomatoes - Pepperoni 🍕: tomato sauce, mozzarella, ' \
                   'pepperoni - Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples '
        self.assertEqual(actual, expected)

    def test_7(self):
        """Тест на вывод заказа"""
        actual = order('Pepperoni', 'XL', delivery_flg=True, test=True)
        expected = 'Pepperoni 🍕 (XL): 👨🏻‍🍳 Приготовлено за 15 минут Pepperoni 🍕 (XL): 🛵 Доставлено за 10 минут'
        self.assertEqual(actual, expected)

    def test_exception_1(self):
        """Тест на выброс исключения при отсутсвии размера"""
        with self.assertRaises(Exception):
            Pizza('Margherita')

    def test_exception_2(self):
        """Тест на выброс исключения при неверном формате названия"""
        with self.assertRaises(Exception):
            Pizza(5, 'L')

    def test_exception_3(self):
        """Тест на выброс исключения при отсутсвующем названии"""
        with self.assertRaises(Exception):
            Pizza('Chicken barbeque', 'L')

    def test_exception_4(self):
        """Тест на выброс исключения при отсутствующем размере"""
        with self.assertRaises(Exception):
            Pizza('Hawaiian', 'M')

    def test_exception_5(self):
        """Тест на выброс исключения при неверном формате флага доставки"""
        with self.assertRaises(Exception):
            order('Pepperoni', 'XL', delivery_flg='1')


if __name__ == '__main__':
    unittest.main()