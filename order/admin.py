from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product',{'fields':['product'],}),
        ('Quantity',{'fields':['quantity'],}),
        ('Price',{'fields':['price'],}),
    ]
    readonly_fields = ['product','quantity','price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id','billingName')
    search_fields = ['id','billingName','emailAddress']
    # readonly_fields = [
    #     'id', 'token', 'total', 'emailAddress', 'created', 'billingName',
    #     'billingAddress1', 'billingCity', 'billingPostcode', 'billingCountry',
    #     'shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostcode',
    #     'shippingCountry'
    # ]
    readonly_fields = [
        'id', 'token', 'total', 'emailAddress', 'created', 'billingName',
        'billingAddress1', 'billingCity', 'billingPostCode', 'billingCountry',
        'shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostCode',
        'shippingCountry'
    ]
    fieldsets = [
        ('ORDER INFORMATION',{'fields': ['id','token','total','created']}),
        ('BILLING INFORMATION', {'fields': ['billingName','billingAddress1','billingCity','billingPostcode','billingCountry','emailAddress']}),
        ('SHIPPING INFORMATION', {'fields': ['shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']}),
    ]
    inlines = [
		OrderItemAdmin,
	]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
