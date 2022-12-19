from tkinter import*
def Giriş():
    giriş_ekran=Tk()
    giriş_ekran.geometry("500x500")
    giriş_ekran.title("Giriş Yap")
    Label(giriş_ekran,text="Giriş yapmak için bilgilerinizi giriniz.").pack()
    Label(giriş_ekran, text="").pack
    Label(giriş_ekran,text="Kullanıcı Adı").pack()
    username_login_entry = Entry(giriş_ekran, textvariable="username")
    username_login_entry.pack()
    Label(giriş_ekran, text="").pack
    Label(giriş_ekran, text=" Şifre").pack
    password_login_entry = Entry(giriş_ekran, textvariable="password", show="*")
    password_login_entry.pack()
    Label(giriş_ekran, text="").pack
    Button(giriş_ekran, text="Giriş Yap", width=10, height=1).pack() 
    giriş_ekran.mainloop()
Giriş()