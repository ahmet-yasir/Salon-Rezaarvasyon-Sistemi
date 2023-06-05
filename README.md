# Salon-Rezervasyon-Sistemi

Sinema, konser, tiyatro, vb. tarzı etkinliklerin düzenlendiği bir konser salonu için basit bir 
rezervasyon sistemi geliştirilecektir. Salondaki koltukların dizilimi aşağıda verilmiştir. 
Salondaki koltuklar 4 farklı fiyat kategorisinde değerlendirilmektedir. Sistem, her kategori için o 
andaki en uygun koltukları rezerve etmek üzerine tasarlanacaktır. Buna göre,  

1. kategoriye ilişkin bilet rezervasyon işlemleri, 1. sıra 6 numaralı koltuktan 
başlayacaktır. Herhangi bir sıranın 15. koltuğunun rezerve edilmesinin ardından 
bir arkadaki sıranın 6. koltuğundan itibaren rezervasyon işlemleri devam edecektir.  

2. kategoriye ilişkin bilet rezervasyon işlemleri, 1. sıra 5 numaralı koltuktan 
başlayacak ve rezerve sırası sola doğru işleyecektir. Sıra başındaki 1 numaralı 
koltuğun rezerve edilmesinin ardından, aynı sıradaki 16. koltuktan itibaren sağa 
doğru işlemlere devam edilecektir. Herhangi bir sıranın 20. koltuğunun rezerve 
edilmesinin ardından bir arkadaki sıranın 5. koltuğundan itibaren rezervasyon 
işlemleri devam edecektir.  

