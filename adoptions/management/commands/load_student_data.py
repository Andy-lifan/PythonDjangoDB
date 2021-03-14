from csv import DictReader
from django.core.management import BaseCommand
from adoptions.models import Student


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the student data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from student_data.csv into our mode"

    def handle(self, *args, **options):
        if Student.objects.exists():
            print('Student data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return 
        print("Creating student data")
        
        for row in DictReader(open('./student_data.csv')):
            student = Student()            
            
            student.first_name = row['First_name']
            student.last_name = row['Last_name']
            student.contact = row['Contact']
            student.email = row['Email']
            student.age = row['Age']
            student.save()        
