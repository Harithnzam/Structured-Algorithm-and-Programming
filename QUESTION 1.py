listA=[]
listB=[]
listC=[]
listD=[]
listE=[]
sumA,sumB,sumC,sumD,sumE=0,0,0,0,0
highSellingList=[]
lowSellingList=[]

#to get the money spent to serve each meals
spentMealA=eval(input("Enter how much do you spend for serving meal A : "))
spentMealB=eval(input("Enter how much do you spend for serving meal B : "))
spentMealC=eval(input("Enter how much do you spend for serving meal C : "))
spentMealD=eval(input("Enter how much do you spend for serving meal D : "))
spentMealE=eval(input("Enter how much do you spend for serving meal E : "))
print("="*50)

#to get each meals sold in the first 5 days
for i in range(1,6):
    mealA = int(input("Meal A sold on day %d : "%i))
    listA.append(mealA)
    mealB = int(input("Meal B sold on day %d : "%i))
    listB.append(mealB)
    mealC = int(input("Meal C sold on day %d : "%i))
    listC.append(mealC)
    mealD = int(input("Meal D sold on day %d : "%i))
    listD.append(mealD)
    mealE = int(input("Meal E sold on day %d : "%i))
    listE.append(mealE)
    print("\n","-"*40,"\n")

#to get the total of each meals sold
for i in range(0,5):
    sumA += listA[i]
    sumB += listB[i]
    sumC += listC[i]
    sumD += listD[i]
    sumE += listE[i]

#to calculate the profit for each meals
profitA=sumA*(3.50-spentMealA)
profitB=sumB*(5.50-spentMealB)
profitC=sumC*(8.50-spentMealC)
profitD=sumD*(6.50-spentMealD)
profitE=sumE*(4.80-spentMealE)

#to separate the meals status either top selling meals or low selling meals
if profitA>=100:
    highSellingList.append("Meal A")
if profitB>=100:
    highSellingList.append("Meal B")
if profitC>=100:
    highSellingList.append("Meal C")
if profitD>=100:
    highSellingList.append("Meal D")
if profitE>=100:
    highSellingList.append("Meal E")
if profitA <=50:
    lowSellingList.append("Meal A")
if profitB <=50:
    lowSellingList.append("Meal B")
if profitC <=50:
    lowSellingList.append("Meal C")
if profitD <=50:
    lowSellingList.append("Meal D")
if profitE <=50:
    lowSellingList.append("Meal E")

#datas that will be shown
print("The total meal A sold is %d"%sumA)
print("The total meal B sold is %d"%sumB)
print("The total meal C sold is %d"%sumC)
print("The total meal D sold is %d"%sumD)
print("The total meal E sold is %d"%sumE)
print()
print("Top Selling Meals :",highSellingList)
print("Low Selling Meals :",lowSellingList)
