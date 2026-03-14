# Source: https://docs.enate.net/enate-help/hu/muvelet-feldolgozasa/aktivald-a-kuelso-api-muveleteket.md

# Műveletek: „Külső API aktiválása”

Más műveleti archetípusokhoz hasonlóan a „Külső API aktiválása” műveletek is felhasználhatók az Ügyfolyamatok során, mégpedig akkor, amikor automatikusan meg kell hívnia egy másik rendszert, hogy adatokat adjon át annak, valamint potenciálisan arra késztesse a külső rendszert, hogy frissített egyéni adatokat küldjön vissza az Enate-nek.&#x20;

A „Külső API aktiválása” műveletek beállításával kapcsolatos bővebb információkért tekintse meg a [Builder ](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab)adott részét.&#x20;

Néha késés fordulhat elő a külső rendszer válaszára várakozás során. Amikor ez megtörténik, azaz amikor a „Külső API aktiválása” művelet arra vár, hogy egy külső rendszerből információ érkezzen vissza, a Művelet információs kártyája „Várakozás” állapotúként jelenik meg a Work Managerben.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MeP0oORczNEORCZRcsN%2F-MeP16TekPQzpdTN1ROc%2Fimage.png?alt=media\&token=16976a41-fe3d-414f-91ad-aff6a36cde4c)

Amikor a külső rendszer végül a frissített adatokat tartalmazó választ küld az Enate-nek, egy jelölővel jelzi, hogy sikeres VAGY sikertelen volt-e:

#### Válasz sikeres teljesítéssel

Amikor a rendszer válaszol és jelzi, hogy sikeres volt, akkor a Művelet automatikusan „Lezárt” állapotú lesz, a megoldási módszer pedig „Sikeresen elvégezve” lesz.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2F99ccSf9wAQgYvzSNkOHz%2Fimage.png?alt=media\&token=b5bf8924-7541-4ee2-9cc7-958e5da14605)

#### Válasz sikertelen teljesítéssel

Ha a rendszer azt válaszolja, hogy sikertelen volt, a művelet „Elvégzendő” állapotúvá válik, okként pedig az „Frissítette: integráció” lesz megjelölve. A külső API további információkkal is szolgálhat a sikertelenség okára vonatkozóan. Ez az információ a művelet információs kártyáján az „Elutasítás oka” részben jelenik meg.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FmQFX1RCCVkWYwtDwOMVl%2Fimage.png?alt=media\&token=0813b8f9-0136-4be7-a8da-c8808e741a63)

Ha a művelet sikertelen mert nem fejeződött be a számára beállított ([a Builderben konfigurált](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab)) időn belül, akkor „Elvégzendő” állapotúvá válik, okként az „Időtúllépés” lesz megjelölve, és a beállított hozzárendelési szabályok alapján várólistára kerül/hozzárendelődik egy felhasználóhoz.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FKIsaQVKhjvJ0QthR2LSh%2Fimage.png?alt=media\&token=828c95a5-12da-4ac7-94d0-2fc0e1b4bf09)

Az ilyen sikertelen Műveletek ettől kezdve szabványos kézzel végzett műveletként viselkednek majd.

{% hint style="info" %}
Kérjük, vegye figyelembe, hogy az Ügy tulajdonosát ilyen helyzetekben NEM értesítjük.
{% endhint %}

### Automatikus újrapróbálkozások

Ha a Művelet nem tud kapcsolatba lépni a külső rendszerrel, automatikusan megpróbálja a csatlakozást egy bizonyos számú alkalommal, attól függően, hogy a rendszer hogyan lett konfigurálva a Builder alkalmazásban (további információt [itt ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)találhat). Egy hibaüzenetsáv is megjelenik a Műveleten, amely a következőket mutatja meg:&#x20;

