from django.contrib import admin
from django.urls import path, include
from service import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Service Request API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('customerclick', views.customerclick_view),
    path('offersclick', views.offersclick_view),

    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('offersignup', views.offer_signup_view,name='offersignup'),

    path('customerlogin', LoginView.as_view(template_name='service/customerlogin.html'),name='customerlogin'),
    path('adminlogin', LoginView.as_view(template_name='service/adminlogin.html'),name='adminlogin'),



    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-customer', views.admin_customer_view,name='admin-customer'),
    path('admin-view-customer',views.admin_view_customer_view,name='admin-view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('admin-add-customer', views.admin_add_customer_view,name='admin-add-customer'),
    path('admin-view-customer-enquiry', views.admin_view_customer_enquiry_view,name='admin-view-customer-enquiry'),
    path('admin-view-customer-invoice', views.admin_view_customer_invoice_view,name='admin-view-customer-invoice'),


    path('admin-request', views.admin_request_view,name='admin-request'),
    path('admin-view-request',views.admin_view_request_view,name='admin-view-request'),
    path('change-status/<int:pk>', views.change_status_view,name='change-status'),
    path('admin-delete-request/<int:pk>', views.admin_delete_request_view,name='admin-delete-request'),
    path('admin-add-request',views.admin_add_request_view,name='admin-add-request'),
    path('admin-approve-request',views.admin_approve_request_view,name='admin-approve-request'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    
    path('admin-view-service-cost',views.admin_view_service_cost_view,name='admin-view-service-cost'),
    path('update-cost/<int:pk>', views.update_cost_view,name='update-cost'),

    path('admin-offer', views.admin_offer_view,name='admin-offer'),
    path('admin-view-offer',views.admin_view_offer_view,name='admin-view-offer'),
    path('delete-offer/<int:pk>', views.delete_offer_view,name='delete-offer'),
    path('update-offer/<int:pk>', views.update_offer_view,name='update-offer'),
    path('admin-add-offer',views.admin_add_offer_view,name='admin-add-offer'),
    path('admin-approve-offer',views.admin_approve_offer_view,name='admin-approve-offer'),
    path('approve-offer/<int:pk>', views.approve_offer_view,name='approve-offer'),
    path('delete-offer/<int:pk>', views.delete_offer_view,name='delete-offer'),

    path('admin-feedback', views.admin_feedback_view,name='admin-feedback'),



    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customer-request', views.customer_request_view,name='customer-request'),
    path('customer-add-request',views.customer_add_request_view,name='customer-add-request'),

    path('customer-profile', views.customer_profile_view,name='customer-profile'),
    path('edit-customer-profile', views.edit_customer_profile_view,name='edit-customer-profile'),
    path('customer-feedback', views.customer_feedback_view,name='customer-feedback'),
    path('customer-invoice', views.customer_invoice_view,name='customer-invoice'),
    path('customer-view-request',views.customer_view_request_view,name='customer-view-request'),
    path('request-details/', views.get_all_enquiries, name='get_all_enquiries'),
    path('specific-request-details/<int:request_id>/', views.get_specific_request, name='get_specific_request'),
    path('customer-delete-request/<int:pk>', views.customer_delete_request_view,name='customer-delete-request'),
    #path('customer-accept-offer/<int:pk>/', views.customer_accept_offer_view, name='customer-view-approved-offers'),
    path('customer-view-approved-offers/<int:rate>/', views.customer_view_approved_offers, name='customer-view-approved-offers'),
    path('approved-offers', views.get_approved_offers_api, name='approved-offers'),
    path('customer-view-approved-request',views.customer_view_approved_request_view,name='customer-view-approved-request'),
    path('customer-view-approved-request-invoice',views.customer_view_approved_request_invoice_view,name='customer-view-approved-request-invoice'),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='service/index.html'),name='logout'),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

    path('docs', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
