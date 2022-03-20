from typing import Final

class RecipeBook:
    def __init__(self):
        self.__NUM_RECIPES: Final= 4
        self.__recipeArray=[]

    def getRecipes(self):
        return self.__recipeArray

    def addRecipe(self,recipe):
        exists = False
        if recipe in self.__recipeArray:
                exists=True

        added=False
        if not exists:
            if len(self.__recipeArray)<self.__NUM_RECIPES:
                self.__recipeArray.append(recipe)
                added=True
        return added

    def deleteRecipe(self,IndexRecipeDelete):
        recipeName=None
        if IndexRecipeDelete < len(self.__recipeArray):
            recipeName =self.__recipeArray[IndexRecipeDelete].getName()
            self.__recipeArray.pop(IndexRecipeDelete)
        return recipeName
    def editRecipe(self,IndexRecipeEdit,newRecipe):
        recipeName = None
        if IndexRecipeEdit < len(self.__recipeArray):
            recipeName=self.__recipeArray[IndexRecipeEdit].getName()
            self.__recipeArray[IndexRecipeEdit]=newRecipe
        return recipeName





