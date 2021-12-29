licensesPurchased = int(input('Please enter the number of licenses purchased: '))
pricePerLicense = 99
if licensesPurchased < 10:
    discount = 0
elif licensesPurchased < 20:
    discount = 20
elif licensesPurchased < 50:
    discount = 30
elif licensesPurchased < 100:
    discount = 40
else:
    discount = 50

print('The discount percent you receive is:',discount,'%')

discountedUnitPrice = pricePerLicense - (pricePerLicense * (discount / 100.00))
print(f'The cost of one license, after the discount has been applied is: ${discountedUnitPrice:.2f}')

totalAmountPurchased = discountedUnitPrice * licensesPurchased
print(f'The total amount of the purchase after the application of the discount is: ${totalAmountPurchased:.2f}')

totalAmountSaved = pricePerLicense * licensesPurchased - totalAmountPurchased
if totalAmountSaved > 0:
    print(f'The total amount of the purchase saved due to the discount is: ${totalAmountSaved:.2f}')
