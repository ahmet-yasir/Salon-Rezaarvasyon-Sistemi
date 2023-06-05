menuEkran="""****************   
*** ANA MENU ***
****************
1. Rezervasyon
2. Salonu Yazdır
3. Yeni Etkinlik
4. Toplam Ciro
0. Cıkıs
****************"""
print(menuEkran) # Giriş ekranı
toplam_ciro=0;
fiyat=[]
indirim = open("İndirim.txt", "r")
for i in range (0,17):          # dosyadaki bilgilerin 2 boyutlu diziye aktarımı
    fiyat.append([])
    fiyat[i]=indirim.readline().strip("\n").split("-")
salon=[[0] * 20 for i in range(20)]     # Salon oluşturma
for i in range(0,20):
    for j in range(0,20):
        salon[i][j]="-"
boskoltuk=[100,100,100,100] # Bos koltuk sayısı
menu=False
while True:
    try:
        secim = int(input("Seciminizi Yapiniz:"))
        break
    except ValueError:
        print("Hatalı giriş!")
        continue
while(secim!=0):
    if menu==True:    # ilk çalışmada ana menünün bir kez gelmesi için
        print(menuEkran)
        while True:
            try:
                secim = int(input("Seciminizi Yapiniz:"))
                break
            except ValueError:
                print("Hatalı giriş!")
                continue
    menu=True
    while (secim > 4 or secim < 0):  # Geçersiz menü kontrolü
        print("Gecersiz secim!")
        while True:
            try:
                secim = int(input("Seciminizi Yapiniz:"))
                break
            except ValueError:
                print("Hatalı giriş!")
                continue
    if (secim==1):
        while True:
            try:
                kategori = int(input("Kategori seciniz: "))
                break
            except ValueError:
                print("Hatalı giriş!")
                continue
        while (kategori >4 or kategori < 0):  # Geçersiz kategori kontrolü
            while True:
               try:
                   print("Gecersiz kategori!")
                   kategori = int(input("Kategori seciniz: "))
                   break
               except ValueError:
                   print("Hatalı giriş!")
                   continue
        while True:
            try:
                biletadet = int(input("Bilet adeti giriniz: "))
                break
            except ValueError:
                print("Hatalı giriş!")
                continue
        try:
            while (biletadet > boskoltuk[(kategori-1)] or biletadet>int(fiyat[0][1]) or biletadet<1):  # Bilet sayısı kontrolü
                if (biletadet>int(fiyat[0][1])):
                    print("Tek seferde maksimum ",int(fiyat[0][1]),"adet bilet alabilirsiniz!")
                elif biletadet<1:
                    print("Bilet adeti 1'den kucuk olamaz!")
                elif(biletadet > boskoltuk[(kategori-1)]):
                    print("Sectiginiz kategoride yeteri kadar bos koltuk bulunmamaktadir.")
                    print("sectiginiz kategoride ", boskoltuk[kategori-1], " tane bos koltuk bulunmaktadir.")
                biletadet = int(input("Bilet adeti giriniz: "))
                break
        except ValueError:
            print("Hatalı giriş!")
            continue
        boskoltuk[(kategori-1)] -= biletadet  # Yeni bos koltuk sayısı
        biletsayac=0
        print("Rezerve edilen koltuklar (sira-koltuk): ", end=" ")
        net_tutar=0
        toplam_tutar=0
        yapilan_indirim=0
        for i in range(0,20):  # Rezervasyon işlemi
            if (biletsayac < biletadet):
                toplam_tutar = biletadet * int(fiyat[1][1])
                if(kategori==1 and i<10):
                    for j in range(5, 15):
                        if (salon[i][j] == "-" and biletsayac < biletadet):
                            print((i+1),"-",(j+1), end=" ")
                            biletsayac+=1
                            salon[i][j] = "x"
                            if biletadet == 1:
                                toplam_ciro += int(fiyat[1][1])
                            elif biletadet>=int(fiyat[5][1]) and biletadet<=int(fiyat[5][2]):
                                toplam_ciro += ((int(fiyat[1][1]))/100)*(100-int(fiyat[5][3]))
                                net_tutar += ((int(fiyat[1][1])) / 100) * (100 - int(fiyat[5][3]))
                            elif biletadet>=int(fiyat[6][1]) and biletadet<=int(fiyat[6][2]):
                                toplam_ciro += ((int(fiyat[1][1])) / 100) * (100 - int(fiyat[6][3]))
                                net_tutar += ((int(fiyat[1][1])) / 100) * (100 - int(fiyat[6][3]))
                            elif biletadet>int(fiyat[6][2]):
                                toplam_ciro += ((int(fiyat[1][1])) / 100) * (100 - int(fiyat[7][3]))
                                net_tutar += ((int(fiyat[1][1])) / 100) * (100 - int(fiyat[7][3]))
                elif(kategori==2 and i<10):
                    toplam_tutar = biletadet * int(fiyat[2][1])
                    for j in range (4,-1,-1):
                        if (salon[i][j] == "-" and biletsayac < biletadet):
                            print((i + 1), "-", (j + 1), end=" ")
                            biletsayac += 1
                            salon[i][j] = "x"
                            if biletadet==1:
                                toplam_ciro+=int(fiyat[2][1])
                            elif biletadet>=int(fiyat[8][1]) and biletadet<=int(fiyat[8][2]):
                                toplam_ciro+=(int(fiyat[2][1])/100)*(100-int(fiyat[8][3]))
                                net_tutar += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[8][3]))
                            elif biletadet>=int(fiyat[9][1]) and biletadet<=int(fiyat[9][2]):
                                toplam_ciro += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[9][3]))
                                net_tutar += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[9][3]))
                            elif biletadet>int(fiyat[9][2]):
                                toplam_ciro += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[10][3]))
                                net_tutar += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[10][3]))
                    for j in range(15,20):
                        if (salon[i][j] == "-" and biletsayac < biletadet):
                            print((i + 1), "-", (j + 1), end=" ")
                            biletsayac += 1
                            salon[i][j] = "x"
                            if biletadet==1:
                                toplam_ciro+=int(fiyat[2][1])
                            elif biletadet>=int(fiyat[8][1]) and biletadet<=int(fiyat[8][2]):
                                toplam_ciro+=(int(fiyat[2][1])/100)*(100-int(fiyat[8][3]))
                                net_tutar += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[8][3]))
                            elif biletadet>=int(fiyat[9][1]) and biletadet<=int(fiyat[9][2]):
                                toplam_ciro += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[9][3]))
                                net_tutar += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[9][3]))
                            elif biletadet>int(fiyat[9][2]):
                                toplam_ciro += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[10][3]))
                                net_tutar += ((int(fiyat[2][1])) / 100) * (100 - int(fiyat[10][3]))
                elif(kategori==3 and i>9):
                    toplam_tutar = biletadet * int(fiyat[3][1])
                    for j in range(5, 15):
                        if (salon[i][j] == "-" and biletsayac < biletadet):
                            print((i+1),"-",(j+1),end=" ")
                            biletsayac += 1
                            salon[i][j] = "x"
                            if biletadet==1:
                                toplam_ciro+=int(fiyat[3][1])
                            elif biletadet>=int(fiyat[11][1]) and biletadet<=int(fiyat[11][2]):
                                toplam_ciro+=((int(fiyat[3][1]))/100)*(100-int(fiyat[11][3]))
                                net_tutar += ((int(fiyat[3][1])) / 100) * (100 - int(fiyat[11][3]))
                            elif biletadet>=int(fiyat[12][1]) and biletadet<=int(fiyat[12][2]):
                                toplam_ciro += ((int(fiyat[3][1])) / 100) * (100 - int(fiyat[12][3]))
                                net_tutar += ((int(fiyat[3][1])) / 100) * (100 - int(fiyat[12][3]))
                            elif biletadet>int(fiyat[12][2]):
                                toplam_ciro += ((int(fiyat[3][1])) / 100) * (100 - int(fiyat[13][3]))
                                net_tutar += ((int(fiyat[3][1])) / 100) * (100 - int(fiyat[13][3]))
                elif (kategori==4 and i>9):
                    toplam_tutar = biletadet * int(fiyat[4][1])
                    for j in range (4,-1,-1):
                        if (salon[i][j] == "-" and biletsayac < biletadet):
                            print((i + 1), "-", (j + 1), end=" ")
                            biletsayac += 1
                            salon[i][j] = "x"
                            if biletadet == 1:
                                toplam_ciro += int(fiyat[4][1])
                            elif biletadet >= int(fiyat[14][1]) and biletadet <= int(fiyat[11][2]):
                                toplam_ciro += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[14][3]))
                                net_tutar += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[14][3]))
                            elif biletadet >= int(fiyat[15][1]) and biletadet <= int(fiyat[15][2]):
                                toplam_ciro += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[15][3]))
                                net_tutar += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[15][3]))
                            elif biletadet > int(fiyat[15][2]):
                                toplam_ciro += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[16][3]))
                                net_tutar += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[16][3]))
                    for j in range(15,20):
                        if (salon[i][j] == "-" and biletsayac < biletadet):
                            print((i + 1), "-", (j + 1), end=" ")
                            biletsayac += 1
                            salon[i][j] = "x"
                            if biletadet == 1:
                                toplam_ciro += int(fiyat[4][1])
                            elif biletadet >= int(fiyat[14][1]) and biletadet <= int(fiyat[11][2]):
                                toplam_ciro += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[14][3]))
                                net_tutar += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[14][3]))
                            elif biletadet >= int(fiyat[15][1]) and biletadet <= int(fiyat[15][2]):
                                toplam_ciro += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[15][3]))
                                net_tutar += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[15][3]))
                            elif biletadet > int(fiyat[15][2]):
                                toplam_ciro += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[16][3]))
                                net_tutar += ((int(fiyat[4][1])) / 100) * (100 - int(fiyat[16][3]))
            else:
                break
        print("\n")
        yapilan_indirim=(toplam_tutar)-(net_tutar)
        print("Toplam Tutar: ",toplam_tutar)
        print("Yapilan İndirim: ",yapilan_indirim)
        print("Net Tutar: ",net_tutar)
        print("\n")
    elif(secim==2):
        for i in range(0,20):
            for j in range(0,20):
                print(salon[i][j], end=" ")
                if j==4 or j==14:
                    print("    ",end="")
                if j==19:
                    print(" ")
            if i==9:
                print("\n")
        print("\n")
    elif(secim==3):
        for i in range(0, 20):
            for j in range(0, 20):
                salon[i][j] = "-"
        boskoltuk = [100, 100, 100, 100]
        toplam_ciro=0
        print("Yeni etkinlik oluşturuldu.")
    elif(secim==4):
        print("Bu etkinliğin toplam cirosu:",toplam_ciro)
    elif(secim==0):
        quit()