from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Equipment(models.Model):

    CATEGORY_CHOICES = [
        ('Tractor', 'Tractor'),
        ('Harvester', 'Harvester'),
        ('Rotavator', 'Rotavator'),
        ('Bore Machine', 'Bore Machine'),
        ('Sprayer', 'Sprayer'),
        ('Cultivator', 'Cultivator'),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to='equipment_images/',
        blank=True,
        null=True
    )

    owner_name = models.CharField(max_length=100)

    owner_mobile = models.CharField(max_length=15)

    location = models.CharField(max_length=100)

    rent_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    security_deposit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available = models.BooleanField(default=True)

    description = models.TextField()

    rules = models.TextField()

    owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class EquipmentBooking(models.Model):

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE
    )

    renter_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    aadhaar_number = models.CharField(max_length=12)

    start_date = models.DateField()

    end_date = models.DateField()

    total_days = models.IntegerField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # NEW FIELDS 👇

    payment_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    payment_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    booking_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.renter_name} - {self.equipment.name}"
    
class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    mobile = models.CharField(
        max_length=15
    )

    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('Owner', 'Owner'),
    ]

    profession = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    address = models.TextField()

    def __str__(self):
        return self.user.first_name
    
class Worker(models.Model):
    SKILL_CHOICES = [

    ('Gehu Katai', 'Gehu Katai'),
    ('Dhaan Katai', 'Dhaan Katai'),
    ('Moong Katai', 'Moong Katai'),
    ('Chana Katai', 'Chana Katai'),

    ('Threshing Worker', 'Threshing Worker'),
    ('Loading Worker', 'Loading Worker'),
    ('Unloading Worker', 'Unloading Worker'),

    ('Lakdi Katai', 'Lakdi Katai'),
    ('Lakdi Loading', 'Lakdi Loading'),

    ('Tractor Driver', 'Tractor Driver'),
    ('Harvester Operator', 'Harvester Operator'),
    ('Rotavator Operator', 'Rotavator Operator'),

    ('Spraying Worker', 'Spraying Worker'),
    ('Fertilizer Worker', 'Fertilizer Worker'),
    ('Seed Sowing Worker', 'Seed Sowing Worker'),

    ('Irrigation Worker', 'Irrigation Worker'),
    ('Borewell Helper', 'Borewell Helper'),

    ('Mandi Loading Worker', 'Mandi Loading Worker'),
    ('Mandi Unloading Worker', 'Mandi Unloading Worker'),

    ('Farm Labour', 'Farm Labour'),
    ('General Labour', 'General Labour'),

]
    
    owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    name = models.CharField(max_length=100)

    skill = models.CharField(
        max_length=50,
        choices=SKILL_CHOICES
    )

    image = models.ImageField(
        upload_to='worker_images/',
        blank=True,
        null=True
    )

    mobile = models.CharField(max_length=15)

    location = models.CharField(max_length=100)

    experience = models.IntegerField()

    wage_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available = models.BooleanField(default=True)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name    
    
class WorkerBooking(models.Model):

    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(
        max_length=100
    )

    mobile = models.CharField(
        max_length=15
    )

    village = models.CharField(
        max_length=100
    )
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    work_date = models.DateField()

    days_required = models.IntegerField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    booking_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.customer_name   
    
class WorkerHireRequest(models.Model):

    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE
    )

    farmer_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    village = models.CharField(max_length=100)

    work_date = models.DateField()

    days = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending','Pending'),
            ('Accepted','Accepted'),
            ('Rejected','Rejected')
        ],
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.farmer_name} - {self.worker.name}"    
    
class Transport(models.Model):

    VEHICLE_CHOICES = [
        ('Pickup', 'Pickup'),
        ('Mini Truck', 'Mini Truck'),
        ('Truck', 'Truck'),
        ('Tempo', 'Tempo'),
        ('Tractor Trolley', 'Tractor Trolley'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    vehicle_name = models.CharField(max_length=100)

    vehicle_type = models.CharField(
        max_length=50,
        choices=VEHICLE_CHOICES
    )

    image = models.ImageField(
        upload_to='transport_images/',
        blank=True,
        null=True
    )

    owner_mobile = models.CharField(max_length=15)

    location = models.CharField(max_length=100)

    rent_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available = models.BooleanField(default=True)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.vehicle_name
    
class TransportBooking(models.Model):

    transport = models.ForeignKey(
        Transport,
        on_delete=models.CASCADE
    )
    
    payment_status = models.CharField(
    max_length=20,
    default='Pending'
)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    customer_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    pickup_location = models.CharField(max_length=200)

    drop_location = models.CharField(max_length=200)

    booking_date = models.DateField()

    booking_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.customer_name    
    
class FarmingGuide(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='guides/')

    content = models.TextField()

    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.title


class GovernmentScheme(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='schemes/'
    )

    description = models.TextField()

    eligibility = models.TextField()

    created_at = models.DateTimeField(
    default=timezone.now
    )

    def __str__(self):
        return self.title


class DailyTip(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    created_at = models.DateTimeField(
    default=timezone.now
    )

    def __str__(self):
        return self.title


class EducationVideo(models.Model):

    title = models.CharField(max_length=200)

    youtube_link = models.URLField()

    created_at = models.DateTimeField(
    default=timezone.now
    )

    def __str__(self):
        return self.title     
class MandiPrice(models.Model):

    crop_name = models.CharField(
        max_length=100,
        default="Wheat"
    )

    mandi_name = models.CharField(
        max_length=100,
        default="Harsud"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )


class AgricultureNews(models.Model):

    title = models.CharField(max_length=300)

    description = models.TextField()

    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.title 

