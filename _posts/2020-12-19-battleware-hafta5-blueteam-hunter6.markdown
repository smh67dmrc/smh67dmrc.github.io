---
layout: post
title: "Battleware CTF Write-Up Blueteam Hunter6"
date: 2020-12-19 05:00:00 +0300
description: Battleware CTF Write-Up Blueteam Hunter6
img: battleware.png
tags: [CTF, Battleware, Write-Up, Capture The Flag]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Blueteam` kategorisinden `Hunter6` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 5.Haftada sorulan sorulardan biridir.

Soru dosyası : [hunter6.pcap]

Soruda `hunter6` isminde bir pcap dosyası verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-60.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-60.png" alt="image-1" /></a>
	</div>
</center>


Soru1 metninde `hmoreo` kullanıcısına gönderilen mailde bulunan bir dokümandan bahsediliyor. İçinde zararlı kodun olduğu dokümanı bulmamız ve pcap dosyasının içerisinden çıkartmamız gerekli. `Hunter6` ismindeki pcap dosyasını `wireshark` aracıyla açalım ve `SMTP` filtresiyle birlikte soruda adı geçen dokümanı bulalım. Pakete sağ tıklayıp `Follow => TCP Stream` seçeneği ile tüm akışa bakalım.


<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-61.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-61.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-62.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-62.png" alt="image-1" /></a>
	</div>
</center>


Akışı incelediğimizde `Customer_Information_List` isminde bir zip dosyasının mail ekinde gönderildiğini görüyoruz. Soru1'in cevabını `Customer_Information_List.zip` olarak bulduk. 

Soru2 metninde zararlı kodda çalıştırılan exe'nin adı sorulmuş. Bunun için öncelikle zip dosyasını pcap dosyasının içinden çıkartmamız gerekli. Base64 türünde dosyanın tamamı pcap dosyasının içinde mevcut. Base64 encoded datayı `Customer_Information_List.txt` dosyası içine kopyalayalım. Txt dosyası içeriğinde karakterler arasında boşluk olmamasına ve tek satırda olmasına dikkat edelim.  

Zip dosyasını oluşturalım ve kontrol edelim.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta5$ base64 -d Customer_Information_List.txt > Customer_Information_List.zip
kali@kali:~/battleware-ctf/hafta5$ file Customer_Information_List.zip 
Customer_Information_List.zip: Zip archive data, at least v2.0 to extract
{% endhighlight %}

Zip dosyasını açalım.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta5$ unzip Customer_Information_List.zip 
Archive:  Customer_Information_List.zip
  inflating: Customer Information List.xlsx
{% endhighlight %}

Zip dosyası içerisinden excel dokümanı çıkıyor.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta5$ file Customer\ Information\ List.xlsx 
Customer Information List.xlsx: Microsoft Excel 2007+
{% endhighlight %}

Excel dosyasını açarak zararlı kodu bulalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-63.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-63.png" alt="image-1" /></a>
	</div>
</center>


A1 hücresinde yazılmış olan zararlı kod içinde exe isminin `rundll32` olduğunu gördük. Böylece soru2'nin de cevabını bulmuş olduk.

Soruda istenen cevapları flag formatı içine yerleştirelim flagi oluşturalım.

{% highlight ruby %}
Flag{Customer_Information_List.zip,rundll32.exe}
{% endhighlight %}

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle..

[Battleware]: https://battleware.zone/
[hunter6.pcap]: {{site.baseurl}}/assets/files/hunter6.pcap

