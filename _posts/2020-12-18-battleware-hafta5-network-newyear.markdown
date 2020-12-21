---
layout: post
title: "Battleware CTF Write-Up Network New Year"
date: 2020-12-18 05:00:00 +0300
description: Battleware CTF Write-Up Network New Year
img: battleware.png
tags: [CTF, Battleware, Write-Up, Capture The Flag]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Network` kategorisinden `New Year` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 5.Haftada sorulan sorulardan biridir.

Soru dosyası : [captured.pcap]

Soruda `captured` isminde bir pcap dosyası verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-50.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-50.png" alt="image-1" /></a>
	</div>
</center>

Pcap dosyasını wireshark ile incelediğimizde http paketleri içerisinde bir jpg dosyası karşımıza çıkıyor. Jpg dosyasının bulunduğu paketi seçip aşağıdaki bölümden dosyanın içeriğinin olduğu yere sağ tıklayıp "show packet bytes" seçeneği ile resmi inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-51.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-51.png" alt="image-1" /></a>
	</div>
</center>

<br>

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-52.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-52.png" alt="image-1" /></a>
	</div>
</center>

Resmi detaylı incelemek için kaydedelim. Resim içerisinde gizli bir bilgi olup olmadığını steghide aracı ile inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-53.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-53.png" alt="image-1" /></a>
	</div>
</center>

Resmin içerisine bir txt dosyası gizlendiğini farkediyoruz. Yine steghide aracıyla passphrase olmadan txt dosyasını resmin içinden çıkartalım ve içeriğini okuyalım.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta5/captured$ steghide --extract -sf christmas.jpg -xf note.txt
Enter passphrase: 
wrote extracted data to "note.txt".

kali@kali:~/battleware-ctf/hafta5/captured$ cat note.txt 
Flag{too_e4sy}
{% endhighlight %}

Flag değerini elde etmiş olduk.

```
Flag{too_e4sy}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/
[captured.pcap]: {{site.baseurl}}/assets/files/captured.pcap

