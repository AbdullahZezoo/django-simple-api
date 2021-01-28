Required tools:
	-python
	-postman

install requiements:
	> pip install -r requiements

run APIs:
	> cd LOAN
	> python manage.py runserver


USE:
  server will be running in http://127.0.0.1:8000
  In postman enter the following urls:

-http://127.0.0.1:8000/accounts           -GET
-> get all accounts 
-> result example:- 
[{"name": "Abdullah", "email": "abdullah@gmail.com", "password": "1234", "balance": 50000.0}, {"name": "Ahmed", "email": "Ahmed@mail.com", "password": "123", "balance": 100000.0}, {"name": "Mohamed", "email": "Mohamed@gmail.com", "password": "123", "balance": 15000.0}]
 

-http://127.0.0.1:8000/accounts          -POST
-> post account

data in body: {"name": "Zero", "email": "Zero@gmail.com", "password": "123", "balance": 15000.0}



-http://127.0.0.1:8000/accounts/<id>     -GET
-> get account by id

-http://127.0.0.1:8000/accounts/<id>     -PUT
-> update account by id

-http://127.0.0.1:8000/accounts/<id>     -DELETE
-> delete account by id

-http://127.0.0.1:8000/user_loans/<id>     -GET
-> get list of user loans
example:-
id = 1
[{"amount": 5000.0, "period": 6, "owner": 1, "status": "Waiting"}]

-http://127.0.0.1:8000/user_loans/<id>     -POST
-> user post a loan
example:-
id = 1
{"amount": 5000.0, "period": 3, "owner": 1, "status": "Waiting"}

** id represent loan owner id and status for created loan will be Waiting


-http://127.0.0.1:8000/available_loans     -GET
-> get all Waiting loans
so you can, make offer to any of them.
example:-
[{"amount": 5000.0, "period": 6, "owner": 1, "status": "Waiting"}, {"amount": 500.0, "period": 1, "owner": 1, "status": "Waiting"}, {"amount": 500.0, "period": 1, "owner": 1, "status": "Waiting"}]


-http://127.0.0.1:8000/loans/<id>           -GET/PUT/DELETE
-> get, put, delete loan by id


-http://127.0.0.1:8000/offers/<investor_id>/<loan_id>              -GET/POST
-> get, post offer by investor_id, loan_id

example of post:-
investor_id = 1
loan_id = 1

data to post  {"annual_rate":15}

example for get with same parms:-
{"annual_rate": 15, "investor": 1, "loan": 1, "status": Waiting}



-http://127.0.0.1:8000/offers/<id>              -GET/PUT/DELETE
-> get, put, delete an offer by id


-http://127.0.0.1:8000/loan_offers/<id>              -GET
-> get all offers for this loan



** for accept offer :-
	-http://127.0.0.1:8000/loans/<id>  
	update by put loan to Funded
	{"status": "Funded"}

	# finish will put status:
	-http://127.0.0.1:8000/loans/<id>  
	update by put loan to Completed
	{"status": "Completed"}