* mikor történt a hiba&#x20;
* mikor próbál majd meg a rendszer automatikusan újracsatlakozni&#x20;
* hány alkalommal próbálkozott a rendszer újracsatlakozni&#x20;
* még hány alkalommal fogja a rendszer automatikusan megkísérelni az újracsatlakozást.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MeP0oORczNEORCZRcsN%2F-MeP18cvEPKzjHC3Eihl%2Fimage.png?alt=media\&token=c7371017-8f3e-4c01-a11d-3fabcf035de0)

A hibaüzenet „Próbáld újra” lehetőségére kattintva innen Ön manuálisan is újra megpróbálhatja létrehozni a kapcsolatot.

{% hint style="info" %}
Kérjük, vegye figyelembe, hogy a manuális újrapróbálkozás is egy újrapróbálkozási kísérletnek számít, ezért megjelenik abban a számban, amely megmutatja, hogy a rendszer hányszor próbálta meg „automatikusan” létrehozni a kapcsolatot.
{% endhint %}

Ha a Művelet az automatikus újrapróbálkozások után sem tud kapcsolatba lépni (pl. ha az újrapróbálkozások 5 alkalomra lett beállítva, és a rendszer nem tud kapcsolatot létrehozni az 5 automatikus újrapróbálkozást követően), akkor az „Lezárva” állapotba kerül, megoldási módként pedig a „Nem sikerült elvégezni” lesz megjelölve.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MeP0oORczNEORCZRcsN%2F-MeP1ABKSvXMgqnzI6h6%2Fimage.png?alt=media\&token=d5d07119-674a-47bd-a8a2-948fd4d3e9b8)

{% hint style="info" %}
Ebben az esetben a Művelet nem tud kapcsolatot létrehozni a külső rendszerrel, erről értesítjük az Ügy tulajdonosát is, az Ügy Műveleti részében pedig kiemeljük, hogy ez a Művelet Lezárva – Nem sikerült elvégezni állapotú lett.
{% endhint %}

Amikor a Művelet megkapja a szükséges információkat, akkor automatikusan lezárul.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FQCGrYzOHB0Xf8nzTHJ0o%2Fimage.png?alt=media\&token=3c191499-b733-4ce8-9513-c9e0f58237da)

#### Az újrapróbálkozások beállításainak módosítása az újrapróbálkozások során, illetve azok megkezdését követően&#x20;

Ha az automatikus újrapróbálkozások beállítása a Builderben megváltozott miután a rendszer megpróbált automatikusan kapcsolatba lépni egy külső rendszerrel, a következő fog történni:&#x20;

Ha például, az újrapróbálkozás eredetileg 5 próbálkozásra lett beállítva, és a rendszer 5 automatikus újrapróbálkozást követően sem tud kapcsolatot létrehozni, a Művelet „Lezárva” állapotba kerül egy hibaüzenettel, amely az 5/5-ös újrapróbálkozási adatot fogja mutatni.&#x20;

Ha az újrapróbálkozások számát ezt követően 5-nél magasabb számra, például 7-re állítják, akkor a hibaüzenet 5/7-es újrapróbálkozási adatot fog mutatni, de a rendszer NEM fog automatikusan a 6. és 7. alkalommal kapcsolatot teremteni, mivel a Művelet már le lett zárva.

Azonban, ha a Művelet nem lett „Lezárva” állapotú, mivel még nem érte el a maximálisan beállított automatikus újrapróbálkozások számát (például csak 4 próbálkozása volt az 5 alkalomból) és ezután a próbálkozások számát 7-re növeljük, ez azt jelenti, hogy a művelet 7 alkalomig automatikusan újra megpróbál majd csatlakozni.&#x20;

Ezzel szemben, ha az újrapróbálkozások megkezdése után csökkenti az újrapróbálkozások számát – pl. 10-ből 4 újrapróbálkozás már megtörtént, de ezt követően 4-re csökkenti a maximumot, akkor a rendszer továbbra is 10-ből 4-et jelenít meg, de valójában lezárva állapotúvá válik.
