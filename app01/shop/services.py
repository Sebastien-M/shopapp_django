import requests


class CustomerService():

    def getallcustomers(self):
        url = 'http://localhost:8001/crm/api/customers'
        req = requests.get(url)
        customers = req.json()
        return customers

    def getonecustomer(self, id):
        pass

    def getallcontracts(self):
        pass

    def getonecontract(self):
        pass