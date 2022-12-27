def hello(to="world"):
    to=to.strip().title()
    print(f"hello, {to}")

def main():
    name=input("whats your name? ")
    hello(name)

main()

#print("hello,",name)

#removendo espaço em branco de string
#name=name.strip()
#deixando a primeira letra em caixa alta
#name=name.title()
#we can also use
#name=name.strip().title()
#first,second= name.split(" ")
#f antes de '' é sinalização para substituir variavel
#print(f'hello {first}')
