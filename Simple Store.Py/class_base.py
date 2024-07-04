import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, askokcancel, askyesno
from PIL import Image, ImageTk

class Notebook_widgets(tk.Tk):
    def __init__(self):
        super().__init__()
        self.note = ttk.Notebook(self)
        self.note2 = ttk.Notebook(self)
        self.note3 = ttk.Notebook(self)

class Frame_widgets(Notebook_widgets):
    def __init__(self):
        super().__init__()
        self.f1 = tk.Frame(self.note, height=180, width=380, bg='OldLace')
        self.f2 = tk.Frame(self.note2, height=300, width=300, borderwidth=25)
        self.f3 = tk.Frame(self.note3)

class Fruit_menu(Frame_widgets):
    def __init__(self):
        super().__init__()

        self.fruits = ['Kiwi', 'Nectarine', 'Pineapple', 'Apple', 'Garnet', 'Grape', 'Plum', 'Pear', 'Watermelon']
        self.fruit_price = [5, 7, 9, 4, 8, 6, 3, 5, 9]

        self.price_recorded = []
        self.recorded_fruit = []
        self.price = None

        image_path = 'Fruits.jpg'
        pil_image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Label(self.f3, image=self.tk_image, width=500, height=500)

class Label_widgets(Fruit_menu):
    def __init__(self):
        super().__init__()

        self.total_price = tk.Label(self.f2, text='Total Price:', font=('Helvetica', 11), bg='OldLace', borderwidth=5)

class Listbox_widgets(Label_widgets):
    def __init__(self):
        super().__init__()

        self.list = tk.Listbox(self.f2, height=8, width=20, bg='OldLace', borderwidth=5)
        self.list2 = tk.Listbox(self.f2, height=8, width=15, bg='OldLace', borderwidth=5)
        self.list3 = tk.Listbox(self.f2, height=8, width=15, bg='OldLace', borderwidth=5)

class Entry_widgets(Listbox_widgets):
    def __init__(self):
        super().__init__()
        self.order_entry = tk.Entry(self.f1, width=22, font=('Bold', 15), borderwidth=8, fg='grey', justify='left')
        self.order_entry.bind('<FocusIn>', self.order_focusin)
        self.order_entry.bind('<FocusOut>', self.order_focusout)
        self.order_entry.insert(0, 'Enter Item Here')

        self.cash_entry = tk.Entry(self.f2, width=20, font=('Bold', 9), fg='grey', justify='left')
        self.cash_entry.bind('<FocusIn>', self.cash_focusin)
        self.cash_entry.bind('<FocusOut>', self.cash_focusout)
        self.cash_entry.insert(0, "Enter Amount of Cash")

        self.quantity_entry = tk.Entry(self.f2, width=12, borderwidth=2)

    def order_focusin(self, event):
        if self.order_entry.get() == 'Enter Item Here':
            self.order_entry.delete(0, tk.END)
            self.order_entry.config(fg='black', font=('Bold', 15), justify='center')

    def order_focusout(self, event):
        if not self.order_entry.get():
            self.order_entry.insert(0, 'Enter Item Here')
            self.order_entry.config(fg='grey', font=('Bold', 15), justify='left')

    def cash_focusin(self, event):
        if self.cash_entry.get() == 'Enter Amount of Cash':
            self.cash_entry.delete(0, tk.END)
            self.cash_entry.config(fg='black', font=('Bold', 9), justify='center')
    def cash_focusout(self, event):
        if not self.cash_entry.get():
            self.cash_entry.insert(0, 'Enter Amount of Cash')
            self.cash_entry.config(fg='grey', font=('Bold', 9), justify='left')

