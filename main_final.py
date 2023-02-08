# import der benoetigeten Pakete
from tkinter import *
import csv
import os
import csv
import time
import matplotlib.pyplot as plt

#inizialiesierung der benoetigten globalen Variablen
sorttimer = []
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

# Die Funktion fuer Quicksort fuer die Laufzeitauswertung
def partition_laufzeit(array, low, high,asc):
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

# Die Funktion fuer Quicksort fuer die Laufzeitauswertung
def quickSort_laufzeit(array, low, high,asc):
    if low < high:
        pi = partition_laufzeit(array, low, high,asc)
        quickSort_laufzeit(array, low, pi - 1,asc)
        quickSort_laufzeit(array, pi + 1, high,asc)

# Bubblesort fuer die Laufzeitauswertung
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

# Selection sort fuer die Laufzeitauswertung

def selection_sort(arr):
    for i in range(len(arr)):
        # finde das minimale Element in dem unsortierten Arraz
        min_idx = i
        for j in range(i+1, len(arr)):
            if float(arr[min_idx][1]) > float(arr[j][1]):
                min_idx = j
        # wechsel das gefundene kleinste Element mit dem aktuellen elemenet       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Methode um die Laufzeit der Algorithmen zu berechnen
def laufzeit():
    # einlesen der CSV und aufteilung in die Globalen variablen
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

    # loesche das 0te Element da Monatsbezeichnung als 0 in der CSV vorhanden ist
    feb.pop(0)
    # stratzeitpunkt ermitteln
    startimer = time.time()
    #algorthimus ausfueren 
    bubblesort(feb)
    # endzaeit ermitteln
    endtimer = time.time()
    sorttimer.append(round(endtimer-startimer,2)) 

    apr.pop(0)
    startimer = time.time()
    quickSort_laufzeit(apr,0,len(apr)-1,True)
    endtimer = time.time()
    sorttimer.append(round(endtimer-startimer,2))

    mar.pop(0)
    startimer = time.time()
    selection_sort(mar)
    endtimer = time.time()
    sorttimer.append(round(endtimer-startimer,2))

    # Diagramm zeichen und Werte ausgeben
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

# Quicksort fuer die Eigentliche sortierung
def partition(array, low, high, asc):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if (asc):
            if float(array[j][1]) <= float(pivot[1]):
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        else:
            if float(array[j][1]) >= float(pivot[1]):
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high, asc):
    if low < high:
        pi = partition(array, low, high, asc)
        quickSort(array, low, pi - 1, asc)
        quickSort(array, pi + 1, high, asc)

# Methode um die neue CSV fuer den Monat zu schreiben
def writetocsv(month, name):
    #den aktuellen Pfad bestimmen
    path = os.path.dirname(__file__) + '/'
    # neue CSV schreiben
    with open(path + name + '.csv', mode='w+', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";")
        csvwriter.writerow(['ID', 'Niderschlag'])
        csvwriter.writerows(month)

