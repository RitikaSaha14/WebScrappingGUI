''''
   used modules ---> csv -->pip install csv
                     bs4--> pip install bs4
                     requests -->pip install requests
                     lxml ---> pip install lxml
'''

# Web Scrapping in Python 3 Using Beautiful Soup with Tkinter GUI

import csv
from bs4 import BeautifulSoup                 
import requests
from tkinter import *
from tkinter import messagebox



# Parsing the data from website

source = requests.get('https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off').text

soup = BeautifulSoup(source, 'lxml')


# Creating three empty list for storing the required data

product_name = []
prices = []
ratings = []


# Extracting the required data from website with the help of <tag> and class name using soup

for i in soup.find_all('div', class_='_4rR01T'):
    string = i.text
    product_name.append(string.strip())

for i in soup.find_all('div', class_='_30jeq3 _1_WHN1'):
    price = i.text
    prices.append(price.strip())

for i in soup.find_all('div', class_='_3LWZlK'):
    rating = i.text
    ratings.append(rating.strip())




def ConsoleDisplay():
    # Printing the data inthe console
    print("\n\n")
    print("%-9s %-70s %-20s %s" %("Sr No.", "Product Name", "Prices", "Rating"))
    print("------------------------------------------------------------------------------------------------------------")
    print()
    for i in range(len(product_name)):
        print("%-9s %-70s %-20s %s" %(i+1, product_name[i],prices[i], ratings[i]))


# Creating the .csv file to store the data
def CreateCSV():

    messagebox.showinfo('file', 'CSV file created successfully in the current directory! You will be able to see the csv file after finishing the whole progran')
    with open('IphoneList.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Sr No.', 'Iphone Product', 'Price', 'Rating'])

        # Entering the extracted data in csv file

        for i in range(len(product_name)):
            writer.writerow([i+1, product_name[i], prices[i], ratings[i]])
        creating = False
        win2.destroy()


# Creating GUI to Display the Content

root = Tk()
root.geometry("600x600")
root['bg'] = "yellow"
root.resizable(False, False)
root.title("Web Scrapping From Flipkart.com")





h1 = Label(root, text="Scrapping It In Your Own Way", bg="black",height=3, fg="white",font=("Arial", 25, "bold"))
h1.pack(fill=X)
label2 = Label(root, text="Scrapping IPhone List\nfrom",bg="sky blue",fg= "white", font=("Arial",30, "bold"))
label2.pack(pady=50)
label2 = Label(root, text="Flipkart.com", font=("Arial",35,"bold"),fg="navy blue")
label2.pack()


def GUIwindow():
    global win3
    win3 = Toplevel(root)
    win3.geometry("1366x768")
    win3.resizable(False, False)
    frame1 = Frame(win3)
    frame1.place(x=100, y=100, width=1000, height=600)


    heading = Label(win3, text="List of Iphones From Flipkart.com", bg='black', fg='white', font=("Arial",18,"bold"))
    heading.pack(fill=X)
    text1 = "PRODUCT NAME"
    text2="PRICE"
    text3="RATING"
    heading2 = Label(win3, text=text1, bg='aqua', fg='black', font=("Arial", 13, "bold"))
    heading2.place(x=105,y=75, width=360)
    heading3 = Label(win3, text=text2, bg='orange', fg='black', font=("Arial", 13, "bold"))
    heading3.place(x=473, y=75, width=350)
    heading4 = Label(win3, text=text3, bg='purple', fg='black', font=("Arial", 13, "bold"))
    heading4.place(x=830,y=75, width=265)


    mainlist = []

    for i in range(len(product_name)):
        t = (product_name[i], prices[i], ratings[i])
        mainlist.append(t)


    totalrow = len(mainlist)
    totalcolumn = len(mainlist[1])


    for i in range(totalrow):
        for j in range(totalcolumn):
            E = Entry(
                frame1,
                width = len(mainlist[1][0])+10,
                fg = 'black',
                bg='grey',
                font=("Arial",12,)
            )
            E.grid(row=i, column=j)
            E.insert(0, mainlist[i][j])


def exitwindow():
    root.destroy()

def gotowin2():
    global win2
    win2 = Toplevel(root)
    win2.geometry("400x500")
    win2.resizable(False, False)
    win2.title("Choose A Mode")
    win2['bg'] = "cyan"
    
    l1 = Label(win2, text="Choose A Mode", bg="blue",fg ="white", font=("Arial", 17, "bold"))
    l1.pack(fill=X)

    b1 = Button(win2, text="Create .CSV file", bg="magenta",fg ="white",font=("Arial", 13, "bold"), width=20, command=CreateCSV)
    b1.place(x=110,y=250)
    b2 = Button(win2, text="Display on GUI", bg="green", fg="white",font=("Arial", 13, "bold"), width=20, command=GUIwindow)
    b2.place(x=110, y=300)
    b3 = Button(win2, text="Display in Console", bg="indigo", fg="white",font=("Arial", 13, "bold"), width=20, command=ConsoleDisplay)
    b3.place(x=110, y=350)


button1 = Button(root, text="Start Scrapping", bg="blue", fg="white", font=("Arial", 15, "bold"), command=gotowin2)
button1.place(x=140, y=430)
button2 = Button(root, text="Exit", bg="red", fg="white", font=("Arial", 15, "bold"), width=10, command=exitwindow)
button2.place(x=350, y=430)


# Mainloop
root.mainloop()
