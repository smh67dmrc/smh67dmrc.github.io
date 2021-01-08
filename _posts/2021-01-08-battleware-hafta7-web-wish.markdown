---
layout: post
title: "Battleware CTF Write-Up Web Wish"
date: 2021-01-08 05:00:00 +0300
description: Battleware CTF Write-Up Web Wish
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Web` kategorisinden `Wish` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 7.Haftada sorulan sorulardan biridir.

Soruda web adresi verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-70.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-70.png" alt="image-1" /></a>
	</div>
</center>

Web adresini ziyaret ettiğimizde karşımıza siyah bir sayfanın içinde bulunan bir input alanı geliyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-71.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-71.png" alt="image-1" /></a>
	</div>
</center>

Web adresine ait sayfanın kaynak kodlarını inceledik. İstek ve yanıtlara ait header bilgilerini inceledik karşımıza bir ipucu çıkmadı. Cookie'lere baktığımızda 4 tane cookie olduğunu farkettik. Cookie'ler sıralı ve hex değerler içeriyordu.

```
cookie1:6B316E646E
cookie2:3373735F31
cookie3:735F696D70
cookie4:307274616E74
```

Cookielerdeki değerleri tek parça hex haline getirip python ile ascii formatına çevirdik.

```
>>> "6B316E646E3373735F31735F696D70307274616E74".decode("hex")
'k1ndn3ss_1s_imp0rtant'
>>>
```

Sayfadaki input alanımıza değerimizi girdik.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-72.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-72.png" alt="image-1" /></a>
	</div>
</center>

Değeri girdikten sonra buton yine pasif durumda kaldı. Sağ tıklayıp inspect element diyerek butonun disabled özelliğini pasif hale getirebilirdik. Fakat biz onun yerine Enter tuşuna basmayı tercih ettik ve flag değerimiz bir pop-up içerisinde karşımıza gelmiş oldu.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-73.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-73.png" alt="image-1" /></a>
	</div>
</center>

Flag değerimizi elde etmiş olduk.

```
Flag{see?kindness_is_th3_solution}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/

