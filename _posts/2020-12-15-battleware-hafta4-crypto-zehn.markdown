---
layout: post
title: "Battleware CTF Write-Up Crypto Zehn"
date: 2020-12-15 05:00:00 +0300
description: Battleware CTF Write-Up Crypto Zehn
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Crypto` kategorisinden `Zehn` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 4.Haftada sorulan sorulardan biridir.

Soru dosyası : [n3rd.rar]

Soruda `n3rd.txt` isminde bir metin dosyası verilmiş. Dosyayı incelediğimizde boyutunun sıradan bir metin dosyasına göre çok büyük olduğunu görüyoruz. 

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ file n3rd.txt 
n3rd.txt: ASCII text, with very long lines, with no line terminators
kali@kali:~/battleware-ctf/hafta4$ ls -lh n3rd.txt | cut -d " " -f 5
58M
{% endhighlight %}
 
Dosya büyük olduğu için sadece belirli kısımları okuyarak ilerlemek daha sağlıklı bir metot olacaktır. Öncelikle satır sayısını öğrenelim.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ wc -l n3rd.txt 
1 n3rd.txt
{% endhighlight %}

Görüldüğü gibi sadece 1 tane satırda uzun bir metnin olduğunu farkediyoruz. Bu durumda satır satır incelemek mümkün olmadığı için örnek bir karakter seti okumalıyız. ilk 200 karakteri okuyarak bir inceleme yapalım.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ head -c 200 n3rd.txt 
Vm0wd2QyVkZOVWRXV0doVlYwZFNUMVpzWkc5V01WbDNXa2M1VjFac2JETlhhMk0xVmpGYWRHVkliRmROYWxaeVZteFZlRll5VGtWUmJIQk9UVEJLU1ZadGNFZFpWMDE0Vkc1T1lWSnRVbGhVVkVwdlpWWmFkR1ZIUmxwV01ERTBWakkxUjFZeVNsWlhiRkpYWVd0YVRG
{% endhighlight %}

Komut çıktısındaki karakterleri incelediğimizde `büyük harfleri`, `küçük harfleri` ve `rakamları` görüyoruz. Eğer CTF geçmişiniz varsa bu değerlerin `base64` ile encode edilmiş bir karakter seti olduğunu farketmek zor olmayacaktır. [Base64] olduğunun anlaşılmadığı durumda uygulanabilecek bir yöntem internette bu karakter setine sahip algoritmaları araştırmak olacaktır. Bir diğer yöntem ise online cipher identifier araçları olabilir.

Son olarak base64 encoded data sonunda bulunan "=" eşittir işareti ipucu verebilir.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ tail -c 10 n3rd.txt
Rd1BRPT0=
{% endhighlight %}

Bu soruda "=" eşittir işareti olduğu için geçerli bir yöntem sayılabilir. Fakat bu işaret bazen güvenilir bir ipucu olmayabilir. Çünkü her base64 encoded data sonunda "=" eşittir işareti olmayabilir. Bunun yerine karakter setinin incelenmesi önerilir. 

Elimizde uzunca bir base64 encoded data var. 1 kez decode edelim ve sonuçları inceleyelim.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ cat n3rd.txt | base64 --decode > decoded.txt
kali@kali:~/battleware-ctf/hafta4$ ls -lh n3rd.txt decoded.txt | cut -d " " -f 5,9
43M decoded.txt
58M n3rd.txt
{% endhighlight %}

1 kez decode işlemini gerçekleştirdikten sonra dosya boyutunun azaldığını gördük. Decode edilmiş haline yakından bakalım.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ head -c 200 decoded.txt 
Vm0wd2VFNUdWWGhVV0dST1ZsZG9WMVl3Wkc5V1ZsbDNXa2M1VjFadGVIbFdNalZyVmxVeFYyTkVRbHBOTTBKSVZtcEdZV014VG5OYVJtUlhUVEpvZVZadGVHRlpWMDE0VjI1R1YySlZXbFJXYWtaTFUxWmFkR05GZEZOTlJGWjZWakkxUzJGR1NuUlZiRkphWWtkU2Rs

kali@kali:~/battleware-ctf/hafta4$ tail -c 10 decoded.txt 
Y2TUQwPQ==
{% endhighlight %}

İnceleme sonunda karşımıza tekrar base64 encoded data çıkıyor. Bu durumda birden çok kez decode işlemi yapmamız gerektiğini anlıyoruz. Birkaç satır kod yazarak bu işi yapan python scriptini yazalım.

```python
------------ solve.py ------------
import os

os.system("mv n3rd.txt 1.txt")

a = 1
b = 2
while a < 15 :
        os.system("cat " + str(a) + ".txt | base64 --decode > " + str(b) + ".txt")
        a = a + 1
        b = b + 1
