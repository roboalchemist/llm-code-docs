# Source: https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatok-hozzaadasa-szerkesztese-es-torlese.md

# Kapcsolatok hozzáadása, szerkesztése és törlése

## Kapcsolatok hozzáadása <a href="#a-adding-editing-and-deleting-contacts" id="a-adding-editing-and-deleting-contacts"></a>

A külső kapcsolatok az Enate-ben többféleképpen is létrehozhatók.

### 1) Automatikusan egy bejövő e-mailből

Lehetőség van az Enate rendszerét úgy beállítani, hogy az új e-mail-címeket tartalmazó e-mailek beérkezésekor automatikusan új külső kapcsolati bejegyzéseket hozzon létre. Ez a [Builderben a „Kapcsolatok automatikus létrehozásának engedélyezése” lehetőség BEkapcsolásával tehető meg](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).

A rendszer az e-mailben megjelenített név alapján automatikusan kitölti a kapcsolat keresztnevét és vezetéknevét. Erről bővebben alább olvashat:

* Ha az e-mailben megjelenített névben egy szóköz található, akkor az első szóköz előtti rész lesz a kapcsolat keresztneve, míg minden az utolsó szóközt követő rész a vezetéknév lesz. Például, ha az e-mailben megjelenített név a „John Smith”, akkor a kapcsolat keresztneve automatikusan „John”, míg a vezetékneve „Smith” lesz.
* Ha az e-mailben megjelenített névben egy vessző található, akkor az első vessző előtti rész lesz a kapcsolat vezetékneve, míg minden a vesszőt követő, ám még a szóköz előtti rész a keresztnév lesz. Például, ha az e-mailben megjelenített név a „Smith, John”, akkor a kapcsolat vezetékneve automatikusan „Smith”, míg a keresztneve „John” lesz.
* Ha a rendszer nem tudja magabiztosan megállapítani és automatikusan kitölteni a keresztnevet és a vezetéknevet, akkor a kapcsolatot kereszt- és vezetéknév nélkül hozzuk létre, és arra kérjük majd a felhasználót, hogy a Munkatétel elküldésekor töltse ki ezeket az adatokat.

