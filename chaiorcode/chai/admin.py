from django.contrib import admin
from .models import ChaiVarity, ChaiCertificate, ChaiReview, Store

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities', )

class ChaiCertificateAdmin(admin.ModelAdmin):    
    list_display = ('chai', 'issued_date', 'valid_until')

admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
admin.site.register(ChaiReview)
admin.site.register(Store, StoreAdmin)
