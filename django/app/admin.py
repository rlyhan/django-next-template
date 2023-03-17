from django.contrib import admin
from .models import TestModel, TestModelImage


class TestModelImageInline(admin.TabularInline):
    model = TestModelImage


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    inlines = [TestModelImageInline,]
