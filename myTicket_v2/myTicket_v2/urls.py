
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('Ticket.urls')),
    path('admin/', admin.site.urls),
]
handler404 = 'myTicket_v2.views.custom_page_not_found'
handler500 = 'myTicket_v2.views.custom_server_error'
