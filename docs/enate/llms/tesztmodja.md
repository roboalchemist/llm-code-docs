# Source: https://docs.enate.net/enate-help/hu/tesztmodja.md

# Tesztmód

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Átváltás teszt üzemmódra <a href="#a-atvaltas-teszt-uezemmodra" id="a-atvaltas-teszt-uezemmodra"></a>

Ha a felhasználói fiók beállításai lehetővé teszik, hogy hozzáférjen a tesztadatokhoz, akkor a Work Managert tesztmódban is futtathatja. Ez a hivatkozás a fejlécsáv jobb oldalán lévő felhasználó legördülő menüből érhető el.

## A tesztmód ismertetés <a href="#b-a-tesztmod-ismertetes" id="b-a-tesztmod-ismertetes"></a>

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FBCI755tRmOsDlLuATnmw%2Fimage.png?alt=media\&token=3ee98edc-16e8-4fdb-982a-59c1d688682a)

Amikor a rendszert teszt üzemmódban futtatja, csak a tesztadatokat fogja látni. A folyamatok próbaverzióival munkatételeket hozhat létre és futtathat, és így az éles használat előtt ellenőrizheti őket anélkül, hogy befolyásolná az élő környezetet.

Teszt üzemmódban a fejlécsáv pirosan jelenik meg, hogy emlékeztesse arra, nem az éles környezetet használja.

## Eltérő kezelők és tagok meghatározása a várólistákhoz tesztmódban <a href="#c-eltero-kezelok-es-tagok-meghatarozasa-a-varolistakhoz-tesztmodban" id="c-eltero-kezelok-es-tagok-meghatarozasa-a-varolistakhoz-tesztmodban"></a>

Teszt üzemmódban mostantól lehetősége van egy sorhoz eltérő kezelőt megadni teszt és éles módban.

Példa: Tegyük fel, hogy Menedzser 1 az éles környezethez fér hozzá, és két sorért felel: Finanszírozás és Fő ügy.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2Fq0OduzBO7KxnfAhZlx6o%2Fimage.png?alt=media\&token=8a71d4c4-d8e1-46a1-85d3-d84056495be5)

Teszt üzemmódban ugyanezt a két várólistát egy másik felhasználó is kezelheti, aki rendelkezik csapatvezetői és tesztmód jogosultsággal – a lenti példán a Menedzser 2 mindkét sor felelőseként lett beállítva tesztmódban.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FhBEXhgqlc1HZ9X7fGLRZ%2Fimage.png?alt=media\&token=60e94728-5b8d-4e65-b46a-e628ecd1058f)

## Robotok átkapcsolása éles és tesztmód között <a href="#d-robotok-atkapcsolasa-eles-es-tesztmod-koezoett" id="d-robotok-atkapcsolasa-eles-es-tesztmod-koezoett"></a>

Mostantól a robotokat átállíthatja, hogy tesztmódban vagy éles módban fussanak-e. Pontosabban az UiPath, az Automation Anywhere és a BluePrism robotok tevékenységtárához két új tevékenységet adtunk (és a szabványos API-kat úgy módosítottuk, hogy ezeket általánosságban meg lehessen hívni):&#x20;

* Set Live Mode (Élő módra váltás)&#x20;
* Set Test Mode (Tesztmódra váltás)&#x20;

Ezekkel a műveletekkel a robotokat átállíthatja a teszt- és az élő mód között. Miután egy adott robotot tesztmódba helyezett, a robot által ezután esetlegesen elvégzett művelethívások (pl.: „Get more work” (További munka lehívása), „Create Ticket/Case” (Jegy/ügy létrehozása) stb.) a tesztkörnyezetre fognak vonatkozni, és csak teszt munkatételek fognak létrejönni. A folyamat éles környezetben való elindítása után a robotot vissza kell kapcsolni élő módba, hogy élő munkatételeket hozzon létre.

## Különálló tesztkapcsolatok a rendszerben <a href="#e-kueloenallo-tesztkapcsolatok-a-rendszerben" id="e-kueloenallo-tesztkapcsolatok-a-rendszerben"></a>

Az Enate mostantól lehetővé teszi, hogy teszt üzemmódban külön kapcsolatrekordokat hozzon létre, vagyis a tesztmódban létrehozott kapcsolatrekordokhoz csak a tesztfelhasználók fognak hozzáférni (az éles módban létrehozottakhoz pedig csak az éles mód használói). Ezzel biztosítható, hogy a tesztcsomagokból küldött e-maileket a rendszer véletlenül ne az éles környezet felhasználóinak küldje, illetve fordítva.
