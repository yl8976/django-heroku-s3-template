from django.contrib import admin

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["document", "description"]}),
        ("Date Information", {"fields": ["uploaded_at"], "classes": ["collapse"]}),
    )

    list_display = ("document", "description", "uploaded_at", "id")
    list_filter = ["uploaded_at"]
    search_fields = ["document", "description"]


admin.site.register(Document, DocumentAdmin)

