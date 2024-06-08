from django.contrib import admin
from myapp.models import  laptop,accessories,Signuptable,Carttable,newproducts,Billtable
# Register your models here.

admin.site.register( laptop)
admin.site.register(accessories)
admin.site.register(Signuptable)
admin.site.register(Carttable)
admin.site.register(newproducts)
admin.site.register(Billtable)

