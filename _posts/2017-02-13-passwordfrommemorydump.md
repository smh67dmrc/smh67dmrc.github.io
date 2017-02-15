---
layout: post
title: "Hafıza İmajından Windows Parolalarını Elde Etme"
date: 2017-02-13
categories: forensics
---
Bu yazımda sizlere "volatility" ile hafıza imajından windows parolalarını elde etmeyi göstereceğim.Hafıza imajını kullandığım sistem "Windows 7 SP1 x86" olacak.Hafıza imajını "DumpIt" adlı tool ile kolayca alabilirsiniz.
Öncelikle imaj dosyası hakkında bilgi edinmek için volatility "imageinfo" plugin kullanıyoruz.

<img src="/images/password-from-memory-dump/passwordfrommemorydump.jpeg" class="fit image">

Burada profile kısmını not ediyoruz çünkü volatility'ye profil tanımlaması yapmamız gerekiyor.
Daha sonraki adımda "hivelist" kullanarak registrylerin memory üzerindeki başlangıç adreslerini bulmamız gerekiyor.

<img src="/images/password-from-memory-dump/passwordfrommemorydump2.jpeg" class="fit image">

Burada ilgilendiğimiz kısım SYSTEM'e ve SAM'e ait virtual adreslerdir.

<img src="/images/password-from-memory-dump/passwordfrommemorydump3.jpeg" class="fit image">

Kullanıcıların parola özetlerini "hashdump" ile alıp text dosyasına kaydediyoruz.

<img src="/images/password-from-memory-dump/passwordfrommemorydump4.jpeg" class="fit image">

Txt dosyasındaki hashleri crack işlemleri uygulayarak plaintext haline getirebiliriz.

NOT : Yazı içinde ismi geçen parametreler , toollar ve dosyalar hakkında detay verilmeden konu anlatılmıştır.Gerek görüldüğü durumda ufak bi research ile ne oldukları hakkında bilgi edinebilirsiniz.

 




