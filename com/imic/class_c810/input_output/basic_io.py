
#n = input("Nhap so nguyen tu 1 toi 10: ");  #Get data from Terminal/System
#print(int(n) + 10)                          #Show data to Terminal/System
print("reading from file... and get sum of Ages")
fNumber = open("../../../../data/ages.txt", mode='r')

ages = fNumber.readlines()
print(ages)

ages = map(lambda x: int(x), ages)
ages = list(ages)
print(ages)


total = sum(ages)
print(total)

fNumber.close()