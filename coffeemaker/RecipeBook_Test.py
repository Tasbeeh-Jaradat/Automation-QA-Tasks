import unittest
from RecipeBook import RecipeBook
from Recipe import Recipe


class RecipeBook_Test(unittest.TestCase):
    def setUp(self) :
        self.rb1=RecipeBook()
        r1=Recipe()
        r1.setName("normal_coffee")
        r2 = Recipe()
        r2.setName("spresso")
        self.rb1._RecipeBook__recipeArray=[r1,r2]

    def test_addRecipe(self):
        r3=Recipe()
        r3.setName("Cappuccino")
        r4=Recipe()
        r4.setName("Black")
        r5=Recipe()
        r5.setName("Ristretto")

        self.assertTrue(self.rb1.addRecipe(r3))#test adding item in middle
        self.assertFalse(self.rb1.addRecipe(r3))  # test adding same item
        self.assertTrue(self.rb1.addRecipe(r4))#test adding last item
        self.assertFalse(self.rb1.addRecipe(r5))#test adding out of boundary

    def test_deleteRecipe(self):
        self.assertEqual(self.rb1.deleteRecipe(1),"spresso") #test deleting item in middle
        self.assertEqual(self.rb1.deleteRecipe(2), None) #test deleting out of boundary

    def test_editRecipe(self):
        r3=Recipe()
        r3.setName("Cappuccino")
        r4=Recipe()
        r4.setName("Black")
        self.assertEqual(self.rb1.editRecipe(1,r3), "spresso")  # test editing item in middle
        self.assertEqual(self.rb1.editRecipe(2,r4), None)  # test editing out of boundary

    def test_getRecipes(self):
        r1=Recipe()
        r1.setName("normal_coffee")
        r2 = Recipe()
        r2.setName("spresso")
        self.assertListEqual(self.rb1.getRecipes(),[r1,r2])


# if __name__=='__main__':
#     unittest.main()