from .models import Company, Sneakers
from django.contrib import admin


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Sneakers)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'slug',
                    'price',
                    'available',
                    'created_at',
                    'updated_at',
                    ]
    list_filter = ['available',
                   'created_at',
                   'updated_at',
                   ]
    list_editable = ['price',
                     'available',
                     ]
    prepopulated_fields = {'slug': ('name', )}