```

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ python solve.py
{% endhighlight %}

Yazdığımız kod sıralı bir şekilde base64 decode işlemi yapıyor ve bu işlemi yaparken her bir decode edilmiş çıktıyı numaralı şekilde farklı bir dosyaya kaydediyor. Kaç kez decode işlemi yapmamız gerektiğini bilmediğimiz için rastgele bir sayı veriyoruz. Daha sonra sonuçları inceleyerek bu sayının yeterli olup olmadığına karar vereceğiz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-01.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-01.png" alt="image-1" /></a>
	</div>
</center>

Dosya boyutlarından da görülebileceği gibi 13.txt dosyasından itibaren boş dosyalar oluşmuş. Dolu gözüken son metin dosyasını inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-02.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-02.png" alt="image-1" /></a>
	</div>
</center>

Karşımıza ascii formatında olmayan anlamsız bir karakter dizisi çıkıyor. Bunun sebebini anlamak için bir önceki dolu metin dosyasını inceleyelim.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ head -c 100 11.txt 
JJFEMRKNKJFU4S2KIZKTIUZSJNEVUS2UJFKVUU2KJZCVMVKTGJLUSTSLKZKVKMSIJJFEGVSLKZFVIR2KJRCU6U2TJRFVUS2WJNGV 
kali@kali:~/battleware-ctf/hafta4$ tail -c 100 11.txt 
MRKVGJMEUSSMIVKVMQ2GJNLEEVKXKNJUWSKKJRCVGVSDJRFVURSFKNGVGVSLIZGEKVKWGJGEWRSOIVEU2U2RJJETEUJ5HU6T2===
{% endhighlight %}

>Bir önceki metin dosyasını incelediğimizde içeriğin base64 encoded data olmadığını farkediyoruz. Peki neden en son dosya içerisinde anlamsız karakterler ile karşılaştık? 

Karşımıza çıkan önceki metinlerden daha farklı karakter setine sahip olan bu encoded data base32 tipindedir. Bu anlamak için karakter setini inceledik. Karakterlerin `büyük harflerden` ve `rakamlardan` oluştuğunu gördük. Ayrıca datanın sonunda "=" eşittir işaretini de gördük. Anlamsız karakterler ile karşılaşmış olmamızın sebebi base64 karakter setinin [base32] karakter setini kapsamasıdır. Dolayısıyla yanlış bir çıktı verse de decode işlemi yapılmış oldu. 

Soru ismi zehn 10 anlamına gelmektedir. Aslında sorunun ismi kaç kez decode işlemi yapmamız gerektiği hakkında bize ipucu veriyor. Ayrıca bir önceki decode işlemi sayısının 10 olması da bir sonraki adımda da 10 kez decode işlemi olması ihtimalini desteklediği için 10 kez base32 decode işlemini uyguluyoruz.

Yazmış olduğumuz kod üzerinde ufak bir düzenleme yaparak base32 ile decode etmeye devam edelim.

```python
------------ solve.py ------------
import os

a = 11
b = 12
while a < 21 :
        os.system("cat " + str(a) + ".txt | base32 --decode > " + str(b) + ".txt")
        a = a + 1
        b = b + 1
```

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ python solve.py
{% endhighlight %}

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-03.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-03.png" alt="image-1" /></a>
	</div>
</center>

Base32 decode işlemleri sonucunda karşımıza çıkan metin dosyasını text editor üzerinde inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-04.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-04.png" alt="image-1" /></a>
	</div>
</center>

Karşımıza çıkan sayı dizisinde çok fazla 3 rakamı bulunmaktadır. Belirli aralıklarla da 3'ten farklı rakamlar bulunmaktadır. Burada aklımıza [base10](Decimal) ve [base16](Hexadecimal) değerler olabileceği gelir. Fazla sayıda 3'ten kurtulmalıyız. Bunun için öncelikle 3'ten farklı değerlerin ne kadar karakter arayla konulduğunu tespit etmemiz ve gereksiz 3 rakamlarından kurtulmamız gerekir. Bunun için manuel olarak birkaç 3'ten farklı rakamı satır sonu olarak yapalım ve inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-05.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-05.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-06.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-06.png" alt="image-1" /></a>
	</div>
</center>

En kısa aralığın 255 olduğunu görüyoruz. Text editor'ün replace özelliğini kullanarak her 255 adet 3 rakamını silelim. Bunun anlamı dosyanın başından sonuna kadar sadece 256. sıradaki karakterlerin kalmasını sağlamaktır.

```
Output : 343636433631363737423645363936333635363436313739363636463732363636393733363836393645363736313639364537343639373437443041
```  

Tüm gerekli olan 3 rakamları ile birlikte datamızı oluşturduk. Burada decimal veya hexadecimal seçeneklerini deniyoruz ve hexadecimal değerlerden ascii formatına([ascii table]) dönüşerek yine hexadecimal formatta bir başka çıktı verdiğini görüyoruz.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ echo 343636433631363737423645363936333635363436313739363636463732363636393733363836393645363736313639364537343639373437443041 | xxd -r -p
Output : 466C61677B6E696365646179666F7266697368696E6761696E7469747D0A
{% endhighlight %}

Tekrar hex to ascii yaptığımızda flag değerimiz ortaya çıkıyor.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta4$ echo 466C61677B6E696365646179666F7266697368696E6761696E7469747D0A | xxd -r -p
Flag{nicedayforfishingaintit}
{% endhighlight %}

```
Flag{nicedayforfishingaintit}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[Battleware]: https://battleware.zone/
[Base64]: https://en.wikipedia.org/wiki/Base64
[base32]: https://en.wikipedia.org/wiki/Base32
[base16]: https://en.wikipedia.org/wiki/Hexadecimal
[base10]: https://en.wikipedia.org/wiki/Decimal
[ascii table]: https://en.wikipedia.org/wiki/ASCII
[n3rd.rar]: {{site.baseurl}}/assets/files/n3rd.rar

