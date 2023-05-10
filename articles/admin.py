from django.contrib import admin

from .models import Student, Curse, Product, Company, Person, Category, Post

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','bron','locic','age')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Person, PersonAdmin)
#admin.site.register(Category, CategoryAdmin)
admin.site.register(Student)
admin.site.register(Curse)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Post)




