from django.core.management.base import BaseCommand
from uzhavankart.models import Employee
from datetime import date

class Command(BaseCommand):
    help = 'Seed a specific employee into the database'

    def handle(self, *args, **options):
        # Data provided by the user
        emp_data = {
            'emp_id': 'SKUKA01',
            'name': 'Balaji S',
            'dob': date(2004, 7, 3),
            'gender': 'M',  # Converting 'Male' to 'M' based on GENDER_CHOICES in models.py
            'mobile_no': '8838818193',
            'address': 'Chennai',
            'job_role': 'ADMIN',
            'photo': 'employee_photos/balaji.jpg'  # Updated to match model's upload_to
        }

        obj, created = Employee.objects.get_or_create(
            emp_id=emp_data['emp_id'],
            defaults=emp_data
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Successfully created employee: {obj.name} ({obj.emp_id})"))
        else:
            self.stdout.write(self.style.WARNING(f"Employee {obj.emp_id} already exists."))