Továbbá az automatikusan létrehozott kapcsolathoz [beállított vállalat](#vallalat-neve-kuelso-kapcsolatok-hatalyanak-meghatarozasa) a [Builder kapcsolat hatókörének beállításától](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope) függ majd. Ha ez „Globális” vagy „Globális és helyi” értékre lett beállítva, akkor az automatikusan létrehozott kapcsolat globális hatókörrel rendelkezik majd, azaz egy adott vállalathoz sem kapcsolódik majd. Ha „Helyi” értékre lett beállítva, akkor az automatikusan létrehozott kapcsolatot az alatt a vállalat alatt hozzuk létre, amely alatt a kapcsolódó Munkatétel is létezik.

### 2) Egy adott kapcsolat hozzáadása a Kapcsolatkezelő oldalról

Önnek lehetősége van kapcsolatokat hozzáadni a [Kapcsolatkezelő oldalról](https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatkezelesi-lap), ha a Kapcsolat létrehozása ikonra kattint, majd a felugró ablakban kitölti az adott kapcsolat részleteit.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2Fff7r9jaqfyzQCJwzVJ2J%2F7%20Adding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=a0064984-31b3-4387-b42b-d75886c29fe1" alt=""><figcaption></figcaption></figure>

### 3) Kapcsolatok importálása a Kapcsolatkezelő oldalra egy Excel-sablonból

A [Kapcsolatkezelő oldalon](https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatkezelesi-lap) lehetősége van egy kapcsolatlista Excel-táblázatból történő importálására. Biztosítunk egy sablont, amely az Enate által kínált összes nyelven támogatott.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FoX8uUUI41WfgQp0dR2Ce%2F7%20Bulk-Adding-Contacts.gif?alt=media&#x26;token=b4583610-4d47-4012-aaac-f0f7d7e8c146" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
A kapcsolatok Excel-táblázatból történő importálása során az e-mail-cím megadása kötelező. Ha nem adja meg a vállalatot, akkor a kapcsolatot automatikusan globális értékre állítjuk. A [vállalatok hatályának meghatározásáról](#vallalat-neve-kuelso-kapcsolatok-hatalyanak-meghatarozasa) bővebb információkat itt találhat.
{% endhint %}

### 4)  Egy kapcsolat hozzáadása a Gyorskeresőből

Ha egy olyan új kapcsolatot keres, amely jelenleg nem létezik a rendszerben, akkor lehetősége van közvetlenül a [Gyorskeresőből ](https://docs.enate.net/enate-help/hu/gyorskereses)egy új kapcsolatot létrehozni. Lépjen az emberek keresése funkcióra a Gyorskeresőben, majd kattintson az „Egy kapcsolat hozzáadása” lehetőségre.

Az „Egy kapcsolat hozzáadása” lehetőségre kattintva a rendszer dekódolja, majd automatikusan kitölti az utónevet, a vezetéknevet, valamint az e-mail-címet. Ha az összes információ kitöltését követően a létrehozás lehetőségre kattint, akkor az új kapcsolat [Kapcsolattevékenységi oldalára](https://docs.enate.net/enate-help/hu/nevjegyek/a-kapcsolattevekenyseg-oldal) irányítjuk Önt.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MbH-BYuK4VLPdtNwqfT%2F-MbHBB9sVuyT_nCkaTfK%2FCreating-a-Contact-from-Quickfin.gif?alt=media\&token=fe49d4ff-b5be-4aee-bbd6-b5aeee0ff1f3)

{% hint style="info" %}
Megjegyzés: A kapcsolat e-mail-címének egyedinek kell lennie a rendszerben.
{% endhint %}

### 5) Egy kapcsolat hozzáadása egy Munkatétel Kapcsolatok kártyájáról

Ön továbbá egy Munkatétel [Kapcsolatok kártyájáról](https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatok-kartya) is létrehozhat egy új kapcsolatot. Amikor egy olyan felhasználóra keres rá a kapcsolatok kártyán, aki még nem létezik a rendszerben, akkor a „Kapcsolat létrehozása” lehetőségre kattintva, majd a kapcsolat adatainak kitöltésével létrehozhat egy új kapcsolatot.

Ha beírta a kapcsolat e-mail-címét, akkor a rendszer dekódolja azt, majd automatikusan kitölti a kapcsolat utónevét és vezetéknevét. Amint minden információt kitöltött és a létrehozásra kattintott, a rendszer átirányítja Önt a Munkatételhez.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FQxaFiFqD4PfiGoK0lTV4%2F7-Create-Contact-from-Work-Item.gif?alt=media&#x26;token=fa947a66-7b4c-4e75-977f-b43e8167e018" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Kérjük, vegye figyelembe, hogy ha tesztmódban hoz létre egy új kapcsolatot, akkor az adott kapcsolat kizárólag tesztcsomagok futtatására áll rendelkezésre a rendszerben.
{% endhint %}

## Kapcsolatok automatikus vagy manuális létrehozása

A [Kapcsolatkezelő oldal](https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatkezelesi-lap) „Automatikusan létrehozva” oszlopa lehetővé teszi az Ön számára annak megtekintését, hogy az adott kapcsolatot a rendszer automatikusan, vagy egy felhasználó manuálisan hozta-e létre.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FTLtVGYHl1F0z1iAdoTHw%2Fimage.png?alt=media\&token=4053becd-6e73-4aff-9bdf-bddf59ccd8b3)

{% hint style="info" %}
Kérjük, vegye figyelembe, hogy egy automatikusan létrehozott kapcsolat szerkesztését követően az többé nem lesz automatikusan létrehozott kapcsolatként feltüntetve a Kapcsolatkezelési oldal „Automatikusan létrehozva” oszlopában.
{% endhint %}

## Vállalatnév – Külső kapcsolat hatóköre

A Builder beállításaitól függően Ön számos módon hozzárendelhet egy vállalatot egy külső kapcsolathoz:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FqCFCSvqgrU0kvJFNVcMh%2F7-Company-Scope.gif?alt=media\&token=d650e781-39a6-4f3a-af2d-a9fea6fde0e7)

* Minden vállalat/globális
  * Ha ilyen hatályúra állítja a vállalatot, az azt jelenti, hogy a külső kapcsolat képes lesz minden vállalat számára új Munkatételeket létrehozni, valamint hozzáférni azokhoz.
  * Ez továbbá azt is jelenti, hogy a Work Manager felhasználói képesek egy Munkatételen szereplő minden külső kapcsolatra rákeresni.

{% hint style="info" %}
Kérjük, vegye figyelembe, hogy ez a beállítás csak akkor érhető el, ha a külső kapcsolat hatálya „Globális” vagy „Globális és helyi” értékként lett meghatározva a Builderben. További információkat erről [itt](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#external-contact-scoping) találhat.
{% endhint %}

* Egy adott vállalat (helyi)
  * Ha a kapcsolat hatályát egy bizonyos vállalatra állítja be, az azt jelenti, hogy a külső kapcsolat csak annak az adott vállalatnak a Munkatételeit hozhatja létre és csak azokhoz férhet hozzá, amelyekhez ez a külső kapcsolat hozzá lett rendelve.
  * A felhasználók továbbá csak akkor tudnak egy API-csomaghoz egy kapcsolatot hozzáadni, ha az adott kapcsolat ugyanabban a vállalatban (vagy egy ernyőcégben) van.

{% hint style="info" %}
Megjegyzés::

1. Egy külső kapcsolathoz hozzárendelt vállalat megváltoztatására csak úgy van lehetőség, hogy az Összes vállalat/globális hatályt egy adott (helyi) vállalatra állítják át, amennyiben a külső kapcsolat nincs több különböző vállalat munkatételéhez is hozzárendelve. Ezt úgy módosíthatja, hogy a kapcsolatot újból hozzárendeli egy munkatételhez.
2. Ha a külső kapcsolatokhoz az Összes vállalat/globális hatókört szeretné rendelni, a tömeges feltöltési fájl Vállalat oszlopát üresen kell hagyni, hogy a rendszer a kapcsolatokat alapértelmezés szerint globális hatókörrel lássa el.
3. Az egy automatikusan létrehozott kapcsolathoz rendelt vállalatot az Ön által beállított kapcsolatok hatálya határozza meg. Ha ez „Globális” vagy „Globális és helyi” hatályúra lett állítva, akkor az automatikusan létrehozott kapcsolat Globális hatályú lesz, azaz nem kapcsolódik majd egy adott vállalathoz. Ha „Helyi” hatályúra állították, akkor az automatikusan létrehozott kapcsolatot az alatt a vállalat alatt hozzuk létre, amely alatt a munkatétel is létezik.

   .
   {% endhint %}

### **A Globális/Helyi hatályok a kapcsolatok Munkatételekhez történő hozzárendelésére gyakorolt hatása**

{% hint style="warning" %}
Kérjük, vegye figyelembe, ha egy külső kapcsolat helyi hatállyal rendelkezik (azaz egy adott vállalathoz kapcsolódik), akkor Ön nem adhatja őket kapcsolatként egy olyan Munkatételhez, amely egy másik vállalaton belül létezik. Ez az ügynökfiókokra is igaz (amelyeknek *mindig* egy adott vállalat alatt kell létezniük). Kapcsolatként CSAK a globális hatályú külső fiókok kapcsolhatók rugalmasan bármely ügyfél Munkatételéhez.
{% endhint %}

## Egy kapcsolat szerkesztése <a href="#a-adding-editing-and-deleting-contacts" id="a-adding-editing-and-deleting-contacts"></a>

Egy kapcsolat szerkesztéséhez lépjen a [Kapcsolatkezelő oldalra](https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatkezelesi-lap), majd kattintson duplán a kapcsolatra, hogy megjelenjen a Kapcsolat szerkesztése felugró ablak.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FhXID62zH4OCNVI53E8CJ%2F7-Editing-a-Conact-in-Contact-Ma.gif?alt=media\&token=b23503b5-32d8-44e9-80f9-ca723be1d450)

Önnek továbbá lehetősége van a vállalat, az időzóna, az iroda helyszínének, valamint a kapcsolatok preferált nyelvének szerkesztésére is, ha kiválasztja a kapcsolat jelölőnégyzetét, majd megjelenik a szerkesztés gomb.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FvigNMWsyGzA50lTY4oz6%2F7%20Bulk-Editing-Contacts-in-Conta.gif?alt=media\&token=e28b2bc2-7df0-4ac1-87cc-2946182166bc)

## Egy kapcsolat törlése <a href="#a-adding-editing-and-deleting-contacts" id="a-adding-editing-and-deleting-contacts"></a>

Egy kapcsolat törléséhez lépjen a [Kapcsolatkezelő oldalra](https://docs.enate.net/enate-help/hu/nevjegyek/kapcsolatkezelesi-lap), majd kattintson a kapcsolat jelölőnégyzetére, amelynek hatására megjelenik a törlés gomb. Egyszerre akár több kapcsolatot is törölhet.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2Fb9YXa6b96g7rhAbsEWgM%2F7-Deleting-Conacts-from-Contact.gif?alt=media\&token=2143c554-585d-4af6-a3d3-6c09bd8ff1a2)
