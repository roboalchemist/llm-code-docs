# Source: https://docs.enate.net/enate-help/hu/fueggelek/a-rendszer-viselkedese-a-munkatetel-megbizottjanak-tulajdonosanak-es-varolistajanak-megadasakor.md

# A rendszer viselkedése a munkatétel megbízottjának, tulajdonosának és várólistájának megadásakor

A jegyek, ügyek és műveletek Enate-es munkafolyamatokban történő kezelése részeként a rendszer rendszeresen kiértékeli, hogy kihez van hozzárendelve a munka, ki van tulajdonosként beállítva, valamint melyik várólistához kapcsolódik a munkatétel. Ennek meghatározásakor részletesen meghatározott szabályrendszert követünk.

Ezeknek a részletesen meghatározott szabályoknak az áttekintése előtt fontos megérteni azt, hogy hogyan és mikor, milyen magasabb szintű mintázat alapján értékeljük ki ezeknek a munkatételeknek a kiosztását. Ez a következőképp működik:

1. Először is [meghatározzuk, hogy MIKOR fordulnak elő ilyen újraértékelések](#az-ujraertekeles-idejenek-meghatarozasa) – lényegében akkor történik ilyen, amikor egy munkatétel „Állapot” kártyáján bármilyen változás történik.
2. Amikor a rendszer úgy dönt, hogy ilyen értékelésre van szükség, akkor először a munkatétel állapotát/helyzetét használjuk fel annak [meghatározására, hogy melyik megbízottat, tulajdonost és várólistaértéket kell beállítani, és melyiket kell teljesen kitörölni](#annak-meghatarozasa-hogy-be-kell-e-allitani-vagy-toeroelni-kell-e-a-megbizott-tulajdonos-vagy-varoli).
3. [Amelyek beállítást igényelnek](#egy-megbizott-tulajdonos-es-varolista-beallitasanak-modja):

   1. Ha be kell állítani egy várólistát, az egyszerű: csak válassza ki a hozzárendelési szabályban hivatkozott várólistát (összesen csak kétféle követendő várólista-hozzárendelési szabály van).
   2. A megbízott és a tulajdonos esetén több részlet áll rendelkezésre – sorban végig kell néznünk egy sor szabályt, majd amikor teljesül a szabály és kiválasztunk egy érvényes\* célt, akkor meg kell állnunk.

\*[Érvényesség-ellenőrzés](#ervenyesseg-ellenorzesek) – a megbízott/tulajdonos hozzárendelési szabályellenőrzés részeként meg kell határoznunk, hogy a cél érvényes-e (számos olyan érvényességet ellenőrző szabály van, amelyen át kell mennie). Ha nem, folytassa a 3. részben foglalt szabályok áttekintésével, amíg egy érvényes célt nem talál.

Most, hogy meghatároztuk a használt magasabb szintű mintázatot, megtekinthetjük azokat az egyes szabályokat és célérvényesség-ellenőrzéseket, amelyeket a fenti 1–3. részben bemutattunk.

## Az újraértékelés IDEJÉNEK meghatározása

A rendszer újra kiértékeli a hozzárendelt felhasználót, tulajdonost és várólistát minden alkalommal, amikor az állapotkártya információinak valamelyike megváltozik, különös tekintettel:

* az állapotváltozásokra,
* a várakozás típusának változásaira,
* az újrafolytatás beütemezve dátumának változásaira,
* a további információra vár dátumának változásaira,
* a várakozás opcióinak változásaira,
* a jegy kontextusának változásaira,
* a jegy kategóriájának változásaira,
* a munkatársi értékelés alatt állapotváltozásaira,
* amikor új információ érkezik be egy munkatételhez,
* amikor az ügy egy problémába ütközik.

## Annak meghatározása, hogy be kell-e állítani vagy törölni kell-e a megbízott, tulajdonos vagy várólista értékeit

Amikor a rendszer úgy dönt, hogy ilyen értékelésre van szükség, akkor először a munkatétel ÁLLAPOTÁT használjuk fel annak meghatározására, hogy melyik megbízottat, tulajdonost és várólistaértéket kell beállítani, és melyiket kell teljesen kitörölni. Ezeket az információkat az alábbi táblázatban láthatja:

| <p><strong>Munka tétel állapota/szituációja</strong></p><p> </p>        | <p><strong>Megbízott</strong></p><p> </p> | <p><strong>Tulajdonos</strong></p><p> </p> | <p><strong>Várólista</strong></p><p> </p> |
| ----------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------ | ----------------------------------------- |
| <p>Lezárva</p><p> </p>                                                  | <p>Érték törlése</p><p> </p>              | <p>Érték törlése</p><p> </p>               | <p>Érték törlése</p><p> </p>              |
| <p>Piszkozat</p><p> </p>                                                | <p>Egy érték beállítása</p><p> </p>       | <p>Érték törlése</p><p> </p>               | <p>Érték törlése</p><p> </p>              |
| <p>Új információ érkezett</p><p> </p>                                   | <p>Egy érték beállítása</p><p> </p>       | <p>Érték törlése</p><p> </p>               | <p>Egy érték beállítása</p><p> </p>       |
| <p>Figyelmet igényel (csak ügy esetén releváns)</p><p> </p>             | <p>Egy érték beállítása</p><p> </p>       | <p>Érték törlése</p><p> </p>               | <p>Egy érték beállítása</p><p> </p>       |
| <p>Elvégzendő vagy Folyamatban egy művelet vagy jegy esetén</p><p> </p> | <p>Egy érték beállítása</p><p> </p>       | <p>Érték törlése</p><p> </p>               | <p>Egy érték beállítása</p><p> </p>       |
| <p>Elvégzendő vagy Folyamatban egy ügy esetén</p><p> </p>               | <p>Érték törlése</p><p> </p>              | <p>Egy érték beállítása</p><p> </p>        | <p>Érték törlése</p><p> </p>              |
| <p>Megoldva vagy Várakozik</p><p> </p>                                  | <p>Érték törlése</p><p> </p>              | <p>Egy érték beállítása</p><p> </p>        | <p>Érték törlése</p><p> </p>              |

## Egy megbízott, tulajdonos és várólista beállításának módja

* **Várólisták** – ha be kell állítani egy várólistát, az igen egyszerű: le kell futtatni a [Várólista-hozzárendelési módszert](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method).
* **Megbízott és tulajdonos** – ha egy megbízottat vagy egy tulajdonost kell beállítani, akkor annak további részletei vannak. Sorban végig kell néznünk egy sor szabályt, majd amikor teljesül a szabály és kiválasztunk egy [érvényes célt](#ervenyesseg-ellenorzesek), akkor meg kell állnunk.

A szabálylista lefuttatását megelőzően egy még magasabb szintű ellenőrzést kell elvégeznünk: ha jelenleg be van állítva egy megbízott/tulajdonos, akkor **hacsak nem változott meg a jegy kategóriája, ne módosítsa a megbízott/tulajdonos személyét**.

Egyéb esetben sorrendben futtassa le a következő szabályokat, és álljon meg, ha talált egy érvényes célt:

1. Ha a „Tartsa nálam” opció be lett állítva egy munkatételen, akkor a megbízottat/tulajdonost jelöljük meg annak a személynek, aki a „Tartsa nálam” lehetőséget kiválasztotta. Ha nem lett beállítva vagy az adott felhasználó érvénytelen, akkor:
2. Ha a tulajdonos felhasználó nem üres, akkor a megbízottat is az adott értékre állítjuk be. Ha nem lett beállítva vagy az adott felhasználó érvénytelen, akkor:
3. Ha a munkatétel egy jegy, és a jegykategória megváltozott, valamint megváltozott a Várakozás típusa vagy Megoldva állapotú lett, akkor a megbízott/tulajdonos lesz megjelölve a jegyet jelenleg frissítő felhasználóként. Ha nem, akkor:
4. Ha a munkatétel nem egy jegy VAGY egy jegy (ahol a jegykategória nem változott ÉS több mint 2 állapotelőzményi sorral rendelkezik, például nem az első nem piszkozat állapotú állapotban van), akkor:
   1. A megbízottat és a tulajdonost arra a legutolsó felhasználóra/robotra állítja be, aki utoljára frissítette a munkatételt. Ha nincs ilyen vagy az adott felhasználó érvénytelen, akkor:
   2. Állítsa be megbízottként/tulajdonosként a (bármelyik) korábban hozzárendelt felhasználót/robotot időrendben visszafelé haladva annak tekintetében, hogy mikor volt az adott személyhez/robothoz rendelve. Ha nincs ilyen vagy az adott felhasználó érvénytelen, akkor:
   3. Ha a műveletet egy munkafolyamat indította el (azaz nem kézzel, ad-hoc indították el), akkor állítsa be megbízottként/tulajdonosként azt az utolsó felhasználót/robotot, amely ugyanazon a korábban befejezett műveleten dolgozott az ügy folyamán (vagy a művelet munkatársi értékelésén, ha munkatársi értékelés történt).  Ha nincs ilyen vagy az adott felhasználó érvénytelen, akkor:
5. Futtassa le a [hozzárendelési szabályt](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) ehhez a munkatételhez:
   1. Ha az elsődleges push-hozzárendelés egy adott felhasználóra lett beállítva, akkor az adott felhasználót állítja be megbízottként/tulajdonosként. Ha nincs ilyen vagy az adott felhasználó érvénytelen, akkor:
   2. Ha a másodlagos push-hozzárendelés egy adott felhasználóra lett beállítva, akkor az adott felhasználót állítja be megbízottként/tulajdonosként. Ha nincs ilyen vagy az adott felhasználó érvénytelen, akkor:
   3. Ha az elsődleges push-hozzárendelés Pozícióra lett beállítva, az ezt a pozíciót elfoglaló felhasználók közül azt a felhasználót állítja be megbízottként/tulajdonosként, aki a postaládájában a legkevesebb munkatétellel rendelkezik. Ha nincs ilyen vagy az adott felhasználó érvénytelen, akkor:
   4. Ha a másodlagos push-hozzárendelés Pozícióra lett beállítva, az ezt a pozíciót elfoglaló felhasználók közül azt a felhasználót állítja be megbízottként/tulajdonosként, aki a postaládájában a legkevesebb munkatétellel rendelkezik. Ha nincs ilyen vagy az adott felhasználó érvénytelen, akkor:
6. Ha az adott munkatétel egy ügy, azt a felhasználót/robotot állítsa be megbízottként/tulajdonosként, aki elindította az ügyet.

## Érvényesség-ellenőrzések

A megbízott/tulajdonos hozzárendelésiszabály-ellenőrzés részeként meg kell határoznunk azt, hogy a cél érvényes-e. Ahhoz, hogy érvényes legyen, számos olyan érvényesség-ellenőrzési szabály van, amelynek meg kell felelnie. Ha nem felel meg, a további megbízott/tulajdonos beállítási szabályok áttekintésével folytatjuk egészen addig, amíg egy érvényes célt nem találunk. Az áttekintett érvényesség-ellenőrzések a következők:

* Ha a felhasználó/robot nem dolgozhat ilyen típusú munkatételeken (pl. Élő/teszt), akkor blokkolás
* Ha a felhasználó/robot nyugdíjazva lett, akkor blokkolás
* Ha a felhasználó nem rendelkezik engedéllyel, akkor blokkolás (robotok esetén nincs engedélyezési ellenőrzés)
* Ha a robot fel van függesztve, akkor blokkolás
* Ha a robot több mint 3 alkalommal elvégezte a További munka beszerzése folyamatot ehhez a munkatételhez, akkor blokkolás
* Ha a kiválasztott felhasználó egy robot, és a munkatétel egy olyan művelet, amely Munkatársi értékelés állapotban van (a robotok nem végezhetnek el munkatársi értékelést), akkor blokkolás
* Ha a kiválasztott felhasználó egy robot, és a munkatétel egy művelet, és a művelethez nem lett robotfarm beállítva, akkor blokkolás
* Ha a kiválasztott felhasználó egy robot, és a munkatétel egy művelet, illetve a robot nem a művelethez beállított robotfarm tagja, akkor blokkolás
* Ha a kiválasztott felhasználó egy robot, és a munkatétel egy ügy, akkor blokkolás (az ügyekhez robotok nem rendelhetők)
* Ha a munkatétel egy munkatársiértékelés-művelettel rendelkező kézikönyv, amely a munkatársi értékelés szakaszában van, és a felhasználó legalább 1 frissítést végzett el rajta, amíg az „elvégzési” szakaszban volt, akkor blokkolás (a felhasználók nem végezhetnek el munkatársi értékelést a saját munkájukon)
* Ha a munkatétel egy munkatársiértékelés-művelettel rendelkező kézikönyv, amely elvégzési szakaszban van, és a felhasználó legalább 1 frissítést végzett el rajta, amíg az a munkatársi értékelés szakaszában volt, akkor blokkolás (a felhasználók nem kérhetők fel egy munka elvégzésére, ha korábban már munkatársi értékelést végeztek el rajta)

&#x20;
