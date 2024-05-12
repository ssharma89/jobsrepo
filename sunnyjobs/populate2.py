import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')
import django
django.setup()
from testapp.models import BangJobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    d1 = randint(6,9)
    num = '' + str(d1)
    for i in range(9):
        num+= str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibilty = fake.random_element(elements=('B.Tech','MCA','M.Tech','Ph.D','B.Com'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        bang_jobs_record = BangJobs.objects.get_or_create(
        date = fdate,
        company = fcompany,
        title = ftitle,
        eligibility = feligibilty,
        address = faddress,
        email = femail,
        phonenumber = fphonenumber
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted Successfully.....')