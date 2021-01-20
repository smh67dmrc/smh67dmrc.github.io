---
layout: post
title: "STMCTF'20 Write-Up Misc Alpha Do You Copy"
date: 2021-01-20 05:00:00 +0300
description: STMCTF'20 Write-Up Misc Alpha Do You Copy
img: stmctf20.png
tags: [STMCTF20]
---
Selamlar, bu yazımda [STMCTF'20] yarışmasında sorulan `Misc` kategorisinden `Alpha Do You Copy` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [Alpha-Do-you-copy.pcap]

Soruda `Alpha-Do-you-copy` isminde bir pcap dosyası verilmiş. Pcap dosyasını wireshark ile inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-a1.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-a1.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-a2.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-a2.png" alt="image-1" /></a>
	</div>
</center>

Pcap içerisinde bulunan `60` paketin tamamının `TCP` protokolüne ait olduğunu görüyoruz. Paketlerde bazı ilgi çekici noktalar var. Hedef ve Kaynak IP adresine baktığımızda aynı IP adresinin yer aldığını görüyoruz. Bu durum normalin dışında olan bir durumdur. Ayrıca tüm paketlerin boyutları aynı. Bir diğer önemli nokta `Flagler`. Flagleri incelediğimizde TCP Threeway handshake'in bulunmadığını görüyoruz. Bazı paketlerde hiç flag değeri set edilmemiş. Bütün bu bilgilere dayanarak normal olmayan bir trafikle karşı karşıya olduğumuzu anladık. Peki bu durumda bu paketler neyi ifade ediyor? 

Wiresharkta en alttaki kısımda paketin bytelarını görebiliyoruz. İki farklı paket arasında byte farklılığının çok az olduğunu farkediyoruz. Bu farklılık flaglerden kaynaklanıyor. Flag değerlerine baktığımızda 3 farklı değer ile karşılaşıyoruz: `SYN bayrağı set edilmiş`, `ACK bayrağı set edilmiş` ve `hiçbir bayrağın set edilmemiş` olmaması. 3 farklı değerin olması aklımıza `morse code` karakter setini getiriyor. Morse code yapısında da 3 farklı karakter bulunur: `-`, `.` ve `Boşluk` değerleri. Flag değerlerini alabilmek için `tcpdump` isimli araçtan faydalanalım.

```
kali@kali:~/STMCTF20/sorular/alpha$ sudo tcpdump -r Alpha-Do-you-copy.pcap | cut -d " " -f 7
reading from file Alpha-Do-you-copy.pcap, link-type EN10MB (Ethernet)
[.],
[.],
[none],
[.],
[.],
[.],
[none],
[S],
[.],
[S],
[none],
.
.
REDACTED
.
.
```

Tcpdump ile birlikte flag değerlerini almış olduk. Burada `[.]` bu değer ACK bayrağı anlamına gelmektedir. `[S]` değeri SYN bayrağı anlamına gelmektedir. `[none]` değeri boşluk değerini ifade etmektedir. Bu değerlerin tamamını `morse.txt` isimli dosyaya kaydedelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf20-a3.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf20-a3.png" alt="image-1" /></a>
	</div>
</center>

Flag değerleri ile morse karakterleri arasındaki doğru eşleştirme değerleri aşağıdaki şekildedir:

```
ACK bayrağı = -
SYN bayrağı = .
none = boşluk
```

Kaydettiğimiz bu değerleri `sed` komutunun yardımıyla morse code karakterlerine çevirelim.


```
kali@kali:~/STMCTF20/sorular/alpha$ sed -i 's/\[\.\]\,/\-/g' morse.txt && sed -i 's/\[S\]\,/\./g' morse.txt && sed -i 's/\[none\]\,/ /g' morse.txt && sed -z 's/\n//g' morse.txt
-- --- .-. ... . ..--.- .. ... ..--.- -- --- .-. ... .      
```

Morse code değerimizi oluşturduktan sonra github üzerinden indirdiğimiz [morse-encode-and-decode] aracına vererek decode işlemini yapabiliriz.

```
kali@kali:~/STMCTF20/sorular/alpha$ morse-encode-and-decode/morse-encode-and-decode -d "-- --- .-. ... . ..--.- .. ... ..--.- -- --- .-. ... . "
base string:
-- --- .-. ... . ..--.- .. ... ..--.- -- --- .-. ... . 

get decode string:
morse_is_morse
```

Morse decode işleminden sonra sonucumuz ortaya çıkıyor: `morse_is_morse` Flag formatı içerisine yerleştirerek flag değerimizi elde etmiş oluyoruz.

```
STMCTF{morse_is_morse}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'20]: https://ctfonline.stm.com.tr/
[Alpha-Do-you-copy.pcap]: {{site.baseurl}}/assets/files/Alpha-Do-you-copy.pcap
[morse-encode-and-decode]: https://github.com/Joker2770/morse-encode-and-decode

