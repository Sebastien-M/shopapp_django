import requests


class CustomerService():

    def getallcustomers(self):
        url = 'http://localhost:8001/crm/api/customers'
        req = requests.get(url)
        customers = req.json()
        return customers

    def getonecustomer(self, customer_id):
        url = 'http://localhost:8001/crm/api/customers/id={}'.format(customer_id)
        req = requests.get(url)
        customer = req.json()
        return customer

    def getallcontracts(self):
        url = 'http://localhost:8001/crm/api/contracts'
        req = requests.get(url)
        contracts = req.json()
        return contracts

    def getonecontract(self):
        pass

    def getcustonercontract(self, customer_id):
        url = 'http://localhost:8001/crm/api/contracts/customer_id={}'.format(customer_id)
        req = requests.get(url)
        contracts = req.json()
        return contracts
