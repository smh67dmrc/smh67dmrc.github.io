---
layout: post
title: "STMCTF'19 Write-Up Misc Particle"
date: 2021-02-12 05:00:00 +0300
description: STMCTF'19 Write-Up Misc Particle
img: stmctf19.jpg
tags: [STMCTF19]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Misc` kategorisinden `Particle` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [flag1401.rar]

Soruda `flag1401` isminde bir rar dosyası verilmiş. Rar dosyasını açtıktan sonra karşımıza `flag466.txt` ve `flag1400.rar` dosyaları çıkıyor. `flag466` isimli text dosyasını okuduğumuzda içinde `e` karakteri olduğunu görüyoruz. Peki `flag1400.rar` içinden ne çıkacak? 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-a1.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-a1.png" alt="image-1" /></a>
	</div>
</center>

Rar dosyası içinden çıkanları anlayabilmek için `flag1400.rar` dosyasını da açıyoruz ve içinden sadece `flag1399.rar` dosyası çıktığını görüyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-a2.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-a2.png" alt="image-1" /></a>
	</div>
</center>

Rar dosyası ismindeki sayısal değerin her bir extract işleminden sonra birer birer azaldığını gördük. İç içe geçmiş rar dosyalarını tek tek extract etmek mantıklı bir yaklaşım olmayacaktır. Bu yüzden bir python scripti yazarak bütün rar dosyalarını extract edebiliriz. 

```python
import os

counter = 1401
name = "flag" + str(counter) + ".rar"

while name != "flag0.rar":

        os.system("unrar e " + name)
        os.system("rm -r " + name)
        counter = counter-1
        name = "flag" + str(counter) + ".rar"
        os.system("clear")

print("islem basarili :)")
```

Python scriptimizi çalıştırdığımızda tüm rar dosyaları extract edilmiş oldu. Karşımıza sıralı olarak `467` adet txt dosyası çıktı.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-a3.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-a3.png" alt="image-1" /></a>
	</div>
</center>

Text dosyalarının içine rastgele baktığımızda her bir dosya içinde sadece bir karakter olduğunu farkediyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-a4.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-a4.png" alt="image-1" /></a>
	</div>
</center>

Tüm bu dosyaların içeriğini sıralı olarak okuyacak bir python scripti yazalım.

```python
import os

counter = 0
characters = ""

while counter != 467:

        file = open("flag" + str(counter) + ".txt", "r")
        temp = file.read()
        characters += temp[0]
        counter += 1
        file.close()

print(characters)
```

Tüm karakterleri sıralı olarak okuduğumuzda karşımıza uzun bir metin çıkıyor:

```
zeroonetwothreezeroonetwofourzerooneonefivezeroonezerothreezeroonetwofourzeroonezerosixzerooneseventhreezeroonezerothreezerosixzerozeroonefivesixzeroonezerosevenzeroonesixtwozerosixfourzeroonesixfourzerooneseventwozerofivesixzerofouronezeroonethreeonezeroonefivesevenzeroonesixfivezeroonethreesevenzeroonezerosixzerosixzerozeroonesixfivezeroonefivesixzeroonezerofourzeroonethreesevenzerooneonefivezerosixthreezeroonethreesevenzeroseventhreezerofiveonezeroonesevenfive
```

Metni incelediğimizde aslında rakamların yazı karşılıklarının olduğunu görüyoruz. Herhangi bir text editorün replace özelliği ile rakamlara çevirelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-a5.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-a5.png" alt="image-1" /></a>
	</div>
</center>

Sayısal görünüme çevirdikten sonra rakamları inceleyelim. Karakter setini ortaya çıkarttığımızda rakamlar arasında `8` ve `9` sayılarının hiç bulunmadığını farkettik : `01234567`  Bu durumda bu sayı dizisi `octal(sekizlik)` formdadır.

```
0123012401150103012401060173010306001560107016206401640172056041013101570165013701060600165015601040137011506301370730510175
```

Octal formdan ascii formatına çevirmek için sayı dizisinde fazla olan `0(sıfır)` rakamlarını da çıkartarak ayıralım.

```
123 124 115 103 124 106 173 103 060 156 107 162 064 164 172 056 041 131 157 165 137 106 060 165 156 104 137 115 063 137 073 051 175
```

Online bir converter'a([http://www.unit-conversion.info/texttools/octal/]) verip ascii karşılığını görelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-a6.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-a6.png" alt="image-1" /></a>
	</div>
</center>

Flag değerimizi elde etmiş oluyoruz.

```
STMCTF{C0nGr4tz.!You_F0unD_M3_;)}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'19]: https://ctfonline.stm.com.tr/
[flag1401.rar]: {{site.baseurl}}/assets/files/flag1401.rar
[http://www.unit-conversion.info/texttools/octal/]: http://www.unit-conversion.info/texttools/octal/
