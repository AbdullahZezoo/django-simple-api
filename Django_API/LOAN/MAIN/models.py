from django.db import models

# Create your models here.



class Account(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    balance = models.FloatField()

    def __str__(self):
        return str(self.id)

class Loans(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    amount = models.FloatField()
    period = models.IntegerField()
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owner')

    status = models.CharField(max_length=50)

    def __str__(self):
        return self.owner

class Offers(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    annual_rate = models.FloatField()
    investor = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='investor')
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE, related_name='loan')
    status = models.CharField(max_length=50)


    def __str__(self):
        return self.investor






