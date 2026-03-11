# Source: https://docs.enate.net/enate-help/hu/muvelet-feldolgozasa/jovahagyasi-muveletek.md

# Jóváhagyási műveletek

## Mik azok a jóváhagyási műveletek? Hogyan működnek?

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==?utm_medium=iframely&utm_source=gitbook>" %}

Az Enate-be beépített üzleti folyamatok ügyein belül gyakran vannak olyan pontok, ahol az adott folyamat folytatásához külső személyek (azaz az Enate-en **kívül** dolgozó emberek, akik az Ön vállalatának vagy egy érintett ügyfélvállalatnak az üzleti vezetői is lehetnek) jóváhagyására van szükség. Az ilyen feladatokra jó példák a bérszámfejtési folyamatok, ahol a folyamat folytatásához az ügyfélmenedzsmentnek jóvá kell hagynia a bérszámfejtési jelentéseket.

Az Enate jóváhagyási műveletét kifejezetten úgy hoztuk létre, hogy jóval integráltabb módon támogassa ezeket a jóváhagyásikérelem-forgatókönyveket annak biztosítása érdekében, hogy ez a „jóváhagyási ciklus” szorosan felügyelt, valamint az Enate műveletfolyamatain belül is jól látható legyen.

## Hogyan működnek a jóváhagyási műveletek futtatás közben?

Az Enate-en kívül dolgozó ügynököknek jóváhagyási kérelmeket küldünk, amelyeket jóváhagyhatnak vagy elutasíthatnak.

A jóváhagyásnak több típusa is van, amelyek befolyásolják a döntéshozatal módját:

* Egy többszintű forgatókönyv esetén a kérelmező e-mailt továbbküldjük a következő szintű jóváhagyónak, amennyiben azt az előző szinten jóváhagyták. Legfeljebb 3 ilyen jóváhagyási szint alkalmazható. Amennyiben egy személy ezt nem hagyja jóvá, a kérelem el lesz utasítva.
* Párhuzamos forgatókönyv esetén a kérelmező e-mailt minden jóváhagyónak elküldjük, és az már az első döntéssel jóváhagyható.
* Párhuzamos: mindenki forgatókönyv esetén a kérelmező e-mailt minden jóváhagyónak elküldjük, és MINDENKINEK jóvá kell azt hagynia ahhoz, hogy a kérelem jóvá legyen hagyva. Amennyiben valaki ezt nem hagyja jóvá, a kérelem el lesz utasítva.

Ha a kérelmet minden szükséges fél jóváhagyja, akkor a jóváhagyási művelet sikeresen megoldódik és automatikusan lezárul, így a Work Manager egyetlen ügynökének sem kell majd azt magához vennie – de a lezárt művelet bármikor megtekinthető, ha automatikusan rákattint arra.

## Kivételek, amelyeket a Work Manager ügynöke kezel

Előfordulhatnak azonban olyan esetek, amikor a Work Manager egyik ügynökének magához kell vennie a jóváhagyási műveletet, és el kell végeznie rajta a szükséges műveleteket annak további feldolgozásához:

* A jóváhagyást elutasították
* Nincsenek automatikusan meghatározott jóváhagyók (vagy nincs elegendő jóváhagyó)

### Jóváhagyási kérelem elutasítva

Abban az esetben, ha a jóváhagyási kérelem **el lett utasítva**, akkor a művelet „Elvégzendő” állapotúvá válik, és a Work Manager ügynökének fel kell majd azt vennie. Át kell tekintenie az elutasítás a jóváhagyó személy által megadott okát, majd el kell döntenie, hogy a továbbiakban hogyan jár el. A következőket teheti:

1. **Szükség szerint frissítheti azt, majd a művelet „Várakozás” módba állításával ismét elküldheti a kérelmet.** Ezzel újra automatikusan elküldi a jóváhagyási kérelmet tartalmazó e-mailt\*\*, és a műveletet „További információra vár” állapotba helyezi – mivel mielőtt a folyamat folytatódhatna, külső információ (egy jóváhagyás) regisztrálására van szükség a rendszerben.
2. **„Nem lehet befejezni” állapotúra állíthatja a műveletet.** Ez figyelmezteti majd az ügy tulajdonosát, aki így eldöntheti, hogy a továbbiakban hogyan fog eljárni – talán átdolgozza vagy teljesen lezárja majd az ügyet.
3. **Megoldva állapotúnak jelölheti meg a műveletet**, amellyel manuálisan jóváhagyottként jelöli meg a kérelmet. Ezt követően az ügy továbblép a következő műveletre.

{% hint style="info" %}
\*\*Megjegyzés: A jóváhagyási kérelmek e-mailben történő kiküldése elölről kezdődik majd, azaz minden kérelmező újra megkapja majd azt. Ha egy korábban elküldött e-mailre kattintanak, akkor egy üzenet jelenik meg számukra, mely szerint az ADOTT jóváhagyási kérelem már nem érvényes, mivel a kért adatok már megváltozhattak.
{% endhint %}

### Nincs elegendő jóváhagyó

Olyan esetben, amikor egy ügynöknek jóváhagyókat kell hozzáadnia egy művelethez, mivel egy vagy több szükséges jóváhagyó üres (vagy olyan változtatásokat kell végrehajtania, amelyek miatt a jóváhagyási kérelmeket újra ki kell küldeni), akkor az ügynök magához veszi az Elvégzendő állapotú jóváhagyási műveletet. A szükséges módosítások végrehajtását és/vagy a hiányzó jóváhagyók neveinek megadását követően **a műveletet Várakozás állapotúként kell beállítaniuk**. Ha így tesznek, akkor azzal automatikusan elküldik a jóváhagyási kérelmet tartalmazó e-mailt, majd „További információra vár” állapotúra állítják a műveletet, mivel az a folytatás előtt külső információra (jóváhagyásra vár).

{% hint style="info" %}
Megjegyzés: Amíg egy jóváhagyási művelet „Elvégzendő” vagy „Folyamatban” állapotú, a jóváhagyási kérelmet fogadó külső felek NEM hagyhatják jóvá és nem is utasíthatják azt el. Ehelyett egy olyan üzenetet láthatnak majd, amely arról értesíti őket, hogy a kérdéses elem feldolgozása jelenleg éppen folyamatban van. A Work Manager ügynökeinek a műveletet ismét „További információra vár” állapotba KELL helyezniük, ha újra kívánják indítani a jóváhagyási tevékenységet.
{% endhint %}

### Ha lejárt a jóváhagyási kérelem

Egy másik lehetséges forgatókönyv az, amikor egy jóváhagyási művelet automatikusan lezárul, mivel az lejárt vagy nem érkezett be időben elegendő válasz. Ebben az esetben a művelet automatikusan Megoldva állapotú lesz, és az ügy folytatódik. Ilyen helyzetben a műveletet a Work Manager egyetlen ügynökének sem kell magához vennie, bár a lezárt művelet arra manuálisan rákattintva mindig megtekinthető lesz.
