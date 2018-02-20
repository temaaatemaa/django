from django.contrib import admin
from .models import FullTable
from .models import Priority
from .models import Systems
from .models import Time
from .models import Users

admin.site.register(FullTable)
admin.site.register(Priority)
admin.site.register(Systems)
admin.site.register(Time)
admin.site.register(Users)
