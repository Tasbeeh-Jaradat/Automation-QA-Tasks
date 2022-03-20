import unittest
from Recipe import Recipe
from RecipeException import RecipeException

class Recipe_Test(unittest.TestCase):
    def setUp(self):
        self.MyRecipe=Recipe()

    def test_setAmtChocolate(self):
        self.MyRecipe.setAmtChocolate("5")
        self.assertEqual(self.MyRecipe._Recipe__amtChocolate,5)
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtChocolate("5.5")
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtChocolate("-5")

    def test_getAmtChocolate(self):
        self.assertEqual(self.MyRecipe.getAmtChocolate(), 0)
        self.MyRecipe._Recipe__amtChocolate=5
        self.assertEqual(self.MyRecipe.getAmtChocolate(),5)

    def test_setAmtCoffee(self):
        self.MyRecipe.setAmtCoffee("5")
        self.assertEqual(self.MyRecipe._Recipe__amtCoffee,5)
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtCoffee("5.5")
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtCoffee("-5")

    def test_getAmtCoffee(self):
        self.assertEqual(self.MyRecipe.getAmtCoffee(), 0)
        self.MyRecipe._Recipe__amtCoffee=5
        self.assertEqual(self.MyRecipe.getAmtCoffee(),5)

    def test_setAmtMilk(self):
        self.MyRecipe.setAmtMilk("5")
        self.assertEqual(self.MyRecipe._Recipe__amtMilk,5)
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtMilk("5.5")
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtMilk("-5")

    def test_getAmtMilk(self):
        self.assertEqual(self.MyRecipe.getAmtMilk(), 0)
        self.MyRecipe._Recipe__amtMilk=5
        self.assertEqual(self.MyRecipe.getAmtMilk(),5)

    def test_setAmtSugar(self):
        self.MyRecipe.setAmtSugar("5")
        self.assertEqual(self.MyRecipe._Recipe__amtSugar,5)
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtSugar("5.5")
        with self.assertRaises(RecipeException):
            self.MyRecipe.setAmtSugar("-5")

    def test_getAmtSugar(self):
        self.assertEqual(self.MyRecipe.getAmtSugar(), 0)
        self.MyRecipe._Recipe__amtSugar=5
        self.assertEqual(self.MyRecipe.getAmtSugar(),5)

    def test_setPrice(self):
        self.MyRecipe.setPrice("5")
        self.assertEqual(self.MyRecipe._Recipe__price,5)
        with self.assertRaises(RecipeException):
            self.MyRecipe.setPrice("5.5")
        with self.assertRaises(RecipeException):
            self.MyRecipe.setPrice("-5")

    def test_getPrice(self):
        self.assertEqual(self.MyRecipe.getPrice(), 0)
        self.MyRecipe._Recipe__price=5
        self.assertEqual(self.MyRecipe.getPrice(),5)

    def test_setName(self):
        self.MyRecipe.setName(None)
        self.assertEqual(self.MyRecipe._Recipe__name,"")
        self.MyRecipe.setName("spresso")
        self.assertEqual(self.MyRecipe._Recipe__name,"spresso")

    def test_rpr(self):
        self.MyRecipe._Recipe__name="spresso"
        self.assertEqual(str(self.MyRecipe),"spresso")

    def test_eq(self):
        self.MyRecipe._Recipe__name = "spresso"
        MyRecipe2 = None
        self.assertFalse(self.MyRecipe.__eq__(MyRecipe2))
        MyRecipe2="not instance of Recipe"
        self.assertFalse(self.MyRecipe.__eq__(MyRecipe2))
        MyRecipe2=Recipe()
        MyRecipe2._Recipe__name = "latte"
        self.assertFalse(self.MyRecipe.__eq__(MyRecipe2))
        MyRecipe2._Recipe__name = "spresso"
        self.assertTrue(self.MyRecipe.__eq__(MyRecipe2))



    def test_hash(self):
        self.MyRecipe._Recipe__name = None
        self.assertEqual(self.MyRecipe.__hash__(),0)
        self.MyRecipe._Recipe__name = "spresso"
        MyRecipe2 = Recipe()
        MyRecipe2._Recipe__name = "spresso"
        setToCheckHashable={self.MyRecipe,MyRecipe2}
        s={self.MyRecipe}
        self.assertSetEqual(setToCheckHashable,s)



# if __name__=='__main__':
#     unittest.main()