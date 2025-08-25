# ------------------- Day 6: Advanced Error Handling & Custom Exceptions -------------------

# ✅ Basic Try-Except
try:
    x = int("abc")  # invalid conversion
except ValueError as e:
    print("Error:", e)

# ✅ Using else
try:
    num = int("10")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful:", num)

# ✅ Using finally
try:
    f = open("test.txt", "w")
    f.write("Hello")
except IOError:
    print("File error")
finally:
    f.close()
    print("File closed safely")

# ✅ Raising Exceptions Manually
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

print(withdraw(100, 50))   # OK
# print(withdraw(100, 150))  # Raises exception

# ✅ Custom Exception Classes
class InsufficientBalanceError(Exception):
    """Custom exception for balance errors"""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance to withdraw!")
    return balance - amount

try:
    print(withdraw(100, 150))
except InsufficientBalanceError as e:
    print("Transaction failed:", e)

# ✅ Real-World ATM Example
class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be greater than zero!")
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance!")
    return balance - amount

try:
    balance = 1000
    amount = int(input("Enter withdrawal amount: "))
    balance = withdraw(balance, amount)
    print("Withdrawal successful. Remaining balance:", balance)
except (InsufficientBalanceError, InvalidAmountError) as e:
    print("Transaction failed:", e)
finally:
    print("Thank you for using our ATM service!")

# ------------------- Exercises -------------------
# 1. Division program with zero check
# 2. Age input program raising ValueError
# 3. BankAccount class with deposit/withdraw + custom exceptions
# 4. File Reader Utility handling FileNotFoundError
