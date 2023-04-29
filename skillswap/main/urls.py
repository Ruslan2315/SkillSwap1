from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
