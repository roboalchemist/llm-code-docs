# Source: https://docs.enate.net/enate-help/hu/muvelet-feldolgozasa/abbyy-flexicapture-muveletek.md

# ABBYY FlexiCapture-műveletek

Az Enate támogatja az [ABBYY FlexiCapture](https://www.abbyy.com/flexicapture/)-rel történő integrációt, ami az ABBYY FlexiCapture-rel integrált művelettel történik. (Az új művelettípus létrehozásával és konfigurálásával kapcsolatos útmutatást tekintse meg [itt](https://docs.enate.net/enate-help/integrations/enate-integrations/ocr-integration/abbyy-integration)).

Amikor ezt az ABBYY-műveletet futtatja egy ügyön, az ügyhöz mellékelt dokumentumok beküldhetők az ABBYY FlexiCapturehöz OCR-beolvasáshoz. A feldolgozott kimeneti fájlokat a rendszer automatikusan visszaküldi és az ügyhöz csatolja.

{% hint style="info" %}
Megjegyzés: Csak az ABBYY 12-es vagy újabb verziója által támogatott fájltípusok lesznek beküldve. Az ABBYY által támogatott formátumok listáját [itt](https://help.abbyy.com/en-us/flexicapture/12/standalone_operator/input_formats/) találja.
{% endhint %}

A rendszer a következő megerősítő üzenetet jeleníti meg, amikor arra vár, hogy dokumentumo(ka)t küldjön be az ABBYY FlexiCapture-rendszerbe feldolgozásra:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FoZtcoLVIoNVgi0asWN3b%2Fimage.png?alt=media\&token=0681ac32-d46b-4961-b279-a22ac083c1d9)

Megerősítést láthat, amikor a dokumentumok feldolgozásra történő beküldése sikeres volt az ABBYY rendszerében.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2Fhen2ec7tSO7h3WZFYst4%2Fimage.png?alt=media\&token=afd9756b-c2fa-4756-82b4-78a8cff8c93f)

Az utolsó próbálkozás akkor történik, amikor a dokumentumo(ka)t beküldte feldolgozásra az ABBY FlexiCapture rendszerébe.&#x20;

Ha a beküldött dokumentumok érvénytelen fájlformátumúak voltak, vagy valamilyen probléma adódott a dokumentumnak a formázásával, akkor a rendszer az alábbi üzenetet küldi el Önnek:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2Fy6uMof6A4JuJOc95u2Al%2Fimage.png?alt=media\&token=b5a1788d-d224-4a19-9c1e-6628de4da75f)

### Automatikus újrapróbálkozások

Ha a dokumentum beküldése során valamilyen hiba történt, akkor a rendszer néhány alkalommal automatikusan újrapróbálja majd a beküldést attól függően, hogy az Ön rendszere hogyan lett beállítva a Builder felületén belül (további információkat [itt ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)találhat).&#x20;

Ha az automatikus újraküldéseket követően továbbra is probléma van a beküldéssel (pl. ha az újrapróbálkozások száma 5-re van állítva, és a rendszernek a következő 5 újrapróbálkozás során sem sikerül kapcsolatot létesítenie), akkor az ABBYY-művelet „Lezárva” állapotúvá válik.

{% hint style="info" %}
Ebben az esetben, amikor a művelet nem képes kapcsolatot létesíteni a külső rendszerrel, akkor az eszkalálódik az ügy tulajdonosához, kiemelve az ügy képernyőjének műveleti részében azt, hogy ez a művelet le lett zárva, és az elvégzése sikertelen volt.
{% endhint %}

## Ellenőrzés

Miután beszkennelt egy dokumentumot, az ABBYY egy pontszámot hoz létre a szkennelés minősége alapján. Ha a megbízhatósági pontszám a megadott küszöbérték felett van, akkor nincs szükség ellenőrzésre, és a rendszer feldolgozza az adatokat és elvégzi a feladatot. Ha a megbízhatósági pontszám egy bizonyos küszöbérték alatt van, emberi ellenőrzésre van szükség.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### Ellenőrzés nem szükséges <a href="#no-verification-required" id="no-verification-required"></a>

