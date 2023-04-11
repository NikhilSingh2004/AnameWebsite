from django.contrib import admin
from home.models import Candels , ResignArt , Order

class CandelsAdmin(admin.ModelAdmin):
    list_display = ('product_title','product_dis','product_price','product_image','product_name')

class ResignArtAdmin(admin.ModelAdmin):
    list_display = ('product_title','product_dis','product_price','product_image','product_name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_no','first_name','last_name','email','phone_number','country','address_1','address_2','state','district','town','quantity','zip_code','payment_done')

admin.site.register(Candels,CandelsAdmin)
admin.site.register(ResignArt,ResignArtAdmin)
admin.site.register(Order,OrderAdmin)
