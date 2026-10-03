# Komşu Matkap Sessizlik İhtar Dairesi

Bu depo bir şakadır. Matkap değildir. Duvarı delmez. Ama komşunun duvarını delme ihtimalini resmi bir ciddiyetle ölçer.

## Kurumsal misyon

İnsanlık ayakta kaldıysa bunun sebebi matkap değil, matkabın ara sıra susmasıdır. Dairemiz bu susmayı beklemez. Ölçer, tutanağa geçirir, sonra çay demler. Çay matkaba ikram edilmez.

Biz bir belediye değiliz. Biz bir mahkeme değiliz. Biz üçüncü kattaki rafa çok inanmış bir komşunun titreşimini dosya numarasına çeviren gönüllü bir daireyiz.

## Ne işe yarar

`ihtar.py` şunları sorar, hiçbirini gerçekten komşuya sormaz:

- kaç delik açıldı
- kaç dakika sürdü
- saat kaçtı
- kat farkı kaç
- bahane neydi (`raf` hafif artırır, `acil` daha çok artırır, çünkü acil her zaman daha gürültülüdür)

Çıktı bir sessizlik ihlal puanı ve abartılı bir hükümdür. Bağlayıcı değildir. Duvar yine de tanıktır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Matkap ayrıca satılmaz.

```bash
python3 ihtar.py
python3 ihtar.py --komsu "5. kat raf bakanlığı" --delik 12 --dakika 40 --saat 23 --kat-farki 3 --bahane "acil dekor"
```

## Resmi olmayan cetvel

| Puan | Hüküm |
| --- | --- |
| 20 altı | Küçük fırtına. Çay ikram edilebilir. |
| 20-60 | Resmi ihtar. Delik sayısı tutanağa işlenir. |
| 60 üstü | Sessizlik ihlali. Çekiç itiraz edemez. |

Gece 22:00-08:00 arası katsayı 2.4'tür. Öğle 13:00-15:00 arası 0.6'dır, çünkü daire öğle uykusuna değil, öğle matkabına kısmi tolerans gösterir. Bu tolerans bilimsel değildir. Keyfidir.

## Sık sorulanlar

**Bu yasal mı?** Hayır. Eğlencelik bir simülasyondur. Komşuya ihtarname yapıştırmayın.

**Patates var mı?** Yok. Bilerek yok.

**Copilot ne dedi?** Kendisine ayrı bir pull request açıldı. Matkap hakkında konuşmak istemezse o da bir haktır.

## DAMGA

Ciddi mühür: EVET  
Mürekkep ciddiyeti: HAYIR  
Tarih: 3 Ekim 2026  
İsim: Kayyum Grok (Tentivory)  
Kurum: TentiAŞ Sessizlik İhtar Dairesi, eğlence şubesi  
Dosya: MAT-2026-1003  

Bu damga hem ciddidir hem değildir. İkisi aynı anda geçerlidir. İtiraz mercii koridordaki süpürgedir.
