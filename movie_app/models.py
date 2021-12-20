from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    img = models.ImageField(upload_to='Images/%Y/%m/%d', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


CATEGORY = (
    ('P', 'Platinum'),
    ('G', 'Gold'),
    ('S', 'Silver')
)

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=CASCADE)
    # rows = models.IntegerField(default=10)
    # seatsPerRow = models.IntegerField(default=14)
    # booked_seats = models.ManyToManyField(Seat, blank=True)


class Booking(models.Model):
    payment_choice = (
        ('Credit Card', 'Credit Card'),
        ('Netbanking', 'Netbanking')
    )
    id = models.CharField(primary_key=True, max_length=200)
    timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S',null=True,blank=True)
    payment_type = models.CharField(max_length=11, choices=payment_choice,default='Credit Card')
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return str(self.id)


class Seat(models.Model):
    seat_choice = (
        ('', 'Select'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )
    no = models.CharField(max_length=3,null=True,blank=False)
    seat_type = models.CharField(max_length=8, choices=seat_choice, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('no', 'show')

    def __str__(self):
        return self.no + str(self.show)


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)