# Methode um die CSV zu filtern
def filterCSV(month, asc):
    # Alle eintraege aus der GUI loeschen
    listEinträge.delete(0,END)
    # Alle golbaelen Variablen leeren
    jan.clear()
    feb.clear()
    mar.clear()
    apr.clear()
    mai.clear()
    jun.clear()
    jul.clear()
    aug.clear()
    sep.clear()
    okt.clear()
    nov.clear()
    dez.clear()
    jahr.clear()
    # CSV einlesen
    with open('Niederschlag.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if (row.__len__() > 0):
                jan.append([str(row[0]), row[2]])
                feb.append([str(row[0]), row[3]])
                mar.append([str(row[0]), row[4]])
                apr.append([str(row[0]), row[5]])
                mai.append([str(row[0]), row[6]])
                jun.append([str(row[0]), row[7]])
                jul.append([str(row[0]), row[8]])
                aug.append([str(row[0]), row[9]])
                sep.append([str(row[0]), row[10]])
                okt.append([str(row[0]), row[11]])
                nov.append([str(row[0]), row[12]])
                dez.append([str(row[0]), row[13]])
                jahr.append([str(row[0]), row[14]])
        # Entsprechend nach der Nutzereinagbe den entsprechenden Monat filtern und in die GUI eintragen
        if (month == 'jan'):
            # das 0te Element loeschen, da das 0te Element der Monatsname in der CSV ist
            jan.pop(0)
            #quicksort fuer den ausgewaehlten Monat anwenden
            quickSort(jan, 0, len(jan) - 1, asc)
            # das Sortierte Ergebnis in eine Neue CSV schreiben
            writetocsv(jan, month)
            counter = 0
            # Die Sortierten Elemente in der GUI anzeigen
            for item in jan:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
        elif (month == 'feb'):
            feb.pop(0)
            quickSort(feb, 0, len(feb) - 1, asc)
            writetocsv(feb, month)
            counter = 0
            for item in feb:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return feb
        elif (month == 'mar'):
            mar.pop(0)
            quickSort(mar, 0, len(mar) - 1, asc)
            writetocsv(mar, month)
            counter = 0
            for item in mar:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return mar
        elif (month == 'apr'):
            apr.pop(0)
            quickSort(apr, 0, len(apr) - 1, asc)
            writetocsv(apr, month)
            counter = 0
            for item in apr:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return apr
        elif (month == 'mai'):
            mai.pop(0)
            quickSort(mai, 0, len(mai) - 1, asc)
            writetocsv(mai, month)
            counter = 0
            for item in mai:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return mai
        elif (month == 'jun'):
            jun.pop(0)
            quickSort(jun, 0, len(jun) - 1, asc)
            writetocsv(jun, month)
            counter = 0
            for item in jun:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return jun
        elif (month == 'jul'):
            jul.pop(0)
            quickSort(jul, 0, len(jul) - 1, asc)
            writetocsv(jul, month)
            counter = 0
            for item in jul:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return jul
        elif (month == 'aug'):
            aug.pop(0)
            quickSort(aug, 0, len(aug) - 1, asc)
            writetocsv(aug, month)
            counter = 0
            for item in aug:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return aug
        elif (month == 'sep'):
            sep.pop(0)
            quickSort(sep, 0, len(sep) - 1, asc)
            writetocsv(sep, month)
            counter = 0
            for item in sep:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return sep
        elif (month == 'okt'):
            okt.pop(0)
            quickSort(okt, 0, len(okt) - 1, asc)
            writetocsv(okt, month)
            counter = 0
            for item in okt:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return okt
        elif (month == 'nov'):
            nov.pop(0)
            quickSort(nov, 0, len(nov) - 1, asc)
            writetocsv(nov, month)
            counter = 0
            for item in nov:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return nov
        elif (month == 'dez'):
            dez.pop(0)
            quickSort(dez, 0, len(dez) - 1, asc)
            writetocsv(dez, month)
            counter = 0
            for item in dez:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return dez
        elif (month == 'jahr'):
            jahr.pop(0)
            quickSort(jahr, 0, len(jahr) - 1, asc)
            writetocsv(jahr, month)
            counter = 0
            for item in jahr:
                listEinträge.insert(counter, [item[0], item[1]])
                counter = counter + 1
            return jahr

# GUI erzeugen

tk = Tk()
tk.title('Niederschlagsverwaltung')
tk.geometry('450x350')
tk.configure(bg='light blue')
tk.resizable(False, False)

MONTH = [
"jan",
"feb",
"mar",
"apr",
"mai",
"jun",
"jul",
"aug",
"sep",
"okt",
"nov",
"dez",
"jahr"
]

zeitraum_label = Label(tk, text='Zeitraum', font=('bold', 14), bg='light blue')
zeitraum_label.grid(row=0, column=1, sticky=W)
variable = StringVar(tk)
variable.set(MONTH[0])
w = OptionMenu(tk, variable, *MONTH)
w.grid(row=0, column=2, sticky=W)
month = variable.get(),
suche_label = Label(tk, text='Suche', font=('bold', 14), bg='light blue')
suche_label.grid(row=1, column=1, sticky=W)
var1 = IntVar()
t1 = Checkbutton(tk, text="asc", variable=var1, onvalue=True, offvalue=False)
t1.grid(row=1, column=2, sticky=W)
asc = var1.get()

listEinträge = Listbox(tk, height=10, width=50, border=0)
listEinträge.grid(row=4, column=0, columnspan=3, rowspan=2, pady=20, padx=20)
scrollbar = Scrollbar(tk)
scrollbar.grid(row=4, column=3)
listEinträge.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listEinträge.yview)

search_btn = Button(tk, text='Suchen', width=15, command=lambda:filterCSV(variable.get(), var1.get()))
search_btn.grid(row=2, column=0, pady=20)
time_btn = Button(tk, text='Laufzeiten', width=15, command=lambda:laufzeit())
time_btn.grid(row=2, column=2, pady=20)

tk.mainloop()