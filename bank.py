#creating the base class - BankAccount
class BankAccount:
    #create common attributes
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    #create common methods
    
    #adds money into the bank account
    def deposit(self, amount):
        self.balance + amount
        return f"your amount:{amount} got successfully deposited."
    
    #remove money from the bank account
    def withdraw(self, amount):
        self.balance - amount
        return f"your amount:{amount} got successfully withdrawed."
    
    #returns the current balance
    def get_balance(self):
        return f"your current balance is {self.balance}"
    
    #returns account details: account holder & account number
    def get_account_details(self):
        return f"account holder: {self.account_holder}"
        return f"account number: {self.account_number}"
       
#create derived class - SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate, periods_per_year , time_periods):
        BankAccount.__init__(self, account_number, account_holder, balance)
        self.interest_rate = interest_rate
        self.periods_per_year = periods_per_year
        self.time_periods = time_periods
        
    #applies interest rate to the balance
    def apply_interest(self):
        # P: principal
        # r: annual interest rate (as a decimal)
        # n: number of times interest is compounded per year
        # t: number of periods the money is invested for
        A = self.balance * (1 + self.interest_rate / self.periods_per_year) ** (self.periods_per_year * self.time_periods)
        return A 
    
#create derived class - CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        BankAccount.__init__(self, account_number, account_holder, balance)
        self.overdraft_limit = 200
        
    def process_check(self, check_amount):
        if self.balance >= check_amount:
            self.balance -= check_amount
            return "your check got successfully processed."
        elif self.balance + self.overdraft_limit >= check_amount:
            self.balance -= check_amount
            return "your check got successfully processed."
        else: 
            return "you are over your Overdraft Limit."
        
#create derived class - BusinessAccount
class BusinessAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, credit_limit, credit_score, existing_debt, income):
        BankAccount.__init__(self, account_number, account_holder, balance)
        self.credit_limit = credit_limit
        self.credit_score = credit_score
        self.existing_debt = existing_debt
        self.income = income
       
    #Basic Validation
    def request_loan(self, loan_amount):
        if loan_amount <= 0:
            return "Invalid loan Amount."
        
        #Check eligibility based on credit score, income, and existing debt
        if self.credit_score < 600:
            return "Loan Request Denied: Low Credit Score."
        if self.income < 2000:
            return "Loan Request Denied: Insufficient Income."
        if self.existing_debt > 10000:
            return "Loan Request Denied: High Existing Debt."
        
        # Determine maximum loan amount based on credit score and income
        max_loan = min(self.credit_score * 1000, self.income * 0.5) 
        
        #check if requested loan amount exceeds maximum allowed.
        if loan_amount > max_loan:
            return f"Loan Request Denied: Maximum Loan Amount is {max_loan}"
        
        #check if requested loan amount exceds credit limit
        if loan_amount > self.credit_limit:
            return f"Loan Request Denied: Exceeds the credit limit of {self.credit_limit}"
        
        #process loan request
        self.balance += loan_amount
        return "Loan Request Approved. Loan Amount Distributed."
    
#example usage
savings_account = SavingsAccount("1234567895", "Selffsta", 10000, 0.05, 12, 1)
savings_account.apply_interest() 

checking_account = CheckingAccount("98756", "Jill", 15000, 4000)
checking_account.process_check(16000)

business_account = BusinessAccount("45045", "Alice", 10000, 5000, 700, 2000, 5000)
print(business_account.request_loan(2500))
        


print(savings_account.deposit(200))
print(checking_account.get_balance()) 


         
        
        
        
        
        
    
    
        