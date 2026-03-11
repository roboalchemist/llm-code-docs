# Source: https://docs.enate.net/enate-help/hu/jegy-feldolgozasa/jegy-toebb-jegyre-bontasa.md

# Egy jegy felosztása

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzNw==>" %}

Ha egy jegy több különálló kérést/kérdést is tartalmaz, amelyek külön-külön jobban kezelhetők, a jegyet szét is bonthatja. A tevékenységlapon kattintson a Felosztás lapra a felosztás megkezdéséhez:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mi184tS683RELF8NCk0%2F-Mi18TZxHsnHbMf-EODY%2Fimage.png?alt=media\&token=4013ee9f-ba76-4b89-a1ee-0e7ed0945382)

A képernyő alapértelmezés szerint két jegyre osztódik. Manuálisan több részre is oszthatja a jegyet. A cím, a leírás és a kontextus (Ügyfél>> Jegykategória stb.) átmásolódik az aktuális jegyből, de a jegyfelosztás befejezése előtt ezeket módosíthatja. Választhatja azt, hogy az összes felosztott jegyet magánál tartja.

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FLwTkJN5Bfv1s0h6Vwh2q%2Fimage.png?alt=media\&token=2f4ab1af-7a97-43dc-929e-4f80eee81cc3)

A felosztás megerősítéséhez kattintson az információs kártya gombjára:

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FXUKKZfTwWp7GmjSGUq2A%2Fimage.png?alt=media\&token=d1170b0b-82ab-4f48-9d21-6992df90b077)

A felosztás után az eredeti jegy állapota „Várakozik – Felosztott jegy” lesz, és ezt követően nem lesz része a szolgáltatásteljesítésnek (lényegében le lesz zárva).

![](https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2Fw0a8VUC9SQjTw3NhVxWh%2Fimage.png?alt=media\&token=31a03ca1-658a-443a-b1e5-0fca7f98366f)

Miután a felosztott jegyeket megoldották, az eredeti jegy teljesen befejezett állapotba kerül. A szolgáltatásiszint-szerződés teljesítése érdekében az eredeti jegy kezdési dátumát a rendszer átmásolja az összes létrejött jegyre.

SLA-célokra az eredeti jegy kezdő dátumát átmásoljuk minden létrejött jegyre, míg az időt, amikor az eredeti jegyet „Megoldottként” jelölték meg, az alapján számoljuk ki, hogy mikor oldják meg az utolsó jegyet, amelyre az fel lett osztva.

Például ha az A jegyet B és C jegyekre osztották fel, és a B jegyet „2022.02.03. 01:10:00” időpontban, míg a C jegyet „2022.02.03. 02:00:00” időpontban oldották meg, akkor az A jegy megoldási idejét „2022.02.03. 02:00:00”-ként jelöljük meg.

A Felosztás lapról kilépve a jegyfelosztást bármikor megszakíthatja. (A jegyen található „Felosztás” gomb megnevezése megváltozik, így biztos lehet benne, hogy azt nem osztja fel.)
