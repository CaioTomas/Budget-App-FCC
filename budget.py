import math

class Category:
    def __init__(self, name, ledger=None):
        if ledger is None:
           ledger = []
        self.ledger = ledger
        self.name = name
        
    def deposit(self, amount, description=''):
        self.ledger.append({"amount":amount, "description":description})
               
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount":-amount, "description":description})
            return True
        else:
            return False
           
    def get_balance(self):
        balance = 0
        for i in range(len(self.ledger)):
            balance += self.ledger[i].get("amount")
        
        return balance
        
    def transfer(self, amount, name):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + name.name)
            name.deposit(amount, "Transfer from " + self.name)
            
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
        
    def __str__(self):
        header = str(self.name)
        
        for i in range((30-len(self.name))//2):
            header = '*' + header + '*' 
            
        header = header + '\n'
        
        items = ''
        for i in range(len(self.ledger)):
            
            value = "{:.2f}".format(self.ledger[i].get("amount"))
        
            if len(value) > 7:
                value = value[:7]
            
            desc = str(self.ledger[i].get("description"))
            
            if len(desc) > 23:
                desc = desc[:23]
            
            spacing = (30-len(desc)-len(value))
            items = items + desc + ' '*spacing + value + '\n'
            
        foot = 'Total: ' +  "{:.2f}".format(self.get_balance())[:7]
        
        final = header + items + foot 
        return final

def create_spend_chart(categories):
    totals_by_category = dict()
    percentages = dict()
    total_spent = 0
    
    for i in range(len(categories)):
        for j in range(len(categories[i].ledger)):
            if categories[i].ledger[j].get("amount") < 0:
                total_spent += abs(categories[i].ledger[j].get("amount"))
                totals_by_category[categories[i].name] = totals_by_category.get(categories[i].name, 0) + abs(categories[i].ledger[j].get("amount"))
    
    for i in range(len(categories)):  
        percentage = (totals_by_category.get(categories[i].name)/total_spent)*100
        
        percentages[categories[i].name] = (math.floor(percentage) - math.floor(percentage)%10)
       
    header = 'Percentage spent by category'
    
    nums = ''
    for i in range(100, -10, -10):
        lst = [' ']*10
        line = ''
        line = line + ' '*(3 - len(str(i))) + str(i) + '|'
        
        for j in range(len(categories)):
            if percentages[categories[j].name] >= i:
                lst[1 + 3*j] = 'o'
                
        for i in range(len(lst)):
            line = line + lst[i]
            
        nums = nums + line + '\n'
           
    trace = '    ' + '-'*(1 + 3*len(percentages))
    
    biggest = 0
    for category in categories:
        if len(category.name) >= biggest:
            biggest = len(category.name)
    
    for category in categories:
        if len(category.name) < biggest:
            category.name = category.name + ' '*(biggest - len(category.name))
        
    foot = ''
    for j in range(biggest):
        line = '     '
        for i in range(len(categories)):
            line = line + categories[i].name[j] + '  '
        if j == biggest - 1:
            foot = foot + line
        else:    
            foot = foot + line + '\n'
     
    chart = header + '\n' + nums + trace + '\n' + foot 
    return chart