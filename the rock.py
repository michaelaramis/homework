def happy_aniversary(name, time):
    print("Happy Anniversary {Josh and Nessa}}!")
    print(f"You guys have been together for {5} years!")
    print("Happy Anniversary!")
    print()

happy_aniversary("Josh and Nessa", "5 years")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("JoeSchmo", 100.01, "01/02")

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z  

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print(add(3, 1))
print(subtract(-1, 2))
print(multiply(2, 2))
print(divide(1, 2))
