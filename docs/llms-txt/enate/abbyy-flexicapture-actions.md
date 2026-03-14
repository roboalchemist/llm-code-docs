# Source: https://docs.enate.net/enate-help/romana/procesarea-unei-actiuni/abbyy-flexicapture-actions.md

# Acțiuni integrate în ABBYY FlexiCapture

Enate poate să ofere integrare cu [ABBYY FlexiCapture](https://www.abbyy.com/flexicapture/) - acest lucru se realizează prin utilizarea unei Acțiuni integrate în ABBYY FlexiCapture (Faceți clic [aici ](https://docs.enate.net/enate-help/integrations/enate-integrations/ocr-integration/abbyy-integration)pentru a vedea instrucțiunile privind modul de creare și configurare a acestui nou tip de Acțiune).

În momentul în care se execută o acțiune ABBYY pentru un Caz, documentele atașate acestui Caz pot fi trimise către ABBYY FlexiCapture pentru scanare OCR, iar fișierele de ieșire procesate vor fi returnate și atașate în mod automat la Caz.

{% hint style="info" %}
Rețineți: Pot fi trimise numai tipurile de fișiere acceptate de ABBYY v12 și de versiunile succesive. Faceți clic [aici ](https://help.abbyy.com/en-us/flexicapture/12/standalone_operator/input_formats/)pentru a vedea următorul link cu lista de formate acceptate de ABBYY.
{% endhint %}

Sistemul va afișa acest mesaj în timp ce așteaptă să trimiteți documentul (documentele) către ABYFlexiCapture pentru procesare:

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2F6kzIL4wwZqdiShVV80qI%2Fimage.png?alt=media\&token=e16c7b8a-eba0-40e8-8dfb-4aa9495c116e)

Veți vedea o confirmare a faptului că documentele au fost trimise cu succes către ABBYY pentru procesare:

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FvUBDUGeXr7TfEZq8EE9z%2Fimage.png?alt=media\&token=db99222c-24dc-4506-aad2-573be97a2ea3)

Se face o ultimă încercare când documentele (sau documentul) sunt trimise pentru procesare către serverul ABBYY FlexiCapture.&#x20;

În cazul în care documentele au fost trimise într-un format incorect sau dacă există probleme de formatare a documentelor în sine, sistemul va afișa acest mesaj:

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2F7V2Oh70jGN5Fhp9JIRd9%2Fimage.png?alt=media\&token=779cea62-9229-43b5-8431-7f97cc79dc7b)

### Încercări automate

Dacă apare o problemă cu trimiterea documentelor, sistemul va reîncerca automat să le trimită în repetate rânduri, în funcție de modul în care a fost configurat sistemul în Builder (consultați [aici](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern) pentru mai multe informații).&#x20;

Dacă problema relaționată cu trimiterea documentelor persistă și în urma încercărilor automate (de exemplu, dacă setarea de reîncercare este configurată la 5 și dacă sistemul nu reușește să stabilească o conexiune după 5 încercări automate), Acțiunea ABBYY va trece la starea de "Închis".&#x20;

{% hint style="info" %}
Notă: Dacă Acțiunea nu se conectează cu serverul extern, aceasta va fi redirecționată către proprietarul cazului, indicând în secțiunea Acțiune din pagina de afișare a Cazului că această Acțiune a fost Închisă – nu nu se poate completa.
{% endhint %}

## Validarea

După ce scanează un document, ABBYY creează un scor bazat pe punctajul de încredere pe care îl are în calitatea scanării. În cazul în care punctajul de încredere este peste valoarea definită, atunci nu este necesară nicio verificare, datele vor fi procesate și se va finaliza sarcina. Dacă punctajul este sub o anumită valoare, este necesar ca scanarea să fie verificată manual.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### Nu este necesară nicio verificare <a href="#no-verification-required" id="no-verification-required"></a>

Un mesaj de status va confirma că nu este necesară validarea manuală:&#x20;

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FfNwi5staNIa5ej7A5125%2Fimage.png?alt=media\&token=40e83627-3b52-45b2-99e5-4aa9598f6d50)

După ce procesarea este finalizată, Acțiunea ABBYY se va închide. Fișierele exportate vor fi atașate la Caz și vor fi vizibile în lista Fișiere.

{% hint style="info" %}
Notă: dacă au fost setate „Etichetele pentru fișierele de ieșire”, ABBYY va aplica eticheta de ieșire tuturor fișierelor pe care le-a procesat, pentru a fi folosite în activitățile ulterioare.
{% endhint %}

### Este necesară verificarea manuală

Sistemul vă va avertiza dacă este necesară o verificare manuală:

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2F6HBtoPBieq2aPhf24X7I%2Fimage.png?alt=media\&token=257c2614-edad-47ce-a9db-727661dc15cc)

În plus, în dreptul statusului Acțiunii va fi afișat un mesaj de atenționare pentru a vă reaminti că trebuie efectuată o verificare manuală în ABBYY înainte de a continua.

Dacă faceți clic pe butonul „Verificare”, veți ajunge la Secțiunea de verificare ABBYY, unde puteți verifica scanările documentelor și modifica informațiile, dacă este necesar.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsuykc2DFaOX6-GsPY%2Fimage.png?alt=media\&token=27953730-e342-4885-9206-fae88572b769)

{% hint style="info" %}
Notă: Pentru a avea acces complet, este necesar un cont ABBYY FlexiCapture valid, cu permisiuni pentru a efectua verificări în proiectul ales.
{% endhint %}

Odată ce v-ați conectat, vi se va afișa ecranul Secțiunii de verificare ABBY FlexiCapture, unde puteți revizui și modifica informațiile, în funcție de caz.

Secțiunea de verificare este alcătuită din trei rubrici: 1.

1. Paginile individuale ale documentului care urmează să fie scanate.
2. Un prim-plan al documentului original care urmează să fie scanat.
3. Rezultat extras – așadar versiunea scanată a documentului original.

Textul marcat cu galben din secțiunea documentului original reprezintă datele imposibil de citit de către ABBYY. Acesta este marcat cu roșu în Rezultatul extras.

Anumite caractere, cum ar fi „i”, pot fi de asemenea marcate în secțiunea Rezultat extras dacă ABBYY nu prezintă certitudine privind copia scanată.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx6MLiLXtXFAmC00W%2Fimage.png?alt=media\&token=adebd784-bdf7-4f4c-b696-4832e40c4ec2)

După ce finalizați verificarea manuală, ecranul va confirma că aceasta a fost efectuată, dar va indica faptul că a apărut o eroare care a necesitat verificarea manuală:

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FaQfI2ewgBz3mcA0LPa9O%2Fimage.png?alt=media\&token=2b8c972f-aedf-42af-b056-c68efc3cb3a8)

‌La finalizarea procesării, fișierele exportate vor fi atașate la Caz și vor fi vizibile în [lista de Fișiere](https://docs.enate.net/enate-help/romana/tipuri-de-elemente-de-lucru-tichete-cazuri-si-actiuni/card-fisiere).

Apoi puteți bifa Acțiunea ca fiind finalizată.

{% hint style="info" %}
Notă: dacă au fost setate „Etichetele pentru fișierele de ieșire”, ABBYY va aplica eticheta de ieșire tuturor fișierelor pe care le-a procesat, pentru a fi folosite în activitățile ulterioare.
{% endhint %}
