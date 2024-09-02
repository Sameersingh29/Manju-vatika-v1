from django.db import models

# Choices for the event type and status fields
EVENT_CHOICES = (
    ('Wedding', 'WEDDING'),
    ('Engagement', 'ENGAGEMENT'),
    ('Birthday', 'BIRTHDAY'),
    ('Conference(Corporate meeting)', 'CONFERENCE'),
    ('Anniversary', 'ANNIVERSARY'),
    ('Other', 'OTHER'),
)

STATUS_CHOICES = (
    ('Pending', 'PENDING'),
    ('Confirmed', 'CONFIRMED'),
    ('Rejected', 'REJECTED')
)

# Enquiry model
class Enquiry(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=10)
    event_date = models.DateField()
    guest_count = models.PositiveIntegerField()
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    comments = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        unique_together = ('email', 'event_date')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.event_type}"

# Event model with a foreign key to Enquiry
class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name
