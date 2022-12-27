'''x=float(input("whats your x?"))
y=float(input("whats your y?"))

z=round(x+y,2)
g=round(x/y,2)
print(f"A soma é {z:,} a divisão é {g}")'''

def main():
    x=int(input('whats your x?'))
    print('x squared is',square(x))

def square(num):
    return num*num

main()