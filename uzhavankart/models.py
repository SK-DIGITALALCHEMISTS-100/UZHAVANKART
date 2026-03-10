from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# ─── Farmer ───────────────────────────────────────────────────────────────────
class Farmer(models.Model):
    farmer_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField()
    land_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    crop = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='farmers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer_id} - {self.name}"


# ─── Product ──────────────────────────────────────────────────────────────────
CATEGORY_CHOICES = [
    ('Vegetables', 'Vegetables'),
    ('Fruits', 'Fruits'),
    ('Oils', 'Oils'),
    ('Seeds', 'Seeds'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"


# ─── Employee ─────────────────────────────────────────────────────────────────
class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    job_role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employee_photos/')

    def __str__(self):
        return f"{self.emp_id} - {self.name}"


# ─── ContactMessage ───────────────────────────────────────────────────────────
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=15)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.mobileno}"


# ─── CropProduct ──────────────────────────────────────────────────────────────
class CropProduct(models.Model):
    farmer_id = models.CharField(max_length=50)
    name_of_crop = models.CharField(max_length=100)
    total_kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name_of_crop} - {self.farmer_id}"

    def total_value(self):
        return self.total_kg * self.price_per_kg


# ─── Stock ────────────────────────────────────────────────────────────────────
class Stock(models.Model):
    STOCK_TYPES = [
        ('VEG', 'Vegetables'),
        ('FRU', 'Fruits'),
        ('OIL', 'Oils'),
        ('SEE', 'Seeds'),
    ]
    crop_name = models.CharField(max_length=100)
    stock_type = models.CharField(max_length=3, choices=STOCK_TYPES)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    stock_image = models.ImageField(upload_to='stock_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop_name} ({self.get_stock_type_display()}) - {self.quantity_kg} kg"


# ─── Driver ───────────────────────────────────────────────────────────────────
class Driver(models.Model):
    driver_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50)
    address = models.TextField()
    photo = models.ImageField(upload_to='driver_photos/', blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver_id} - {self.name}"


# ─── Staff ────────────────────────────────────────────────────────────────────
class Staff(models.Model):
    staff_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_id} - {self.name}"


class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    staff_code = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def save(self, *args, **kwargs):
        if self.staff:
            self.staff_code = self.staff.staff_id
        super().save(*args, **kwargs)


# ─── Driver Attendance ────────────────────────────────────────────────────────
class DriverAttendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.driver.driver_id} - {self.date} - {self.status}"


# ─── Vehicle ──────────────────────────────────────────────────────────────────
class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100, unique=True)  # removed primary_key=True
    driver_id = models.CharField(max_length=50, unique=True)
    owner_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    vehicle_company = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50, unique=True)
    vehicle_img = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.registration_number} - {self.owner_name}"


# ─── Customer ─────────────────────────────────────────────────────────────────
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.name} ({self.email})"


# ─── Cart ─────────────────────────────────────────────────────────────────────
class Cart(models.Model):
    customer_email = models.EmailField()
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["customer_email", "product"],
                                    name="uniq_cart_item_per_customer")
        ]

    def subtotal(self):
        return self.product.price_per_kg * self.quantity


# ─── Order ────────────────────────────────────────────────────────────────────
class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=100)
    customer_mobile = models.CharField(max_length=15)
    address = models.TextField()
    crop_name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.crop_name}"