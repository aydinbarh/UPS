import tkinter as tk 
from tkinter import messagebox

students = []

def open_login_window():
    global window , username_entry , password_entry

    window = tk.Tk()
    window.title("UPS")
    window.geometry("700x500")

    tk.Label(window , text="نام کاربری را وارد کنید").pack(pady=5)
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window , text="رمز عبور را وارد کنید").pack(pady=5)
    password_entry = tk.Entry(window , show="*")
    password_entry.pack()

    tk.Button(window , text="ورود" , command=login).pack(padx=20)
    

    window.mainloop()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("ورود با موفقیت")
        window.destroy()
        open_second_window()
    else:
        messagebox.showerror("نام کاربری یا رمز ورود اشتباه")


def open_second_window():
    second = tk.Tk()
    second.title("داشبورد")
    second.geometry("800x600")

    tk.Label(second , text="به سیستم یو پی اس خوش آمدید").pack(pady=10)
    tk.Label(second , text="ثبت نام دانشجو").pack(pady=5)

    tk.Label(second , text="نام دانشجو").pack(pady=5)
    name_entry = tk.Entry(second)
    name_entry.pack()

    tk.Label(second , text="نام خانوادگی").pack(pady=5)
    sname_entry = tk.Entry(second)
    sname_entry.pack()

    tk.Label(second , text="تاریخ تولد").pack(pady=5)
    brit_entry = tk.Entry(second)
    brit_entry.pack()

    tk.Label(second , text="شماره دانشجویی").pack(pady=5)
    codd_entry = tk.Entry(second)
    codd_entry.pack()


    def sumbit():
        name = name_entry.get()
        sname = sname_entry.get()
        brit = brit_entry.get()
        codd = codd_entry.get()
        messagebox.showinfo("دانشجو ثبت نام شد")

        student = {"نام":name,
         "نام خانادگی":sname,
         "تاریخ تولد":brit,
         "شماره دانشجویی":codd
         }
        students.append(student)

    def show_students():
        if not students:
            messagebox.showinfo("هیچ دانشجویی ثبت نشد")
            return
        info_window = tk.Toplevel(second)
        info_window.title("لیست دانشجوها")
        info_window.geometry("400x400")

        tk.Label(info_window, text="اطلاعات دانشجوها").pack(pady=10)
        text_arra = tk.Text(info_window, width=50 , height=50)
        text_arra.pack(padx=10, pady=10)

        for i , s in enumerate(students , 1):
            students_text = (students)
            text_arra.insert(tk.END , students_text)

        text_arra.config(state="disabled")

    def exit_and_back():
        second.destroy()
        open_login_window()

    tk.Button(second , text="ثبت" , command=sumbit).pack(pady=10)
    tk.Button(second , text="خروج", command=exit_and_back).pack(pady=10)
    tk.Button(second , text="نمایش لیست دانشجوها",command=show_students).pack(pady=50)

    second.mainloop()

open_login_window()