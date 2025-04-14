import random

class DataGenerator:
    # Creates random data for sorting
    
    def generate_data(self, num_elements=50, min_value=1, max_value=100):
        # Make list of random numbers
        return [random.randint(min_value, max_value) for _ in range(num_elements)]