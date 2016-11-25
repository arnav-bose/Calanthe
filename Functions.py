import math
import pandas


def maxValue(a, b):
    if a > b:
        return a
    else:
        return b


def sumOfSquares(list):
    sum = 0
    for i in list:
        sum += math.pow(i, 2)

    return sum


def squareOfSum(list):
    sum = 0
    for i in list:
        sum += i

    return math.pow(sum, 2)


def productOfRatings(listA, listB):
    listAB = []
    for i in zip(listA, listB):
        listAB.append(i[0] * i[1])

    return listAB


def sumOfList(list):
    sum = 0
    for i in list:
        sum += i

    return sum


def similarityPearson(listRatingUserA, listRatingUserB):
    # Calculating the least Size of List
    size = maxValue(len(listRatingUserA), len(listRatingUserB))

    # Calculating the Sum of Squares of both lists
    sumOfSquaresUserA = sumOfSquares(listRatingUserA)
    sumOfSquaresUserB = sumOfSquares(listRatingUserB)

    # Calculating the Square of Sums of both lists
    squareOfSumUserA = squareOfSum(listRatingUserA)
    squareOfSumUserB = squareOfSum(listRatingUserB)

    # Calculating product of Ratings A and Ratings B
    listProductRatingsAB = productOfRatings(listRatingUserA, listRatingUserB)

    # Calculating the sum of Product of Ratings A and Ratings B
    sumOfProductsRatingsAB = sumOfList(listProductRatingsAB)

    # Calculating the sum of User A Ratings
    sumOfRatingsUserA = sumOfList(listRatingUserA)
    sumOfRatingsUserB = sumOfList(listRatingUserB)

    numerator = sumOfProductsRatingsAB - ((sumOfRatingsUserA * sumOfRatingsUserB) / size)

    denominator = math.pow(sumOfSquaresUserA - (squareOfSumUserA / size), 0.5) * math.pow(
        sumOfSquaresUserB - (squareOfSumUserB / size), 0.5)

    return numerator / denominator


def extractUserListFromCSV():
    with open('ratings.csv', 'r') as file:
        column = pandas.read_csv(file)
        return column.userId


def extractRatingsListFromCSV():
    with open('ratings.csv', 'r') as file:
        column = pandas.read_csv(file)
        return column.rating


listUser = extractUserListFromCSV()
listRatings = extractRatingsListFromCSV()


def listOfRatingsByUserID(id):
    listA = []
    for i in zip(listUser, listRatings):
        if i[0] == id:
            listA.append(i[1])

    return listA


listA = listOfRatingsByUserID(13)
listB = listOfRatingsByUserID(23)

print(similarityPearson(listA, listB))



# listA = [18, 25, 57, 45, 26, 64, 37, 40, 24, 33]
# listB = [15000, 29000, 68000, 52000, 32000, 80000, 41000, 45000, 26000, 33000]
#
# print(similarityPearson(listA, listB))
