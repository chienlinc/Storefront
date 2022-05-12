from django.urls import path

from .views import (product_list_view,
                    product_create_view, 
                    dynamic_lookup_view, 
                    product_delete_view,
                    product_update_view,
                    )

app_name = 'products'
urlpatterns = [
    path("", product_list_view, name='plist'),
    path("<int:id>/", dynamic_lookup_view, name='product'),
    path("create/", product_create_view, name='create'),
    path("<int:id>/delete/", product_delete_view, name='delete'),
    path("<int:id>/update/", product_update_view, name='update'),
]