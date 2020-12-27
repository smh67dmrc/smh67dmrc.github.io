---
layout: post
title: "Siber Yıldız 2020 Write-Up EKS Elektrikler Gitti"
date: 2020-12-27 05:00:00 +0300
description: Siber Yıldız 2020 Write-Up EKS Elektrikler Gitti
img: siberyildiz.png
tags: [Siberyıldız]
---
Selamlar, bu yazımda [Siber Yıldız 2020] yarışmasında sorulan `Elektrikler Gitti` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [Siber_Yildiz_ICS.pcap]

Soruda `Siber_Yildiz_ICS` isminde bir pcap dosyası verilmiş. Ağ analizini yaparak flag değerini elde etmemiz istenmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-10.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-10.png" alt="image-1" /></a>
	</div>
</center>

Pcap dosyasını wireshark aracıyla incelediğimizde içinde birçok protokole ait paket olduğunu farkediyoruz. Fakat soru adının `Elektrikler Gitti` olması ve kategorisinin `EKS` olması bize ipucu veriyor. Aradığımız paket türü endüstriyel sahada kullanılan bir protokole ait olabilir diye düşünerek incelemeye devam ediyoruz. İstatistikler sekmesinden protokol hiyerarşisini incelediğimizde pcap içindeki tüm protokolleri görüyoruz. Protokol hiyerarşisi içerisinde `EKS` spesifik `ModbusTCP` protokolünü ve `S7Comm` protokolünü görüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-11.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-11.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-12.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-12.png" alt="image-1" /></a>
	</div>
</center>

Pcap içerisindeki paket oranlarına baktığımızda `ModbusTCP` protokolünün `S7Comm`'a göre daha fazla pakete sahip olduğunu görüyoruz. Bu bir ipucu mu yoksa bir yanıltmaca mı diye öğrenmek için pcap'i incelemeye devam ediyoruz. Pcap içinde `FTP` trafiğinin olduğunu görüyoruz. FTP trafiğini incelediğimizde `Aciklama.txt` isminde bir text dosyasının transfer edildiğini görüyoruz. İlgili pakete sağ tıklayıp `Follow -> TCP Stream` seçeneği ile akışı görebiliriz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-13.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-13.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-14.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-14.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-15.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-15.png" alt="image-1" /></a>
	</div>
</center>

Transfer edilen dosyayı bulabilmek için `ftp-data` filtresini kullanıyoruz. Filtre sonucunda karşımıza çıkan iki paketten birinde `Aciklama.txt` dosyasının yer aldığını görüyoruz. Sağ alttaki kısımda text dosyasının içinde bir `python` scriptinin olduğunu farkediyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-16.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-16.png" alt="image-1" /></a>
	</div>
</center>

Python scriptini daha net görebilmek ve scripti export edebilmek için ilgili pakate sağ tıklayıp `Follow -> TCP Stream` seçeneği ile açıyoruz. Açtıktan sonra python scriptini `eks.py` ismiyle kaydedelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-17.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-17.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-18.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-18.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-19.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-19.png" alt="image-1" /></a>
	</div>
</center>

Python scriptini incelediğimizde flag değerini verilen inputa göre ürettiğini görüyoruz. Peki bu input nedir?

```python

#!/usr/bin/python
#coding:utf-8

coils_bytes = '**********************************'.decode('hex')
print len(coils_bytes)
flag = ''
for data in coils_bytes:
        #print int('{:08b}'.format(ord(data)))
        #print int('{:08b}'.format(ord(data)), 2)
        #print int('{:08b}'.format(ord(data))[::-1])
        #print int('{:08b}'.format(ord(data))[::-1], 2)
    #print int('{:08b}'.format(ord(data)),2),int('{:08b}'.format(ord(data))[::-1], 2)
    flag += chr(int('{:08b}'.format(ord(data))[::-1], 2))
print flag

```

Python scripti içerisindeki input değerini tutan değişkenin ismi ipucu niteliğinde : `coils_bytes`. Coil değişkeni ModbusTCP protokolünde kullanılan bir değişken tipidir. 

Öncelikle ModbusTCP iletişimini anlamamız için protokol hakkında bilgi sahibi olmamız gerekir. ModbusTCP protokolü seri haberleşme ile değerleri `cleartext` olarak gönderir. ModbusTCP iletişiminde 2 taraf vardır: `Master Cihaz` ve `Slave Cihaz`. Master cihazı IT altyapılarında bulunan istemci(client) cihazlara benzetebiliriz. Slave cihazı ise yine IT altyapılarında bulunan sunucu(server) cihazlarına benzetebiliriz. Master ve slave cihazlar arasında istemci-sunucu mimarisine benzer şekilde `request-response` ilişkisi bulunur. Master cihaz slave cihaza istek paketi gönderir ve slave cihazdan gelen yanıtı bekler. Fakat buradaki bir diğer önemli husus ModbusTCP protokolünde bulunan fonksiyon kodlarıdır. `Fonksiyon kodları` protokol içinde gönderilen paketin içinde bulunan bir değerdir. Bu değer ile slave cihaz master cihazın isteğinin ne olduğunu anlar.

S7comm yerine ModbusTCP paketlerine bakmamız gerektiğini anlamış olduk. `Modbus` filtresiyle birlikte ModbusTCP paketlerini inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-191.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-191.png" alt="image-1" /></a>
	</div>
