import unittest
from Recipe_Test import Recipe_Test
from RecipeBook_Test import RecipeBook_Test

test_case1=unittest.TestLoader().loadTestsFromTestCase(Recipe_Test)
test_case2=unittest.TestLoader().loadTestsFromTestCase(RecipeBook_Test)

SystemSuite=unittest.TestSuite([test_case1,test_case2])
runner= unittest.TextTestRunner()
runner.run(SystemSuite)
