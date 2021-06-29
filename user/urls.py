from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout_user, name='logout'),
    path('femalesignup', FemaleSignUpView.as_view(), name='female_signup'),
    path('malesignup', MaleSignUpView.as_view(), name='male_signup'),
    path('subscription/<int:pk>/', CreateSubscription, name='subscription'),

    

    path('updatesubscription/<int:pk>/', EditSubscription, name='edit_subscription'),
    path('subscriptiondetails/<int:pk>/', ViewSubscription, name='subscriptiondetails'),
    path('makepayment/<int:pk>', Payment, name='make_payment'),
    path('successpayment', SuccessPayment, name='success_payment' )


]
