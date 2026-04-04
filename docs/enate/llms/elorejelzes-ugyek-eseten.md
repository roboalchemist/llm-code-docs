# Source: https://docs.enate.net/enate-help/hu/a-kepernyok-attekintese-minden-munkatetel-eseten/elorejelzes-ugyek-eseten.md

# Előrejelzés ügyek esetén

## Áttekintés

A 2024.1-es verzió felhasználói az előrejelzési funkció segítségével képesek lesznek pontosabban megbecsülni a munkatételekre fordítandó erőfeszítések mértékét, lehetővé téve ezzel a szükséges erőforrások hatékonyabb megtervezését.

Hosszú távon ezen adatok összegyűjthetők és a rendszergazda szintű felhasználók rendelkezésére bocsáthatók, akik így módosíthatják a munkára fordítandó erőfeszítések időzítőit, ezáltal pontosabb előrejelzést nyújthatnak a jövőbeli munkamennyiségekről.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2F1CtcOEDrj4szZHsC3nii%2Fimage.png?alt=media&#x26;token=9616aaf8-dcd1-4198-8c82-07c15ee3521a" alt=""><figcaption></figcaption></figure>

## Az „Előrejelzés” használata

Az „Előrejelzés” funkció bekapcsolását követően egy új „Erőfeszítés-becslés” lap jelenik meg a Work Manager Ügyeinek felületén.

Itt az egész ügyre vonatkozó erőfeszítés-becslést megtekintheti, valamint láthatja az ügyet alkotó műveletek vagy alügyek erőfeszítés-becslésének lebontását, illetve a még létrehozásra váró műveletek vagy alügyek erőfeszítés-becslésének lebontását is.

#### Az Ügy erőfeszítéseinek összefoglalása

Az „Ügy erőfeszítéseinek összefoglalása” részben a felhasználónak lehetősége van az ügy becsült idejének módosítására. Ez további hasznos mutatókat is biztosít az ügyhöz.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FihxZ7oKGZzRuuGxcYLIG%2Fimage.png?alt=media&#x26;token=31e27fe9-6bd6-47d7-8f88-5175bdce7f89" alt=""><figcaption></figcaption></figure>

* A „Becsült” erőfeszítés az ügy teljes becsült időtartamát mutatja meg. Ezt a felhasználó igény szerint egy pontosabb becsléssel frissítheti.
  * Az ügyet alkotó összes létrehozott munka és művelet (valamint alügy-művelet) „Becsült” erőfeszítéseinek, valamint a „Még létrehozásra váró munka erőfeszítése” érték összege.
  * A mező először a Builderben fellelhető manuálisan megadott „Kezdeti becsült erőfeszítés bejegyzésenként” értéket jeleníti meg (ha van ilyen), megszorozva azt a bejegyzések számával.
    * Ha frissül a „Bejegyzésszám”, akkor frissül a Work Manager felhasználója által nem frissített ügyhöz tartozó „Becsült erőfeszítés” is, hogy tükrözze a bejegyzésszám változását.
  * Ha az ügy Megoldva vagy Lezárva állapotú, akkor a becsült erőfeszítés többé már nem módosítható.
  * Vegye figyelembe, hogy ennek az értéknek a megnövelése megnöveli a „Még létrehozásra váró munka erőfeszítése” becslését, és fordítva.
* A „Tényleges” erőfeszítés azt az időt jeleníti meg, amelyet a még létrehozásra váró munka esetén az ügyön elvégzett erőfeszítésekre fordítottak.
  * Ez az ügyet alkotó összes létrehozott művelet és alügy „tényleges” erőfeszítésének összege, amelyet ezek időráfordítás-követőiből gyűjtünk össze.
