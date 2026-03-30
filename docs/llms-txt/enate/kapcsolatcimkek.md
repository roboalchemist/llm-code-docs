# Source: https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatcimkek.md

# Kapcsolatcímkék

A kapcsolatcímkék a névjegyek és a munkatételek összekapcsolására szolgálnak.

## A rendszer alapértelmezett címkéi

A rendszer elérhető alapértelmezett címkéi a következők:

* **Elsődleges kapcsolat** – az az elsődleges személy, akivel Ön a kéréssel kapcsolatban kommunikál. Egy munkatételhez mindig csak egy elsődleges kapcsolat tartozhat. Ez jegy esetén kötelező. Az ügy a Builderben meghatározott beállításaitól függően ez ügy esetén lehet kötelező, de nem kötelező is (ha az ügytípus esetén kötelező, akkor az ügy műveletei esetén is kötelező).
* **Eredeti kérelmező** – az a személy, aki először beküldte a kérést. Egy munkatételhez mindig csak egy eredeti kérelmező tartozhat, és ez a „Kérelmező” címkétől független. Az eredeti kérelmezőt automatikusan beállítjuk az olyan helyzetekben, amikor egy érvényes kapcsolat küldte be a munkatételt elindító e-mailt, vagy az lesz az „eredeti kérelmező”, akit manuálisan „kérelmezőként” állítanak be. Az eredeti kérelmező címke a beállítását követően nem módosítható, és az eredeti kérelmezőként megjelölt kapcsolat a munkatételből nem távolítható el.
* **Kérelmező** – a kérést elindító személy. Egy munkatételhez mindig csak egy kérelmező tartozhat. Ez jegy esetén kötelező. Az ügy a Builderben meghatározott beállításaitól függően ez ügy esetén lehet kötelező, de nem kötelező is (ha az ügytípus esetén kötelező, akkor az ügy műveletei esetén is kötelező).
* **Érintett** – akiről a munkatétel szól (ez lehetséges, hogy a fentiek közül egyik sem). Egy munkatételhez mindig csak egy érintett tartozhat.

Gyakran mindhárom ugyanaz a személy lesz. Ha a rendszer alapértelmezett kapcsolattípusainak egyikeként egy másik kapcsolatot állít be, akkor az előző kapcsolatról eltávolítjuk az adott címkét – mivel a rendszer alapértelmezett kapcsolatainak egy munkatételen belül egyszerre csak egy tulajdonosa lehet.

Amikor egy munkatételhez manuálisan hozzáadja az első kapcsolatot, akkor azt alapértelmezés szerint Elsődleges kapcsolatként, Kérelmezőként és Érintettként állítjuk be. Ezt követően Ön ezeket a címkéket igény szerint manuálisan más felhasználókhoz rendelheti.

* Másolatot kapó címek – bármely további olyan kapcsolattartó személy, akit a levelezésre rácsatolhat. Amikor egy kapcsolatot kizárólag „Másolatot kap” címként jelölnek meg, az a külön Másolatot kap részben jelenik meg (ez addig rejtve van, amíg a munkatételhez kizárólag Másolatot kap kapcsolatok tartoznak).

## További alapértelmezett címkék beállítása egy kapcsolati bejegyzésen

A rendszer alapértelmezett kapcsolatcímkéi (elsődleges kapcsolat, érintett, másolatot kap, kérelmező) mellett Ön egy további alapértelmezett kapcsolatcímkét is hozzáadhat egy kapcsolati bejegyzéshez, hogy gyorsabbá és egyszerűbbé tegye a munkatételeken a kapcsolatcímkék használatát.

Példa: Ha tudja, hogy „Jane Smith” mindig „Brókerként” szerepel majd az összes olyan munkatételen, amelyekhez Ön kapcsolatként adja hozzá, Jane kapcsolati bejegyzésén egy „Bróker” alapértelmezett címkét helyezhet el, amelyet így az ő esetében automatikusan kitöltünk majd a munkatételen – ahelyett, hogy Önnek mindig manuálisan kellene ezt a címkét beállítania.

A kiválasztható alapértelmezett címkék listája a Builder [Általános beállítások >> Kapcsolatcímkék](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags) részben állítható be.

