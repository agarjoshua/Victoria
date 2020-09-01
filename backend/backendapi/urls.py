from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
from . import views as core_views

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('Order', views.OrderViewSet)
router.register('Complaints', views.ComplaintsViewSet)
router.register('Stock', views.StockViewSet) 

#IMPORTS FOR LOG IN CONTROLS
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth import authenticate,logout,login
from backendapi import views as v
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home, name ='home'),
    path('accounts/login', LoginView.as_view(), name='login'),
    # path('accounts/logout', core_views.logout, {'next_page': 'logout'}, name='logout'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('accounts/signup', core_views.signup, name='signup'), 
    path('stock', views.manage_stock, name='stock'),
    path('ajax/crud/create',  views.CreateStock.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update',  views.UpdateStock.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/<int:pk>/',  views.DeleteStock.as_view(), name='crud_ajax_delete'),
    path('orders', views.manage_orders, name='orders'),

    #rest-api views
    path('rest-api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