* A „Becsült hátralévő idő” az ügyön még hátralévő becsült időtartamot jeleníti meg.
  * Ez az ügyet alkotó összes létrehozott művelet és alügy „Becsült hátralévő idő” erőfeszítéseinek ÉS a még létrehozásra váró munka becsült hátralévő idejének összege (ezért előfordulhat, hogy ez nem mindig egyenlő az „Ügy becsült” mínusz az „Ügy tényleges” erőfeszítéseinek különbségével).

A „Becsült” erőfeszítés értékének módosítása egy ügy esetén a következő hatásokkal jár:

* A „Még létrehozásra váró munka erőfeszítése” becsült értékének automatikus frissítése. Ez azért történik így, mert az ügy „Becsült erőfeszítés” értéke az ügyet alkotó összes létrehozott munka és művelet (valamint alügy-művelet) „Becsült” erőfeszítéseinek, valamint a „Még létrehozásra váró munka erőfeszítése” összege.
  * Ha egy ügy esetén megnöveli a „Becsült” erőfeszítés értékét, akkor ugyanezzel az értékkel növeli meg a „Még létrehozásra váró munka erőfeszítése” értékét is.
  * Egy ügy „Becsült” erőfeszítés értékének csökkentésével ugyanezzel az értékkel csökkenti a „Még létrehozásra váró munka erőfeszítése” értékét.

#### A létrehozott munka erőfeszítéseinek lebontása

A „Létrehozott munka erőfeszítéseinek lebontása” részben a felhasználó módosíthatja az ügyet alkotó egyes létrehozott műveletek (és alügyek) becsült idejét. Emellett további hasznos mutatókat is megjelenít az ügyet alkotó összes létrehozott művelethez (és alügyhöz).

Ne feledje, ha a művelet Megoldva vagy Lezárva állapotú, akkor a becsült erőfeszítés többé már nem módosítható.

A műveletek (és alügyek) létrehozásakor a becsült erőfeszítésüket az alábbi Még létrehozásra váró munka rész Becsült erőfeszítés értéke alapján adjuk majd meg.

#### Művelet lebontása

Minden egyes művelet esetén Ön a következőket látja majd:

* Egy hivatkozás az egyes műveletekhez
* A „Becsült” erőfeszítés a művelet teljes becsült időtartamát mutatja meg. Ezt a felhasználó igény szerint egy pontosabb becsléssel frissítheti.
  * A mező először a Builderben fellelhető manuálisan megadott „Kezdeti becsült erőfeszítés bejegyzésenként” értéket jeleníti meg, megszorozva azt a bejegyzések számával.
    * Ha frissül a „Bejegyzésszám”, akkor frissül a Work Manager felhasználója által nem frissített, bármilyen folyamatban lévő művelethez tartozó „Becsült erőfeszítés” is, hogy tükrözze a bejegyzésszám változását.
  * Ennek az értéknek a növelése csökkenteni fogja a „Még létrehozásra váró munka” becslését, és fordítva is, ezért a teljes „Ügy becsült” erőfeszítésére is hatással lehet.
  * Ne feledje, ha a művelet Megoldva vagy Lezárva állapotú, akkor a becsült erőfeszítés többé már nem módosítható.
* A „Tényleges” erőfeszítés megmutatja, hogy eddig mennyi időt töltöttek el az adott műveleten dolgozva.
  * Ezt az értéket a művelet időráfordítás-követőjéből olvassuk ki.
* A „Becsült hátralévő idő” a műveleten még hátralévő becsült időtartamot jeleníti meg.
  * Úgy számítjuk ki, hogy a művelet „Becsült” erőfeszítéséből kivonjuk a „Tényleges” erőfeszítést.
* A művelet esedékességének időpontja
  * Ezen kívül megjelenik egy „Kezdési határidő” érték is, ha a „Tényleges” erőfeszítés jelenleg nulla. Ez az érték azt mutatja, hogy melyik az az időpont, amikor a művelet annak esedékességi dátumának teljesítése érdekében még elindítható.
* A művelet állapota

A „Becsült” erőfeszítés értékének módosítása egy művelet esetén a következő hatásokkal jár:

