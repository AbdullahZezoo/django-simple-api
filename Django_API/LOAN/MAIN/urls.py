
from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/', manage_accounts),
    path('accounts/<int:pk>', manage_account),
    path('login/<email>/<password>', login),
    path('user_loans/<int:id>', user_loans),
    path('available_loans', get_waiting_loans),
    path('loans/<int:pk>', manage_loan),
    path('offers/<int:investor_id>/<int:loan_id>', manage_offers),
    path('offers/<int:pk>', manage_offer),
    path('offers', get_offers),
    path('loan_offers/<int:id>', get_offers_byLOAN),
]
