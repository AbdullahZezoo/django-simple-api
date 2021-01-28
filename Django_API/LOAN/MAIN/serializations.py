from rest_framework import serializers
from .models import Account, Loans, Offers

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('name', 'email', 'password', 'balance')

class LoansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loans
        fields = ('amount', 'period', 'owner', 'status')


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = ('annual_rate', 'investor', 'loan', 'status')