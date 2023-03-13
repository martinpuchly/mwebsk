from django.contrib import admin
from .models import Contact
from django.utils.html import format_html


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'read_over')
    fields = ('subject', 'email', 'message', 'read_over')
    readonly_fields=('subject', 'email', 'message')

    def has_add_permission(self, request, obj=None):
        return False

    def contact_link(self,obj):
        return u'<a href="/foos/%s/">%s</a>' % (obj.foo,obj)