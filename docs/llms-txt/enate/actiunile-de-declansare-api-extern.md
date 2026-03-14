# Source: https://docs.enate.net/enate-help/romana/procesarea-unei-actiuni/actiunile-de-declansare-api-extern.md

# Acțiuni de „Declanșare IPA extern”

Ca și alte prototipuri de acțiune, acțiunile de „Declanșare IPA extern” pot fi utilizate în cadrul Cazurilor și sunt folosite atunci când trebuie să apelați automat la un alt sistem, să-i transmiteți date și, eventual, să determinați sistemul extern să transmită date personalizate actualizate înapoi în Enate.&#x20;

Pentru informații despre cum să configurați acțiunile de „Declanșare IPA extern”, consultați această secțiune din [Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab).&#x20;

Uneori pot apărea întârzieri în așteptarea unui răspuns din partea sistemului extern. Dacă se întâmplă ca acțiunea de „Declanșare IPA extern” să aștepte un răspuns de la un sistem extern, fișa informativă a Acțiunii va apărea în Work Manager ca fiind „În așteptare”.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdIBzKCBFELItvgF6IQ%2F-MdICQ6--nMXmTFoQhoY%2Fimage.png?alt=media\&token=66a938b8-1fb4-49c6-b8cf-bfa801615ef2)

Când sistemul extern transmite în cele din urmă actualizarea datelor către Enate, o va face cu un marcaj care va preciza dacă a fost un rezultat pozitiv SAU negativ:

#### Răspuns cu rezultat pozitiv

În cazul în care sistemul răspunde cu un rezultat pozitiv, Acțiunea va trece automat în starea de „Închis”, cu o metodă de rezoluție de „Realizat cu succes”.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FQ1TQlHdwADqdqCkl0J30%2Fimage.png?alt=media\&token=db996134-d5b7-4009-aba1-35ec5c9ac6fd)

#### Răspuns cu rezultat negativ

În cazul în care sistemul răspunde cu un rezultat pozitiv, Acțiunea va trece în starea „De făcut”, cu motivul „Actualizat prin integrare”. IPA-ul extern poate răspunde, de asemenea, cu informații suplimentare privind motivul pentru care rezultatul a fost negativ. Aceste informații vor fi afișate în fișa de Informații a Acțiunii în secțiunea „Motiv respins”.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FoAOBdeUoTmKCzCQnPbDX%2Fimage.png?alt=media\&token=b9a2a99e-001f-46b1-acd1-a063902eb887)

Dacă Acțiunea nu a avut succes deoarece nu s-a finalizat în timpul stabilit pentru aceasta ([configurat în Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab)), atunci aceasta se va muta în starea „De făcut ” cu motivul „Timp expirat” și va fi alocată unei cozi de așteptare/unei persoane, pe baza regulilor de alocare configurate.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2F34t4rrASUwLngmInEoMc%2Fimage.png?alt=media\&token=6afdc185-6afd-44b8-a32b-525de24d0832)

Astfel de Acțiuni nereușite se vor manifesta în mod efectiv ca o acțiune manuală standard.

{% hint style="info" %}
Vă rugăm să rețineți că proprietarul Cazului NU va fi notificat în astfel de situații.
{% endhint %}

### Reîncercări automate

Dacă Acțiunea nu se poate conecta la sistemul extern, va reîncerca sistematic să se conecteze de multiple ori, în funcție de configurările sistemului dvs. din Builder (vedeți [aici ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)mai multe informații). De asemenea, pe pagina de afișare a Acțiunii va apărea o bară de mesaje de eroare, precizând:

* când s-a produs eroarea
* când se va încerca din nou stabilirea unei conexiuni în mod automat de către sistem
* de câte ori s-a încercat stabilirea unei conexiuni în mod automat de către sistem și
* numărul de încercări automate de restabilire a conexiunii efectuate de către sistem. De

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdIBzKCBFELItvgF6IQ%2F-MdIClMeYKTCgkVUzyGl%2Fimage.png?alt=media\&token=0a281965-6988-4ed5-92f8-8a92553ec147)

De asemenea, puteți reîncerca manual stabilirea unei conexiuni de aici, făcând clic pe link-ul „Reîncercare” din mesajul de eroare.

{% hint style="info" %}
Vă rugăm să rețineți că atunci când efectuați o reîncercare manuală, aceasta va fi considerată ca o tentativă de reîncercare și, astfel, va fi inclusă în numărul de reîncercări automate ale sistemului.
{% endhint %}

Dacă, în urma reîncercărilor automate, Acțiunea nu reușește să stabilească o conexiune (de exemplu, dacă limita de reîncercare este setată la 5 și nu se stabilește o conexiune în urma a 5 reîncercări automate), aceasta va trece la starea de „Închis”, cu o metodă de rezolvare de tipul „Nu se poate completa”.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdIBzKCBFELItvgF6IQ%2F-MdICW2uUyU9f6wQlle-%2Fimage.png?alt=media\&token=b0058210-7c09-44d9-9098-c0371c769460)

{% hint style="info" %}
În aceste condiții, în care Acțiunea nu stabilește o legătură cu sistemul extern, aceasta va fi redirecționată către Proprietarul cazului și, în secțiunea Acțiune din cadrul Cazului, se menționează că această Acțiune a fost Închisă – Nu se poate completa.
{% endhint %}

În momentul în care Acțiunea primește informațiile necesare, aceasta se va închide automat.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FAflAUkFXNT7IqEaVlunf%2Fimage.png?alt=media\&token=34b0bd73-504b-481b-9555-6945a3f65338)

#### Modificarea setărilor de reîncercare din Builder în timpul/ după ce s-au demarat reîncercările

Dacă setarea de reîncercare automată din Builder este modificată după ce sistemul a reîncercat automat să stabilească o conexiune cu un sistem extern, vor apărea următoarele situații:

Dacă, de exemplu, limita de reîncercare a fost setată inițial la 5, iar sistemul a reîncercat automat stabilirea conexiunii de 5 ori și a eșuat, Acțiunea va trece la starea de „Închis”, cu un mesaj de eroare ce indică un număr de 5/5 reîncercări.&#x20;

Dacă limita este apoi schimbată peste 5, de exemplu la 7, mesajul de eroare va indica un număr de 5/7 reîncercări, dar sistemul NU va reîncerca automat să stabilească o conexiune pentru a 6-a și a7-a dată deoarece Acțiunea va fi fost deja închisă.&#x20;

Totuși, dacă Acțiunea nu a apucat sa intre în starea de „Închis” deoarece limita maximă de reîncercări automate nu a fost atinsă (de exemplu, dacă s-a încercat doar de 4 ori din totalul de 5), atunci mărirea limitei de reîncercări la 7 va permite Acțiunii sa reîncerce stabilirea conexiunii automat până la atingerea limitei de 7.&#x20;

În schimb, dacă se reduce limita după ce au început încercările, de exemplu, dacă se reîncearcă de 4 ori din 10, dar apoi se reduce maximul la 4, sistemul va afișa în continuare 4 din 10, dar va fi de fapt închis.
