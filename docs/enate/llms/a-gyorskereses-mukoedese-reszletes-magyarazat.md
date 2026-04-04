# Source: https://docs.enate.net/enate-help/hu/gyorskereses/a-gyorskereses-mukoedese-reszletes-magyarazat.md

# A gyorskeresés működése – részletes magyarázat

A gyorskeresés használatával kapcsolatos néhány további tudnivaló: Amikor megadja a gyorskereséshez használandó adatokat, a rendszer párhuzamosan három különböző kereséstípust hajt végre:

**1) Hivatkozási szám szerinti egyedi keresés**. A rendszer a formátum alapján felismeri, hogy munkatételekhez tartozó hivatkozási számot adott meg, és azokat a jegyeket, ügyeket és műveleteket fogja megjeleníteni a találatok között, amelyek ezzel a hivatkozási számmal rendelkeznek. Elegendő, ha beírja a hivatkozási számot (pl. „40308-T”), és azt a rendszer hivatkozási számként azonosítja. A rövid kódot nem kell a szám elé beírnia.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FHsPiHtZHgwyfKSKG7zOY%2Fimage.png?alt=media\&token=467d1b55-df08-46dc-b98a-35bf3f371360)

**2) Egyéni adatmezőkben történő keresések**. A fent leírtak szerint a rendszer felismeri, hogy ilyen típusú keresést hajt végre, ha beír egy ismert rövid kódot (pl. „FN:”). A rendszer azokat a mezőket fogja megkeresni, amelyek a beírt értéket tartalmazzák. Lásd a helyettesítő karakterekre vonatkozó alábbi megjegyzést.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FW0zIBPGFSocydARdhB9j%2Fimage.png?alt=media\&token=09add090-0f54-4a80-b0f4-b34e5eba5686)

**3) A munkatételek, kommunikációk és emberek szabad szöveges keresése** minden olyan egyéb, Ön által beírt keresőkifejezéssel szemben, amelyek nem felelnek meg az első két felismert adattípusnak. A rendszer szabad szöveges keresője az egyes szavakra keres rá a munkatételek, kommunikációk és emberek különféle rendszerattribútumaival szemben, például: munkatétel címe, e-mail tárgya és szövegtörzse.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FS2swv6llaCwGCz8Mlr1g%2Fimage.png?alt=media\&token=798f591c-f68a-48c1-b6ce-b6c99d73e287)

**4) Fájlok keresése „a következővel kezdődik” logika alapján.** A rendszer „a következővel kezdődik” logikát használja a fájlkeresés során, amikor egy helyettesítő kifejezést ad a keresőszöveg VÉGÉHEZ. Ez azt jelenti, hogy ha Ön egy „Számla feldolgozása.docx” nevű fájlra keres rá, akkor a „feldolgozása” szóra keresve az adott fájl nem jelenne meg a találatok között, viszont a „Számla” szóra keresve igen.

## Helyettesítő karakterek használata a szabad keresésekben <a href="#a-helyettesito-karakterek-hasznalata-a-szabad-keresesekben" id="a-helyettesito-karakterek-hasznalata-a-szabad-keresesekben"></a>

A keresések során a rendszer egy helyettesítő karaktert szúr be a keresett szöveg VÉGÉRE, de az elejére nem.

Példa az egyéni adatkeresésekre: amikor például a „p:John Smi” karakterlánc szerint keres, a rendszer azokat a tételeket fogja megjeleníteni, amelyek esetében a „person” mező értéke „John Smith”, ha azonban a „p: Smith” karakterláncra keres, a rendszer NEM fogja megtalálni a „John Smith” értékű mezőket.

Azaz az egyéni adatmezőkben történő keresések során a mező pontos értéke vagy az érték kezdő karakterlánca szerint keresünk. A szabad szöveges keresések nem egészen így működnek, mivel a szabad szöveges keresés a szöveg összes szavát egyenként próbálja megkeresni, vagyis a szöveget nem egészként kezeli.

A rendszer a hivatkozási szám szerinti keresések végére is helyettesítő karaktert fűz.

### Helyettesítő karakteres keresés a szöveg beírása közben <a href="#helyettesito-karakteres-kereses-a-szoeveg-beirasa-koezben" id="helyettesito-karakteres-kereses-a-szoeveg-beirasa-koezben"></a>

Amikor a gyorskereső mezőbe szöveget ír be, a rendszer a legutolsó szóhoz fűz helyettesítő karaktereket, és az alapján keres. Például, ha az alábbi szöveg beírásával végez szabad szöveges keresést: "John return prio". A rendszer az utolsó szóhoz fűz helyettesítő karaktert, és például olyan találatokat is visszaad, amelyek a „priority” szót tartalmazzák.

