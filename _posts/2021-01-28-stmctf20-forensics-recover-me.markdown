---
layout: post
title: "STMCTF'20 Write-Up Forensics Recover Me"
date: 2021-01-28 05:00:00 +0300
description: STMCTF'20 Write-Up Forensics Recover Me
img: stmctf20.png
tags: [STMCTF20]
---
Selamlar, bu yazımda [STMCTF'20] yarışmasında sorulan `Forensics` kategorisinden `Recover Me` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [BadDisk.rar]

Soruda `BadDisk` isminde bir rar dosyası verilmiş. Rar dosyasını açtığımızda karşımıza `001` uzantılı imaj dosyası çıkıyor. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-b1.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-b1.png" alt="image-1" /></a>
	</div>
</center>

`RecoverMe.001` dosyasını `Autopsy` aracıyla incelediğimizde içinde PDF streamlerinin olduğunu görüyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-b2.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-b2.png" alt="image-1" /></a>
	</div>
</center>

Dosyanın adından da anlaşılabileceği gibi `File Carving` işlemi ile tahminen PDF uzantılı dosya recover etmemiz gerekiyor. `Foremost` isimli araç ile file carving işlemini gerçekleştirelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-b3.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-b3.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-b4.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-b4.png" alt="image-1" /></a>
	</div>
</center>

File carving sonucunda 1 PDF ve 1 JPG dosyası extract edildiğini görüyoruz. PDF dosyasını açtığımızda flag değerimizi elde etmiş oluyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-b5.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-b5.png" alt="image-1" /></a>
	</div>
</center>

```
STMCTF{Top_Secret_File}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'20]: https://ctfonline.stm.com.tr/
[BadDisk.rar]: {{site.baseurl}}/assets/files/BadDisk.rar