class Button_widgets(Entry_widgets):
    def __init__(self):
        super().__init__()

        self.add_button = tk.Button(self.f1, text='ADD',bg='black', fg='white', font=('Bold', 10), width=15, command=self.click_add)
        self.delete_button = tk.Button(self.f1, text='DELETE',bg='black', font=('Bold', 10), fg='white', width=15, command=self.click_delete)
        self.delete_all_button = tk.Button(self.f1, text='DELETE ALL',bg='black', fg='white', width=20, font=('Bold', 10),command=self.click_delete_all)
        self.update_button = tk.Button(self.f1, text='UPDATE',bg='black', fg='white', width=20, font=('Bold', 10), command=self.click_update)
        self.pay_button = tk.Button(self.f2, text='PAY', width=12, bg='green', fg='black', borderwidth=5,command=self.click_pay)
        self.show_total_price = tk.Button(self.f2, text='COMPUTE THE TOTAL PRICE', bg='Teal',fg='white', command=self.click_show_total_price)
        self.ok_button = tk.Button(self.f2, text='OK', width=2, command=self.click_ok)

    def click_pay(self):
        total_price = self.price
        Cash = self.cash_entry.get()
        cash = int(Cash)
        Change = cash - total_price

        if Cash:
            if cash >= total_price:
                self.payment_success_label = tk.Label(self.f2,text=f"YOU SUCCESSFULLY PAID FOR YOUR ORDERS:\n Your Change: ${Change}.00",font=('Helvetica', 10), bg='green', fg='black')
                self.payment_success_label.place(x=10, y=260)
                self.cash_entry.delete(0, tk.END)
                self.Total_Price.place_forget()
                self.list.delete(0, tk.END)
                self.list2.delete(0, tk.END)
                self.list3.delete(0, tk.END)
            else:
                showerror('INVALID', f'YOUR CASH SHOULD BE AT LEAST {total_price}')

        elif Cash == 'Enter Amount of Cash':
            showerror('INVALID', "YOU DON'T HAVE ANY ORDERS")
        else:
            showerror('INVALID', "INVALID")

    def click_show_total_price(self):
        All_Price = 0
        all_price = self.list3.get(0, tk.END)
        Price = list(all_price)
        price_values = list(map(int, Price))

        for i in price_values:
            All_Price += i
        self.Total_Price = tk.Label(self.f2, text=f"${All_Price}.00")
        self.Total_Price.place(x=300, y=180)
        self.price = All_Price

    def click_update(self):

        anchored = self.list2.get(tk.ANCHOR)

        if anchored:
            self.quantity_entry.place(x=150, y=-22)
            self.ok_button.place(x=230, y=-22)

        else:
            showerror('INVALID', 'CLICK THE QUANTITY NUMBER TO UPDATE')

    def click_ok(self):
        anchored = self.list2.get(tk.ANCHOR)
        index = self.list2.curselection()
        index2 = self.list3.curselection()
        Quantity = self.quantity_entry.get()
        quantity = int(Quantity)

        if anchored:
            if quantity >= 1:
                confirmation = askokcancel('CONFIRMATION',f"Do You Really Want to Buy a Quantity of {Quantity} of this Fruit?")
                selected_value = self.list2.get(index[0])
                selected_value2 = self.list3.get(index[0])
                value = int(selected_value2)

                latest_price = value * quantity

                self.list2.delete(tk.ANCHOR)
                self.list2.insert(index, quantity)

                self.list3.delete(index)
                self.list3.insert(tk.END, f"{latest_price}")
                self.quantity_entry.place_forget()
                self.ok_button.place_forget()
            else:
                showerror('INVALID', 'ENTER AN EXACT NUMBER OF QUANTITY \n 0 QUANTITY IS INVALID')

    def click_add(self):
        item = self.order_entry.get().title()
        quantity = 1
        self.order_list = []

        if item =='Enter Item Here':
            showerror('INVALID', "Enter an Item to Add")
        elif not item:
            showerror('INVALID', "Enter an Item to Add")
        else:
            if item in self.fruits:
                if item not in self.order_list:
                    ask_permission = askyesno('ADD CONFIRMATION', "DO YOU REALLY WANT TO ADD THIS ITEM?")
                    if ask_permission:
                        if item == self.fruits[0]:
                            self.price_recorded.append(5)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[0]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[1]:
                            self.price_recorded.append(7)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[1]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[2]:
                            self.price_recorded.append(9)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[2]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[3]:
                            self.price_recorded.append(4)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[3]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[4]:
                            self.price_recorded.append(8)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[4]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[5]:
                            self.price_recorded.append(6)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[5]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[6]:
                            self.price_recorded.append(3)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[6]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[7]:
                            self.price_recorded.append(5)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[7]}")
                            self.order_entry.delete(0, tk.END)
                        elif item == self.fruits[8]:
                            self.price_recorded.append(9)
                            self.list.insert(tk.END, f"{item.title()}")
                            self.list2.insert(tk.END, f"{quantity}")
                            self.list3.insert(tk.END, f"{self.fruit_price[8]}")
                            self.order_entry.delete(0, tk.END)
                        else:
                            showerror('INVALID', 'ERROR')
                    else:
                        self.order_entry.delete(0, tk.END)
                else:
                    showerror('INVALID', 'THIS ITEM IS ALREADY IN THE LIST')
            else:
                showerror('INVALID', "Unknown Product \n Try Again")
                self.order_entry.delete(0, tk.END)

    def click_delete(self):
        item = self.order_entry.get()
        anchored = self.list.get(tk.ANCHOR)
        selected_index = self.list.curselection()

        if item == 'Enter Item Here' and self.list.size() == 0:
            showerror("ERROR", "LIST IS EMPTY")
        elif not item and self.list.size() == 0:
            showerror('ERROR', 'LIST IS EMPTY')
        elif item == 'Enter Item Here' and not anchored:
            showerror('INVALID', "SELECT ITEM TO DELETE")
        elif not item and not anchored:
            showerror('INVALID', "SELECT AN ITEM TO DELETE")
        elif anchored:
            ask_permission = askyesno('DELETE CONFIRMATION', 'DO YOU REALLY WANT TO DELETE THIS ITEM?')
            if ask_permission:
                if selected_index:
                    index = selected_index[0]
                    self.list.delete(tk.ANCHOR)
                    self.list2.delete(index)
                    self.list3.delete(index)
                    self.price_recorded.pop(index)
        else:
            showerror('INVALID', 'ERROR')


    def click_delete_all(self):
        item = self.order_entry.get()

        if item == 'Enter Item Here' and self.list.size() == 0:
            showerror('ERROR', "YOUR LIST IS ALREADY EMPTY")
        elif not item and self.list.size() > 0:
            ask_permission = askokcancel('CONFIRMATION',
                                         " '- WARNING -' \n \n THIS WILL DELETE ALL ITEMS IN YOUR LIST \n \n -- CLICK OK TO PROCEED -- ")
            if ask_permission:
                self.list.delete(0, tk.END)
                self.list2.delete(0, tk.END)
                self.list3.delete(0, tk.END)
        elif item and self.list.size() > 0:
            ask_permission = askokcancel('CONFIRMATION',
                                         " '- WARNING -' \n \n THIS WILL DELETE ALL ITEMS IN YOUR LIST \n \n -- CLICK OK TO PROCEED -- ")
            if ask_permission:
                self.list.delete(0, tk.END)
                self.list2.delete(0, tk.END)
                self.list3.delete(0, tk.END)
        elif item == 'Enter Item Here' and self.list.size() > 0:
            ask_permission = askokcancel('CONFIRMATION',
                                         " '- WARNING -' \n \n THIS WILL DELETE ALL ITEMS IN YOUR LIST \n \n -- CLICK OK TO PROCEED -- ")
            if ask_permission:
                self.list.delete(0, tk.END)
                self.list2.delete(0, tk.END)
                self.list3.delete(0, tk.END)
        elif not item and self.list.size() == 0:
            showerror('ERROR', "YOUR LIST IS ALREADY EMPTY")