* A „Még létrehozásra váró munka erőfeszítése” becsült értékének automatikus frissítése az ügyhöz.
* A „Becsült” erőfeszítés esetleges automatikus frissítése az egész ügyre vonatkozóan.

Részletek:

* Egy művelet „Becsült” erőfeszítésének csökkentése ugyanezzel az összeggel növeli meg az ügy „Még létrehozásra váró munka erőfeszítése” értékét (így a „Becsült” erőfeszítés az egész ügy esetén ugyanaz marad).
* Egy művelet „Becsült” erőfeszítésének növelése ugyanezzel az értékkel csökkenti az ügy „Még létrehozásra váró munka erőfeszítése” értékét. Ez lehetséges, hogy befolyással lesz az ügy egészére vonatkozó „Becsült” erőfeszítésre.
  * Ha egy művelet frissített „Becsült erőfeszítés” értéke nem nő meg kellő mértékben ahhoz, hogy az ügy „Még létrehozásra váró munka erőfeszítése” értéke 0 alá csökkenjen, akkor az ügy „Becsült” erőfeszítésére ez nem lesz hatással.
    * Példa: Tegyük fel, hogy az 1. művelet esetén a „Becsült” erőfeszítés 2 óra, a becsült „Még létrehozásra váró munka erőfeszítése” 1 óra, végül az ügy „Becsült erőfeszítése” pedig 3 óra. A felhasználó úgy dönt, hogy az 1. művelet 1 órával hosszabb ideig tart majd, így az 1. művelet „Becsült” erőfeszítését 2 óráról 3 órára frissítette. A „Még létrehozásra váró munka erőfeszítése” érték 1 óráról 0-ra csökken majd, míg az ügy „Becsült” erőfeszítése nem változik, az 3 óra marad.
  * Ha egy művelet frissített „Becsült erőfeszítés” értéke kellő mértékben megnő ahhoz, hogy az ügy „Még létrehozásra váró munka erőfeszítése” értéke 0 alá csökkenjen, akkor a különbözetet hozzá kell adni a teljes ügy „Becsült erőfeszítés” értékéhez.
    * Példa: Tegyük fel, hogy egy ügyhöz csak egy művelet lett létrehozva, amelyet 1. műveletnek hívnak. Az 1. művelet esetén a „Becsült” erőfeszítés 2 óra, a becsült „Még létrehozásra váró munka erőfeszítése” 0, ezért az egész ügy „Becsült erőfeszítése” 2 óra. Egy felhasználó úgy dönt, hogy az 1. művelet 1 órával hosszabb ideig tart majd, így az 1. művelet „Becsült” erőfeszítését 2 óráról 3 órára frissíti. Mivel a „Még létrehozásra váró munka erőfeszítése” 0, a teljes ügy „Becsült” erőfeszítése ezért 2-ről 3 órára, tehát 1 órával megnő majd.
    * 2\. példa: Tegyük fel, hogy egy ügyhöz csak egy művelet lett létrehozva, amelyet 1. műveletnek hívnak. Az 1. művelet esetén a „Becsült” erőfeszítés 2 óra, a becsült „Még létrehozásra váró munka erőfeszítése” 1 óra, ezért az egész ügy „Becsült erőfeszítése” 3 óra. Egy felhasználó úgy dönt, hogy az 1. művelet 2 órával hosszabb ideig tart majd, így az 1. művelet „Becsült” erőfeszítését 2 óráról 4 órára frissíti, és ezzel a „Még létrehozásra váró munka erőfeszítése” 1-ről 0 órára, tehát 1 órával csökken majd (a lehető legkisebb értékre csökken). A „fennmaradó” 1 órát így tulajdonképpen hozzáadjuk az ügy teljes „Becsült” erőfeszítéséhez, amely emiatt 1 órával 3 óráról 4 órára növekszik.

#### Alügy lebontása

