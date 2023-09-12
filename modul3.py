a=input("Skriv in vad som helst: ")
for i in range(10):
    print(a)
x=1
while x<=10:
    print(x)
    x=x+1
y=int(input("Skriv ett tal: "))
x=1
while x<=y:
    print(x)
    x=x+1
for table in range(1,12):
    for product in range(1,11):
        print(f"Tabell {table+1}) {table+1} * {product} ={(table+1)*product}")
