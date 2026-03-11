# Source: https://docs.enate.net/enate-help/hu/muvelet-feldolgozasa/dokumentumkivonatolasi-muveletek.md

# Dokumentumkivonatolási műveletek

## Áttekintés

A dokumentumkivonatolási komponens automatikusan kivonja a beérkező e-mailekhez csatolt fájlok releváns adatait, hogy ezek az adatok a munkatétel további feldolgozása során is használhatók legyenek, időt és munkát takarítva meg ezzel az Ön ügynökeinek. Ez azt is jelenti, hogy az olyan dokumentumok, mint például a PDF-ek, beolvashatók és felhasználhatók az ügyek Enate-ben történő elindításához és a folyamatban lévő tevékenységek részeként is.

Amikor dokumentumkivonatolási műveletet fut le egy ügyön, az ügyhöz mellékelt dokumentumok az Ön által kívánt technológiát használva beolvashatók, és a feldolgozott kimeneti fájlokat a rendszer automatikusan visszaküldi és az ügyhöz csatolja.

Ha az Ön által használt technológia a beállított megbízhatósági küszöb alapján nem kellően biztos az eredményekben, akkor az Enate a munkát azonnal átküldi egy ügynöknek a Work Managerben, aki átnézheti és ellenőrizheti azt, így biztosítva az emberi felülvizsgálatot, ha szükség van rá.

Ezt a komponenst az Enate Builder <mark style="color:blue;">Piacterének</mark> felületén az Ön rendszergazdája állíthatja be.

Bővebb információkért tekintse meg a következő videót:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

## Hogyan működik ez futtatás közben?

Amikor Ön egy ügyet futtat a Work Managerben, a beérkező e-mailek fájljaiból származó releváns adatokat a rendszer automatikusan elemzi és kivonatolja.

Amennyiben az Ön által használt technológia kellően biztos az adatkivonatolás eredményében, akkor ezt a műveletet egyáltalán nem kell egy emberi felhasználónak látnia – az egyszerűen automatikusan befejeződik, és az ügy a következő műveletre lép majd. A befejezett adatkivonatolási művelet rákattintást követően továbbra is megtekinthető, azonban azt nem kell átadni, és abban nem kell egy emberi felhasználónak részt venni.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FzTvRO8D90D2bYyMsD1VA%2Fimage.png?alt=media&#x26;token=8be89562-2723-42d2-b5d7-fec143b2b9c3" alt=""><figcaption></figcaption></figure>

Ha azonban a kivonatolási technológia kevésbé biztos az adatkivonatolás eredményeiben, akkor a műveletet átadja egy emberi felhasználónak, aki ha legközelebb a „Lehívás a várólistáról” lehetőséget használja a kezdőlapján, akkor felveheti és áttekintheti azt. Amikor egy ügynök megnyitja a műveletet, akkor láthatja, hogy az azért került hozzájuk, mert további ellenőrzésekre van szükség.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FuaHACOawZwIM7YziJ33a%2Fimage.png?alt=media&#x26;token=9f610d69-9dc1-4a9e-9473-ddfe75606e32" alt=""><figcaption></figcaption></figure>

Ehhez csupán rá kell kattintania a „Hitelesítés most” lehetőségre, majd a művelet „Érvényesítőállomás” képernyőjére kell görgetnie, amely megmutatja a beolvasott dokumentum képét, valamint az adatértékek kivonatolt táblázatát. Ezzel megtekintheti, hogy hol vannak azok a kiemelt részek, ahol alacsonyabb a megbízhatósági szint, áttekintheti azokat, majd szükség szerint javíthatja is őket. Ezek az eredeti helyükön, illetve egy felugró ablakban is megtekinthetők, hogy teljes képernyőn láthassa azokat.

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FUKbAIAriZSnTuBgRHorp%2Fimage.png?alt=media&#x26;token=ee83d5e2-a14a-45e1-9ab0-6586b2287e0f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Megjegyzés: Egyszerre csak egy dokumentum tekinthető meg.
{% endhint %}

<figure><img src="https://2320817298-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-4190165790%2Fuploads%2FjOeoDGTg2qh1L7sevZQO%2Fimage.png?alt=media&#x26;token=677fd714-f0ad-42a6-8cb6-6afa63e39b03" alt=""><figcaption></figcaption></figure>

Ezen az ellenőrző képernyőn az ügynök láthatja a fájl beolvasott másolatát, amely több oldalból is állhat, valamint két fület, amelyek a kivont adatokat tartalmazzák.

* Az Extracted Data (Kivont adatok) fülön láthatók a kivont adatok ügynök kulcs-érték párosai, valamint az EnateAI által nekik adott megbízhatósági szint. Az értékek szükség szerint módosíthatók, és az ügynök az adott érték frissítés gombra kattintásával mentheti őket. Ezzel a kulcs megbízhatósági értéke 100%-ra áll.
* A Táblázatok fülön láthatók az összes ismétlődő adat, amelyeket táblázatként kiválasztottak. A törlés gombbal törölheti a felesleges sorokat.

Ha az ügynöknek bármikor el kell hagynia a Validációs állomás képernyőt, akkor egyszerűen kattintson a „Mentés vázlatként” gombra, hogy elmentse az adott dokumentumhoz tartozó módosításait.

{% hint style="info" %}
Megjegyzés: Ha egy ügynök egy nem neki rendelt művelet érvényesítési képernyőjére lép, az adatok csak olvashatóak és nem szerkeszthetők. Az adatok szerkesztéséhez az ügynöknek először magának kell hozzárendelni a műveletet.
{% endhint %}

Ha az ügynök elégedett az adatokkal, a frissített adatok elküldéséhez csak a „Küldés” gombra kell kattintania. Az EnateAI a háttérben befejezi a feldolgozást, és a Művelet képernyőn jelzi, ha elkészült. A háttérben zajló feldolgozás lehetővé teszi az ügynöknek, hogy továbblépjen a többi ellenőrzésre váró dokumentumra.

Miután az utolsó érvényesítést igénylő dokumentumra kattintott a „Küldés” gombra, a Művelet képernyő automatikusan bezárul. Az EnateAI ismét a háttérben fejezi be a feldolgozást, és rövid időn belül a Műveletet Megoldottként jelöli, majd Lezárva állapotba helyezi.

*Megjegyzés: Minden alkalommal, amikor áttekinti és frissíti az adatokat, az EnateAI tanul és egy kicsit jobb lesz az adatkinyerési javaslatokban. Ha azt veszi észre, hogy a technológia rendszeresen téves javaslatokat ad, kérje az adminisztrátori csapat segítségét a bizalmi küszöbérték módosításában.*
