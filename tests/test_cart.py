import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"Disc {i}", cost=1.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("One too many", cost=1.0)))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=19.95))
        cart.add_dvd(DigitalVideoDisc("B", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("C", cost=18.99))
        self.assertAlmostEqual(cart.total_cost(), 63.89)

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_percent_out_of_range(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        for title in ("Star Wars", "Aladdin", "The Lion King"):
            cart.add_dvd(DigitalVideoDisc(title, cost=1.0))
        cart.sort_by_title()
        self.assertEqual([d.title for d in cart.items], ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost(self):
        cart = Cart()
        for title, cost in (("A", 24.95), ("B", 18.99), ("C", 19.95)):
            cart.add_dvd(DigitalVideoDisc(title, cost=cost))
        cart.sort_by_cost()
        self.assertEqual([d.cost for d in cart.items], [18.99, 19.95, 24.95])


if __name__ == "__main__":
    unittest.main()