</center>

Yukarıdaki görselde görüldüğü üzere `fonksiyon kodu 15`'tir. Bunun anlamı `Write Multiple Coils` şeklinde bir görev tanımıdır. Bu görev tanımıyla master cihaz slave cihaza der ki: göndermiş olduğum datayı benim sana belirtmiş olduğum birime kaydet. Yani bir başka deyişle slave cihaz üzerindeki coil değişkenlerinin değer alanına datayı yaz. Write görevi olan fonksiyon kodlarında `data` alanı, query paketleri içindedir. Bir query paketinin içindeki dataya bakalım. 28 byte uzunluğunda bir data gördük. Python scriptimize verebileceğimiz türden bir data. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-192.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-192.png" alt="image-1" /></a>
	</div>
</center>

Peki vereceğimiz data gerçekten bu mu? Birden çok query paketi var. Öncelikle response paketlerini eleyelim. `modbus.data` filtresiyle sadece query paketlerini görelim. 403 adet query paketinin olduğunu farkediyoruz. Manuel olarak tek tek data alanlarına bakmak pek mantıklı değil. Bu işi otomatize hale getirmeliyiz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-193.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-193.png" alt="image-1" /></a>
	</div>
</center>

Query paketleri içindeki data alanlarının hepsini tek seferde alabilmek için `tshark` aracını kullanabiliriz. Öncelikle tshark aracına verebilmek için sadece query paketlerinden oluşan bir pcap dosyası olarak paketleri export edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-194.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-194.png" alt="image-1" /></a>
	</div>
</center>

Dosya adını `queries.pcap` olacak şekilde yazalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-195.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-195.png" alt="image-1" /></a>
	</div>
</center>

Tshark aracının outputunda tekrar edecek sonuçları da eleyerek tüm modbus data alanlarını görelim.  

```
kali@kali:~/siberyildiz2020$ tshark -r ./queries.pcap -T fields -e modbus.data | sort | uniq
9a86d63686ce2e9676fa82b686fa9a86763696cefa0a86d6a62e0000

f46c6c9c2ccc8666c61c0c66661c4ca6462cec0cec46c626462caccc2c9c86c6ac740e160efc9626bcac6c2c666c2ccc2c1ca666268626a69c0ccc86cc461ccc869c1cacecac9c260c
```

Karşımıza iki farklı hex değeri geliyor. Daha önceden kaydetmiş olduğumuz `eks.py` isimli python scriptimizdeki `coils_bytes` değişkeni içerisine bu iki hex değerini sırasıyla yazarak scripti çalıştıralım.

```python

#!/usr/bin/python
#coding:utf-8

coils_bytes = '9a86d63686ce2e9676fa82b686fa9a86763696cefa0a86d6a62e0000'.decode('hex')
print len(coils_bytes)
flag = ''
for data in coils_bytes:
        #print int('{:08b}'.format(ord(data)))
        #print int('{:08b}'.format(ord(data)), 2)
        #print int('{:08b}'.format(ord(data))[::-1])
        #print int('{:08b}'.format(ord(data))[::-1], 2)
    #print int('{:08b}'.format(ord(data)),2),int('{:08b}'.format(ord(data))[::-1], 2)
    flag += chr(int('{:08b}'.format(ord(data))[::-1], 2))
print flag

```
<br>
```
kali@kali:~/siberyildiz2020$ sudo python eks.py 
28
Yaklastin_Ama_Yanlis_Paket
```

Yanlış paketteki değer ile flag değerini oluşturmaya çalıştığımızı söyleyen bir yanıt ile karşılaştık. Diğer hex değerini deneyelim.

```python

#!/usr/bin/python
#coding:utf-8

coils_bytes = 'f46c6c9c2ccc8666c61c0c66661c4ca6462cec0cec46c626462caccc2c9c86c6ac740e160efc9626bcac6c2c666c2ccc2c1ca666268626a69c0ccc86cc461ccc869c1cacecac9c260c'.decode('hex')
print len(coils_bytes)
flag = ''
for data in coils_bytes:
        #print int('{:08b}'.format(ord(data)))
        #print int('{:08b}'.format(ord(data)), 2)
        #print int('{:08b}'.format(ord(data))[::-1])
        #print int('{:08b}'.format(ord(data))[::-1], 2)
    #print int('{:08b}'.format(ord(data)),2),int('{:08b}'.format(ord(data))[::-1], 2)
    flag += chr(int('{:08b}'.format(ord(data))[::-1], 2))
print flag

```
<br>
```
kali@kali:~/siberyildiz2020$ sudo python eks.py 
73
/66943afc80ff82eb4707bcdb45349ac5.php?id=564f64348efdade903a3b83a985759d0
```

Bingo! Flag değerini alacağımız adrese ait path değerini elde etmiş olduk. Soruya ait IP adresine path olarak ekleyip flag değerimizi alalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-196.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-196.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-197.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-197.png" alt="image-1" /></a>
	</div>
</center>

Yarışma sorusunu hazırlayan ve yarışmayı düzenleyen ekibe teşekkürler.

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Siber Yıldız 2020]: https://www.siberyildiz.com/
[Siber_Yildiz_ICS.pcap]: {{site.baseurl}}/assets/files/Siber_Yildiz_ICS.pcap
