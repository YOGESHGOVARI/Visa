from django.contrib import admin
from details.models import Details
from details.models import A_Details
class DetailsAdmin(admin.ModelAdmin):

    list_display=('uname','passw')
admin.site.register(Details,DetailsAdmin)

class Details_A(admin.ModelAdmin):

    list_display=('uname1','passw1')
admin.site.register(A_Details,Details_A)
# Register your models here.
