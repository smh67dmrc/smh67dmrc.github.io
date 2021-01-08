---
layout: post
title: "Battleware CTF Write-Up Misc Secret Message"
date: 2021-01-08 05:00:00 +0300
description: Battleware CTF Write-Up Misc Secret Message
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Misc` kategorisinden `Secret Message` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 7.Haftada sorulan sorulardan biridir.

Soru dosyası : [sql_hash.txt]

Soruda `sql_hash` isminde bir `txt` dosyası verilmiş.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a10.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a10.png" alt="image-1" /></a>
	</div>
</center>

```
sql_hash.txt içeriği

admin:200ceb26807d6bf99fd6f4f0d1ca54d4
test:828e096fef42d94858dd49b27ab903f3
demo:4823c694493f639645e824b1adfe4ba7
giris:098f6bcd4621d373cade4e832627b4f6
yetkili:d8578edf8458ce06fbc5bb76a58c5ca4
superuser:0b180078d994cb2b5ed89d7ce8e7eea2
pliyirmen:bffa5cb2b4ce9a469e91294817c9ac31

```

Dosya içeriğine baktığımızda username-password hash ikililerini görüyoruz. Hashlerin hangi algoritmaya ait hash olduğunu tespit edebilmek için bir tanesini `hash-identifier` aracına verelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a11.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a11.png" alt="image-1" /></a>
	</div>
</center>

Hash algoritmasının md5 olabileceğini gördük. Soruda da belirtildiği gibi öncelikle `sql_hash.txt` dosyasındaki hashlerin plaintext hallerini bulmalıyız. Hash crack işlemini yapabilmek için [https://crackstation.net/] adresini kullanalım. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a12.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a12.png" alt="image-1" /></a>
	</div>
</center>

En sondaki `pliyirmen` kullanıcısının parolası hariç diğer tüm parolaları elde etmiş olduk. Pliyirmen kullanıcısına ait md5 hashi `john` aracıyla birlikte kırabiliriz. Fakat sorunun çözümü için gerekli olmadığı için yazıda yer almamaktadır. Elde etmiş olduğumuz kullanıcı adı ve parola ikilileri aşağıdaki şekildedir.

```
admin:administrator
test:creative
demo:demoo
giris:test
yetkili:qwerty
superuser:su
pliyirmen:pliyirmen
```

Elde etmiş olduğumuz bu kullanıcı adı ve parola bilgilerini kullanabilmek için bir login ekranına ihtiyacımız var. Soruda verilen sayfayı ziyaret edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a13.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a13.png" alt="image-1" /></a>
	</div>
</center>

Sayfada apache web server default sayfası bulunuyor. Peki bu login nerde? Nasıl login sayfasını bulacağız? Bunun için `wfuzz` aracıyla bruteforce yöntemiyle dizin keşfi yapmalıyız. Wfuzz aracına megabeast wordlistini verelim ve sonuçlarını inceleyelim. Wfuzz sonuçlarında `panel` isminde bir dizin olduğunu öğreniyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a14.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a14.png" alt="image-1" /></a>
	</div>
</center>

Panel dizini sayfasını ziyaret edelim. Karşımıza login ekranı çıktı.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a15.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a15.png" alt="image-1" /></a>
	</div>
</center>

Daha önceden elde etmiş olduğumuz kullanıcı adı ve parolaları denediğimizde `yetkili` kullanıcı adı ve `qwerty` parolasıyla login olabildik.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a16.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a16.png" alt="image-1" /></a>
	</div>
</center>

Login olduktan sonra karşımıza aşağıdaki gibi bir sayfa geldi.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a17.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a17.png" alt="image-1" /></a>
	</div>
</center>

Butonlara tıkladığımızda pop-uplar çıkıyor ve ihtiyacımız olan ipucuna ulaşamıyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a18.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a18.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a19.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a19.png" alt="image-1" /></a>
	</div>
</center>

Sorgu sekmesine girdiğimizde bizden secret code istiyor. Secret code değerini bulabilmek için araştırmaya devam ediyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a191.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a191.png" alt="image-1" /></a>
	</div>
</center>

Ekle sekmesi altında bir `pcapng` dosyası bulunuyor. İndirip inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a192.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a192.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a193.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a193.png" alt="image-1" /></a>
	</div>
</center>

Pcapng dosyasını wireshark ile açtığımızda icmp paketlerinin bazılarının boyutlarının daha büyük olduğunu gördük. Paketi incelediğimizde paketin data bölümünde bir değer olduğunu farkettik. Aradığımız secret code değerini bulmuş olduk : `SECRETbATTLeWaRe`

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a194.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a194.png" alt="image-1" /></a>
	</div>
</center>

Bulduğumuz secret code değerini sorgu sekmesi altındaki input alanına girelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a195.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a195.png" alt="image-1" /></a>
	</div>
</center>

Secret code değerini girdikten sonra flag değerimizi elde etmiş oluyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-a196.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-a196.png" alt="image-1" /></a>
	</div>
</center>

```
Flag{cc066bdb532b32c5adebeb5028784e02d1631f37fa1d931f04c75315feec5404}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/
[sql_hash.txt]: {{site.baseurl}}/assets/files/sql_hash.txt
[https://crackstation.net/]: https://crackstation.net/

