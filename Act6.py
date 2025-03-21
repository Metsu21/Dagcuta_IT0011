class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            new_item = Item(item_id, name, description, price)
            self.items[item_id] = new_item
            print("Item created successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def read_item(self, item_id):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            print(self.items[item_id])
        except KeyError as e:
            print(f"Error: {e}")

    def update_item(self, item_id, name=None, description=None, price=None):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            
            item = self.items[item_id]
            if name:
                item.name = name
            if description:
                item.description = description
            if price is not None:
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                item.price = price
            print("Item updated successfully.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            del self.items[item_id]
            print("Item deleted successfully.")
        except KeyError as e:
            print(f"Error: {e}")

    def list_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)


# Example Usage
if __name__ == "__main__":
    manager = ItemManager()
    manager.create_item(1, "Laptop", "High-performance laptop", 1200.99)
    manager.create_item(2, "Phone", "Latest smartphone", 799.49)
    manager.list_items()
    manager.update_item(1, price=1100.50)
    manager.read_item(1)
    manager.delete_item(2)
    manager.list_items()
