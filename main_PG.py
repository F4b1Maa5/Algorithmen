from tkinter import *
import csv
import os

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

def writetocsv(month, name):
    path = os.path.dirname(__file__) + '/'
    with open(path + name + '.csv', mode='w+', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";")
        csvwriter.writerow(['ID', 'Niderschlag'])
        csvwriter.writerows(month)

def filterCSV_Month(month, asc):
    listEinträge.delete(0,END)
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

        if (month == 'jan'):
            jan.pop(0)
            quickSort(jan, 0, len(jan) - 1, asc)
            writetocsv(jan, month)
            counter = 0
            for item in jan:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
        elif (month == 'feb'):
            feb.pop(0)
            quickSort(feb, 0, len(feb) - 1, asc)
            writetocsv(feb, month)
            counter = 0
            for item in feb:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return feb
        elif (month == 'mar'):
            mar.pop(0)
            quickSort(mar, 0, len(mar) - 1, asc)
            writetocsv(mar, month)
            counter = 0
            for item in mar:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return mar
        elif (month == 'apr'):
            apr.pop(0)
            quickSort(apr, 0, len(apr) - 1, asc)
            writetocsv(apr, month)
            counter = 0
            for item in apr:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return apr
        elif (month == 'mai'):
            mai.pop(0)
            quickSort(mai, 0, len(mai) - 1, asc)
            writetocsv(mai, month)
            counter = 0
            for item in mai:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return mai
        elif (month == 'jun'):
            jun.pop(0)
            quickSort(jun, 0, len(jun) - 1, asc)
            writetocsv(jun, month)
            counter = 0
            for item in jun:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return jun
        elif (month == 'jul'):
            jul.pop(0)
            quickSort(jul, 0, len(jul) - 1, asc)
            writetocsv(jul, month)
            counter = 0
            for item in jul:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return jul
        elif (month == 'aug'):
            aug.pop(0)
            quickSort(aug, 0, len(aug) - 1, asc)
            writetocsv(aug, month)
            counter = 0
            for item in aug:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return aug
        elif (month == 'sep'):
            sep.pop(0)
            quickSort(sep, 0, len(sep) - 1, asc)
            writetocsv(sep, month)
            counter = 0
            for item in sep:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return sep
        elif (month == 'okt'):
            okt.pop(0)
            quickSort(okt, 0, len(okt) - 1, asc)
            writetocsv(okt, month)
            counter = 0
            for item in okt:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return okt
        elif (month == 'nov'):
            nov.pop(0)
            quickSort(nov, 0, len(nov) - 1, asc)
            writetocsv(nov, month)
            counter = 0
            for item in nov:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
            return nov
        elif (month == 'dez'):
            dez.pop(0)
            quickSort(dez, 0, len(dez) - 1, asc)
            writetocsv(dez, month)
            counter = 0
            for item in dez:
                listEinträge.insert(counter,[item[0],item[1]])
                counter = counter +1
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

tk = Tk()
tk.title('Niederschlagsverwaltung')
tk.geometry('750x350')
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

monat_label = Label(tk, text='Monat', font=('bold', 14), bg='light blue')
monat_label.grid(row=0, column=1, sticky=W)
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

searchMonth_btn = Button(tk, text='Suchen', width=15, command=lambda:filterCSV_Month(variable.get(), var1.get()))
searchMonth_btn.grid(row=2, column=0, pady=20)

tk.mainloop()