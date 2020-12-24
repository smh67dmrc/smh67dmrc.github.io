---
layout: post
title: "Battleware CTF Write-Up Osint GG"
date: 2020-12-17 05:00:00 +0300
description: Battleware CTF Write-Up Osint GG
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Osint` kategorisinden `GG` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 4.Haftada sorulan sorulardan biridir.

Soru dosyası : [GG.txt]

Soruda `GG.txt` isminde bir dosya verilmiş. Dosya içeriğini incelediğimizde içerisinde daha önceden karşılaşmadığımız bir formatta koordinatlar olduğunu gördük. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-20.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-20.png" alt="image-1" /></a>
	</div>
</center>

İnternette kısa bir araştırma yaptıktan sonra dosya içeriğinin GCode([https://reprap.org/wiki/G-code]) formatında olduğunu öğrendik. GCode formatı 3D printerlarda kullanılıyormuş. Online bir GCode Viewer aracına([https://ncviewer.com/]) dosyamızı verdik ve flag değerini elde ettik.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-21.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-21.png" alt="image-1" /></a>
	</div>
</center>
<br>
```
Flag{c4nt_wa1T_t0_pr1NT_th1sS}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:

[Battleware]: https://battleware.zone/
[GG.txt]: {{site.baseurl}}/assets/files/GG.txt
[https://ncviewer.com/]: https://ncviewer.com/
[https://reprap.org/wiki/G-code]: https://reprap.org/wiki/G-code
