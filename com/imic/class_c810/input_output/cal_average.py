import statistics

print("reading from file... and get sum of Ages")
fNumber = open("../../../../data/ages.txt", mode='r')
ages = fNumber.readlines()
fNumber.close()
print(ages)


#conver to number
ages = map(lambda x: int(x), ages)
ages = list(ages)
print(ages)

average = statistics.mean(ages)
print(average)
