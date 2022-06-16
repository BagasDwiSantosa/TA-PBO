from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod
from tkinter import messagebox

class Utama(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inputan(self):
        pass

    @abstractmethod
    def tampil(self):
        pass

class Login(Utama):
    def __init__(self, SubFrame):
        self.SubFrame1 = SubFrame
        self.SubFrame1.title("Login Vaksinasi Covid-19")

        self.username = StringVar()
        self.__password = StringVar()

    def varPendaftaran(self):
        self.nama = StringVar()
        self.noNIK = StringVar()
        self.noTlp = StringVar()
        self.alamat = StringVar()
        self.jenisKel = StringVar()
        self.jenisVaksin = StringVar()

    def inputan(self):
        return super().inputan()

    def tampil(self):
        canvas0 = Canvas(self.SubFrame1, width=400, height=420, relief='raised', bg="white")
        canvas0.grid()

        L1label1 = Label(self.SubFrame1, text="Vaksinasi COVID-19", font='Verdena 14 bold', bg='white')
        canvas0.create_window(200, 30, window=L1label1)

        self.foto1 = PhotoImage(file='Peduli.png')
        display1 = Label(self.SubFrame1, image=self.foto1, bg='white')
        canvas0.create_window(200, 120, window=display1)

        L1label2 = Label(self.SubFrame1, text="Username", font='Verdena 10 normal', bg='white')
        canvas0.create_window(75, 210, window=L1label2)

        L1label3 = Label(self.SubFrame1, text="Password", font='Verdena 10 normal', bg='white')
        canvas0.create_window(75, 250, window=L1label3)

        entry1 = Entry(self.SubFrame1, textvar=self.username, font='Verdena 10 normal', width=25, borderwidth=1.5)
        canvas0.create_window(260, 210, window=entry1)

        entry2 = Entry(self.SubFrame1, textvar=self.__password, font='Verdena 10 normal', width=25, borderwidth=1.5)
        canvas0.create_window(260, 250, window=entry2)

        Bt1 = Button(self.SubFrame1, text="Login", command=self.lanjut, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas0.create_window(195, 300, window=Bt1)

        self.foto2 = PhotoImage(file='Kemenkes3.png')
        display2 = Label(self.SubFrame1, image=self.foto2, bg='white')
        canvas0.create_window(150, 370, window=display2)

        self.foto3 = PhotoImage(file="kampus.png")
        display3 = Label(self.SubFrame1, image=self.foto3, bg='white')
        canvas0.create_window(240, 370, window=display3)

    def lanjut(self):
        user = self.username.get()
        passw = self.__password.get()

        if user == "" and passw == "":
            messagebox.showerror(
                'Error!!!', "Silahkan masukkan Username dan Password dengan benar!!!")
        else:
            self.ke_menu()

    def ke_menu(self):
        menuuu = Toplevel(self.SubFrame1)
        self.window = Menu(menuuu)
        self.window.tampil()


class Menu(Login):
    def __init__(self, SubFrame2):
        self.SubFrame2 = SubFrame2
        self.SubFrame2.title("Menu Vaksinasi Covid-19")

    def inputan(self):
        return super().inputan()

    def tampil(self):
        canvas1 = Canvas(self.SubFrame2, width=400, height=420, relief='raised', bg="white")
        canvas1.grid()

        L2label1 = Label(self.SubFrame2, text="Menu Vaksinasi COVID-19", font='Verdena 14 bold', bg='white')
        canvas1.create_window(200, 30, window=L2label1)

        self.foto4 = PhotoImage(file='Sivaksin.png')
        display4 = Label(self.SubFrame2, image=self.foto4, bg='white')
        canvas1.create_window(200, 120, window=display4)

        Bt2 = Button(self.SubFrame2, text="Pendaftaran Vaksinasi Covid-19", command=self.pendaftaran, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas1.create_window(195, 220, window=Bt2)

        Bt3 = Button(self.SubFrame2, text="Data Vaksinasi Covid-19", command=self.dataCovid19, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas1.create_window(195, 260, window=Bt3)

        Bt4 = Button(self.SubFrame2, text="Informasi dan Saran", command=self.info_kami, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas1.create_window(195, 300, window=Bt4)

        Bt5 = Button(self.SubFrame2, text="Logout", command=self.SubFrame2.quit, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas1.create_window(195, 340, window=Bt5)

    def pendaftaran(self):
        daftar2 = Toplevel(self.SubFrame2)
        self.window1 = PendaftaranVaksin(daftar2)
        self.window1.inputan()

    def dataCovid19(self):
        data2 = Toplevel(self.SubFrame2)
        self.window2 = DataVaksinasi(data2)
        self.window2.tampil()

    def info_kami(self):
        info = Toplevel(self.SubFrame2)
        self.window3 = InfoKami(info)
        self.window3.tampil()


class PendaftaranVaksin(Menu):
    def __init__(self, SubFrame3):
        self.SubFrame3 = SubFrame3
        self.tabel = SubFrame3
        self.SubFrame3.title("Pendaftaran")
        self.head = ["NAMA", "NIK", "HP", "JENIS KELAMIN", "ALAMAT", "JENIS VAKSIN"]

        PendaftaranVaksin.varPendaftaran(self)

    def inputan(self):
        canvas2 = Canvas(self.SubFrame3, width=400, height=455, relief='raised', bg="white")
        canvas2.grid()

        L3label1 = Label(self.SubFrame3, text="Formulir Vaksinasi COVID-19", font='Verdena 12 bold', bg='white')
        canvas2.create_window(200, 30, window=L3label1)

        L3label2 = Label(self.SubFrame3, text='Nama ', font='Verdena 10 normal', bg="white")
        canvas2.create_window(65, 90, window=L3label2)

        entry1 = Entry(self.SubFrame3, textvar=self.nama, font='Verdena 10 normal', width=30, borderwidth=1.5)
        canvas2.create_window(260, 90, window=entry1)

        L3label3 = Label(self.SubFrame3, text='noNIK ', font='Verdena 10 normal', bg="white")
        canvas2.create_window(65, 130, window=L3label3)

        entry2 = Entry(self.SubFrame3, textvar=self.noNIK, font='Verdena 10 normal', width=30, borderwidth=1.5)
        canvas2.create_window(260, 130, window=entry2)

        L3label4 = Label(self.SubFrame3, text='No Telepon ', font='Verdena 10 normal', bg="white")
        canvas2.create_window(65, 170, window=L3label4)

        entry3 = Entry(self.SubFrame3, textvar=self.noTlp, font='Verdena 10 normal', width=30, borderwidth=1.5)
        canvas2.create_window(260, 170, window=entry3)

        L3label5 = Label(self.SubFrame3, text='Jenis Kelamin ', font='Verdena 10 normal', bg="white")
        canvas2.create_window(65, 210, window=L3label5)

        rd1 = Radiobutton(self.SubFrame3, text="Laki-Laki", padx=5, variable=self.jenisKel, value="Laki-Laki", font='Verdena 10 normal', bg="white")
        canvas2.create_window(190, 210, window=rd1)

        rd2 = Radiobutton(self.SubFrame3, text="Perempuan", padx=5, variable=self.jenisKel,  value="Perempuan", font='Verdena 10 normal', bg="white")
        canvas2.create_window(290, 210, window=rd2)

        L3label6 = Label(self.SubFrame3, text='Alamat', font='Verdena 10 normal', bg="white")
        canvas2.create_window(65, 250, window=L3label6)

        entry4 = Entry(self.SubFrame3, textvar=self.alamat, font='Verdena 10 normal', width=30, borderwidth=1.5)
        canvas2.create_window(260, 250, window=entry4)

        L3label7 = Label(self.SubFrame3, text='Jenis Vaksinasi', font='Verdena 10 normal', bg="white")
        canvas2.create_window(65, 290, window=L3label7)

        listVaksin = ["Sinovac", "Moderna", "AstraZeneca"]
        listVaksin.append("Sinopharm")
        droplist = OptionMenu(self.SubFrame3, self.jenisVaksin, *listVaksin)
        droplist.config(font='Verdena 10 normal', bg="white", width=25)
        self.jenisVaksin.set('Pilih jenis Vaksinasi')
        canvas2.create_window(260, 290, window=droplist)

        Bt6 = Button(self.SubFrame3, text="Submit", command=self.tampil, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas2.create_window(195, 350, window=Bt6)

        Bt7 = Button(self.SubFrame3, text="Update", command=self.hasil, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas2.create_window(195, 390, window=Bt7)

        Bt8 = Button(self.SubFrame3, text="Exit", command=self.SubFrame3.quit, width=42, relief=GROOVE, font='Verdena 10 bold', bg='white')
        canvas2.create_window(195, 430, window=Bt8)

        self.tabelll = Toplevel(self.SubFrame3)
        self.tabel = ttk.Treeview(self.tabelll, columns=self.head, 
                show='headings')
        for kolom in self.head:
            self.tabel.heading(kolom, text=kolom)
        self.tabel.heading('#0', text='Nomor')
        self.tabel.heading('#1', text='Nama')
        self.tabel.heading('#2', text='NIK')
        self.tabel.heading('#3', text='Nomor HP')
        self.tabel.heading('#4', text='Jenis Kelamin')
        self.tabel.heading('#5', text='Alamat')
        self.tabel.heading('#6', text='Jenis Vaksin')
        self.tabel.column('#0',stretch=YES, minwidth=0, width=0)
        self.tabel.column('#1', stretch=YES, minwidth=0, width=100)
        self.tabel.column('#2', stretch=YES, minwidth=0, width=100)
        self.tabel.column('#3',stretch=YES, minwidth=0, width=100)
        self.tabel.column('#4',stretch=YES, minwidth=0, width=100)
        self.tabel.column('#5',stretch=YES, minwidth=0, width=100)
        self.tabel.column('#6',stretch=YES, minwidth=0, width=100)
        self.tabel.grid(row=1, columnspan=1)

    def tampil(self):
        name = self.nama.get()
        Nik = self.noNIK.get()
        no = self.noTlp.get()
        almt = self.alamat.get()
        klmn = self.jenisKel.get()
        vksn = self.jenisVaksin.get()

        if name == "" and Nik == "" and no == "" and almt == "":
            messagebox.showerror('Error!!!', "Data tidak boleh kosong!!!")

        else:
            try:
                Nik = int(Nik)
                no = int(no)
            except ValueError:
                messagebox.showerror('Error!!!', "NIK atau Nomor harus berupa angka!!!")
            else:
                messagebox.showinfo("Informasi", f"Selamat {name}, Anda telah terdaftar Vaksinasi Covid-19")
         
        teks = ("\nNama\t: {}\nNIK\t: {}\nTelepon\t: {}\nKelamin\t: {}\nAlamat\t: {}\nVaksin\t: {}\n".format(name, Nik, no, klmn,almt, vksn))
        filetxt = open("Data.txt", "a")
        filetxt.write(teks)
        filetxt.close()

    def hasil(self):
        self.tabel.insert('', 'end',  values=(self.nama.get(), self.noNIK.get(),self.noTlp.get(), self.jenisKel.get(), self.alamat.get(), self.jenisVaksin.get()))

       
class DataVaksinasi(Menu):
    def __init__(self, SubFrame4):
        self.SubFrame4 = SubFrame4
        self.SubFrame4.title("Data Vaksinasi Covid-19")

        self.dosis1 = '198.907.985 Dosis'
        self.dosis2 = '163.959.616 Dosis'
        self.dosis3 = '35.014.143 Dosis'

    def inputan(self):
        return super().inputan()

    def tampil(self):
        canvas4 = Canvas(self.SubFrame4, width=400, height=465, relief='raised', bg="white")
        canvas4.grid()

        L5label1 = Label(self.SubFrame4, text="Vaksinasi COVID-19 Nasional", font='Verdena 14 bold', bg='white')
        canvas4.create_window(200, 30, window=L5label1)

        L5label2 = Label(self.SubFrame4, text="(Data per tanggal 24 April 2022 pukul 18.00 WIB)", font='Verdena 8 normal', bg='white')
        canvas4.create_window(200, 50, window=L5label2)

        self.foto6 = PhotoImage(file='Kemenkes4.png')
        display6 = Label(self.SubFrame4, image=self.foto6, bg='white')
        canvas4.create_window(200, 130, window=display6)

        # DOSIS 1
        L5label3 = Label(self.SubFrame4, text="Total Vaksinasi Dosis 1", font='Verdena 10 normal',  bg='white', borderwidth=1.5, relief=RIDGE, width=35, height=2)
        canvas4.create_window(200, 210, window=L5label3)

        L5label4 = Label(self.SubFrame4, text=(f"===>  {self.dosis1}  <==="), font='Verdena 10 bold', bg='white', )
        canvas4.create_window(200, 250, window=L5label4)

        # DOSIS 2
        L5label5 = Label(self.SubFrame4, text="Total Vaksinasi Dosis 2", font='Verdena 10 normal',
                         bg='white', borderwidth=1.5, relief=RIDGE, width=35, height=2)
        canvas4.create_window(200, 290, window=L5label5)

        L5label6 = Label(self.SubFrame4, text=(f"===>  {self.dosis2}  <==="), font='Verdena 10 bold', bg='white')
        canvas4.create_window(200, 330, window=L5label6)

        # DOSIS 3
        L5label6 = Label(self.SubFrame4, text="Total Vaksinasi Dosis 3", font='Verdena 10 normal', bg='white', borderwidth=1.5, relief=RIDGE, width=35, height=2)
        canvas4.create_window(200, 370, window=L5label6)

        L5label7 = Label(self.SubFrame4, text=(f"===>  {self.dosis3}  <==="), font='Verdena 10 bold', bg='white')
        canvas4.create_window(200, 410, window=L5label7)

        L5label8 = Label(self.SubFrame4, text="Source : https://vaksin.kemkes.go.id/", font='Verdena 7 normal', bg='white')
        canvas4.create_window(200, 450, window=L5label8)


class InfoKami(Menu):
    def __init__(self, SubFrame5):
        self.SubFrame5 = SubFrame5
        self.SubFrame5.title("Info Kami")

    def inputan(self):
        return super().inputan()

    def tampil(self):
        canvas5 = Canvas(self.SubFrame5, width=400, height=520, relief='raised', bg="white")
        canvas5.grid()

        L6label1 = Label(self.SubFrame5, text="Informasi Kami", font='Verdena 13 bold', bg='white')
        canvas5.create_window(200, 20, window=L6label1)

        self.foto6 = PhotoImage(file='orang.png')
        display6 = Label(self.SubFrame5, image=self.foto6, bg='white')
        canvas5.create_window(200, 90, window=display6)

        L6label2 = Label(self.SubFrame5, text="", font='Verdena 10 normal', bg='white', borderwidth=1.5, relief=RIDGE, width=40, height=4)
        canvas5.create_window(200, 200, window=L6label2)

        L6label3 = Label(self.SubFrame5, text="Tentang Program", font='Verdena 10 bold', bg='white')
        canvas5.create_window(200, 150, window=L6label3)

        program = "Judul Program\t: Vaksinasi Covid-19\t      \nMata Kuliah\t: Pemrograman Berorientasi Objek\nDosen Pengampu\t: Ulfi Saidata Aesyi, S.Kom., M.Cs."

        L6label4 = Label(self.SubFrame5, text=program, font='Verdena 8 normal', bg='white')
        canvas5.create_window(200, 200, window=L6label4)

        L6label5 = Label(self.SubFrame5, text="", font='Verdena 10 normal', bg='white', borderwidth=1.5, relief=RIDGE, width=40, height=5)
        canvas5.create_window(200, 315, window=L6label5)

        Llabel6 = Label(self.SubFrame5, text="Tentang Kami", font='Verdena 10 bold', bg='white')
        canvas5.create_window(200, 255, window=Llabel6)

        kami = "Nama\t: Bagas Dwi Santosa\t(212103006)\n\t: Paramadina Evita Pertiwi\t(212103006)\n\t: Vindiani Nora Putri\t\t(212103006)\nProdi\t: Sistem Informasi\t\t\t     "

        L6label7 = Label(self.SubFrame5, text=kami, font='Verdena 8 normal', bg='white')
        canvas5.create_window(200, 315, window=L6label7)

        L6label8 = Label(self.SubFrame5, text="Saran dan Tanggapan",
                         font='Verdena 10 bold', bg='white')
        canvas5.create_window(200, 375, window=L6label8)

        self.Text1 = Text(self.SubFrame5, height=5, width=40, borderwidth=1.5, relief=RIDGE)
        canvas5.create_window(200, 435, window=self.Text1)

        Bt1 = Button(self.SubFrame5, text="Submit", command=self.terkirim, width=40, relief=RIDGE, font='Verdena 10 bold', bg='white', borderwidth=1.5)
        canvas5.create_window(200, 500, window=Bt1)

    def terkirim(self):
        saranTanggapan = self.Text1.get("1.0", END)
        saran = (saranTanggapan+"\n")

        filetxt = open("Saran.txt", "a")
        filetxt.write(saran)
        filetxt.close()

        messagebox.showinfo(
            "Informasi", "Saran dan Tanggapan anda telah terkirim")


def main_program():
    main = Tk()
    main_login = Login(main)
    main_login.tampil()
    main.mainloop()


main_program()