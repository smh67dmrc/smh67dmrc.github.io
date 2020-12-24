---
layout: post
title: "Battleware CTF Write-Up Misc Mito"
date: 2020-12-18 05:00:00 +0300
description: Battleware CTF Write-Up Misc Mito
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Misc` kategorisinden `Mito` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 5.Haftada sorulan sorulardan biridir.

Soru dosyası : [mito.rar]

Soruda `mito` isminde bir rar dosyası verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-40.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-40.png" alt="image-1" /></a>
	</div>
</center>

Rar dosyasını açtığımızda 499 tane png dosyası bizi karşılıyor. Her bir png dosyası bir karakter olacak şekilde toplamda 499 karakterlik metni temsil ediyor. Sırasının belli olması için dosya isimleri numaralandırılmış.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-41.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-41.png" alt="image-1" /></a>
	</div>
</center>

Metin çok uzun olmadığı için manuel olarak okuma yapılıp flag elde edilmeye çalışılır. Metnin tamamı aşağıdaki şekilde ortaya çıkıyor.

```
it is kind of interesting bec4use hack1ng is a skill that could be used for criminal purposes or legitimate purpos3s, and so even th0ugh in the past i was hacking for the cur1osity, and th3 thrill, to get a bite of the forbidden fruit of knowledge, i am now working in the security field as a public speaker, says kevin. your answer is here `k3vind4v1dm1tn1ck`.i went to prison for my hacking and now people hire me to do the same thing i went to prison for but in a legal and beneficial way, he adds.
```

Soru metninde bir cevaba ulaşmamız gerektiği söylenmiş. Yukarıda elde ettiğimiz metinde ortaya çıkan cevabımız `k3vind4v1dm1tn1ck` cevabıdır.

```
Flag{k3vind4v1dm1tn1ck}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/
[mito.rar]: {{site.baseurl}}/assets/files/mito.rar

