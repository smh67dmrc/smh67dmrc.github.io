---
layout: post
title: "STMCTF'19 Write-Up Crypto Pseudo Words"
date: 2020-12-22 05:00:00 +0300
description: STMCTF'19 Write-Up Crypto Pseudo Words
img: stmctf19.jpg
tags: [CTF, STMCTF19, Write-Up, Capture The Flag]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Crypto` kategorisinden `Pseudo Words` isimli sorunun çözümünü anlatacağım.

Soruda `xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx` şeklinde şifreli bir metin verilmiş. Şifreli metnin çözülmesi istenmiş.

Şifreli metni internette araştırdığımızda `Bubble Babble Encoding` tekniği ile encode edildiğini görüyoruz. Decode işlemini yapan bir araç([https://github.com/MartinIngesen/BubbleBabble]) indirelim ve decode edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-01.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-01.png" alt="image-1" /></a>
	</div>
</center>

Decode işlemi sonucunda flag değerimiz ortaya çıkmış olur.

```
STMCTF{R0tTen_P0t4t0NG}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:

[STMCTF'19]: https://ctfonline.stm.com.tr/
[https://github.com/MartinIngesen/BubbleBabble]: https://github.com/MartinIngesen/BubbleBabble





