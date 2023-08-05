import tkinter as tk

body = tk.Tk()
body.title("LOVEMETER")
body.geometry("300x150")
body.configure(bg="black")


def remove_widgets():
    for widget in body.winfo_children():
        widget.destroy()


def page1():
    remove_widgets()
    tk.Label(text=" Welcome\n\nLoveMeter ", bg="white").place(relx=.5, rely=.5, anchor="s", relheight=.4, relwidth=.4)
    tk.Label(text=" ♡ ", bg="white", fg="red").place(relx=.5, rely=.3, anchor="center", relheight=.1, relwidth=.4)
    tk.Button(body, text="Start", bg="white", command=page2).place(relx=.5, rely=.7, anchor="center", relheight=.2, relwidth=.8)
    tk.Label(text="    @for entertainment purposes only:) ", bg="black", fg="white").place(relx=.3, rely=.9, anchor="n", relheight=.1, relwidth=.8)

def page2():
    remove_widgets()
    tk.Label(body, text="Your name:\n\n\nYour darling's name:", bg="black", fg="white").place(relx=.3, rely=.5, anchor="s", relheight=.4, relwidth=.9)
    fir_name_var = tk.StringVar()
    sec_name_var = tk.StringVar()
    fir_name_entry = tk.Entry(body, bg="white", fg="black", textvariable=fir_name_var).place(relx=.7, rely=.3, anchor="s", relheight=.2, relwidth=.3)
    sec_name_entry = tk.Entry(body, bg="white", fg="black", textvariable=sec_name_var).place(relx=.7, rely=.6, anchor="s", relheight=.2, relwidth=.3)
    calculate_button = tk.Button(body, text="Meter", bg="white", command=lambda: ask_olc(fir_name_var.get(), sec_name_var.get())).place(relx=.5, rely=.8, anchor="center", relheight=.2, relwidth=.2)
    print("test")

def ask_olc(fir_name, sec_name):
    if (isinstance(fir_name, str) and 1 < len(fir_name) < 15 ) and (isinstance(sec_name, str) and 1 < len(sec_name) < 15):

        ask = len(fir_name) + len(sec_name)
        if len(fir_name) > len(sec_name):
            ask -= 5
        else:
            ask += 3
            ask *= 52
            ask = ask / (100 + len(sec_name))
        if ask > 10:
            ask = 10
        else:
            ask = round(ask, 2)

        print("test1")
        remove_widgets()
        label_ask = tk.Label(body, text="{} and {}\nlove score:  {}".format(fir_name, sec_name, ask), bg="black", fg="white").place(relx=.5, rely=.5, anchor="center", relheight=.2, relwidth=.3)
        tk.Label(text=" ♡ ", bg="black", fg="red").place(relx=.7, rely=.5, anchor="center", relheight=.1, relwidth=.1)
    else:
        print("test2")
        remove_widgets()
        label_ask = tk.Label(body,text=" Information is missing or incorrect!\n Please enter all the information correctly.",bg="black", fg="yellow").place(relx=.5, rely=.5, anchor="center", relheight=.3,relwidth=.9)


page1()
body.mainloop()