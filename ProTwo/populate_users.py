import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')

import django
django.setup()


from appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_fisrt_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()


        user = User.objects.get_or_create(fisrt_name=fake_fisrt_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]



if __name__=='__main__':
    print('POPULATING databases')
    populate(20)
    print('complete!')
