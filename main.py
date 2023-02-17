from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letter = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letter)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password = password_num + password_symbols + password_letters

    random.shuffle(password)
    password_join="".join(password)
    password_entry.insert(0,password_join)
    pyperclip.copy(password_join)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    Filenotexixt=None
    user_web = website_entry.get()
    user_email_username = email_entry.get()
    user_password = password_entry.get()
    new_data={
        user_web:{
            "email": user_email_username,
            "password": user_password

        }
               }

    if len(user_web)==0  or len(user_email_username)==0 or len(user_password)==0 :
        messagebox.showinfo(title="oops", message=f"Please don't leave any fields empty")

#json have three methods which are important , such as update, load, dump where as dump refere to write . update to update , load to read.



    else:
        try:
            with open(".Data.json",mode="r") as datafile:
                data = json.load(datafile)  # reading data file


        except FileNotFoundError:
            with open("./Data.json", mode="w") as data_file:
                json.dump(new_data,data_file,indent=4)#saving file

        else:
            data.update(new_data)  # updating new data file
            with open(".Data.json",mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:

            website_entry.delete(0, END)

            password_entry.delete(0, END)

# ---------------------------- Find Password ------------------------------- #
def find_password():
    web_entry=website_entry.get()

    try:
            with open("Data.json", mode="r") as datafile:
                data = json.load(datafile)
                main_dic=data[web_entry]

    except KeyError:

                 messagebox.showinfo(title="oops",message=f"Such {web_entry} data is not avaliable")

    except FileNotFoundError:
                messagebox.showinfo(title="opps", message="No Data File Found")
    else:

                messagebox.showinfo(title="find_password result", message=f"Email: {main_dic['email']}\n Password: {main_dic['password']}")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=70, pady=70)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_label.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "syedalauddin.b@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password",command=password_generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button=Button(text="Search", width=15, command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()
