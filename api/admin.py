from django.contrib import admin
from .models import Certificate, Institution, Learner,Employer,User

# Register your models here.
admin.site.register(User)
admin.site.register(Institution)
admin.site.register(Learner)
admin.site.register(Employer)
admin.site.register(Certificate)
