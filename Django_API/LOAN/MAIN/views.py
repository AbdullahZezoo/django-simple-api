from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .controller import check_balance
from .models import Account, Loans, Offers
from .serializations import AccountSerializer, LoansSerializer, OffersSerializer

# Create your views here.

@api_view(['GET'])
def login(request, email, password):
    try:
        account = Account.objects.get(email=email, password=password)
    except Account.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return JsonResponse(serializer.data)


@api_view(['GET', 'POST'])
def manage_accounts(request):
    if request.method == 'GET':

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'DELETE', 'PUT'])
def manage_account(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(account, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        account.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def user_loans(request, id):
    if request.method == 'GET':

        user_loans = []
        loans = Loans.objects.all()
        for loan in loans:
            if str(loan.owner) == str(id):
                user_loans.append(loan)

        serializer = LoansSerializer(user_loans, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data["owner"] = id   # foreign key for Account
        data["status"] = "Waiting"  # create a loan request
        serializer = LoansSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def get_waiting_loans(request):
    if request.method == 'GET':
        loans = Loans.objects.all()

        _loans = []
        for loan in loans:
            if str(loan.status) == "Waiting":
                _loans.append(loan)
        serializer = LoansSerializer(_loans, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST', 'GET', 'DELETE', 'PUT'])
def manage_loan(request, pk):
    try:
        loan = Loans.objects.get(pk=pk)
    except Loans.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        serializer = LoansSerializer(loan)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LoansSerializer(loan, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        loan.delete()
        return HttpResponse(status=204)

@api_view(['GET'])
def get_offers(request):
    if request.method == 'GET':
        offers = Offers.objects.all()
        serializer = OffersSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_offers_byLOAN(request, id):
    if request.method == 'GET':
        offers = Offers.objects.get(loan=id)
        serializer = OffersSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)



@api_view(['POST'])
def manage_offers(request, investor_id, loan_id):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data["investor"] = investor_id
        data["loan"] = loan_id
        data["status"] = "Waiting"

        serializer = OffersSerializer(data=data)

        if check_balance(data["annual_rate"], data["loan"], data["investor"]):
            if serializer.is_valid():
                serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST', 'GET', 'DELETE', 'PUT'])
def manage_offer(request, pk):
    try:
        offer = Offers.objects.get(pk=pk)
    except Offers.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OffersSerializer(offer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OffersSerializer(offer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        offer.delete()
        return HttpResponse(status=204)

