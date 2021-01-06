---
layout: post
title: "Siber Yıldız 2020 Write-Up Hazırlık Sorusu Zararlı Gibiyim"
date: 2021-01-06 05:00:00 +0300
description: Siber Yıldız 2020 Write-Up Hazırlık Sorusu Zararlı Gibiyim
img: siberyildiz.png
tags: [Siberyıldız]
---
Selamlar, bu yazımda [Siber Yıldız 2020] yarışması öncesinde sorulan `Zararlı Gibiyim` isimli hazırlık sorusunun çözümünü anlatacağım.

Soru dosyası : [Zararligibiyimm.exe.zip]

Soruda `Zararligibiyimm.exe` isminde windows ortamında çalıştırılabilir bir dosya verilmiş. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-01.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-01.png" alt="image-1" /></a>
	</div>
</center>

Öncelikle statik olarak inceleme yapalım ve stringlerine bakalım. Dosyaya ait stringlere baktığımızda bir GET isteği olduğunu farkediyoruz. 

{% highlight ruby %}
kali@kali:~/siberyildiz2020/hazirlik$ strings Zararligibiyimm.exe
{% endhighlight %}

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-02.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-02.png" alt="image-1" /></a>
	</div>
</center>

Sayfayı ziyaret ettiğimizde([http://ti.siberyildiz.com/ti.php]) karşımıza encoded bir data çıkıyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-03.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-03.png" alt="image-1" /></a>
	</div>
</center>

Karakter setini incelediğimizde ve sonundaki padding karakteri olan "=" işaretini dikkate aldığımızda base64 ile encode edildiğini farkediyoruz. Base64 decode işlemini yapalım ve sonucu inceleyelim.

{% highlight ruby %}
kali@kali:~/siberyildiz2020/hazirlik$ echo "aHR0cHM6Ly9naG9zdGJpbi5jby9wYXN0ZS9tdmZxNy9yYXc=" | base64 -d
https://ghostbin.co/paste/mvfq7/raw
{% endhighlight %}

Karşımıza bir websayfasına ait URL çıkıyor. Sayfayı ziyaret edelim ve incelemeye devam edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-04.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-04.png" alt="image-1" /></a>
	</div>
</center>

Yukarıdaki encoded data üzerinde yaptığımız incelemeyi benzer şekilde burada da uygularsak yine karşımıza base64 encoded data çıktığını rahatlıkla görebiliriz. Base64 decode işlemini yapalım ve sonucu inceleyelim.

{% highlight ruby %}
kali@kali:~/siberyildiz2020/hazirlik$ echo "L2I0YjBkNDcyZjI4NjU5ZDJmMzQzMDJiM2UyYWRiODljLnBocD9pZD02ZDliODI2ZGRjMDcyNTNmOTRjMWExODZlNGFlYWE3ZDE5YzVkYmM1" | base64 -d
/b4b0d472f28659d2f34302b3e2adb89c.php?id=6d9b826ddc07253f94c1a186e4aeaa7d19c5dbc5
{% endhighlight %}

Base64 decode işlemi sonucunda karşımıza bir path çıkıyor. Bu pathi yukarıdaki incelememizde bulduğumuz URL içine ekleyerek sayfayı ziyaret edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/sy-05.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/sy-05.png" alt="image-1" /></a>
	</div>
</center>

Flag değerimizi elde ettik.

```
Siberyildiz3{eTBaYTRybjd178JKVKLLSlkaDE87L016L3Uwb3FLTHNpSk5NRmF6VG5VamE3WE5MTlN0ajllK3R5elFZVlZPK1FROUs5dFlxSXpSNnZkdWxybmorQlE5PQ==}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Siber Yıldız 2020]: https://www.siberyildiz.com/
[http://ti.siberyildiz.com/ti.php]: http://ti.siberyildiz.com/ti.php
[Zararligibiyimm.exe.zip]: {{site.baseurl}}/assets/files/Zararligibiyimm.exe.zip
