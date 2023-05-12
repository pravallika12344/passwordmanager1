# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


def generate_password():
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    list3 = ['@', '#', '$', '*', '(', ')', '&', '^', '_']
    a = randint(8, 10)
    b = randint(2, 4)
    c = randint(2, 4)
    i = 0
    output = []
    output_result = ''
    output = [choice(list1) for i in range(a)]
    output1 = [choice(list2) for i in range(b)]
    output2 = [choice(list3) for i in range(c)]
    output3 = output+output2+output1

    shuffle(output3)
    output_result = "".join(output3)
    input3.insert(0, output_result)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = input1.get()
    email = input2.get()
    password = input3.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    if len(password) == 0 or len(website) == 0:

        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:

             # f.write(f"{website} | {email} | {password}\n")
             # json.dump(new_data, f, indent=4)
             # data = json.load(f)
             # print(data)
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', "w") as f:
                json.dump(new_data, f, indent=4)
        else:

            with open("data.json", "w") as f:

                json.dump(data, f, indent=4)
        finally:
            input1.delete(0, END)
            input3.delete(0, END)


def search():
    website = input1.get()
    try:
        with open("data.json") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message="No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

input1 = Entry(width=50)
input1.grid(row=1, column=1, columnspan=2, pady=1)
input1.focus()
input2 = Entry(width=53)
input2.grid(row=2, column=1, columnspan=2, pady=1)
input2.insert(0, "pathipatipravallika@gmail.com")
input3 = Entry(width=32)
input3.grid(row=3, column=1, pady=1)
label6 = Button(width=45, text="Add",
                bg="WHITE", highlightthickness=0, command=save)
label6.grid(row=4, column=1, columnspan=2, pady=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0, padx=1, pady=1)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0, padx=1, pady=1)
# label2.insert(0, 'pathipatipravallika@gmail.com')

label3 = Label(text="Password:")
label3.grid(row=3, column=0, padx=1, pady=1)

label4 = Button(text="Generate Password:", width=16, bg="WHITE",
                highlightthickness=0, command=generate_password)
label4.grid(row=3, column=2)

label5 = Button(text='search', width=16, bg="WHITE", command=search)
label5.grid(row=1, column=2)


window.mainloop()


# exceptions
# if one except block is executed it does not go further to another except blocks also
# except IndexError and except KeyError
# file must be closed
# file need not to be closed if used with 'with' keyword.
# i can raise my own exceptions using 'raise' keyword
