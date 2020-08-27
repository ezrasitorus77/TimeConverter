secs = input("Masukkan detik : ") # Sampai disini tipe data dibiarkan sebagai str untuk memenuhi kondisi "Invalid Input" seperti di soal.

def timeConverter(seconds): # Fungsi timeConverter memiliki 1 parameter sesuai ketentuan soal, yaitu seconds.
    try: # Try pada dasarnya digunakan untuk mengetes suatu blok kode yang kondisi errornya bisa kita tangani.
        seconds = int(seconds) # Mengetes apakah var 'secs' bisa dijadikan int. Hanya digit str bulat yang bisa dijadikan int. Maka itu, bila kode ini error berarti user menginput str atau float.
    except: # Except digunakan untuk menangani error sehingga seluruh blok kode tetap bisa berjalan (tidak terhenti karena error).
        print("Invalid input!")  # Penanganan yang digunakan adalah mencetak "Invalid input!" sesuai ketentuan di soal.
    
    else: # Klausul ini terpenuhi apabila blok kode sebelumnya tidak mengalami error, dengan kata lain lolos seleksi klausul "try".
        if (seconds > 359999) or (seconds < 0): # Klausul terakhir sesuai ketentuan soal apabila tipe data sudah berupa int.
            print("Invalid input!") # Pemenuhan klausul yang mencetak "Invalid input!" karena int melewati batas ketentuan.
        # Klausul dibuat menjadi 3 bagian agar proses lebih efisien. Asumsinya, jika digabung menjadi satu, maka input yang outputnya hanya merubah detik dengan input yang outputnya merubah seluruh digit akan menjadi satu. Menurut saya tidak cukup efisien.
        else: # Klausul final untuk input yang sesuai seluruh ketentuan. 
            if seconds < 60: # Jika input di bawah 60, maka sudah pasti yang berubah hanya digit detiknya.
                print(f"Konversi : 00:00:{seconds}") if len(str(seconds)) == 2 else print(f"Konversi : 00:00:0{seconds}") # Maka langsung cetak "00:00:seconds".

            elif 59 < seconds <= 3599: # Jika masuk di antaranya, maka sudah pasti yang berubah hanya menit dan detiknya.
                m = int(seconds / 60) # Karena ingin mengkonversi ke menit, maka dibagi dengan 60. Penggunaan int() untuk mendapatkan angka bulat sebagai menitnya (begitu pula untuk proses identik selanjutnya).
                s = seconds - (m * 60) # Sisanya menjadi detik.
                m, s = str(m) if len(str(m)) == 2 else "0" + str(m), str(s) if len(str(s)) == 2 else "0" + str(s) # Menambah angka "0" jika menit dan detik hanya memiliki satu digit (1 - 9).               
                
                print(f"Konversi : 00:{m}:{s}") # Mencetak konversi.
            
            else: # Kondisi dimana input sudah pasti merubah ketiga digit.
                h = int(seconds / 3600) # Dibagi dengan 3600 karena ingin mengkonversi jam.
                m = seconds - (h * 3600) # Sisanya dikonversi menjadi menit.
                if m > 59: # Jika True, maka m akan dikonversi kembali untuk mendapatkan detik sisanya.
                    mm = int(m / 60) # Dibagi 60 untuk mendapat angka terdekat sebagai menitnya.
                    s = m - (mm * 60) # Sisanya menjadi detik.
                else: # Kondisi apabila seluruh sisa pembagian sebelumnya sudah pasti menjadi digit detik.
                    mm = 0
                    s = m
                h, mm, s = str(h) if len(str(h)) == 2 else "0" + str(h), str(mm) if len(str(mm)) == 2 else "0" + str(mm), str(s) if len(str(s)) == 2 else "0" + str(s) # Menambah angka "0" jika jam, menit, dan detik hanya memiliki 1 digit (1 - 9).
                
                print(f"Konversi : {h}:{mm}:{s}") # Mencetak konversi.


timeConverter(secs)