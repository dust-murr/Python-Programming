def getKilometers():
    kilometers = float(input("Please enter a distance in kilometers: "))
    return kilometers

def convertKilometers2Miles(kilometers):
    MILES_PER_KILOMETERS = 0.6214
    miles = kilometers * MILES_PER_KILOMETERS
    return miles

def reportResults(kilometers, miles):
    print(kilometers, "kilometers is", miles, "miles")

def main():
    kilometers = getKilometers()
    miles = convertKilometers2Miles(kilometers)
    reportResults(kilometers, miles)

main()
