#What Ravel taught us
file = None
with open("data.csv") as data: file = data.read()

result = {}

for i in range(1, len(file.split("\n"))): #Iterate through line number
    print(i) #This print the line number
    data = file.split("\n")[i].split(",") #Create list of data of each line
    if len(data) < 3: #Skip if entry is not within length of 3
        continue #Entry always has the lenght of 3 or else it is invalid
    if data[1] in result:
        if data[0] != "NA":
            result[data[1]][0] += int(data[0])
            result[data[1]][2][data[2]] = int(data[0])
        else:
            result[data[1]][1] += 1
            result[data[1]][2][data[2]] = 0

    else:
        if data[0] != "NA":
            result[data[1]] = [int(data[0]), 0, {data[2]: data[0]}]
        else:
            result[data[1]] = [0, 1, {data[2]: 0}]

print(result)
