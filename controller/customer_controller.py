from utils.file_manager import FileManager

class CustomerController:
    file_name = "data/customers.pkl"

    def get_all(self):
        return FileManager.load(self.file_name)

    def add(self, customer):
        data = self.get_all()
        if any(c.customer_id == customer.customer_id for c in data):
            raise ValueError("شناسه مشتری تکراری است")
        data.append(customer)
        FileManager.save(self.file_name, data)

    def update(self, new_customer):
        data = self.get_all()
        for i, customer in enumerate(data):
            if customer.customer_id == new_customer.customer_id:
                data[i] = new_customer
                FileManager.save(self.file_name, data)
                return
        raise ValueError("مشتری پیدا نشد")

    def delete(self, customer_id):
        data = [c for c in self.get_all() if c.customer_id != str(customer_id)]
        FileManager.save(self.file_name, data)

    def search(self, text):
        return [c for c in self.get_all()
                if text.lower() in c.name.lower() or text in c.customer_id]
