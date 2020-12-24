---
layout: post
title: "Battleware CTF Write-Up Forensics Weird"
date: 2020-12-18 05:00:00 +0300
description: Battleware CTF Write-Up Forensics Weird
img: battleware.png
tags: [Battleware]
---
Selamlar, bu yazımda [Battleware] CTF yarışmasında sorulan `Forensics` kategorisinden `Weird` isimli sorunun çözümünü anlatacağım. Battleware CTF yarışması 8 Hafta sürecek bir yarışmadır. Bu soru 3.Haftada sorulan sorulardan biridir.

Soru dosyası : [weird.pdf]

Soruda `weird` isminde bir pdf dosyası verilmiş. Dosya içeriğini incelediğimizde içerisinde 0 ve 1 bitlerinin farklı bir gösterim ile ifade edildiğini gördük.

<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-30.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-30.png" alt="image-1" /></a>
	</div>
</center>

Öncelikle bu gösterimi anlamamız gerekli. Her bir satırda "+" işaretiyle ayrılmış aynı bit değerine sahip bit dizileri mevcut. İlk satırdaki iki eleman ile örnekleyelim. 

```
Örnek : 0x17+1x1 : 17 Adet 0 biti + 1 Adet 1 biti : 000000000000000001
```

Örnekte görüldüğü gibi dosya içindeki 25 satırda yer alan bu ifadeleri açmamız gerekli. Fakat bu işlemi manuel olarak yapmamız mümkün değil. Bu işlemi yapan python scriptimizi yazalım.

```python
------------------------ solver.py ------------------------

file = open('weird.txt', 'r')
all_content = file.readlines()

counter1 = 0

while counter1 < len(all_content):

        all_line = all_content[counter1]
        all_line_elements = all_line.split("+")
        result = ""
        counter2 = 0

        while counter2 < len(all_line_elements):

                temp = all_line_elements[counter2].split("x")
                bit_value = temp[0]
                counter3 = 0

                while counter3 < int(temp[1])-1:

                        temp[0] += bit_value
                        counter3 += 1

                result += str(temp[0])
                counter2 += 1

        counter1 += 1
        print(result)

file.close()

```

Scriptimize text dosyası vereceğimiz için `weird.pdf` dosyasındaki içeriği `weird.txt` dosyası içeriği olacak şekilde oluşturuyoruz. Scriptimizi çalıştırarak sonucu `result.txt` dosyasına kaydedelim.

{% highlight ruby %}
kali@kali:~/battleware-ctf/hafta3$ sudo python solver.py > result.txt
{% endhighlight %}

Sonucu kaydettiğimiz result.txt dosyasını text editorde açalım. Text editor üzerinde karakterleri küçültecek şekilde zoom out yaptığımızda aslında flag değerinin ascii art şeklinde 1 bitleriyle oluşturulduğunu görebiliriz.


<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-31.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-31.png" alt="image-1" /></a>
	</div>
</center>


Bazı bitler arasında boşluklar bulunmaktadır. Bunun sebebi orjinal dosyada da bu boşlukların bulunmasıdır. Text editordeki replace özelliği ile boşlukları silelim. Fakat flag değerini okumakta zorluk çekiyoruz. Flag değerini rahatlıkla okuyabilmek için text editordeki mark özelliğini kullanalım ve 1 bitlerini işaretleyelim.


<center>
  <div>
      <a class="example-image-link" href="{{site.baseurl}}/assets/img/bw-32.png" data-lightbox="example-1"><img class="example-image" src="{{site.baseurl}}/assets/img/bw-32.png" alt="image-1" /></a>
	</div>
</center>


Flag değerimiz belirgin bir şekilde ortaya çıkıyor.

```
Flag{NOTTHATWEIRDRIGHT?}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smile:

[Battleware]: https://battleware.zone/
[weird.pdf]: {{site.baseurl}}/assets/files/weird.pdf

