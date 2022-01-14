tot = int(input("Enter Number of Bananas at Starting: "))

dist = int(input("Enter Distance you want to Cover(Km): "))

camelCapacity = int(input("Enter Maximum Load Capacity of the Camel: "))

ate = 0 #(bananas being eaten by the camel)

start = tot

for i in range(dist):
    while start>0:
        start = start-camelCapacity 
        if start == 1:
            ate = ate - 1 
        
        ate = ate + 2
        
    ate = ate - 1
    start = tot- ate 
    if start == 0: 
        break
    
final = start

print(f"The Maximum Number of Bananas that can be transported by the camel at the Market Place = {final}.")