from django.contrib import admin
from NykaaBackend.models import CategoryDB, ProductDB
from NykaaFrontend.models import ContactDB, RegisterDB

# Register your models here.
admin.site.register(CategoryDB)
admin.site.register(ProductDB)
admin.site.register(ContactDB)
admin.site.register(RegisterDB)

