
class RecipeException(Exception):
    def __init__(self,message):
        self.message=message
        super(RecipeException, self).__init__(self.message)