class Store(Button_widgets):
    def __init__(self, title, size, color, menu, price):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.configure(bg=color)
        self.fruits = menu
        self.fruit_price = price

        self.note.place(x=15, y=5)
        self.f1.pack(fill='both', expand=True)
        self.order_entry.place(x=60, y=10)
        self.add_button.place(x=40, y=65)
        self.delete_button.place(x=210, y=65)
        self.delete_all_button.place(x=110, y=107)
        self.update_button.place(x=110, y=140)
        self.note.add(self.f1, text='MANAGE YOUR ORDER HERE')

        self.note2.place(height=369, x=15, y=220)
        self.f2.pack(fill='both', expand=True)
        self.list.grid(row=1, column=0)
        self.list2.grid(row=1, column=1)
        self.list3.grid(row=1, column=2)
        self.cash_entry.place(x=-2, y=180)
        self.pay_button.place(x=10, y=210)
        self.total_price.place(x=150, y=180)
        self.show_total_price.place(x=155, y=215)
        self.note2.add(self.f2, text='YOUR ORDER LIST')

        self.note3.place(x=450, y=25)
        self.f3.pack()
        self.image_label.pack()
        self.note3.add(self.f3, text="  FRUIT MENU  ")
        self.mainloop()



fruits = ['Kiwi', 'Nectarine', 'Pineapple', 'Apple', 'Garnet', 'Grape', 'Plum', 'Pear', 'Watermelon']
fruit_price = [5, 7, 9, 4, 8, 6, 3, 5, 9]

Store("MEKUS_MEKUS STORE", [1000, 600], 'Teal', fruits, fruit_price)