Egy állapotüzenet jelzi, hogy nincs szükség emberi ellenőrzésre:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsm0__59qGFBexYyWZ%2Fimage.png?alt=media\&token=a49da588-38c2-4784-b771-a144ada2ec54)

A feldolgozás befejezése után az ABBYY-művelet befejeződik. Az exportált fájlok az ügyhöz lesznek csatolva, és megjelennek a Fájlok kártyán.

{% hint style="info" %}
Megjegyzés: Ha a kimeneti fájlcímke be van állítva, akkor az ABBYY a kimeneti címkét az összes feldolgozott fájlra alkalmazza, és készen áll a későbbi tevékenységek során történő felhasználásra.
{% endhint %}

### Emberi ellenőrzés szükséges

A rendszer figyelmeztetni fogja Önt, ha emberi ellenőrzésre van szükség:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FwJExx5UhAZoKVopjkEER%2Fimage.png?alt=media\&token=f56c3fbb-423c-485e-a155-375fb8890fa3)

Ezen kívül a művelet állapota mellett egy emlékeztető szöveg lesz látható, ami tájékoztatja arról, hogy a manuális ellenőrzést el kell végezni az ABBYY rendszerben, mielőtt folytathatná a folyamatot.&#x20;

Az „Ellenőrzés” gombra kattintva megnyílik az ABBYY Verification Station (ABBYY Ellenőrzési Állomás) alkalmazás, ahol ellenőrizheti a beolvasott dokumentumokat, és szükség szerint módosíthatja az információkat.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsuykc2DFaOX6-GsPY%2Fimage.png?alt=media\&token=27953730-e342-4885-9206-fae88572b769)

{% hint style="info" %}
Megjegyzés : A teljes hozzáféréshez egy érvényes ABBYY FlexiCapture-fiókra van szüksége, és az adott projekten belül rendelkeznie kell az ellenőrzés elvégzésére vonatkozó jogosultsággal.
{% endhint %}

Miután bejelentkezett, megjelenik az ABBY FlexiCapture Verification Station képernyője, ahol szükség szerint áttekintheti és módosíthatja az információkat.

A Verification Station három részből áll:

1. A beolvasandó dokumentum egyes oldalai.
2. Közelkép a beolvasandó eredeti dokumentumról
3. A kivonatolt kimenet, vagyis az eredeti dokumentum beszkennelt változata.

Az eredeti dokumentum lapján sárgával kiemelt szöveg az az adat, amelyet az ABBYY nem tud beolvasni. Ez piros színnel van kiemelve a kivonatolt kimeneten.

Bizonyos karakterek, mint például az „i”, szintén ki lehetnek emelve a kivonatolt kimenet szakaszában, ha az ABBYY bizonytalan a beolvasott másolattal kapcsolatban.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx6MLiLXtXFAmC00W%2Fimage.png?alt=media\&token=adebd784-bdf7-4f4c-b696-4832e40c4ec2)

Miután végzett a manuális ellenőrzéssel, a képernyőn megjelenik ennek megerősítése, valamint azt is láthatja, hogy egy kivétel történt, amely manuális beavatkozást igényelt:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FxU8bR7Fc3rQRbktAwzxv%2Fimage.png?alt=media\&token=086d4a8e-9c70-4bf3-9707-db61bb8c6106)

‌A feldolgozás befejezése után az exportált fájlok az ügyhöz lesznek csatolva, és megjelennek a [Fájlok kártyán](https://docs.enate.net/enate-help/hu/a-kepernyok-attekintese-minden-munkatetel-eseten/fajlkartya).

Ezt követően a műveletet megjelölheti befejezettként.

{% hint style="info" %}
Megjegyzés: Ha a kimeneti fájlcímke be van állítva, akkor az ABBYY a kimeneti címkét az összes feldolgozott fájlra alkalmazza, és készen áll a későbbi tevékenységek során történő felhasználásra
{% endhint %}
