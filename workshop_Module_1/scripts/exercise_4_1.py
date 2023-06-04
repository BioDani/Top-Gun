from datetime import datetime
import uuid

class BankAccount():
    
    def __init__(self,
                 customer_id: str,
                 balance: float = 0):
        
        self.account_id  = uuid.uuid4()
        self.opening_date = datetime.now()
        self.customer_id = customer_id
        self.balance = balance
        self.transactions = list()
        
    def depositing(self, amount: float):
        self.balance += amount
        self.new_transaction(type_transaction= 'Deposit',amount= amount)
        return f'Desposit for $ {amount} USD'
    
    def withdrawing(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            self.new_transaction(amount= -amount, type_transaction= 'Withdrawl')
            return f'Withdrawl for $ {amount} USD'
        return 'Not enough funds to complete this transaction.'
    
    def new_transaction(self, amount: float, type_transaction: str):
        new = {
            'date': datetime.now(),
            'type': type_transaction,
            'amount': amount
        }
        self.transactions.append(new)
        
    def checking_balance(self):
        return {
            'Account' : self.account_id,
            'Enquiery date': datetime.now(),
            'Balance account': f'$ {self.balance} USD'
        }

def main():
    account_1 = BankAccount(customer_id='12345', balance= 1000)
    print(account_1.depositing(700))
    print(account_1.depositing(100))
    print(account_1.withdrawing(50))
    print(account_1.withdrawing(2500))
    
if __name__ == '__main__':
    main()