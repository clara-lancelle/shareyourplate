"""
URL configuration for shareyourplate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import recipes.views
import handler.views
from django.contrib.auth.views import LoginView, PasswordChangeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', LoginView.as_view(
                    template_name='authentication/login.html',
                    redirect_authenticated_user=True), 
                    name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('logout/', authentication.views.UserLogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
                                success_url='done/',
                                template_name='authentication/change_password.html'),
                                name='change-password'),
    path('change-password/done/', authentication.views.UserPasswordChangeDoneView.as_view(),
                                    name='change-password-done'),
    path('profile-photo/upload/', authentication.views.upload_profile_photo, name='profile_photo_upload'),
    path('home/', recipes.views.home, name='home'),
    path('recipe/create', recipes.views.recipe_create, name='recipe-create'),
    path('recipe/<int:recipe_id>/view', recipes.views.recipe_view, name='recipe-view'),
    path('recipe/<int:recipe_id>/edit', recipes.views.recipe_edit, name='recipe-edit'),
    path('recipes/<int:account_id>/feed', recipes.views.recipes_feed, name='recipes-feed'),
    path('recipes/all', recipes.views.recipes_all, name='recipes-all'),
    path('follow-users', recipes.views.follow_users, name='follow-users'),
    path('search/', recipes.views.search_page, name='search'),
]
# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handling the 404 error
# handler404 = 'handler.views.error_404'