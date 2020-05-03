from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='books api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doc/', schema_view),
    path('account/', include('account.urls')),
    path('book/', include('book.urls')),
    path('order/', include('order.urls')),
    
]