Ezt az alapértelmezett címkét bármikor beállíthatja, amikor egy új kapcsolatot ad a rendszerhez.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2F5PRCsetm93DaFDy7mJ2M%2Fimage.png?alt=media&#x26;token=2271706d-e7c8-4d67-99b0-c6468321dde0" alt=""><figcaption></figcaption></figure>

A címkét már meglévő kapcsolatokhoz is hozzáadhatja, valamint a Kapcsolatok oldalon lehetősége van az egy adott kapcsolathoz megadott alapértelmezett címke szerkesztésére is.

Az alapértelmezett címke attribútum tömegesen is szerkeszthető, azaz egyszerre több kapcsolathoz is beállíthat egy alapértelmezett címkét – csak egyszerűen válasszon ki néhány kapcsolati bejegyzést a Kapcsolatok oldal rácsán, majd kattintson a Szerkesztés gombra, hogy megnyissa a Tömeges szerkesztés felugró ablakot.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2Fc2ayiF173lEYemtC1MI3%2Fimage.png?alt=media&#x26;token=ba5c476b-4352-43fb-94d0-86406468794b" alt=""><figcaption></figcaption></figure>

## Kapcsolatcímkék automatikus viselkedése, ha a „Több engedélyezése” lehetősége ki van kapcsolva

Ha egy adott címke értéke esetén ki van kapcsolva a „Több engedélyezése” lehetőség, akkor egy munkatételen belül az adott értékkel csak egy kapcsolat rendelkezhet. Példa: előfordulhat, hogy egy jegyhez kizárólag csak egy „Bróker” kapcsolat társulhat. Ez nyilvánvalóan hatással van az alapértelmezett címkézésre is, amennyiben két, azonos „egyedinek kell lennie” alapértelmezett címkével rendelkező kapcsolatot adnak egy munkatételhez, akár manuális, akár automatikus hozzáadásról is van szó. Ebben az esetben a rendszer kizárólag egy kapcsolathoz rendeli hozzá az alapértelmezett címkét (és így eltávolítja a többi kapcsolat alapértelmezett címkéjét). A rendszer egy már meglévő *egyéb* címkeértékkel megjelölt kapcsolathoz az alábbi prioritási sorrendben rendeli hozzá a címkéket:

* Elsődleges kapcsolat
* Kérelmező
* Érintett
* Másolatot kap
* Minden a munkatételen dolgozó további kapcsolat

### T**ovábbi megjegyzések a szállítóvállalat nem megfelelő kapcsolatcímkéivel kapcsolatban:**

* Nem adhat alapértelmezett címkét egy kapcsolathoz, ha a vállalat, amelyhez a kapcsolat hozzá van rendelve, az alapértelmezett címkétől eltérő szállítóvállalattal rendelkezik.
* Nem tud majd olyan kapcsolattal rendelkező munkatételt beküldeni, amely alapértelmezett címkéje egy a munkatételétől eltérő szállítóvállalatra van állítva.

## Kapcsolatok automatikus címkézése a munkatételekben

### Az egy kezdeti e-mailből kitöltött kapcsolatok

**Ismert kapcsolatok**

Ha egy adott e-mail olyan címről érkezik be, amely egy már a rendszerben lévő kapcsolathoz van hozzárendelve, valamint a kapcsolat:

* globális hatályúra van állítva, vagy
* helyi hatályúra van állítva, azonban az e-mail útválasztási szabályai alapján ugyanahhoz a vállalathoz tartozik, mint amelyhez a munkatétel is fog,

ebben az esetben ha a rendszer létrehozza a munkatételt, az adataikat automatikusan kitöltjük a kapcsolat kártyán, majd automatikusan a munkatétel elsődleges kapcsolataként, eredeti kérelmezőjeként és kérelmezőjeként jelöljük meg őket. Továbbá amennyiben hozzájuk van rendelve egy alapértelmezett címke, akkor azt is megkapják. Azonban ne feledje, hogy a munkatétel létrehozását követően Önnek bármikor lehetősége van a címkék manuális szerkesztésére.