Egy alügy létrehozásakor Ön a következőket fogja látni:

* Egy az alügyre mutató hivatkozás, ha van jogosultsága a hozzáférésre (egyéb esetben csak az alügy nevét és hivatkozási számát láthatja majd a hivatkozás nélkül).
* Egy alügyes „összesen” sort a következőkkel:
  * A „Becsült” erőfeszítés az alügy teljes becsült időtartamát mutatja meg. Ezt a felhasználó igény szerint egy pontosabb becsléssel frissítheti.
    * Ez az alügyet alkotó összes létrehozott és még létrehozandó művelet „Becsült” erőfeszítéseinek összege.
    * A mező először a Builderben fellelhető manuálisan megadott „Kezdeti becsült erőfeszítés bejegyzésenként” értéket jeleníti meg, megszorozva azt a bejegyzések számával.
      * Ha frissül a „Bejegyzésszám”, akkor frissül a Work Manager felhasználója által nem frissített alügyhöz tartozó „Becsült erőfeszítés” is, hogy tükrözze a bejegyzésszám változását.
    * Ha az alügy Megoldva vagy Lezárva állapotú, akkor a becsült erőfeszítés többé már nem módosítható.
    * Vegye figyelembe, hogy ennek az értéknek a megnövelése megnöveli az alügy „Még létrehozásra váró munka” becslését, és fordítva.
  * A „Tényleges” erőfeszítés megmutatja, hogy eddig mennyi időt töltöttek el az adott alügyön dolgozva.
    * Ez az alügyet alkotó összes létrehozott művelet „tényleges” erőfeszítésének összege, amelyet ezek időráfordítás-követőiből gyűjtünk össze.
  * A „Becsült hátralévő idő” az alügyön még hátralévő becsült időtartamot jeleníti meg.
    * Ez az alügyet alkotó összes létrehozott művelet „Becsült hátralévő idő” erőfeszítéseinek ÉS a még létrehozásra váró munka becsült hátralévő idejének összege az adott alügyhöz (ezért előfordulhat, hogy ez nem mindig egyenlő az „Alügy becsült” mínusz az „Alügy tényleges” erőfeszítéseinek különbségével).
    * Az alügy esedékességének időpontja
    * Az alügy állapota
* Egy sor minden egyes alügy-művelethez a következőkkel együtt:
  * A „Becsült” erőfeszítés az alügy-művelet teljes becsült időtartamát mutatja meg. Ezt a felhasználó igény szerint egy pontosabb becsléssel frissítheti.
    * A mező először a Builderben fellelhető manuálisan megadott „Kezdeti becsült erőfeszítés bejegyzésenként” értéket jeleníti meg, megszorozva azt a bejegyzések számával.
      * Ha frissül a „Bejegyzésszám”, akkor frissül a Work Manager felhasználója által nem frissített, jelenleg bármilyen folyamatban lévő alügy-műveletekhez tartozó „Becsült erőfeszítés” is, hogy tükrözze a bejegyzésszám változását.
    * Ennek az értéknek a növelése csökkenteni fogja a „Még létrehozásra váró munka” alügy-becslését, és fordítva is, ezért a teljes „Alügy becsült” erőfeszítésére is hatással lehet.
    * Ha a művelet Megoldva vagy Lezárva állapotú, akkor a becsült erőfeszítés többé már nem módosítható.
  * A „Tényleges” erőfeszítés megmutatja, hogy eddig mennyi időt töltöttek el az adott alügy-műveleten dolgozva.
    * Ezt az értéket az alügy-művelet időráfordítás-követőjéből olvassuk ki.
  * A „Becsült hátralévő idő” az alügy-műveleten még hátralévő becsült időtartamot jeleníti meg.
    * Úgy számítjuk ki, hogy az alügy-művelet „Becsült” erőfeszítéséből kivonjuk a „Tényleges” erőfeszítést.
  * Az alügy-művelet esedékességének időpontja
    * Ezen kívül megjelenik egy „Kezdési határidő” érték is, ha a „Tényleges” erőfeszítés jelenleg nulla. Ez az érték azt mutatja, hogy melyik az az időpont, amikor az alügy-művelet annak esedékességi dátumának teljesítése érdekében még elindítható.
  * Az alügy-művelet állapota
