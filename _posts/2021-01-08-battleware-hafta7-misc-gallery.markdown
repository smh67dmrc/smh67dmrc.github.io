---
layout: post
title: "Battleware CTF Write-Up Misc Gallery"
date: 2021-01-08 05:00:00 +0300
description: Battleware CTF Write-Up Misc Gallery
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Misc` kategorisinden `Gallery` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 7.Haftada sorulan sorulardan biridir.

Soru dosyası : [123.JPG]

Soruda `123` isminde bir `JPG` dosyası verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-80.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-80.png" alt="image-1" /></a>
	</div>
</center>

Soru metnini okuduğumuzda bir fotoğrafçıdan bahsedildiğini gördük. Fotoğrafçının profilini bulmamız ve son paylaşımları içerisinde kuzey ışıkları olan fotoğrafları bulmamız gerekiyordu. İlk olarak fotoğrafı google görsellere yükleyip karşımıza çıkan sosyal medya hesaplarını incelemeye başladık. Bu araştırma süreci uzun sürdü ve maalesef doğru sosyal medya hesabına ulaşamadık. Vakit kaybetmemek adına diğer sorulara yöneldik. Uzun bir süre soru hiçbir takım tarafından çözülemeyince bir ipucu paylaşıldı: `Russian Search Engine`. İpucu geldikten sonra tekrar soruyla ilgilenmeye başladık. Russian search engine dediği arama motoru `Yandex` olmalı diye düşündük. Tıpkı google görsellere yüklediğimiz gibi aynı fotoğrafı bu sefer de yandex görsellere yükledik ve araştırmaya başladık. Kısa bir süre sonra bir `instagram` hesabına ulaştık: [https://www.instagram.com/jaworskyjfilter/].

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-81.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-81.png" alt="image-1" /></a>
	</div>
</center>

Instagram hesabı içerisinde yapılan son paylaşımlar içerisinde kuzey ışıkları olan fotoğrafları inceledik. Esasında yakın tarihlerde kuzey ışıkları paylaşımları çok azdı ve yapılan yorumlarda da herhangi bir ipucu yoktu. Acaba yanlış hesabı mı inceliyoruz diye şüphelenmeye başladık. Bir süre sonra karşımıza hesabın storylerinde bir başka benzer bir hesabın olduğunu gördük: [https://www.instagram.com/jaworskyj/]

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-82.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-82.png" alt="image-1" /></a>
	</div>
</center>

Bulduğumuz yeni hesabı incelediğimizde yorum sayısı oldukça fazla olan bir kuzey ışığı fotoğrafına denk geldik. Yorumları incelediğimizde aradığımız adresi bulduğumuzu gördük.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-83.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-83.png" alt="image-1" /></a>
	</div>
</center>

Sayfayı ziyaret ettiğimizde karşımıza fotoğraf seçiminin yapılabildiği bir menü olan galeri sayfası ile karşılaştık.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-84.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-84.png" alt="image-1" /></a>
	</div>
</center>

Sayfayı inceledik ve sırasıyla menüdeki 3 fotoğrafa da baktık. Hiçbir anlamlı bir ipucu çıkmadı. Daha sonra fotoğrafların daha fazla olduğunu farkettik. Eğer 4.cü fotoğrafı görüntülemek istersek görüntüleyebiliyorduk. POST isteği parametresi olarak `photo=1` şeklinde isteğin gittiğini gördük. Peki kaça kadar gidecektik, kaç fotoğraf vardı? Hemen Burpsuite içindeki `Intruder`'ı açarak 20'ye kadar istekte bulunacak şekilde ayarladık ve sonuçları incelemeye başladık.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-85.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-85.png" alt="image-1" /></a>
	</div>
</center>

17.fotoğraf için istekte 302 status kodu olan redirect'in son redirect olduğunu farkettik. 18.fotoğraf isteğinden itibaren 200 status kodu dönüyordu. Ne olduğunu anlayabilmek için ve response içerisinde dönen sayfanın kaynak kodunu görebilmek için `Repeater` üzerinden `photo=17` parametresiyle istekte bulunduk.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-86.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-86.png" alt="image-1" /></a>
	</div>
</center>

Follow redirection ile yönlendirilen sayfanın kaynak kodlarını gördük ve flag değerinin yorum satırı şeklinde sayfa kaynağında bulunduğunu farkettik.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-87.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-87.png" alt="image-1" /></a>
	</div>
</center>

Flag değerini elde etmiş olduk.

```
Flag{Art_1s_L0nG_lif3_1s_sh0rT}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/
[https://www.instagram.com/jaworskyjfilter/]: https://www.instagram.com/jaworskyjfilter/
[https://www.instagram.com/jaworskyj/]: https://www.instagram.com/jaworskyj/
[123.JPG]: {{site.baseurl}}/assets/files/123.JPG

