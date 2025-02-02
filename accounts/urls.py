from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Vista de login usando la vista genérica de Django
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Vista de logout (redirige a la página de login al cerrar sesión)
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]

from .views import edit_profile

urlpatterns = [
    path('edit-profile/', edit_profile, name='edit_profile'),
]