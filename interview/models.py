from django.db.models import Model, UUIDField, CharField, EmailField, URLField, DateTimeField, ManyToManyField
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Participant(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email = EmailField(max_length=240, unique=True)
    phone = PhoneNumberField(null=True, blank=True)
    resume = URLField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.id)[-12:]} {self.first_name} {self.email}"


class Interview(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=100)
    start_time = DateTimeField()
    end_time = DateTimeField()
    participants = ManyToManyField(Participant, related_name="interviews", related_query_name="interview")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_time']

    @property
    def duration(self):
        return (self.end_time - self.start_time).total_seconds()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"