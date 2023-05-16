from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from products.models import Product, ProductEntry, ProductList


class Command(BaseCommand):
    help = 'Creates some test data for the products app'

    def handle(self, *args, **options):
        # Get the existing admin User
        admin_user = User.objects.get(username='admin')

        # Create some Products
        chocolate = Product.objects.create(name="Chocolate", description="Delicious milk chocolate")
        milk = Product.objects.create(name="Milk", description="Fresh whole milk")

        # Create a Product List for the admin user
        grocery_list = ProductList.objects.create(name="Grocery List", description="My weekly groceries", user=admin_user)

        # Add some Product Entries to the Product List
        ProductEntry.objects.create(name="Chocolate", description="Need some chocolate", quantity=5, product_id=chocolate.id, product_list=grocery_list)
        ProductEntry.objects.create(name="Milk", description="Running low on milk", quantity=2, product_id=milk.id, product_list=grocery_list)

        self.stdout.write(self.style.SUCCESS('Successfully created test data'))
