---
layout: post
title: "STMCTF'19 Write-Up Forensics Travel"
date: 2021-07-13 05:00:00 +0300
description: STMCTF'19 Write-Up Forensics Travel
img: stmctf19.jpg
tags: [STMCTF19]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Forensics` kategorisinden `Travel` isimli sorunun çözümünü anlatacağım.

Soru dosyası : [ubuntu16044x64.zip]

Soruda `ubuntu16044x64` isminde bir zip dosyası verilmiş. Zip dosyasını extract ettiğimizde içinden `ubuntu16044x64.mem` isimli bir linux memory imaj dosyası çıkıyor. İmaj dosyasını açıp incelemek için [volatility] isimli araçtan yararlanalım. Volatility aracı memory imajlarını incelemek için geliştirilmiş bir araçtır. Gui ve konsol tabanlı sürümleri mevcuttur. Bu yazımda konsol tabanlı sürümü kullanacağım. Volatility aracı memory imajlarını incelerken profil dosyalarını kullanır. Windows sistemler için profil dosyaları sistem sürümüne göre hazır durumda volatility ile beraber gelmektedir. Fakat linux sistemler için hazır profil dosyaları volatility ile birlikte gelmediği için kendi profil dosyamızı oluşturmamız gerekir. Eğer bu profil dosyası oluşturulmazsa analizi gerçekleştirmemiz mümkün değildir. Profil dosyası canlı sistem üzerinden elde edilir. Öncelikle memory imajı verilmiş sistemi sanal ortama kurmamız gerekir. Sistemi kurarken kernel sürümü ve sistem versiyonu bilgisi memory imajı alınmış sistem ile aynı olmalıdır. Aksi takdirde doğru profil dosyası oluşturulmamış olacaktır ve analiz yapılamayacaktır. Profil dosyası, içerisinde iki dosya barındıran zip uzantılı bir dosyadır. Bu iki dosya `System.map` ve `module.dwarf` dosyalarıdır. Linux sistemi kurduğunuzda `System.map` dosyası isminde kernel sürüm bilgisi de olacak şekilde `/boot` dizini altında bulunur. Yaklaşık olarak 3-10 MB boyutlarında metin tabanlı bir dosyadır. `Module.dwarf` dosyası ise hazır bir şekilde linux içinde bulunmaz. `dwarfdump` isimli araç ile birlikte linux içerisinde oluşturulması gerekir.

Not : Yazının uzamaması için profil dosyası oluşturma aşaması yazılı olarak ifade edilmiştir. 

Profil Dosyasının Hazırlanması : 

1 - Profil dosyası hazırlanacak sistem üzerine `dwarfdump` aracı kurulur.

2 - Volatility aracı indirilir ve `volatility/tools/linux` dizini altına geçilir. Bu dizinde `make` komutu ile `module.dwarf` dosyası oluşturulur.
 
3 - `/boot` altındaki system.map dosyası kopyalanarak ismi `System.map` olacak şekilde oluşturulan `module.dwarf` dosyası ile tek bir zip dosyası haline getirilir ve profil dosyası hazır duruma gelmiş olur.


Profil dosyası hazırlandıktan sonra analiz aşamasına geçilebilir. Analizi yapabilmek için oluşturulan profil dosyası([Ubuntu16044.zip]) `../volatility/volatility/plugins/overlays/linux/` dizini altına kopyalanır.

Analiz aşamasının ilk adımı olarak profil dosyası ismini volatility içerisinden öğrenelim. Aynı zamanda profil dosyasını doğru yere kopyaladığımızdan da emin olmuş olalım.

```Uygulanan Komut : sudo python2.7 vol.py --info | more ```

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d1.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d1.png" alt="image-1" /></a>
	</div>
</center>

Profil ismini öğrendikten sonra volatility pluginleri ile birlikte prosesleri incelemeye başlayalım.

```Uygulanan Komut : sudo python2.7 vol.py --profile=LinuxUbuntu16044x64 -f ubuntu16044x64.mem linux_pslist ```

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d2.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d2.png" alt="image-1" /></a>
	</div>
</center>

Listelenen prosesleri incelediğimizde 3 farklı PID numarasına sahip python prosesi olduğunu görüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d3.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d3.png" alt="image-1" /></a>
	</div>
</center>

Çalıştırılan python proseslerine ait python scriptlerini tespit edelim.

```Uygulanan Komut : sudo python2.7 vol.py --profile=LinuxUbuntu16044x64 -f ubuntu16044x64.mem linux_enumerate_files | grep .py ```

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d4.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d4.png" alt="image-1" /></a>
	</div>
</center>

İsimleri benzer olan 3 farklı python scriptini tespit etmiş olduk. Python scriptlerinin içeriğini görmek için export edelim. Export işlemi esnasında -i parametresiyle bir önceki komut çıktısında bulunan dosyaya ait `inode number` verilmelidir.

```Uygulanan Komut : sudo python2.7 vol.py --profile=LinuxUbuntu16044x64 -f ubuntu16044x64.mem linux_find_file -i 0xffff98c379e337c0 -O part1.py ```

```Uygulanan Komut : sudo python2.7 vol.py --profile=LinuxUbuntu16044x64 -f ubuntu16044x64.mem linux_find_file -i 0xffff98c379e35110 -O part2.py ```

```Uygulanan Komut : sudo python2.7 vol.py --profile=LinuxUbuntu16044x64 -f ubuntu16044x64.mem linux_find_file -i 0xffff98c379e300e8 -O part3.py ```


<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d5.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d5.png" alt="image-1" /></a>
	</div>
</center>

Sırasıyla 3 farklı python scriptini kaydettikten sonra kaynak kodları inceleyelim.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d6.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d6.png" alt="image-1" /></a>
	</div>
</center>

Her bir python scriptinin içinde base64 encoded data olduğunu görüyoruz.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d7.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d7.png" alt="image-1" /></a>
	</div>
</center>

<br>

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d8.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d8.png" alt="image-1" /></a>
	</div>
</center>

Base64 encoded dataları decode ettiğimizde koordinatlar karşımıza çıkıyor.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d9.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d9.png" alt="image-1" /></a>
	</div>
</center>

Koordinat bilgileri sırasıyla haritaya flag değerini yazıyor. Bunun için `gmplot` isimli bir araçtan yararlanalım. Gmplot aracıyla flagi haritaya yazdırmak için bir python scripti hazırlanmalıdır.([flag_draw.py]) Bu python scripti çalıştırıldığında harita html uzantılı olarak oluşturulur. Html dosyasını browser ile açtığımızda flag değerini harita üzerinde görebiliriz.([my_map.html])

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/stmctf19-d10.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/stmctf19-d10.png" alt="image-1" /></a>
	</div>
</center>

Flag değerini elde etmiş oluyoruz.

```
STMCTF{KEEPCALMANDSENDMETHEFLAG}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:


[STMCTF'19]: https://ctfonline.stm.com.tr/
[volatility]: https://github.com/volatilityfoundation/volatility
[ubuntu16044x64.zip]: https://s7.dosya.tc/server19/cllspx/ubuntu16044x64.zip.html
[Ubuntu16044.zip]: {{site.baseurl}}/assets/files/Ubuntu16044.zip
[my_map.html]: {{site.baseurl}}/assets/files/my_map.html
[flag_draw.py]: {{site.baseurl}}/assets/files/flag_draw.py

