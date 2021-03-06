---
layout: post
title: "STMCTF'19 Write-Up Forensics Recovery"
date: 2021-03-06 05:00:00 +0300
description: STMCTF'19 Write-Up Forensics Recovery
img: stmctf19.jpg
tags: [STMCTF19]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Forensics` kategorisinden `Recovery` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [image.zip]

Soruda `image` isminde bir zip dosyası verilmiş. Zip dosyasını extract ettiğimizde içinden `image.001` isimli bir imaj dosyası çıkıyor. İmaj dosyasını açıp incelemek için [autopsy] isimli yazılımdan yararlanalım. Autopsy yazılımını kullanabilmek için bazı işlemleri gerçekleştirmemiz gerekiyor. Öncelikle yeni bir case oluşturalım. Aşağıdaki resimlerde sırasıyla işlemler belirtilmiştir.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c1.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c1.png" alt="image-1" /></a>
	</div>
</center>

Case ismi belirleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c2.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c2.png" alt="image-1" /></a>
	</div>
</center>

CTF imaj dosyası inceleyeceğimiz için bu kısımda gerçek bilgiler doldurmamıza gerek yoktur, gelişigüzel doldurabiliriz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c3.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c3.png" alt="image-1" /></a>
	</div>
</center>

Bu kısım oldukça önemli çünkü imaj dosyamızın parse edilebilmesi için data source tipini doğru seçmemiz gerekir. Seçmemiz gereken data source tipi `Disk Image or VM File` olmalıdır.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c4.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c4.png" alt="image-1" /></a>
	</div>
</center>

Bu kısımda `image.001` dosyamızı seçelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c5.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c5.png" alt="image-1" /></a>
	</div>
</center>

Uygulanacak olan modülleri varsayılan seçimde bırakabiliriz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c6.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c6.png" alt="image-1" /></a>
	</div>
</center>

Finish ile birlikte analizi başlatalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c7.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c7.png" alt="image-1" /></a>
	</div>
</center>

Analiz birkaç dakika sürebilir. Sağ alttaki kısımda tamamlandığını gördükten sonra incelememize başlayabiliriz. Karşımıza aşağıdaki gibi bir ekran çıkacak ve burada soldaki menüden kategori spesifik inceleme yapabiliriz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c8.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c8.png" alt="image-1" /></a>
	</div>
</center>

İncelemeye başlamadan önce belirtmek istediğim bir konu var. Autopsy aracının `4.17.0` sürümünden önceki versiyonları kullanıyorsanız bazı modüller ve özellikler eksik olabilir. Bu yazının yazıldığı tarih itibariyle güncel Autopsy sürümü 4.17.0 olduğu için bu sürüm tercih edilmiştir. Daha önceki incelemelerime bakarak söyleyebilirim ki bazı özellikler eski versiyonlarda bulunmadığı için ekstra olarak diğer araçlarla birlikte kullanmak zorunda kalmıştım. Son olarak kabaca datalara baktığımda gördüm ki oldukça fazla incelenmesi gereken data var. Dolayısıyla yazının uzamaması için sadece sorunun çözümünde kullanılan gerçek bulgular ile yazı devam edecektir.

İncelememizde imajı alınan diskin `windows` makineye ait olduğunu farkediyoruz. `STMCTF` kullanıcısının masaüstünde `music` adında bir klasör içinde 5 farklı `wav` uzantılı medya dosyası olduğunu görüyoruz. Dosya isimlendirmesi `1,2,3,4,5` şeklinde ilerlemiş ve ilginç olan kısım sadece son wav dosyasının boyutunun düşük olmasıdır. `Application` sekmesinden wav uzantılı medyaları oynatabiliyoruz. Sesleri dinlediğimizde 4 tanesinin müzik olduğunu kalan son wav dosyasının ise `morse code` içerdiğini farkediyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c9.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c9.png" alt="image-1" /></a>
	</div>
</center>

`5.wav` dosyasını extract edip online morse decode işlemi yapan bir adrese([https://morsecode.world/international/decoder/audio-decoder-adaptive.html]) verelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c10.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c10.png" alt="image-1" /></a>
	</div>
</center>

Morse içeren ses dosyasını decode ettiğimizde karşımıza `private key`'i bulmamız gerektiğini söyleyen bir ipucu çıktı. İncelemeye devam edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c11.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c11.png" alt="image-1" /></a>
	</div>
</center>

İncelememizin devamında `Documents` klasörü altında yine aynı mantıkta önümüze sunulmuş `1,2,3,4,5` isimlendirmesi ile 5 adet `PDF` uzantılı doküman verilmiş. İlk PDF dosyasının içeriğine `Application` sekmesinden baktığımızda içinde sadece `What!?` yazan bir ifade ile karşılaştık. Acaba bu ifade ne anlama geliyor ve gerçekten PDF içeriği boş mu? 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c12.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c12.png" alt="image-1" /></a>
	</div>
</center>

Bunu anlamak için `Text` sekmesine geçelim. Text sekmesi içinden baktığımızda PDF içerisine gizlenmiş olan `RSA Private Key` değeri ile karşılaşıyoruz. Morse ipucunda belirtilen private key bu olmalı.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c13.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c13.png" alt="image-1" /></a>
	</div>
</center>

Peki bu key nasıl gizlenmiş? Aslında application sekmesinden de gizli bir şeyin olduğunu farkedebilirdik çünkü yazıya ait renk `beyaz` olarak ayarlanmış. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c14.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c14.png" alt="image-1" /></a>
	</div>
</center>

Şuana kadar elimizde sadece bir `RSA Private Key` var. Bu key'i kullanabilmek için encrypted bir data olmalı peki nerde? İmaj içerisindekileri incelemeye devam edelim. STM logosunun olduğu bir `PNG` dosyası ile birlikte `ENC` uzantılı bir encrypted dosya ile karşılaşıyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c15.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c15.png" alt="image-1" /></a>
	</div>
</center>

Öncelikle PNG dosyasını inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c16.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c16.png" alt="image-1" /></a>
	</div>
</center>

PNG dosyasını incelediğimizde exif bilgilerinde `comment` bırakıldığını görüyoruz : `openssl rsa`. Böylelikle decryption yöntemimize ait ipucunu da bulmuş olduk. `step1.enc` dosyamızı export edelim ve elimizde bulunan key ile birlikte decrypt edelim. Private keyimizi `private_key.pem` olarak kaydedelim. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c17.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c17.png" alt="image-1" /></a>
	</div>
</center>

Decryption işlemini başarıyla gerçekleştirdik. Decryption işlemi sonucunda karşımıza flag değerine benzeyen ama flag olmayan bir string değer çıktı. Bu değeri nerede kullanacağız? İmaj içerisini inceleyip kullanacağımız kısmı bulalım. `NTUSER.DAT` dosyası içerisinde (Software/Microsoft/Internet Explorer/TypedURLs) `Internet Explorer` ile ziyaret edilen adresler tutulur. Bu adresleri incelediğimizde bir `dropbox` linki gözümüze çarpıyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c18.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c18.png" alt="image-1" /></a>
	</div>
</center>

Dropbox adresini ziyaret ettiğimizde `road_of_flag` adında bir zip dosyası karşımıza çıkıyor. Dosyayı indirip açmaya çalıştığımızda içinde `flag.png` dosyasının olduğunu fakat `parola korumalı` olduğu için açamadığımızı görüyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c19.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c19.png" alt="image-1" /></a>
	</div>
</center>

Acaba öncesinde encrypted dosya içerisinden bulmuş olduğumuz string değer `parola` olabilir mi diye düşünerek deneyelim. Denediğimizde parolanın doğru olduğunu görüyoruz. İçerisinden `flag` adında bir resim dosyası çıkıyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c20.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c20.png" alt="image-1" /></a>
	</div>
</center>

Görseli araştırdığımızda `pic-a-pix` puzzle olduğunu farkediyoruz. Bu puzzle'ı elimizle de çözebiliriz fakat internette araştırdığımızda otomatik çözen araçların([http://jsimlo.sk/griddlers/]) olduğunu görüyoruz. Bu araç ile puzzle'ı çözdüğümüzde karşımıza `QR code` çıkıyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c21.gif" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c21.gif" alt="image-1" /></a>
	</div>
</center>

QR kodu [https://webqr.com/] adresine verdiğimizde flag değerimizi elde etmiş oluyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-c22.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-c22.png" alt="image-1" /></a>
	</div>
</center>

```
STMCTF{K3eP_y0ur_Fri3nds_Clo5e_bUt_yoUR_eNemi3s_cLosEr}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'19]: https://ctfonline.stm.com.tr/
[image.zip]: https://s5.dosya.tc/server/sq7o9r/image.zip.html
[autopsy]: https://www.autopsy.com/
[https://morsecode.world/international/decoder/audio-decoder-adaptive.html]: https://morsecode.world/international/decoder/audio-decoder-adaptive.html
[http://jsimlo.sk/griddlers/]: http://jsimlo.sk/griddlers/
[https://webqr.com/]: https://webqr.com/