![image](https://github.com/ahmet-yasir/Salon-Rezaarvasyon-Sistemi/assets/131553807/e62c0bb7-3f48-402f-a7a7-92d0bb5cf682)

3. kategoriye ilişkin bilet rezervasyon işlemleri, 11. sıra 6 numaralı koltuktan 
başlayacaktır. Herhangi bir sıranın 15. koltuğunun rezerve edilmesinin ardından 
bir arkadaki sıranın 6. koltuğundan itibaren rezervasyon işlemleri devam edecektir.  

4. kategoriye ilişkin bilet rezervasyon işlemleri, 11. sıra 5 numaralı koltuktan 
başlayacak ve rezerve sırası sola doğru işleyecektir. Sıra başındaki 1 numaralı 
koltuğun rezerve edilmesinin ardından, aynı sıradaki 16. koltuktan itibaren sağa 
doğru işlemlere devam edilecektir. Herhangi bir sıranın 20. koltuğunun rezerve 
edilmesinin ardından bir arkadaki sıranın 5. koltuğundan itibaren rezervasyon 
işlemleri devam edecektir. 

Her kategorinin toplam koltuk kapasitesi 100’dür. Herhangi bir anda rezerve edilmek istenen 
toplam koltuk sayısı, o kategoride kalan boş koltuk sayısını aşıyorsa rezervasyon işlemi red 
edilmelidir.

## Program Arayüzü  
Program çalıştırıldığında ekrana bir ana menü gelir:   
Kullanıcı rezervasyon işlemi için 1 seçimini yaptığında , sırası ile kategori ve bilet adedini 
girmesi gerekecektir. Kategori 1-4 arasında olmalı; bilet adedi ise 1-10 arasında olmalıdır (yani 
tek bir işlemde 10’dan fazla bilet rezervasyonu yapılmayacaktır). Kullanıcı bu değerlerin dışında 
değerler girerse sistem aynı soruyu sormaya devam edecektir. Uygun değerler girildiğinde sistem 
rezervasyon işlemini yapacak ve sonuçta rezerve edilen koltuklar ekrana çıkarılacaktır.  

Rezervasyon işleminin ardından ana menü tekrar ekrana gelecektir. Kullanıcı tekrar 1 seçeneğini 
seçerse, yeni bir rezervasyon yapabilir. Herhangi bir rezervasyon işleminde istenen bilet adedi o 
kategoride kalan boş koltuk adedini aşıyorsa, rezervasyon yapılmamalı ve buna ilişkin bir mesaj 
ekrana çıkartılmaldır.  

Ana menüden 2 seçeneği seçilirse, boş koltuklar “-“ dolu koltuklar “X” ile gösterilecek şekilde 
salonun genel görünümü ekrana yansıtılmalıdır.

Ana menüden 3 seçeneği seçilirse, sistem var olan tüm rezervasyonları sıfırlamalıdır. Diğer bir 
deyişle salon sanki yeni bir etkinlik için ilk durumunu almalıdır (bu aşamada kullandığınız tüm 
değişkenleri başlangıç durumuna getirmeniz gerekecektir).  

Her işlemin sonunda ana menü tekrar ekrana gelmelidir. Herhangi bir anda 0 seçeneği seçilirse 
program sonlanacaktır.   

Geliştirdiğiniz uygulamaya ücret ve indirim bilgilerinin entegre edilmesi istenmektedir. 
Tüm kategoriler için bir kerede en fazla kaç bilet satılacağı bilgisi ile, her kategoride satın alınan 
bilet adedine göre uygulanacak indirim tutarları, "indirim.txt" isimli bir dosyadan okunacaktır. 

Örnek bir "indirim.txt" dosyası aşağıda görülebilir :  

![image](https://github.com/ahmet-yasir/Salon-Rezaarvasyon-Sistemi/assets/131553807/9fc831da-48cb-4748-b06d-935fcbcdccc4)  

Dosyanın ilk satırı : M-XX şeklinde olup, XX sayısı tüm kategoriler için geçerli olmak üzere, bir 
seferde satın alınabilecek maksimum bilet sayısını göstermektedir (yukarıdaki örnekte, max. 30 
bilet). Rezervasyon işlemlerinde bu sayıdan daha fazla bilet alınmak istendiğinde hata mesajı 
çıkarılmalıdır.  

Dosyanın 2., 3., 4. ve 5. satırları, her kategori için bir bilet ücretini göstermektedir (yukarıdaki 
örnekte; 1. kategori 200TL, 2.kategori 150TL, 3.kategori 100TL ve 4.kategori 60TL 'dir). 

Dosyanın geri kalan (6. satır ve sonrası) satırları K-MIN-MAX-ORAN formatındadır. 

K : kategori  
MIN : bilet adedi alt limit  
MAX : bilet adedi üst limit  
ORAN : uygulanacak indirim oranı  

Bir örnek olarak: 1-05-10-10 şeklinde bir satır; 1. kategoride [5-10] aralığında adette bir bilet 
alımı yapıldığında toplam ücrette %10'luk bir indirim uygulanacağı anlamına gelmektedir.  

Bu bilgiler ışığında, ilk aşamada yazdığınız uygulama için yapmanız gereken ilaveler özetle 
şunlardır :  

1. "indirim.txt" dosyasının program içinde uygun veri yapılarına okunmalıdır (değişken, liste, 
sözlük gibi yapılardan yararlanabilirsiniz).  

2. Ana menüden Rezervasyon seçeneği seçildiğinde;   
• • Bilet adedinin maksimum değeri geçip geçmediğinin kontrolü yapılmalıdır. İzin verilen 
maksimum sayıdan daha fazla bilet istendiğinde hata mesajı verdirilip ana menüye 
dönülmelidir.    
• • Rezerve edilecek bilet adedi uygunsa, ücret bilgisi hesaplanmalı ve rezerve edilen 
koltuklar yazdırıldıktan sonra toplam ücret de ekrana yansıtılmalıdır (bilet adedi, toplam 
tutar, yapılan indirim, net tutar şeklinde).  

3. Ana menüye "Toplam Ciro" şeklinde yeni bir seçenek eklenmeli ve satılan biletler 
bağlamında her kategori için elde edilen ücret toplamları ile salonun toplam cirosu ekrana 
yazdırılmalıdır (Her bilet satışından sonra oluşan ücret bilgisini ayrı toplamlarda 
saklayabilirsiniz).

