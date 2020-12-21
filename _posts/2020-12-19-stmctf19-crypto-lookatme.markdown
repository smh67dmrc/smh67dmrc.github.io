---
layout: post
title: "STMCTF'19 Write-Up Crypto Look At Me"
date: 2020-12-20 05:00:00 +0300
description: STMCTF'19 Write-Up Crypto Look At Me
img: stmctf19.jpg
tags: [CTF, STMCTF19, Write-Up, Capture The Flag]
---
Selamlar, bu yazımda [STMCTF'19] yarışmasında sorulan `Crypto` kategorisinden `Look At Me` isimli sorunun çözümünü anlatacağım.

Soruda `xk9awxk9awexk9awar` şeklinde şifreli bir metin verilmiş ve şifre çözülerek cevabın flag formatı içine yerleştirilmesi istenmiş.(Flag Formatı : STMCTF{flag}) Bu soru yarışmada ilk açılan sorulardan biri ve ısınma(Warm-Up) amaçlı hazırlanmış.

Şifreli metnimiz `Keyboard Shift Cipher` şifreleme yöntemi ile şifrelenmiş. Q klavyeye göre karakterler sağa 1 kez kaydırıldığında anlamlı metin ortaya çıkmış olur. Çözüm manuel olarak yapılabileceği gibi online araçlardan da faydalanılabilir.([https://www.dcode.fr/keyboard-shift-cipher])

```
Karakterlerin 1 kez shift edilmiş halleri :

x => c
k => l
9 => 0
a => s
w => e
e => r
r => t

```

Decrypt ettiğimiz şifreli metinden ortaya çıkan düz metni flag formatı içine yerleştirdiğimizde flag ortaya çıkar.

```
STMCTF{cl0secl0sercl0sest}
```

Yazımı okuduğunuz için teşekkürler, bir başka yazıda görüşmek dileğiyle.. :smiley:

[STMCTF'19]: https://ctfonline.stm.com.tr/
[https://www.dcode.fr/keyboard-shift-cipher]: https://www.dcode.fr/keyboard-shift-cipher





