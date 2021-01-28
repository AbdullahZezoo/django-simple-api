from .models import Account, Loans, Offers

Lenme_fee = 3
#
def check_balance(annual_rate, loan_id, investor_id):
    investor = Account.objects.get(pk=investor_id)
    loan = Loans.objects.get(pk=loan_id)

    total_amount = Lenme_fee + loan.amount
    balance = investor.balance

    if total_amount <= balance:
        return True
    return False

def accept_offer(loan_id, offer_id):
    # both offer, loan status should be Funded
    #  other offers should by Closed
    loan = Loans.objects.get(pk=loan_id)
    offer = Offers.objects.get(pk=offer_id)

    loan.status = "Funded"
    offer.status = "Funded"

    return loan, offer

def complete_payments():
    # both offer, loan status should be Completed
    return