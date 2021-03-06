---
layout: post
title: "Battleware CTF Write-Up Crypto Names"
date: 2021-01-08 05:00:00 +0300
description: Battleware CTF Write-Up Crypto Names
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Crypto` kategorisinden `Names` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 7.Haftada sorulan sorulardan biridir.

Soru dosyası : [names.rar]

Soruda `names` isminde bir `rar` dosyası verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-90.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-90.png" alt="image-1" /></a>
	</div>
</center>

Rar dosyası içerisine baktığımızda 4 tane text dosyası olduğunu gördük.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-91.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-91.png" alt="image-1" /></a>
	</div>
</center>

Dosya isimleri özellikle ipucu olması için `c,p,q,e` şeklinde isimlendirilmiş. `Crypto` kategorisinden bir soru olduğu için text dosyası isimlerinden kullanmamız gereken şifreleme algoritmasının `RSA` şifreleme olduğu anlaşılıyordu. Ama bir problem var. Bu değerler hesap yapabilmemiz için sayısal değerler olmalı. Fakat dosya içeriklerine baktığımızda farklı bir formatta içeriğin olduğunu gördük.

Örnek olarak `q.txt` içeriği :

```
11011 00111 10110 11000 00001 10011 10011 10011 11000 01010 10000 00001 10111 10110 11000 10101 11000 10110 10101 00001 00001 00111 10111 00111 00110 01010 00111 00110 10101 00111 00111 01010 10110 01010 10000 10011 10011 00110 00110 11000 10000 01010 00111 10101 00001 00001 10101 10101 00001 01010 10000 00111 10011 10111 00001 00110 10000 11000 10011 10101 10101 10111 00111 10011 10101 01010 00001 10011 10000 01010 10101 10000 01010 00111 00111 10110 10000 11000 10110 10011 00001 10011 10101 10011 10110 10011 00110 00001 10111 00001 10000 10000 00001 10101 10101 10111 10011 10101 00001 01010 10011 00110 10011 00110 11000 00001 10110 00110 00110 00111 00111 10110 00110 10011 10011 10111 10011 11000 10110 00001 10000 10000 10011 00001 10000 00111 00111 00111 10111 00110 10011 10101 10000 00111 11000 10000 10111 00110 01010 10110 00110 11000 11000 10011 10000 01010 11000 00110 10011 10011 10101 10000 10110 00110 10000 10011 10101 10111 10011 11000 01010 00110 01010 11000 01010 01010 00001 00001 10110 00001 10101 10000 10000 10110 11000 00111 10000 10011 01010 10111 01010 10101 00111 00111 10111 10110 00110 10111 00110 10101 10000 10110 11000 10110 00110 10111 10011 10000 11000 11000 10111 00110 11000 10011 11000 10111 10101 11000 10000 10000 01010 01010 10110 10111 10011 10011 10110 00111 00111 01010 10111 10110 10000 10101 10111 01010 00110 00110 10101 01010 10111 11000 10110 10111 00001 10000 10111 10011 10011 10111 10011 10000 10000 10110 00110 10101 10101 10000 10000 10000 10000 10101 10111 01010 00110 00110 00110 10000 10000 11000 10000 01010 00110 00110 00001 01010 10000 10111 10000 10011 10000 00001 00001 11000 00111 00110 10011 11000 10101 00110 00110 10110 11000 10111 00001 10011 01010 00001 10011 00111 11000 01010 10101 00001 01010 10111 11000 00110 10110 10101 10111 00110 11000 10111 00001 10110 10011 10101 00110 00110 10101 11000 10111 00110 01010 00001 00001 10011 00111 10011 00110 11000 10000 01010 11000 00111 11000 10000 10000 00001 00111 10011 10111 10111 00110 00111 00001 10111 10110 10101 10110 00001 10011 00001 00111 00001 10000 10000 10000 00111 00111 10110 00001 00111 00111 10011 10111 10110 00111 10011 10101 01010 10000 01010 11000 10111 10111 10011 10111 10110 01010 10000 10011 10111 00110 00110 10110 10000 10011 00110 00001 11000 10111 10111 10101 00001 10011 00111 00110 00001 01010 00111 00110 01010 10011 00111 10101 00111 10000 01010 10110 11000 10111 00110 11000 10110 01010 11000 10111 10110 10111 11000 10110 01010 10101 00001 11000 00001 10110 00001 00111 00111 11000 10000 10101 10011 10101 10111 10011 00001 01010 00001 00111 10011 11000 10110 01010 10101 00111 11000 10111 00001 00110 10011 10111 10000 00110 10111 01010 10101 10011 10111 10101 11000 01010 10000 10000 10101 10011 10000 10111 01010 00110 00110 11000 00111 10011 01010 00110 00110 00110 10110 00111 00110 11000 00110 00001 10000 10011 10000 11000 10101 00111 10000 00001 10101 00111 00110 10011 10111 10111 11000 01010 01010 10000 10111 10111
```

İlk başta dosya içeriği binary ifade gibi görünüyor. Soruda verilen ipucunda binary olmadığı söylendiği için başka bir format olmalı diye düşündük. Telgraf iletişiminden bahsedildiği için aklımıza morse code olabileceği geldi. Tüm denemelerimize rağmen morse code ile decode ettiğimizde anlamlı bir çıktıya ulaşamadık. Peki bu format neydi ve nasıl olacaktı ki sayısal değere dönüşecekti?

İnternette beşli gruplar halinde karakter seti 0 ve 1'lerden oluşan bu formata benzer encoding tekniklerini araştırdığımızda daha önceden karşılaşmadığımız bir encoding tekniğini keşfettik : `Baudot-Murray-Code`.

4 dosya içeriğini de [https://v2.cryptii.com/ita2/text] adresindeki online decoder'ı kullanarak decode ettik.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-92.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-92.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-93.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-93.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-94.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-94.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-95.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-95.png" alt="image-1" /></a>
	</div>
</center>

RSA şifrelemede kullacağımız sayısal değerleri elde ettik.

```