Miután lenyomta a szóköz billentyűt, a rendszer érzékeli, hogy befejezte a keresőkifejezés beírását, és helyettesítő karakter használata nélkül a megadott szót fogja megkeresni.

## Egyéb keresőkifejezések figyelmen kívül hagyása

A rendszerteljesítmény megőrzése érdekében a rendszer az alábbi kifejezéseket figyelmen kívül hagyja a keresések során:

* 1 vagy 2 karakterből álló szavak.
* A rendszer „tiltólistáján” szereplő szavak. Ezek az olyan gyakori szavak, mint az „és”, „az”, „én” stb., amelyek használata túl sok találatot eredményezne. Kérjük, hogy olvassa el ezt a részt [azoknak a tiltólistás szavaknak a listájához, amelyeket a keresések során nem veszünk figyelembe](https://docs.enate.net/enate-help/hu/fueggelek/figyelmen-kivul-hagyott-keresesi-kifejezesek-tovabbi-reszletek) (a gyorskeresőben, valamint valójában a rendszerben elvégzett bármilyen egyéb keresés során).&#x20;
* A gyorskeresőben figyelmen kívül hagyott konkrét karakterek, pl. „\*”, „?”, „@” stb. A [figyelmen kívül hagyott karakterek teljes listáját](https://docs.enate.net/enate-help/hu/fueggelek/figyelmen-kivul-hagyott-keresesi-kifejezesek-tovabbi-reszletek#a-gyorskeresoben-figyelmen-kivuel-hagyott-karakterek) itt találhatja meg. Ez például azt jelenti majd, hogy ha a gyorskeresőben Ön a customer.com kifejezésre keres rá, akkor a „customer” (ügyfél) és a „com” szavakra keres majd rá. Ezért ajánlatos az ilyen szóösszetételeket idézőjelbe tenni, hogy konkrét kifejezésként kereshessen rájuk – például a „customer.com” kifejezésre keresve a keresés valószínűleg a megfelelő találatokat listázza majd.

## További információk a gyorskereséssel kapcsolatban

A gyorskereső egy szöveges kereső. Amennyiben Ön dátumokat ad meg a szöveges keresés során, az inkonzisztens eredményeket adhat. Ha lehetséges, használjon „idézőjeleket” a szükséges keresések esetén, amelyek segítenek Önnek abban, hogy a keresés során teljes karakterláncokra keressen, például: „keresse meg, hogy hol fordul elő ez a szöveg”.

Használja a dátumcsúszkákat, hogy az adott dátumtartományokban kapja meg az eredményeket.

Amikor egyszerre több szóra keres rá, a keresés az „ÉS” logikát használja majd a „VAGY” logika helyett, azaz olyan találatokat ad majd, amelyek eredménye: „alma” ÉS „banán” ÉS „körte”.

## A munkatételek és az e-mailek közötti keresések sajátosságai

Fontos megjegyezni, hogy a gyorskeresés három független keresést végez el:

* egyet a munkatételekhez (ügyek, műveletek és jegyek),
* egyet az ezekhez esetlegesen kapcsolódó e-mailekhez, valamint
* egyet az emberekhez.

Ennek hatására, ha Ön három szó kombinációjára keres rá, például: „alma”, és „banán” és „körte”, akkor a gyorskeresés olyan munkatételeket hoz majd eredményül, ahol mindhárom szó előfordul, és külön jelenít meg minden olyan e-mailt, ahol ez a három szó mindegyike előfordul. Abban az esetben, amikor a három közül csak kettő fordul elő egy munkatételben, míg a harmadik csak egy kapcsolódó e-mailben tűnik fel, ezt az eredményt NEM tüntetjük fel egyik keresésben sem.

A munkatétel-keresések elvégzésének specifikus jellemzői a következők:

* Munkatétel referenciája
* Cím
* Ügyfél neve
* Szolgáltató neve
* Szerződés neve
* Szolgáltatás neve
* Szolgáltatásfajta neve
* Folyamattípus neve

A kommunikációkeresések elvégzésének specifikus jellemzői a következők:

* E-mail címe
* E-mail törzse
* E-mail-címek (feladó, címzett, másolatot kap, titkos másolatot kap)
* Belső megjegyzéstörzs (az Enate-en/önkiszolgáló felületén belül hozzáadott megjegyzésekhez)
