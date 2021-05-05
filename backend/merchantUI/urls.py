from django.urls import path
from merchantUI import views

urlpatterns = [
    path("", views.merchantLandingPage, name="landingPage"),
    path("login/", views.loginMerchantAction, name='login'),
    path("register/", views.registerMerchantAction, name='register'),
    path("itemUpload/", views.itemUploadPage, name='itemUpload'),
    path('logout/', views.logoutAction, name='logout'),
]
