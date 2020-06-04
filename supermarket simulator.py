import random
import matplotlib.pyplot as plt
import csv
import matplotlib

product_dictionary = {}  # the products will be added here from the csv file.
with open("product_data.csv", mode="r") as file_csv:  # open a csv file.
    csv_reader = csv.reader(file_csv)  # use the reader method from the csv module
    # the reader function will return an iterable that has an iterator
    # we can call next on it to skip the first row that give us the information about the data
    next(csv_reader)
    # loop through the csv_reader and add each product and its price to the product_dictionary
    for line in csv_reader:
        product_dictionary[line[0]] = float(line[1])

# debugging lines
print(product_dictionary)
print(random.choice(list(product_dictionary.keys())))

# create a class to hold all information about customers
class Costumer:
    # this class variable will hold all products that have been bought
    bought_product = {}
    # initialise the class that takes 4 kwargs
    def __init__(self, c_name="Unknown", c_money=0.0, c_product="Unknown", *args):
        self.c_name = c_name  # customer name
        self.c_money = c_money  # customer money
        self.c_product = c_product  # customer products
        # loop through each random customer products and add it to the dictionary
        for i in self.c_product:
            # check if product exists
            if i in Costumer.bought_product:
                # if yes add 1 to the total
                Costumer.bought_product[i] += 1
            else:
                # if no set the new product to 1
                Costumer.bought_product[i] = 1
    # create a classmethod to read customer string data for further processing
    @classmethod
    def costumer_data(cls, costumer_string):
        # split data into 3 chunks name and money the first 2 variables then the rest is products
        name, money, *product = costumer_string.split("/")
        # return the processed data to the class
        return cls(name, float(money), product)

# random customer name with their budget
john_data = "John/5/"
jamie_data = "Jamie/1500/"
buford_data = "Buford/752/"
cathi_data = "Cathi/380/"
cicely_data = "Cicely/880/"
basil_data = "Basil/197/"
patrica_data = "Patrica/700/"
vonnie_data = "Vonnie/188/"
dominick_data = "Dominick/98/"
margherita_data = "Margherita/378/"

# this function will give a random number of items that does not exceed 10 items for each customer
# and returns a different dictionary every time it is called
# this function uses the product dictionary
def rand_items():
    # get a random number
    end = random.randint(1, 10)
    groceries = ""
    for _ in range(0, end):
        # add a random product to the groceries sting and split each with "/"
        groceries += random.choice(list(product_dictionary.keys())) + "/"
    return groceries

# create an object for each customer and feed their name, budget and what random products that they have chosen
john = Costumer.costumer_data(john_data + rand_items())
jamie = Costumer.costumer_data(jamie_data + rand_items())
buford = Costumer.costumer_data(buford_data + rand_items())
cathi = Costumer.costumer_data(cathi_data + rand_items())
cicely = Costumer.costumer_data(cicely_data + rand_items())
basil = Costumer.costumer_data(basil_data + rand_items())
patrica = Costumer.costumer_data(patrica_data + rand_items())
vonnie = Costumer.costumer_data(vonnie_data + rand_items())
dominick = Costumer.costumer_data(dominick_data + rand_items())
margherita = Costumer.costumer_data(margherita_data + rand_items())

# remove any empty data from the class variable dictionary
Costumer.bought_product.pop("")
# debugging line
print(Costumer.bought_product)

# this dictionary will store each product and the total
final = {}
for k, v in Costumer.bought_product.items():
    # get products and multiply them by their price
    final[k] = product_dictionary[k] * v
# debugging line
print(final)
# set font in matplotlib
font = {'family': 'Courier',
        'weight': 'bold',
        'size': 5}

matplotlib.rc('font', **font)
# choose the bar method and make sure you feed it X and Y in a list format.
plt.bar(list(final.keys()), list(final.values()))
# show the final result
plt.show()
