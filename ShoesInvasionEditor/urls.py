from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'ShoesInvasionEditor'

urlpatterns = [
    # Home page Routing
    path('', views.login, name='login'),
    path('index', views.login, name='index'),
    path('login', views.login, name='login'),
    # User Table Route
    path('manage', views.manage, name='manage'),
    # Login API Point
    path('remove/', views.remove, name='remove'),
    path('create', views.create, name='create'), 
    path('logout/', views.logout, name='logout'),
    path('updateProduct/<str:pk>/', views.updateProduct, name='updateProduct'),
    path('twoFA', views.twoFA, name='twoFA' )
]

# For error 404 pages
handler404 = "ShoesInvasionApp.views.page_not_found_view"

# for error 500 pages
handler500 = "ShoesInvasionApp.views.server_error_view"

# for error 401 pages
handler401 = "ShoesInvasionApp.views.unauthorized_view"

# for error 502 pages
handler502 = "ShoesInvasionApp.views.bad_gateway_view"
