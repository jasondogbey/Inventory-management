class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        print(f"Product: {self.name}\nPrice: ${self.price}\nQuantity: {self.quantity}")

class InventoryItem:
    def __init__(self, product, in_stock):
        self.product = product
        self.in_stock = in_stock
    
    def add_stock(self, quantity=1):
        self.in_stock += quantity
    
    def sell(self, quantity):
        if self.in_stock >= quantity:
            self.in_stock -= quantity
            return True
        else:
            print('Not enough items in stock')
            return False
        
    def display_inventory(self):
        self.product.display_info()
        print(f"In Stock: {self.in_stock}")
        

class SalesTransaction:
    def __init__(self):
        self.sales = []
    
    def add_sale(self, product, quantity):
        sale_amount = product.price * quantity
        self.sales.append((product.name, quantity, sale_amount))
        return sale_amount

    def display_sales(self):
        if self.sales:
            print("Sales Transactions")
            total_sale = 0
            for sale in self.sales:
                print(f"Product: {sale[0]}, Quantity: {sale[1]}, Amount: ${sale[2]}")
                total_sale += sale[2]
            print(f"Total Sales: ${total_sale}")
        else:
            print("No sale transaction yet.")

# Example usage
# Create products
product1 = Product("Phone", 500, 10)
product2 = Product("Laptop", 1200, 5)

# Create inventory items
item1 = InventoryItem(product1, 10)
item2 = InventoryItem(product2, 5)

# Sell products
item1.sell(3)
item2.sell(2)

# Display current inventory
print("\nInventory:")
item1.display_inventory()
item2.display_inventory()

# Create sales transaction and add sales
sales = SalesTransaction()
sales.add_sale(product1, 2)
sales.add_sale(product2, 1)

# Display sales transactions
print("\nSales:")
sales.display_sales()