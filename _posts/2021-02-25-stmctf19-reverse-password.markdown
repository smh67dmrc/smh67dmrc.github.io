---
layout: post
title: "STMCTF'19 Write-Up Reverse Password"
date: 2021-02-25 05:00:00 +0300
description: STMCTF'19 Write-Up Reverse Password
img: stmctf19.jpg
tags: [STMCTF19]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Reverse` kategorisinden `Password` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [password]

Soruda `password` isminde bir executable dosya verilmiş. Reverse kategorisinden bir soru olduğu için öncelikle çalıştırılabilir dosyanın hangi işletim sistemine ait olduğunu öğrenmemiz gerekli. Elde ettiğimiz bilgiye göre inceleme yapacağımız makinemizi ve araçlarımızı seçmeliyiz. Linux üzerindeki `file` komutu ile dosya hakkında bilgi alalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b1.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b1.png" alt="image-1" /></a>
	</div>
</center>

File komutu çıktısında `ELF` türünde `64-bit` linux executable bir binary olduğunu gördük. `Go` diliyle yazılmış. Ayrıca `strip` edilmediğini de görüyoruz. Strip edilmemiş olması debug sembollerinin binary içinde tutulduğu anlamına gelir bu da reversing işlemi sırasında analiste kolaylık sağlar. Örneğin fonksiyon isimleri kaynak koddaki şekliyle görünür. İncelemeye başlamadan önce binary dosyamızı çalıştırıp ne yaptığına bakalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b2.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b2.png" alt="image-1" /></a>
	</div>
</center>

Binary'yi çalıştırdığımızda bir parola istedi ve doğruluğunu kontrol edip bize bilgi verdi. Soruda bizden istenen parolanın ne olduğunu tespit etmektir. Bu parolayı bulduktan sonra flag formatı(STMCTF{Flag}) içine koyduğumuzda flag değerimizi elde etmiş olacağız. [GDB] ile binary'yi debug ederek incelemeye başlayalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b3.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b3.png" alt="image-1" /></a>
	</div>
</center>

Go diliyle yazılmış bir binary'yi reverse etmek genellikle kolay değildir fakat burda strip edilmediği için bazı kolaylıklar karşımızda bulunmaktadır. Örneğin main fonksiyonundan analize başlayabiliriz. GDB internal komutlarından `info` komutu yardımıyla `main` fonksiyonunu bulalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b4.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b4.png" alt="image-1" /></a>
	</div>
</center>

Main fonksiyonunu disassemble ederken kullanacağımız main fonksiyonu isminin `main.main` şeklinde olduğunu gördük. Main fonksiyonunu disassemble ederek kodu anlamaya çalışalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b5.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b5.png" alt="image-1" /></a>
	</div>
</center>

Binary'yi çalıştığımızda bizden parola istemişti ve doğru parola olup olmadığını kontrol ederek bize geri dönüş sağlamıştı. Parolanın doğru olup olmadığını karşılaştırdığı noktayı bulursak aslında hangi değer ile karşılaştırma yaptığını da görebiliriz. Bu kısımda artık assembly kodu okumamız gerekmektedir. Fakat buradaki kolaylık karşılaştırma yapılan yerlere bakarak ilerleme avantajımızın olmasıdır. Bu yüzden `cmp` instruction'ını takip etmek mantıklı olacaktır. 

`fmt.Fscan` ifadesinin olduğu `call` instruction'ı go dilindeki kullanıcıdan input almayı sağlayan `fmt.Scan` fonksiyonunu göstermektedir. Bu kısımdan sonraki 3.instructionda `cmp` ile karşılaştırma yapıldığını görüyoruz. Arada kalan 2 assembly koduna bakarsak aslında aradığımız parola değerini görebiliriz. `RAX` registerına doğru parola değerinin ataması yapılıyor ve kullanıcıdan alınan input değeri ise `RCX` registerına atanıyor. cmp instruction'ı ile RCX ve RAX register'ındaki değerlerin karşılaştırılması yapılıyor. Burda RAX register'ına atanan değer gerçek `parola` bilgisidir. Burda dikkat edilmesi gereken husus parolanın `hexadecimal` formatta debuggerda görünüyor olmasıdır fakat input olarak bu değer kullanıcıdan `decimal` olarak alınır. Dolayısıyla hex değeri decimal değere çevirirsek parolamızı ele geçirmiş olacağız.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b6.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b6.png" alt="image-1" /></a>
	</div>
</center>

Değeri decimal formata çevirelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b7.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b7.png" alt="image-1" /></a>
	</div>
</center>

Parolamızı programa verip doğruluğunu kontrol edelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-b8.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-b8.png" alt="image-1" /></a>
	</div>
</center>

Parolamızın doğru olduğunu gördük. Flag formatı içine yerleştirip flag değerimizi elde edelim.

```
STMCTF{964358233091465775}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'19]: https://ctfonline.stm.com.tr/
[password]: {{site.baseurl}}/assets/files/password
[GDB]: https://www.gnu.org/software/gdb/
