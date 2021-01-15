---
layout: post
title: "Battleware CTF Write-Up Joker Mockumentary"
date: 2021-01-15 05:00:00 +0300
description: Battleware CTF Write-Up Joker Mockumentary
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Joker` kategorisinden `Mockumentary` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta süren bir yarışmadır. Bu soru 8.Haftada sorulan sorulardan biridir.

Soruda web adresi verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a20.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a20.png" alt="image-1" /></a>
	</div>
</center>

Soruda verilen web adresini ziyaret ettiğimizde karşımıza bir soru ve harita çıkıyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a21.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a21.png" alt="image-1" /></a>
	</div>
</center>

Soruda bizden istenen harita üzerindeki alanda bulunan ismi `liman free internet` olan kablosuz ağa ait `BSSID` değeridir. Bu kablosuz ağın BSSID değerini dünyadaki kablosuz ağları gösteren [https://wigle.net/] web adresinde bulabiliriz. Harita üzerinden Kıbrıs'a ait bu konuma gittiğimizde BSSID değerini görebiliriz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a22.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a22.png" alt="image-1" /></a>
	</div>
</center>

BSSID değerimizi input alanına girelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a23.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a23.png" alt="image-1" /></a>
	</div>
</center>

Bu aşamayı geçerek bir başka soruyla karşılaşıyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a24.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a24.png" alt="image-1" /></a>
	</div>
</center>

Soruda bizden Mersin-Kıbrıs arasındaki fiberoptik altyapının kurulum yılını istiyor. Bu sorunun çözümü için dünya üzerindeki tüm fiberoptik altyapıları gösteren bir web adresinden yararlanacağız: [https://www.submarinecablemap.com/]. Web adresini ziyaret ettiğimizde Kıbrıs üzerinden Mersin'e sadece 1 hat olduğunu görüyoruz. Hattın üzerine tıkladığımızda sağ tarafta hatta ait bilgiler görünüyor. Aradığımız RFS değerini `1993` olarak görüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a25.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a25.png" alt="image-1" /></a>
	</div>
</center>

Bulduğumuz değeri input alanımıza girelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a26.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a26.png" alt="image-1" /></a>
	</div>
</center>

Bu aşamayı da geçerek bir başka soruyla karşılaşıyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a27.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a27.png" alt="image-1" /></a>
	</div>
</center>

Soruda bizden MITM(Man In The Middle) saldırısına ait att&ck technique id değerini istemiş. Mitre attack matrisine baktığımızda([https://attack.mitre.org/matrices/enterprise/]) rahatlıkla T kodlu technique id değerini görebiliriz. Cevabımız `T1557` id değeridir.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a28.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a28.png" alt="image-1" /></a>
	</div>
</center>

Cevabımızı input alanımıza girelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a29.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a29.png" alt="image-1" /></a>
	</div>
</center>

Cevabı girdikten sonra flag değerimizi elde etmiş oluyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a291.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a291.png" alt="image-1" /></a>
	</div>
</center>

```
Flag{l3t_m3_1n}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/
[https://wigle.net/]: https://wigle.net/
[https://www.submarinecablemap.com/]: https://www.submarinecablemap.com/
[https://attack.mitre.org/matrices/enterprise/]: https://attack.mitre.org/matrices/enterprise/
