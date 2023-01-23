from django.db import models
from django.contrib.auth.models import User



STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

CATEGORY_CHOICES=(
    ('MN', 'Mens' ),
    ('WM', 'Women'),
)

class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    selling_price = models.FloatField(max_length=200, null=True)
    discount_price = models.FloatField(max_length=200,null=True)
    description = models.TextField(max_length=200, null=True)
    apppro = models.TextField(max_length=200, null=True)
    category = models.CharField( choices= CATEGORY_CHOICES,  max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=500)
    locality = models.CharField(max_length=200)
    city = models.TextField(max_length=500)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state= models.CharField(STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


    
    
    
    
