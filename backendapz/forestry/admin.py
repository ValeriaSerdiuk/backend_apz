from django.contrib import admin

from django.contrib import admin
from .models import Forestry
from .models import Animal
from .models import Feeder
from .models import Vaccination


admin.site.register(Forestry)
admin.site.register(Animal)
admin.site.register(Feeder)
admin.site.register(Vaccination)

