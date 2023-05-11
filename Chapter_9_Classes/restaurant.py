class Restaurant:
    """A simple class for restaurants"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This restaurant is called {self.restaurant_name} and has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant, {self.restaurant_name} is open!")


my_restaurant = Restaurant('Kaze Sushi', 'Thai/Japanese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()