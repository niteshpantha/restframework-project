from django.contrib import admin
from .models import User , ProductType, Product, Order,Design
# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","user"]
    list_display_links = ["__str__",]

    class Meta:
        model = User
    




class ProductTypeModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","Type",
                    "created_date", "updated_date"]
    list_display_links = ["__str__","Type"]
    list_filter = ["Type"]

    class Meta:
        model = ProductType




class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","name","product_type",
                    "created_date", "updated_date","available_sizes","available_colors"]
    list_display_links = ["__str__"]
    list_filter = ["name"]

    class Meta:
        model = Product



class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","ordered_date","user",
                "status", "size","color"]
    list_display_links = ["__str__"]
    list_filter = ["user"]

    class Meta:
        model = Order   

class DesignModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","file","created_date",
                "updated_date"]
    list_display_links = ["__str__"]
    list_filter = ["file"]

    class Meta:
        model = Design   

admin.site.register(User, UserModelAdmin)
admin.site.register(ProductType, ProductTypeModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Order, OrderModelAdmin)
admin.site.register(Design, DesignModelAdmin)