# Source: https://docs.enate.net/enate-help/hu/toebbnyelvu-tamogatas.md

# Többnyelvű támogatás

Az Enate jelenleg az alábbi nyelveket támogatja

1. Angol
2. Portugál (brazíliai)
3. Spanyol
4. Román
5. Magyar
6. Lengyel
7. Orosz
8. Francia
9. Német

A végfelhasználók által a szolgáltatás nyújtásához használt működési környezet teljes körűen támogatja a többnyelvű használatot, és a felhasználói profilon keresztül minden felhasználó kiválaszthatja saját előnyben részesített nyelvét, valamint a dátum és idő formátumát.

Az előnyben részesített nyelv kiválasztásához a Felhasználói beállítások szakasz Nyelv legördülő listájából válasszon ki egy nyelvet.

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCCjQMZrIXW_c-JAut%2F-MZCWE2H20vuRKMcEY_D%2FChange-Language.gif?alt=media\&token=112e24b6-1177-4eba-8d46-043d1fae0317)

A képernyő címkéi a bejelentkezett felhasználó nyelvén jelennek meg – ezt az **Enate** rendszer nyelvi csomaggal való bővítésével lehet elérni. Minden nyelvi csomag tartalmazza a felhasználóspecifikus nyelvnek megfelelő társításokat, például a „**Sor**” portugálul „**Fila”,** a „**Művelet**” pedig „**Açao**” lesz.

A kezelőfelület alábbi elemei lesznek elérhetőek a bejelentkezett felhasználó nyelvén:

| **Elem**                        | **Részletek**                                                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kezdőlap**                    | <ol><li>RAG-szűrők</li><li>Saját csapat</li><li>Robotcsoport</li><li>Várólista</li><li>Diagram)</li><li>Táblázat- és oszlopbeállítások viselkedés.</li></ol><p>A Postaláda lap ugyanígy viselkedik.</p> |
| **Gyorskeresés**                | Emberek, kommunikáció és munkatételek keresése                                                                                                                                                          |
| **Várólista lap**               |                                                                                                                                                                                                         |
| **Navigációs hivatkozások**     | A Builder eszközre, a Várólista lapra, és a legutóbb megnyitott munkatételekre stb. mutató hivatkozások.                                                                                                |
| **Felhasználói profil oldal**   | Itt a felhasználó az előnyben részesített nyelv mellett a dátum és az idő formátumát tudja beállítani.                                                                                                  |
| **Híváskezelés oldal**          | Ez az oldal az adott felhasználóhoz tartozó összes kommunikációt és munkatételt megjeleníti.                                                                                                            |
| **Munkatételek kezelőfelülete** | Címkék és gombok, mint például Kategóriaválasztó, Állapot stb.                                                                                                                                          |

{% hint style="info" %}
Megjegyzés: A valódi nevek, mint például az ügyfél neve és a felhasználónév, az eredeti nyelven fog szerepelni, úgy, ahogyan azt a Builder eszközben megadták.
{% endhint %}

## A Work Manager végfelhasználói által megadott adatok <a href="#a-work-manager-vegfelhasznaloi-altal-megadott-adatok" id="a-work-manager-vegfelhasznaloi-altal-megadott-adatok"></a>

Az Enate a Work Manager képernyőin és menüelemein, mint például címkéin, hivatkozásain és gombjain teljes mértékben támogatja a felhasználó által választott nyelvet, a felhasználó által beírt tartalom azonban ugyanúgy fog megjelenni, ahogyan azt a felhasználó eredetileg beírta, azt a rendszer nem fogja automatikusan másik nyelvre fordítani, amikor a tartalmat egy másik nyelvet használó személy tekinti meg.

Ha például egy brazil felhasználó portugálul ír be egy megjegyzést, az Enate azt portugál nyelven menti az adatbázisba, és azt mindig portugálul fogja megjeleníteni, úgy, ahogyan azt a felhasználó beírta.

Az alábbi lista azokat az elemeket tartalmazza, amelyek a felhasználó által beírt módon jelennek meg, és amelyeket a rendszer **NEM** fordít le automatikusan:

| **Elem**                          | **Részletek**                                                                                                                                                                                                                                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ügy                               | <p>1. Megjegyzések </p><p>2. E-mailek </p><p>3. Ügy – Rövid leírás/cím </p><p>4. A végfelhasználó által elindított új művelethez tartozó felülbírálási utasítás</p>                                                                                                                                         |
| Művelet                           | <p>1. Megjegyzések </p><p>2. E-mailek </p><p>3. Ellenőrzőlista megjegyzései </p><p>4. Művelet állapota – A „Nem lehet befejezni” okaként megadott szöveg </p><p>5. A végfelhasználó által elindított új művelethez tartozó felülbírálási utasítás </p><p>6. A művelet munkatársi értékelési megjegyzése</p> |
| Jegy                              | <p>1. Az új alárendelt jegyek címe és leírása </p><p>2. A felhasználó által elindított új művelet neve 3. A felhasználó által elindított új ügy neve</p>                                                                                                                                                    |
| Kapcsolat                         | A kapcsolatra vonatkozó adatok, például cím                                                                                                                                                                                                                                                                 |
| Fájlok                            | A fájl neve és a fájlra vonatkozó megjegyzés                                                                                                                                                                                                                                                                |
| Hiba                              | A hiba leírása                                                                                                                                                                                                                                                                                              |
| Újbóli hozzárendelés megjegyzései | A felhasználó által megadott szöveg, amikor a munkát egy másik csapattárshoz rendeli                                                                                                                                                                                                                        |

### Egyéni adatok és kártyák <a href="#egyeni-adatok-es-kartyak" id="egyeni-adatok-es-kartyak"></a>

A többnyelvű támogatás első verziója nem teszi lehetővé az egyéni adatok és a gyorskártyák Builder eszközben való többnyelvű konfigurálását. Ehhez több kártyára és adattételre lenne szükség.

### Az alkalmazásban megjelenő értesítések <a href="#az-alkalmazasban-megjeleno-ertesitesek" id="az-alkalmazasban-megjeleno-ertesitesek"></a>

A többnyelvű funkcionalitás első verziója nem támogatja az értesítések angoltól eltérő nyelven való megjelenítését.
