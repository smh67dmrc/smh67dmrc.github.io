---
layout: post
title: "STMCTF'19 Write-Up Misc Circuit"
date: 2020-12-31 05:00:00 +0300
description: STMCTF'19 Write-Up Misc Circuit
img: stmctf19.jpg
tags: [STMCTF19]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Misc` kategorisinden `Circuit` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [circuit.png]

Soruda `circuit` isminde bir png dosyası verilmiş. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/circuit.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/circuit.png" alt="image-1" /></a>
	</div>
</center>

Soruda sadece resim verildiği için resmi incelemeye başlıyoruz. Birçok teknik uyguladıktan sonra sıra bir image editor ile resmi incelemeye geliyor. Gimp bu işi yapabilen faydalı araçlardan biridir. Gimp ile resmin parlaklık ayarlarını değiştirdiğimizde gizli olan binary şeklinde bir data karşımıza çıkıyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-20.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-20.png" alt="image-1" /></a>
	</div>
</center>

Binary datayı text formatına çevirmemiz gerekir. Fakat uzun bir bit dizisi olduğu için elle yazmak pek mantıklı değil. Bu yüzden OCR tekniği kullanan bir araç ile resim içerisindeki binary datayı text halinde export edelim. Kullanacağımız araç online bir araçtır.([https://convertio.co/tr/ocr/]) Aracın doğru sonucu verebilmesi için beyaz-siyah renk oranını net bir ayrım sağlayacak şekilde gimp üzerinden resimde değişiklik yaparak `bits.png` olarak kaydedelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-21.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-21.png" alt="image-1" /></a>
	</div>
</center>

`bits.png` olarak hazırladığımız resmi siteye upload ediyoruz ve txt formatında çıktı üretmesini istiyoruz. `bits.ocr.txt` olarak indirdiğimiz text dosyasını açıyoruz. Dosyayı açtığımızda birkaç tane "0" değerinin "Q" şeklinde kaydedildiğini görüyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-22.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-22.png" alt="image-1" /></a>
	</div>
</center>

Tüm "Q" olan karakterleri "0" ile değiştirip kaydedelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-23.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-23.png" alt="image-1" /></a>
	</div>
</center>

Binary datamızı kullanılabilir hale getirmiş oluyoruz. Şimdilik binary datamız kenarda dursun. Elimizde bir devre ve bit dizisi var. Bu bit dizisinin devrenin inputu olacağını ve devredeki ledlerin output bitlerini oluşturacağını düşünüyoruz. Peki bu output bitlerini nasıl hesaplayacağız? Hesabı yapabilmenin birçok yöntemi var. Bir yöntem devre çizimi yapabilen araçlardan(Örnek olarak : Multimedia Logic) yararlanmaktır. Bir yöntem ise manuel olarak devre analizini yaparak hangi inputta hangi outputu verdiğini bulmaktır. Manuel olarak devre analizini yapalım. Öncelikle input olarak "3" input alanımız var. Değer olarak "0" ve "1" bitlerini verebiliyoruz. Dolayısıyla `2^3` hesabından "8" farklı input olabilir. Bu ihtimaller aşağıdaki şekildedir:

```
Input1 : 000
Input2 : 001
Input3 : 010
Input4 : 011
Input5 : 100
Input6 : 101
Input7 : 110
Input8 : 111
```

İlk satırdaki `000` bitlerini örnek olarak devremize verelim ve output bitlerini bulalım. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-24.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-24.png" alt="image-1" /></a>
	</div>
</center>

Yukarıdaki örnekteki gibi "8" input için bu işlemleri yaptığımızda "8" tane output bit dizisi elde ederiz. Output bit dizileri aşağıdaki şekildedir.

```
INPUT => OUTPUT
000 => 001
001 => 010
010 => 111
011 => 100
100 => 101
101 => 110
110 => 011
111 => 000
```

Artık hangi inputa karşılık hangi outputun geleceğini bildiğimiz için bir python scripti yazarak bit dizisini devreden geçirip output bit dizisini elde edelim ve output bit dizisinin ascii karşılığını bulalım.

```python

import binascii

input1 = "000" 
input2 = "001" 
input3 = "010" 
input4 = "011" 
input5 = "100" 
input6 = "101" 
input7 = "110" 
input8 = "111" 

file_open = open("bits.ocr.txt", "rw+")
line = file_open.readline()
result = ""
counter = 0

while counter < 240:

        if line[counter] == "0":
                if line[counter+1] == "0":
                        if line[counter+2] == "0":
                                result += input2 
                        else:
                                result += input3
                else:
                        if line[counter+2] == "0":
                                result += input8
                        else:
                                result += input5
        else:
                if line[counter+1] == "0":
                        if line[counter+2] == "0":
                                result += input6
                        else:
                                result += input7
                else:
                        if line[counter+2] == "0":
                                result += input4
                        else:
                                result += input1
        counter += 3

print("result : " + result)

file_open.close()

value = int(result, 2)
ascii_value = binascii.unhexlify('%x' %value)
print("\nFlag : " + str(ascii_value))

```
<br>
```
result : 010100110101010001001101010000110101010001000110011110110100011001101100001101000100011101011111011001110011001101001110011001010101001000110100011101000011000001010010010111110100001100110001010100100110001101010101001100010101010001111101

Flag : STMCTF{Fl4G_g3NeR4t0R_C1RcU1T}
```

Script çalıştıktan sonra flag değerimizi elde etmiş oluyoruz.

```
STMCTF{Fl4G_g3NeR4t0R_C1RcU1T}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'19]: https://ctfonline.stm.com.tr/
[circuit.png]: {{site.baseurl}}/assets/files/circuit.png
[https://convertio.co/tr/ocr/]: https://convertio.co/tr/ocr/
