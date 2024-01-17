from django.contrib import admin
from .models import UserProfile, Ticket, AdminProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_department')
    search_fields = ('user__username', 'user__email',)

    def get_department(self, obj):
        related_ticket = Ticket.objects.filter(user=obj.user).first()
        if related_ticket:
            return related_ticket.department_name
        return "N/A"

    get_department.short_description = 'Department'

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'department_name', 'request_type', 'status', 'created_at',)
    list_filter = ('status', 'department_name', 'created_at',)
    date_hierarchy = 'created_at'
    search_fields = ('name', 'last_name', 'department_name', 'request_type', 'description',)

@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email',)
