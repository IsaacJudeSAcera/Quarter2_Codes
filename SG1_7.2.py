dist=float(input("Enter distance in kilometers: "))
rate=float(input("Enter rate per kilometer (₱): "))
def cost(dist,rate):
    total = dist*rate
    print("Total Delivery Fee: ₱",total)
print(cost(dist,rate))
