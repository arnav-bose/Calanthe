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

def extractAllFromCSV():
    with open('ratings.csv', 'r') as file:
        column = pandas.read_csv(file)
        listRatings = column.rating
        listUsers = column.userId
        listMovieIDs = column.movieId

        return listRatings, listUsers, listMovieIDs


listUser = extractUserListFromCSV()
listRatings = extractRatingsListFromCSV()


def listOfRatingsByUserID(id):
    listA = []
    for i in zip(listUser, listRatings):
        if i[0] == id:
            listA.append(i[1])

    return listA


listA = listOfRatingsByUserID(4)
# listB = listOfRatingsByUserID(3)
listSimilarToA = []

print("Finding Similarities...")
for i in range(1, 671):
    listSimilarToA.append([similarityPearson(listA, listOfRatingsByUserID(i)), i])

print("Done!\nFinding top 20 matches...")

# print(listSimilarToA)

top20NearestNeighbours = sorted(listSimilarToA, reverse = True)
top20NearestNeighbours = top20NearestNeighbours[1:21]
top20NearestNeighboursUsers = []

def getUsersTop20(top20NearestNeighbours):
    for i in top20NearestNeighbours:
        top20NearestNeighboursUsers.append(i[1])
    return top20NearestNeighboursUsers

print(top20NearestNeighbours)
listTop20NearestNeighboursUsers = getUsersTop20(top20NearestNeighbours)

def getListOfTopUsers(listTop20NearestNeighbourUsers):
    list = []
    for i in listTop20NearestNeighbourUsers:
        list.append(listOfRatingsByUserID(i))

    return list
# print(heapq.nlargest(20, (random.gauss(0, 1) for _ in range(len(listSimilarToA)))))
print("Done!")

print("Prediction Computation...")

def getListofItemRatingsByItem(listtop20NearestNeighboursUserID, itemNumber):
    r, u, m = extractAllFromCSV()
    listRatings = []
    for i in zip(r, u, m):
        if i[1] in listtop20NearestNeighboursUserID and i[2] == itemNumber:
            listRatings.append(i)

    return listRatings

prediction = (sumOfList(listOfRatingsByUserID(1))/len(listOfRatingsByUserID(1))) + (sumOfList(getListofItemRatingsByItem(listTop20NearestNeighboursUsers, 1029)) / len(getListofItemRatingsByItem(listTop20NearestNeighboursUsers, 1029))) - (sumOfList(getListOfTopUsers(listTop20NearestNeighboursUsers)) / len(getListOfTopUsers(listTop20NearestNeighboursUsers)))
print(prediction)

# listA = [18, 25, 57, 45, 26, 64, 37, 40, 24, 33]
# listB = [15000, 29000, 68000, 52000, 32000, 80000, 41000, 45000, 26000, 33000]
#
# print(similarityPearson(listA, listB))