* Egy sor a „Még létrehozásra váró alügy-munka” elemekhez a következőkkel együtt:
  * A „Becsült” erőfeszítés megmutatja, hogy a becslések szerint mekkora erőfeszítésre van szükség azon alügy-műveletek elvégzésére, amelyeket még nem hoztak létre az adott alügyhöz. Ezt a felhasználó igény szerint egy pontosabb becsléssel frissítheti.
    * E becslés módosítása hatással lesz a teljes „Alügy becsült” erőfeszítésre, valamint hatással lehet a teljes ügy becsült erőkifejtésére.

A „Becsült” erőfeszítés értékének módosítása egy alügy-művelet esetén a következő hatásokkal jár:

* A „Még létrehozásra váró munka erőfeszítése” becsült értékének automatikus frissítése az alügyhöz.
* A „Becsült” erőfeszítés esetleges automatikus frissítése az egész alügyre vonatkozóan.
* A „Becsült” erőfeszítés esetleges automatikus frissítése az egész eredeti ügyre vonatkozóan.

Részletek:

* Az alügy-művelet „Becsült” erőfeszítésének csökkentése ugyanezzel az összeggel növeli meg az alügy „Még létrehozásra váró munka erőfeszítése” értékét (így a „Becsült” erőfeszítés az egész alügy esetén ugyanaz marad, ezért nincs hatással az egész eredeti ügy „Becsült” erőfeszítésére).
* Egy alügy-művelet „Becsült” erőfeszítésének növelése ugyanezzel az értékkel csökkenti az alügy „Még létrehozásra váró munka erőfeszítése” értékét. Ez lehetséges, hogy befolyással lesz az ügy egészére vonatkozó „Becsült” erőfeszítésre.
  * Ha egy alügy-művelet frissített „Becsült erőfeszítés” értéke nem nő meg kellő mértékben ahhoz, hogy az alügy „Még létrehozásra váró munka erőfeszítése” értéke 0 alá csökkenjen, akkor az alügy „Becsült” erőfeszítésére ez nem lesz hatással (és ezért az egész eredeti ügy „Becsült” erőfeszítésére sem lesz hatással).
    * Példa: Tegyük fel, hogy egy alügyhöz csak egy művelet lett létrehozva, amelyet 1. műveletnek hívnak. Az 1. alügy-művelet esetén a „Becsült” erőfeszítés 2 óra, és a becsült „Még létrehozásra váró munka erőfeszítése” az alügy esetén 1 óra, ezért az alügy „Becsült erőfeszítése” 3 óra. Egy felhasználó úgy dönt, hogy az 1. alügy-művelet 1 órával hosszabb ideig tart majd, így az 1. alügy-művelet „Becsült” erőfeszítését 2 óráról 3 órára frissíti, és ezzel a „Még létrehozásra váró munka erőfeszítése” az alügy esetén 1-ről 0 órára csökken majd. Az alügy „Becsült” erőkifejtése nem változik, az 3 óra marad (és ezért az egész eredeti ügyre vonatkozó „Becsült” erőfeszítésre sem lesz hatással).
  * Ha egy alügy-művelet frissített „Becsült erőfeszítés” értéke kellő mértékben megnő ahhoz, hogy az alügy „Még létrehozásra váró munka erőfeszítése” értéke 0 alá csökkenjen, akkor a különbözetet hozzá kell adni a teljes alügy „Becsült erőfeszítés” értékéhez (és ezáltal hatással lehet az egész eredeti ügy „Becsült” erőfeszítésére).
    * Példa: Tegyük fel, hogy egy alügyhöz csak egy művelet lett létrehozva, amelyet 1. műveletnek hívnak. Az 1. alügy-művelet esetén a „Becsült” erőfeszítés 2 óra, és a becsült „Még létrehozásra váró munka erőfeszítése” az alügy esetén 0, ezért az egész alügy „Becsült” erőfeszítése 2 óra. Egy felhasználó úgy dönt, hogy az 1. alügy-művelet 1 órával hosszabb ideig tart majd, így az 1. alügy-művelet „Becsült” erőfeszítését 2 óráról 3 órára frissíti. Mivel az alügy „Még létrehozásra váró munka erőfeszítése” 0, ezért az alügy „Becsült” erőfeszítése 2-ről 3 órára, tehát 1 órával megnő majd.
      * Ha elegendő idő áll rendelkezésre az eredeti ügy „Még létrehozásra váró munka erőfeszítése” részében, akkor ez az 1 órás növekedés onnan igénybe vehető, ezért az nem lesz hatással az egész eredeti ügy „Becsült” erőfeszítésére.
      * Ha nem áll elegendő idő rendelkezésre az eredeti ügy „Még létrehozásra váró munka erőfeszítése” részében, akkor ez az 1 órás növekedés az egész eredeti ügy „Becsült” erőfeszítésének növekedését eredményezi.
    * 2\. példa: Tegyük fel, hogy egy alügyhöz csak egy művelet lett létrehozva, amelyet 1. műveletnek hívnak. Az 1. alügy-művelet esetén a „Becsült” erőfeszítés 2 óra, és a becsült „Még létrehozásra váró munka erőfeszítése” az alügy esetén 1 óra, ezért az egész alügy „Becsült” erőfeszítése 3 óra. Egy felhasználó úgy dönt, hogy az 1. alügy-művelet 2 órával hosszabb ideig tart majd, így az 1. alügy-művelet „Becsült” erőfeszítését 2 óráról 4 órára frissíti, és ezzel a „Még létrehozásra váró munka erőfeszítése” az alügy esetén a lehető legkisebb értékre, azaz jelen esetben 1-gyel, tehát 1-ről 0 órára csökken majd. A „fennmaradó” 1 órát így tulajdonképpen hozzáadjuk az alügy teljes „Becsült” erőfeszítéséhez, amely emiatt 1 órával 3 óráról 4 órára növekszik.
      * Ha elegendő idő áll rendelkezésre az eredeti ügy „Még létrehozásra váró munka erőfeszítése” részében, akkor ez az 1 órás növekedés onnan igénybe vehető, ezért az nem lesz hatással az egész eredeti ügy „Becsült” erőfeszítésére.
      * Ha nem áll elegendő idő rendelkezésre az eredeti ügy „Még létrehozásra váró munka erőfeszítése” részében, akkor ez az 1 órás növekedés az egész eredeti ügy „Becsült” erőfeszítésének növekedését eredményezi.

#### Még létrehozásra váró munka erőfeszítése

A „Még létrehozásra váró munka erőfeszítése” rész megmutatja, hogy a becslések szerint mekkora erőfeszítésre van szükség azon műveletek (és alügy-műveletek) elvégzésére, amelyeket még nem hoztak létre ehhez az ügyhöz.

Ennek kiszámítása úgy történik, hogy kivonjuk a már létrehozott munka „Becsült” erőfeszítésének összegét az ügy „Becsült” erőfeszítéséből. Ezért a „Még létrehozásra váró munka erőfeszítése” megnövelése az egész ügy becsült erőfeszítését is megnöveli majd, és fordítva.

A műveletek (és alügyek) létrehozásakor a becsült erőfeszítésüket a „Még létrehozásra váró munka erőfeszítése” érték alapján adjuk majd meg.

Ha az ügy Megoldva vagy Lezárva állapotú, akkor „Még létrehozásra váró munka erőfeszítése” többé már nem módosítható.
