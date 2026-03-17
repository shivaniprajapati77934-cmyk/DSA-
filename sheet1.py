#code 1 to check whether a number is prime or not

def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
num=int(input("enter number:"))
print(prime(num))

#code 2 generate pythagorean triplets
limit= int(input("enter limit:"))

for a in range(1,limit):
    for b in range(a,limit):
        for c in range(b,limit):
            if a*a + b*b==c*c:
                print(a,b,c)

#code 3 maximum marks in each semester 
sem = int(input("Enter number of semesters: "))

for i in range(1, sem+1):
    subjects = int(input(f"Enter number of subjects in semester {i}: "))
    
    marks = list(map(int, input(f"Enter marks for semester {i}: ").split()))
    
    invalid = False
    for m in marks:
        if m < 0 or m > 100:
            print("You have entered invalid mark")
            invalid = True
            break
    
    if not invalid:
        print(f"Maximum mark in semester {i}: {max(marks)}")
# code 4 solve expression
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result = a**3 + a**2*b + 2*a**2*b + 2*a*b**2 + a*b**2 + b**3

print("Result:", result)
#code 5 types of each dealership
dealerships = int(input("Enter number of dealerships: "))
total_tyres = int(input("Enter total number of tyres: "))

tyres_each = total_tyres // dealerships

print("Tyres in each dealership:", tyres_each)
#code 6 minimum discount product
n = int(input("Enter number of items: "))

min_discount = float('inf')
min_item = ""

for i in range(n):
    data = input("Enter item,price,discount%: ").split(",")
    
    item = data[0]
    price = int(data[1])
    discount = int(data[2])

    discount_amount = (price * discount) / 100

    if discount_amount < min_discount:
        min_discount = discount_amount
        min_item = item

print("Item with minimum discount:", min_item)

