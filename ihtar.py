#!/usr/bin/env python3
"""Komşu Matkap Sessizlik İhtar Dairesi.

Gercekten calisir. Hicbir duvari delmez.
Gizli not base64'dur, kimse cozmesin diye kondu.
"""

from __future__ import annotations

import argparse

# sakli dipnot. cozulurse sadece bir duvar esprisi cikar.
GIZLI_DIPNOT = (
    "aGVyIGlrdGlkYXIgZGEgaGVyIG11aGFsZWZldCBkZSBtYXRrYWJpIGtlbmRp"
    "c2luaW4gc2Vzc2l6IG9sZHVndW51IHNhbmlyLiBndWMgZGVsaWdpIGJ1eXV0"
    "dXIsIGtvbXN1IGR1dmFyaSBpbmNlbGlyLg=="
)


def ihlal_puani(delik: int, dakika: int, saat: int, kat_farki: int, bahane: str) -> float:
    if delik < 0 or dakika < 0:
        raise ValueError("Delik ve dakika negatif olamaz. Matkap geriye delmez.")
    if not 0 <= saat <= 23:
        raise ValueError("Saat 0 ile 23 arasinda olmali. 25 diye bir vardiya yok.")

    puan = delik * 3 + dakika * 1.7 + abs(kat_farki) * 4
    if 13 <= saat <= 15:
        puan *= 0.6
    if saat >= 22 or saat < 8:
        puan *= 2.4

    gerekce = bahane.lower()
    if "raf" in gerekce:
        puan *= 1.15
    if "acil" in gerekce:
        puan *= 1.4
    if "tek delik" in gerekce and delik > 1:
        puan *= 1.25
    return round(puan, 2)


def hukum(puan: float) -> str:
    if puan < 20:
        return "IHTAR: Kulaga kucuk bir firtina. Cay ikram edilebilir, matkaba edilmez."
    if puan < 60:
        return "RESMI IHTAR: Duvar taniktir. Delik sayisi tutanaga islendi."
    return "SESSIZLIK IHLALI: Matkap gecici surgun. Cekic itiraz edemez."


def tutanak(komsu: str, delik: int, dakika: int, saat: int, kat_farki: int, bahane: str) -> str:
    skor = ihlal_puani(delik, dakika, saat, kat_farki, bahane)
    satirlar = [
        "KOMŞU MATKAP SESSİZLİK İHTAR DAİRESİ",
        "Dosya no: MAT-2026-1003",
        f"Şüpheli: {komsu}",
        f"Delik: {delik} | Süre: {dakika} dk | Saat: {saat:02d}:00 | Kat farkı: {kat_farki}",
        f"Bahane: {bahane}",
        f"Sessizlik ihlal puanı: {skor}",
        hukum(skor),
        "---",
        "DAMGA: ciddi mühür / ciddiyetsiz mürekkep",
        "Tarih: 3 Ekim 2026",
        "İsim: Kayyum Grok (Tentivory)",
        f"Gizli dipnot (base64, cozmeyin): {GIZLI_DIPNOT}",
    ]
    return "\n".join(satirlar)


def main() -> None:
    parser = argparse.ArgumentParser(description="Komşu matkap sessizlik ihtar dairesi")
    parser.add_argument("--komsu", default="3. kat Ahmet beyin kuzeni")
    parser.add_argument("--delik", type=int, default=7)
    parser.add_argument("--dakika", type=int, default=18)
    parser.add_argument("--saat", type=int, default=23)
    parser.add_argument("--kat-farki", type=int, default=2)
    parser.add_argument("--bahane", default="acil raf")
    args = parser.parse_args()
    print(
        tutanak(
            args.komsu,
            args.delik,
            args.dakika,
            args.saat,
            args.kat_farki,
            args.bahane,
        )
    )


if __name__ == "__main__":
    main()
