"""
Créer une classe BankAccount().
Le constructeur de cette classe initialisera deux attributs: name et balance,
avec les valeurs par défaut 'John' et 1000.
Implémenter 3 méthodes :
    - deposit : qui permet de déposer une somme
    - withdrawal : qui permet de retirer une somme
    - display : qui permet d'afficher le nom du titulaire du compte, 
                ainsi que son solde.

Instancier deux comptes différents, et réaliser des opérations dessus.


"""
class BankAccount():
    def __init__(self, name:str='John', balance:float=1000):
        self.name = name
        self.balance = balance

    def deposit(self, amount:float):
        self.balance += amount

    def withdrawal(self, amount:float):
        if self.balance < amount:
            print('Not enough money...')
            return

        self.balance -= amount

    def __str__(self):
        return f"Name : {self.name} Balance : {self.balance}"  


savings_account = BankAccount('savings', 5470.70)
current_account = BankAccount('current', 845.65)

savings_account.deposit(500)
print(savings_account)

current_account.withdrawal(918.20)
current_account.withdrawal(310)
print(current_account)



"""
Créer une classe SavingsAccount(), dérivant de la class BankAccount() importée,
qui permette de créer des comptes d'épargne rapportant un certain intérêt au cours du temps.
Pour simplifier, nous admettrons que ces intérêts sont calculés tous les mois.

Le constructeur de votre nouvelle class devra initialiser un taux d'intérêt mensuel
(monthlyInterestRate) par défaut égal à 0,3%

Une méthode set_rate devra permettre de modifier ce taux à volonté. 
Une méthode capitalisation(monthNumber) devra :
Afficher le nombre de mois et le taux d'intérêt pris en compte.
Calculer le solde atteint en capitalisant les intérêts composés,
pour le taux et le nombre de mois qui auront été choisis. 


"""
class SavingsAccount(BankAccount):
    def __init__(self, name:str='John', balance:float=1000, monthlyInterestRate=0.3):
        BankAccount.__init__(self, name, balance)
        self.monthlyInterestRate = monthlyInterestRate / 100

    def set_rate(self, monthlyInterestRate):
        self.monthlyInterestRate = monthlyInterestRate / 100

    def capitalization(self, month_number):
        self.balance *= (1 + self.monthlyInterestRate) ** month_number
        print(self)

    def __str__(self):
        return f"Name : {self.name} Balance : {self.balance} Rate : {self.rate}"

    def __gt__(self, other):
        return self.solde > other.solde


s_account = SavingsAccount()
s_account.deposit(300)
s_account.capitalization(12)