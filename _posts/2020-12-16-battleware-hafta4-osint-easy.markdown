---
layout: post
title: "Battleware CTF Write-Up Osint Easy"
date: 2020-12-16 05:00:00 +0300
description: Battleware CTF Write-Up Osint Easy
img: battleware.png
tags: [CTF, Battleware, Write-Up, Capture The Flag]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Osint` kategorisinden `Easy` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 4.Haftada sorulan sorulardan biridir.

Soruda `bw` isminde bir dosya verilmiş. Dosya içeriğini incelediğimizde içerisinde koordinat bilgilerinin yer aldığını görüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-10.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-10.png" alt="image-1" /></a>
	</div>
</center>

Elimizde içerisinde koordinatlar olan bir lokasyon dosyası olduğunu gördük fakat dosyanın uzantısı ve hangi aracın bu dosyayı açabileceği hakkında bir fikrimiz yok. İnternette yaptığımız kısa bir araştırma ile bu dosyanın `kml` formatında bir dosya olduğunu ve [Google Earth]'ün online haritasında açılabildiğini farkettik. 

Sol taraftaki menüdeki projeler kısmından dosyamızı yüklüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-11.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-11.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-12.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-12.png" alt="image-1" /></a>
	</div>
</center>

Dosyayı yüklediğimizde dosya içinde bulunan fazla birkaç satırdan dolayı parse edemediğini ve hata verdiğini görüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-13.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-13.png" alt="image-1" /></a>
	</div>
</center>

İlgili satırları silerek dosyayı tekrar yüklüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-14.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-14.png" alt="image-1" /></a>
	</div>
</center>

Flag değerimiz harita üzerinde görünür duruma geliyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-15.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-15.png" alt="image-1" /></a>
	</div>
</center>

{% highlight ruby %}
Flag{BW1337TR2020}
{% endhighlight %}

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle..

[Battleware]: https://battleware.zone/
[Google Earth]: https://earth.google.com/web/
