# Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


# Bill class
class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 18

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        total = 0

        for product in self.products:
            total = total + product.get_total()

        return total

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate / 100

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()

        return subtotal + tax

    def display_bill(self):
        print("\n================ FINAL BILL ================")
        print("{:<15} {:>10} {:>10} {:>10}".format(
            "Product", "Price", "Qty", "Total"
        ))
        print("-" * 50)

        for product in self.products:
            print("{:<15} {:>10.2f} {:>10} {:>10.2f}".format(
                product.name,
                product.price,
                product.quantity,
                product.get_total()
            ))

        print("-" * 50)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print("Subtotal: ₹", round(subtotal, 2))
        print("Tax (18%): ₹", round(tax, 2))
        print("Final Total: ₹", round(total, 2))


# Create Bill object
bill = Bill()

# Get products from user
n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = Product(name, price, quantity)

    bill.add_product(product)


# Display final bill
bill.display_bill()
