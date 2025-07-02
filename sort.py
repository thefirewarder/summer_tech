import random
list1 = []
for i in range(50):
    list1.append(random.randint(1,50))
def bubbleSort(list1):
    checks = 0
    for i in range(1,len(list1)):
        if list1[i] > list1[i-1] and checks == len(list1):
            print(list1)
            return list1
        elif list1[i] > list1[i-1]:
            checks+=1
        else:
            for i in range(1,len(list1)):
                if list1[i] < list1[i-1]:
                    list1[i-1], list1[i] = list1[i], list1[i-1]
                    return bubbleSort(list1)
            

bubbleSort(list1)