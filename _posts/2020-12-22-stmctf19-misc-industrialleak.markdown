---
layout: post
title: "STMCTF'19 Write-Up Misc Industrial Leak"
date: 2020-12-22 05:00:00 +0300
description: STMCTF'19 Write-Up Misc Industrial Leak
img: stmctf19.jpg
tags: [STMCTF19]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Misc` kategorisinden `Industrial Leak` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [ics.pcap]

Soruda `ics` isminde bir pcap dosyası verilmiş. Pcap dosyasını wireshark aracıyla incelediğimizde içinde birçok protokole ait paket olduğunu farkediyoruz. Fakat soru adının `Industrial Leak` olması bize ipucu veriyor. Aradığımız paket türü endüstriyel sahada kullanılan bir protokol olabilir diye düşünerek incelemeye devam ediyoruz. İstatistikler sekmesinden protokol hiyerarşisini incelediğimizde pcap içindeki tüm protokolleri görüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-10.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-10.png" alt="image-1" /></a>
	</div>
</center>

Protokoller içerisinde [ModbusTCP] protokolü dikkatimizi çekiyor. Araştırdığımızda ModbusTCP protokolünün [PLC] cihazlarında haberleşme amaçlı kullanıldığını öğreniyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-11.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-11.png" alt="image-1" /></a>
	</div>
</center>

İncelememiz gereken protokol ModbusTCP olduğu için modbus filtresiyle paketleri incelemeye devam ediyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-12.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-12.png" alt="image-1" /></a>
	</div>
</center>

Öncelikle ModbusTCP iletişimini anlamamız için protokol hakkında bilgi sahibi olmamız gerekir. ModbusTCP protokolü seri haberleşme ile değerleri `cleartext` olarak gönderir. ModbusTCP iletişiminde 2 taraf vardır: `Master Cihaz` ve `Slave Cihaz`. Master cihazı IT altyapılarında bulunan istemci(client) cihazlara benzetebiliriz. Slave cihazı ise yine IT altyapılarında bulunan sunucu(server) cihazlarına benzetebiliriz. Master ve slave cihazlar arasında istemci-sunucu mimarisine benzer şekilde `request-response` ilişkisi bulunur. Master cihaz slave cihaza istek paketi gönderir ve slave cihazdan gelen yanıtı bekler. Yukarıda görüldüğü gibi istek ve yanıt paketleri ile iletişim sağlanmıştır. Fakat buradaki bir diğer önemli husus ModbusTCP protokolünde bulunan fonksiyon kodlarıdır. `Fonksiyon kodları` protokol içinde gönderilen paketin içinde bulunan bir değerdir. Bu değer ile slave cihaz master cihazın isteğinin ne olduğunu anlar. Yukarıdaki görselde görüldüğü üzere fonksiyon kodu 3'tür. Bunun anlamı `Read Holding Registers` şeklinde bir görev tanımıdır. Bu görev tanımıyla master cihaz slave cihaza der ki: benim sana belirtmiş olduğum birimde bulunan holding register değerini/değerlerini gönder. Yani bir başka deyişle slave cihaz üzerindeki değişkenlerin değerlerini okumak istiyorum. Böylelikle request paketini alan slave cihaz ilgili değeri response paketi içinde gönderir.

ModbusTCP hakkındaki bu bilgileri öğrendikten sonra değişkenlerin değerlerini inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-13.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-13.png" alt="image-1" /></a>
	</div>
</center>

Değişkenlerin değerlerine baktığımızda tek haneli sayılar olduğunu görüyoruz fakat son paket ilgimizi çekiyor çünkü diğer tüm paketlerden boyutu daha büyük. Büyük olan paketi incelediğimizde bir değişken yerine birden çok değişkenin değerinin yer aldığını görüyoruz. 

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-14.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-14.png" alt="image-1" /></a>
	</div>
</center>

Bu decimal değerlere `show packet bytes` seçeneğiyle bakalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-15.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-15.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-16.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-16.png" alt="image-1" /></a>
	</div>
</center>

Xor keyimizin `1` olduğunu öğrendik peki xor işlemini gerçekleştireceğimiz değerler nerede? Bu değerlerin tamamı ModbusTCP paketleri ile gönderilen değişkenlerin değerlerinin birleşimi olabilir. Çünkü modbusTCP protokolündeki data kısmı register değerlerinin bulunduğu alandır. Tek haneli sayıların yan yana gelerek oluşturduğu sayı dizisinde bulunan her bir rakamı 1 ile xor işlemine tabi tuttuğumuzda anlamlı bir çıktı olmasını bekliyoruz. Bu 79 paket içerisinde gönderilen değerlerin tamamını manuel olarak almak pek mantıklı değil. Bu yüzden terminal üzerinden çalışan `tshark` aracıyla tüm değerleri tek seferde alabiliriz. Gönderilen değerler sadece response paketlerindedir. Tshark aracına sadece ModbusTCP response paketlerini verebilmek için modbus paketlerini `modbus_response.pcap` isminde bir başka dosyaya export edelim. Bunun için filtre olarak `modbus.response_time` filtresini kullanabiliriz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-169.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-169.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-17.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-17.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-18.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-18.png" alt="image-1" /></a>
	</div>
</center>

Pcap dosyasını export ettikten sonra tshark aracına dosyayı vermeliyiz. Fakat tshark aracının bize sadece istediğimiz alanın değerlerini vermesini istiyoruz. Bunun için de filtre kullanmalıyız. Filtre yazmayı bilmiyorsak internetten tshark aracının kullanımına dair bilgi alabiliriz ayrıca wiresharktan yardım alabiliriz. Wiresharktan filtre kısmına yazmamız gereken alanın adını öğrenelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-19.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-19.png" alt="image-1" /></a>
	</div>
</center>
<br>
<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-191.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-191.png" alt="image-1" /></a>
	</div>
</center>

Filtre kısmına `modbus.regval_uint16` yazmamız gerektiğini öğrendik. Öğrendiğimiz bilgilerle birlikte tshark aracımızı çalıştıralım.

```
kali@kali:~/stmctf19$ tshark -r ./modbus_response.pcap -T fields -e modbus.regval_uint16
9
0
1
1
.
.
REDACTED
.
.
8
2
6
120,111,114,107,101,121,61,49
```

Komut çıktısında görüldüğü gibi değerlerin tamamını okuyabildik. Son kısımdaki `xorkey=1` bölümü hariç diğer tüm rakamları yanyana getirelim.

```
Sayı dizisi : 901189437217115916619526583979278599273549097389152422294800681956007725815826
```

Her bir rakamı 1 sayısı ile xor edelim. Burada dikkat edilmesi gereken input ve output değerlerinin `decimal` tipinde olmasıdır. Bu işlem için [http://xor.pw/] adresini kullanalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-192.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-192.png" alt="image-1" /></a>
	</div>
</center>

Sonuç olarak karşımıza decimal değerler çıkıyor. Bu değerleri boşluklu bir hale getirerek ascii karşılıklarına çevirelim. Bu işlem için [https://www.asciitohex.com/] adresini kullanalım.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf-193.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf-193.png" alt="image-1" /></a>
	</div>
</center>

Flag değerimizi elde etmiş oluyoruz.

```
STMCTF{InDu5tRi4L_C0ntR0L_SyST3mS}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'19]: https://ctfonline.stm.com.tr/
[ModbusTCP]: https://otomasyonadair.com/2014/09/22/modbus-protokolu/
[ics.pcap]: {{site.baseurl}}/assets/files/ics.pcap
[http://xor.pw/]: http://xor.pw/
[https://www.asciitohex.com/]: https://www.asciitohex.com/
[PLC]: https://tr.wikipedia.org/wiki/PLC