e değeri : 65537

p değeri : 327721

c değeri : 648282232071909432378396477790994964321638277611102824678929034087137641946421438506794009162027209797666374205951430817992595202913560302264135553641509423441513509002433073005732128883937375881893675821594845944567605518885634205861732446939501024757755279529051140023540539623206199212032727808512359501466115077849107407441879992473130352274957667559082992889238747778968227705051174549125385652513066138306171637448845156385467511644247602504520404297663256902472678875167300170945757039160930606

q değeri : 7093222945310969063371784786774045228895476336634572138592661726432546547705902326202831355366126342828930887708221290355235777182657951840899254982265085261294849443303655097524146771081865090812599189291695544012207741056148864190135122125508665555614888559548834515253397829688091324327946341980618913026886918433272895497955372118731060323735557703772107264549112104521880528391163278347842767540918904910190463930377956261234372904679138215814621694556251488972488807898352596753678211944511

```

RSA şifreleme kullanarak bu 4 değer ile flag değerini oluşturmak için çok güzel bir araçtan faydalanacağız : `RsaCtfTool`

C değerimiz ciphertext metnimiz anlamına geliyor. Yazının uzamaması için RSA şifrelemeden kısaca bahsedelim. RSA şifreleme matematiksel işlemler ile çok büyük basamaklı asal sayıları kullanarak şifreleme ve şifre çözme işlemi yapan bir algoritmadır. Şifrelemede kullanılan bit sayısının artması ve asal sayıların tahmin edilememesi şifrenin kırılamamasını sağlar.

Kısa bir önbilgiden sonra elimizdeki 4 değeri `RsaCtfTool` aracına verelim ve şifreli metnimizi plaintext haline çevirerek flag değerimizi elde edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-96.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-96.png" alt="image-1" /></a>
	</div>
</center>
<br>

```
kali@kali:~/RsaCtfTool$ python3 RsaCtfTool.py -p 327721 -q 7093222945310969063371784786774045228895476336634572138592661726432546547705902326202831355366126342828930887708221290355235777182657951840899254982265085261294849443303655097524146771081865090812599189291695544012207741056148864190135122125508665555614888559548834515253397829688091324327946341980618913026886918433272895497955372118731060323735557703772107264549112104521880528391163278347842767540918904910190463930377956261234372904679138215814621694556251488972488807898352596753678211944511 -e 65537 --uncipher 648282232071909432378396477790994964321638277611102824678929034087137641946421438506794009162027209797666374205951430817992595202913560302264135553641509423441513509002433073005732128883937375881893675821594845944567605518885634205861732446939501024757755279529051140023540539623206199212032727808512359501466115077849107407441879992473130352274957667559082992889238747778968227705051174549125385652513066138306171637448845156385467511644247602504520404297663256902472678875167300170945757039160930606
```

Flag değerimizi elde etmiş oluyoruz.

```
Flag{r1v3sT_Sh4m1R_adL3m4N}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/
[names.rar]: {{site.baseurl}}/assets/files/names.rar
[https://v2.cryptii.com/ita2/text]: https://v2.cryptii.com/ita2/text