Ha egy olyan címről érkezik be egy e-mail, amely kapcsolata már megtalálható a rendszerben, azonban helyi hatállyal rendelkezik és az e-mail útválasztási szabályai alapján egy a munkatételétől *eltérő* vállalathoz tartozik, akkor a kapcsolat kártyát NEM töltjük ki automatikusan annak adataival a munkatétel rendszerben történő létrehozásakor (és ezért nem címkézhetők automatikusan a munkatételhez). Ne feledje, hogy a munkatétel létrehozását követően Önnek bármikor lehetősége van a címkék manuális szerkesztésére.

**Ismeretlen kapcsolatok**

*Alapértelmezett „globális” vagy „globális és helyi” hatály*

Ha ismeretlen címről érkezik egy e-mail, valamint:

* [a Builderben BE van kapcsolva a „Kapcsolatok automatikus létrehozásának engedélyezése” ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)lehetőség, és
* az Ön rendszerét úgy állították be, hogy a külső kapcsolatok hatályát „**globális**” vagy „**globális és helyi**” hatályúra állítsa be,

akkor a kapcsolatot automatikusan létrehozzuk, globális hatályú lesz (azaz egyetlen adott vállalathoz sem kapcsolódik majd), és a munkatétel rendszerben történő létrehozásakor a kapcsolat kártyát automatikusan kitöltjük az adataikkal. Továbbá automatikusan a munkatétel elsődleges kapcsolataként, eredeti kérelmezőjeként és kérelmezőjeként lesznek megjelölve. Mivel a rendszer számára korábban ismeretlenek voltak, nem rendelkeznek majd alapértelmezett címkével. Ne feledje, hogy a munkatétel létrehozását követően Önnek bármikor lehetősége van a címkék manuális szerkesztésére.

*Alapértelmezett „helyi” hatály*

Ha ismeretlen címről érkezik egy e-mail, valamint

* [a Builderben BE van kapcsolva a „Kapcsolatok automatikus létrehozásának engedélyezése” ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)lehetőség, és
* az Ön rendszerét úgy állították be, hogy a külső kapcsolatok hatályát „**helyi**” hatályúra állítsa be,

akkor a kapcsolatot automatikusan létrehozzuk, az helyi hatályú lesz (azaz egy adott vállalathoz kapcsolódik majd), és az alatt a vállalat alatt hozzuk létre őket, amelyhez a munkatétel is kapcsolódik. Amikor a rendszer létrehozza a munkatételt, az adataikat automatikusan kitöltjük a kapcsolat kártyán, majd automatikusan a munkatétel elsődleges kapcsolataként, eredeti kérelmezőjeként és kérelmezőjeként jelöljük meg őket. Mivel a rendszer számára korábban ismeretlenek voltak, nem rendelkeznek majd alapértelmezett címkével. Ne feledje, hogy a munkatétel létrehozását követően Önnek bármikor lehetősége van a címkék manuális szerkesztésére.

*Kapcsolatok automatikus létrehozása KI*

Ha ismeretlen címről érkezik egy e-mail, valamint

* [a Builderben KI van kapcsolva a „Kapcsolatok automatikus létrehozásának engedélyezése”](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) lehetőség,

ezt követően a munkatétel az e-mail útválasztási szabályai alapján jön létre, azonban a munkatétel rendszerben történő létrehozásakor a kapcsolat kártyát NEM töltjük ki automatikusan az e-mail feladójának adataival (így nem címkézhetők automatikusan a munkatételhez). Ne feledje, hogy a munkatétel létrehozását követően Önnek bármikor lehetősége van a kapcsolatok és címkék manuális szerkesztésére.

### **A kapcsolattevékenységi oldalról kitöltött kapcsolatcímkék**

Ha egy munkatételt egy kapcsolat [Kapcsolattevékenységi oldalának](https://docs.enate.net/enate-help/hu/nevjegyek/a-kapcsolattevekenyseg-oldal)„Munkatétel elindítása” gombját használva hoznak létre, akkor az adott kapcsolatot automatikusan a munkatétel eredeti kérelmezőjeként, kérelmezőjeként, érintettjeként és elsődleges kapcsolataként is megjelöljük, valamint hozzáadjuk az alapértelmezett címkéjüket is (ha rendelkeznek ilyennel).
