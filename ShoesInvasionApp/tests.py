from django.test import TestCase, Client
from .models.user import UserTable
from .models.products import ProductsTable

# Create your tests here.

# HTTP Response Code Legend
# HTTP_200_OK
# HTTP_201_CREATED
# HTTP_302_FOUND
# HTTP_404_NOT_FOUND

# Test if pages loads properly
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('/ShoesInvasionApp/')
        self.assertEqual(response.status_code, 200)

# Test to create product and extract details from table
class ProductsTableTestCase(TestCase):
    # Setting up the test case by creating a new product
    def setUp(self):
        product = ProductsTable.objects.create(
            product_name="NMD_R1 V3 SHOES", 
            product_price="240", 
            review="Authentic and best shoe i've worn!", 
            product_info="ULTRA-COMFORTABLE SHOES WITH SEMI-TRANSPARENT DETAILS. A play on transparency, these adidas NMD_R1 V3 Shoes continue to build on the NMD franchise's signature expression of tactical tech. Here's what you need to know about the BOOST cushioning: it makes every step feel supported. Which is great, since you take a lot of them throughout the day. The other thing to know is that it's partially encapsulated in TPU, met by the TPU heel plugs that signal that these are in fact NMD trainers. They have a laser-cut upper, complete with embroidered details for a fresh take on the iconic style.",
            product_brand="Adidas",
            product_category="Sneakers",
            gender_type="M",
            available="Yes",
            status="1")
        product.save()

    def test_products_can_get_details(self):
        # New Product added as shown above
        nmdProduct = ProductsTable.objects.get(product_name="NMD_R1 V3 SHOES")
        self.assertEqual(nmdProduct.product_price, 240)
        self.assertEqual(nmdProduct.status, "1")

# Login Test Case
class LoginTestCase(TestCase):
    # Setting up the test case by creating a new product
    def setUp(self):
        user = UserTable.objects.create(
            first_name = "John",
            last_name = "Smith",
            username = "johnsmith",
            password = "ilovecatsanddogs",
            email = "jonhsmithcad@gmail.com",
            phone = "98765475",
            bannedStatus = 0,
            verifiedStatus = 0,
            lockedStatus = 0,
            lockedCounter = 0,
            accountType = "User",
            unique_id="aslkhbio2qhnfeoiy0giewpjgniohawnioelkgj193hipenk3")
        user.save()

    def test_login_loads_properly(self):
        response = self.client.get('/ShoesInvasionApp/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='ShoesInvasionApp/login_user.html')

    def test_login(self):
        c = Client()
        # Dummy OTP because OTP is required to login but for unit test, unable to generate QR Code to do
        response = c.post('/ShoesInvasionApp/login', {'username': 'johnsmith', 'password': 'ilovecatsanddogs', "otpToken": "123456", "g-recaptcha-response":"123"})
        self.assertEqual(response.status_code, 200)

# Register Test Case
class RegisterTestCase(TestCase):

    def test_register_load_properly(self):
        response = self.client.get('/ShoesInvasionApp/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='ShoesInvasionApp/register.html')

    def test_register(self):
        response = self.client.post('/ShoesInvasionApp/register/', 
        {'first_name': 'john',
         'last_name': 'smith', 
         "username": "johnsmith",
         "password": "ilovecatsanddogs",
         "verify_password": "ilovecatsanddogs",
         "email": "johnsmithcad@gmail.com",
         "phone": 98765476,
         "bannedStatus": 0,
         "verifiedStatus": 0,
         "verificationCode": "564afg2wr43g",
         "lockedStatus": 0,
         "lockedCounter": 0,
         "accountType": "User",
         "unique_key": "aslkhbio2qhnfeoiy0giewpjgniohawnioelkgj193hipenk3",
         "secret_key": "pi24ktjk2212l3jk5"})
        self.assertEqual(response.status_code, 200)

# Shopping Cart Test Case
# class ShoppingCartTestCase(TestCase):

#     def test_shopping_cart_load_properly_without_redirect(self):
#         session = self.client.session
#         session['unique_id'] ='aslkhbio2qhnfeoiy0giewpjgniohawnioelkgj193hipenk3'
#         session.save()
#         response = self.client.get('/ShoesInvasionApp/cart')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name='ShoesInvasionApp/cart.html')

#     def test_checkout_cart(self):
#         session = self.client.session
#         session['unique_id'] ='aslkhbio2qhnfeoiy0giewpjgniohawnioelkgj193hipenk3'
#         session.save()
#         response = self.client.post('/ShoesInvasionApp/cart', 
#         {'quantity': 2,
#          'size': 'UK9', 
#          "color": "Black",
#          "total_price": "240",
#          "status": "1",
#          "product_id": 10,
#          "unique_id": "aslkhbio2qhnfeoiy0giewpjgniohawnioelkgj193hipenk3",})
#         self.assertEqual(response.status_code, 200)