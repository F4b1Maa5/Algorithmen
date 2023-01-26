import csv
import time
import matplotlib.pyplot as plt

sorttimer = []

def partition(array, low, high,asc):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if(asc):
            if float(array[j][1]) <= float(pivot[1]):
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        else:
            if float(array[j][1]) >= float(pivot[1]):
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1 
 
def quickSort(array, low, high,asc):
    if low < high:
        pi = partition(array, low, high,asc)
        quickSort(array, low, pi - 1,asc)
        quickSort(array, pi + 1, high,asc)

def bubblesort(tosortarray):
    n = len(tosortarray)
    swapped = False
    for i in range(n-1):
        for j in range(1, n-i-1):
            if float(tosortarray[j][1]) > float(tosortarray[j + 1][1]):
                swapped = True
                tosortarray[j], tosortarray[j + 1] = tosortarray[j + 1], tosortarray[j]         
        if not swapped:
            return
    return tosortarray

def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if float(arr[min_idx][1]) > float(arr[j][1]):
                min_idx = j
        # Swap the found minimum element with the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

jan = []
feb = []
mar = []
apr = []
mai = []
jun = []
jul = []
aug = []
sep = []
okt = []
nov = []
dez = []
jahr = []

with open('Niederschlag.csv', newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=';')
    for row in reader:
        if(row.__len__() > 0):  
            jan.append([str(row[0]),row[2]])
            feb.append([str(row[0]),row[3]])
            mar.append([str(row[0]),row[4]])
            apr.append([str(row[0]),row[5]])
            mai.append([str(row[0]),row[6]])
            jun.append([str(row[0]),row[7]])
            jul.append([str(row[0]),row[8]])
            aug.append([str(row[0]),row[9]])
            sep.append([str(row[0]),row[10]])
            okt.append([str(row[0]),row[11]])
            nov.append([str(row[0]),row[12]])
            dez.append([str(row[0]),row[13]])
            jahr.append([str(row[0]),row[14]])

    feb.pop(0)
    startimer = time.time()
    bubblesort(feb)
    endtimer = time.time()
    sorttimer.append(endtimer-startimer) 

    apr.pop(0)
    startimer = time.time()
    quickSort(apr,0,len(apr)-1,True)
    endtimer = time.time()
    sorttimer.append(endtimer-startimer)

    mar.pop(0)
    startimer = time.time()
    selection_sort(mar)
    endtimer = time.time()
    sorttimer.append(endtimer-startimer)
    

xpoints = [1,2,3]
ypoints = [sorttimer[0],sorttimer[1],sorttimer[2]]
plt.plot(xpoints,ypoints,'o')
plt.text(xpoints[0],ypoints[0], 'Bubblesort in '+str(sorttimer[0])+ ' sek')
plt.text(xpoints[1],ypoints[1], 'Quicksort in '+str(sorttimer[1])+ ' sek')
plt.text(xpoints[2],ypoints[2], 'Selectionsort in '+str(sorttimer[2])+ ' sek')
plt.axis([0, 4, 0 , 20])
plt.ylabel("Laufzeit in s")
plt.xlabel("Sortieralgorithmen")
plt.xticks([1,2,3])
plt.show()