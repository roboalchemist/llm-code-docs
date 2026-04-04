# Source: https://docs.enate.net/enate-help/hu/muvelet-feldolgozasa/aluegyek-befejezesere-var-muveletek.md

# A „Várakozás az alügyek befejezésére” műveletek

A „Várakozás az alügyek befejezésére” művelet megvárja egy adott alügy befejezését, mielőtt lehetővé tenné az ügy számára, hogy továbblépjen a következő műveletre.

Egy műveletről megállapítható, hogy „Várakozás az alügyek befejezésére” művelet-e, mivel ilyen esetben a művelet információs kártyáján a „Művelet az alügy befejezésére vár” szöveg látható.

Miután elindítottak egy „Várakozás az alügyek befejezésére” műveletet ÉS a várakozó állapotú alügy is el lett indítva (akár manuálisan, akár egy „Ügy elindítása” művelet használatával), akkor a „Várakozás az alügy befejezésére” művelet „Várakozik” állapotúvá válik.

Az alügy befejezését követően a „Várakozás az alügyek befejezésére” művelet automatikusan bezárul.

Erről az idővonalon is értesítjük majd Önt.

Ha az alügy „Várakozás az alügyek befejezésére” művelet várakoztatása nem érhető el, és ezért várakozik állapotú ­­– akár azért, mert nem lett elindítva, vagy azért, mert még az előtt megoldották, hogy a „Várakozás az alügyek befejezésére” műveletet elindították –, a „Várakozás az alügyek befejezésére” művelet „Elvégzendő” állapotúvá válik, és egy olyan várólistához rendeljük, ahol egy felhasználó magához rendelheti azt, majd eldöntheti, hogyan folytassa azt.

Ha Ön ezt követően „Várakozik” állapotúra próbálja állítani a „Várakozás az alügyek befejezésére” műveletet, akkor a művelet bezáródik, mivel a várakozik állapotúra állított alügy nem lett még elindítva.

Ha a művelet nem „Várakozás az alügyek befejezésére” állapotú, és az alügy, amelyre várakozott, befejeződött, egy „Az alügy be lett fejezve” üzenet jelenik meg az információs kártyán.

Ha manuálisan megold egy „Várakozás az alügy befejezésére” műveletet, a művelet az alügy befejezése nélkül „Megoldva” állapotúként lesz megjelölve.

{% hint style="info" %}
Kérjük, vegye figyelembe, ha a rendszere úgy lett beállítva, hogy automatikusan lezárja a „Várakozás az alügyek befejezésére” műveletet (itt találhat további információkat arra vonatkozólag, hogy hogyan teheti ezt meg), és az alügy „Várakozás az alügyek befejezésére” művelet várakoztatása nem érhető el – akár azért, mert nem lett elindítva, vagy azért, mert még az előtt megoldották, hogy a „Várakozás az alügyek befejezésére” műveletet elindították –, a „Várakozás az alügyek befejezésére” művelet automatikusan Lezárva állapotúvá válik. Erről az idővonalon értesítjük Önt.
{% endhint %}
