# Source: https://docs.enate.net/enate-help/romana/e-mailuri/e-mailuri-negestionate/creare-de-noi-rute-de-e-mail-din-e-mailuri-negestionate.md

# Creare de noi rute de e-mail din e-mailuri negestionate

Ca parte a procesului de procesare a mesajelor de e-mail negestionate, utilizatorii pot configura rutarea e-mailurilor direct din Work Manager. Aceste reguli previn ca e-mailurile ulterioare să fie considerate e-mailuri negestionate, astfel încât să se garanteze crearea unui Tichet sau a unui Caz pentru fiecare dintre ele. În acest mod, se reduce volumul de e-mailuri negestionate și se poate începe mai repede activitatea referitoare la respectivele e-mailuri. Pentru a asigura un anumit control, capacitatea utilizatorilor din Work Manager de a crea noi rute de e-mail este o opțiune care poate fi activată/dezactivată în Rolurile de utilizator din Builder.

Îndată ce aceste reguli se creează în Work Manager, ele devin instantaneu active și funcționale; totuși, utilizatorii din Builder vor fi notificați cu privire la orice noi reguli de rutare create în acest mod, acestea rămânând marcate până când administratorul le confirmă. Administratorii vor avea în continuare posibilitatea de a ajusta sau chiar dezactiva astfel de reguli după evaluare.

## Accesul acordat utilizatorilor din Work Manager pentru a crea noi rute de e-mail

Funcția de Acces pentru crearea de noi rute de e-mail în Work Manager este controlată prin intermediul sistemului de Roluri de utilizator din Enate, cu o nouă opțiune adăugată la secțiunea Opțiuni de vizualizare a e-mailurilor.

{% hint style="info" %}
Rețineți: Acest acces la "Creare rute de e-mail" va fi setat ca fiind **ACTIVAT** pentru rolul Standard de membru al echipei
{% endhint %}

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FTRRTTfcIx2NOkSU86II3%2Fimage.png?alt=media&#x26;token=02bc5073-4d1f-4c93-90af-5165b5ff5e67" alt=""><figcaption></figcaption></figure>

## Cum se creează o nouă rută de e-mail în E-mailuri negestionate

La preluarea unui e-mail negestionat în secțiunea E-mailuri negestionate din secțiunea de e-mailuri primite, dacă decideți să transformați e-mailul într-un Tichet / Caz (prin bifarea opțiunii „Articol de lucru nou”), se va afișa următoarea fereastră pop-up:

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FxB2LSN28AH3qz5F3Cu7m%2Fimage.png?alt=media&#x26;token=021f0965-55ce-4428-ae15-bf69adca354d" alt=""><figcaption></figcaption></figure>

Puteți realiza o căutare după ruta de e-mail (care va completa automat câmpurile Client/Contract/Serviciu/Proces pe baza sugestiilor referitoare la cutia poștală selectată) sau puteți efectua o selecție manuală. Dacă faceți clic pe opțiunea Creare, se va crea un anumit Tichet sau Caz din e-mail, conform procedurii normale.

Dacă *de asemenea* doriți ca acest lucru să se întâmple în mod automat și permanent, faceți clic pe link-ul „Aplicați la alte e-mailuri” din partea de jos a ferestrei pop-up înainte de a apăsa „Creare”. În cazul în care selectați această opțiune, la apăsarea butonului „Creare” se vor întâmpla două lucruri:

* Va apărea un scurt mesaj de confirmare a creării unui articol de lucru nou.
* În continuare, se va deschide o fereastră pop-up cu mențiunea „Creare nouă regulă de rutare a e-mailurilor”, în care veți putea completa restul detaliilor regulii de rutare înainte de a confirma crearea acesteia.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FdapkqqbETdnvVu0IRn9m%2Fimage.png?alt=media&#x26;token=18e3cd6e-f89c-4c62-bd7d-75e0c0093cbf" alt=""><figcaption></figcaption></figure>

Puteți decide dacă traseul va fi de tip „Către” sau „De la”, și anume

* „Tratează toate e-mailurile DE LA această adresă în același mod”, SAU
* &#x20;„Tratează toate e-mailurile Către *această* adresă în același mod”

și apoi ce adresă de e-mail va fi utilizată împreună cu aceasta. Enate va completa automat adresa de e-mail cu adresa de e-mail corespunzătoare asociată cu e-mailul neprocesat la care ați lucrat.

{% hint style="info" %}
În secțiunea „Sugestii” din această fereastră, se găsește un link către pagina E-mailuri negestionate din ajutorul online Enate, în cazul în care utilizatorii au nevoie de informații suplimentare.
{% endhint %}

## Aplicarea Regulii la un e-mail existent (Executare retrospectivă)

Pe lângă setarea unei reguli care va gestiona toate e-mailurile corespunzătoare acestui tipar, puteți opta, de asemenea, ca această regulă să fie executată în raport cu toate/unele dintre e-mailurile existente care corespund acestei reguli și care nu au fost gestionate. În acest caz, selectați opțiunea „Aplicare automată” și activați acest buton din fereastra pop-up.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2F5SmvtkitKyC3Sf4BOe0Z%2Fimage.png?alt=media&#x26;token=64db6a2b-5a39-4ef7-8ff8-0fab61093408" alt=""><figcaption></figcaption></figure>

Sistemul va afișa câte dintre e-mailurile negestionate actuale corespund regulii, respectiv câte vor fi reprocesate.

**Alegeți un interval de timp pentru a determina e-mailurile negestionate care trebuie reprocesate.**

Dacă selectați această opțiune, se va afișa un filtru cronologic prin care puteți selecta un subgrup de e-mailuri existente pentru care să executați regula (dacă, de ex., doriți să aplicați regula numai pentru e-mailuri vechi de o săptămână/lună etc.).

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FAtp2UqVvxLHKYsFvnKxy%2Fimage.png?alt=media&#x26;token=2dc2d063-59ad-44b1-acd2-a8b46c5b5fe4" alt=""><figcaption></figcaption></figure>

Cu ajutorul cursorului puteți seta diferite intervale de date, inclusiv date specifice. Pe măsură ce modificați această setare, sistemul se va actualiza pentru a reflecta numărul de e-mailuri pentru care ar trebui executată regula.

Odată finalizată selecția, apăsați butonul Creare - regula va fi reluată, iar mesajele de e-mail vor începe să fie reprocesate în tipul de Caz sau Tichet indicat de dvs.

{% hint style="info" %}
Atenție: Odată ce creați o nouă regulă de rutare a e-mailurilor prin intermediul Work manager, aceasta va fi activată instantaneu și se va aplica la toate e-mailurile primite ulterior.
{% endhint %}

## Vizibilitatea administratorului pentru noile reguli de rutare a e-mailurilor în Builder

Dacă s-au creat noi rute de e-mail în secțiunea E-mailuri negestionate din Work Manager, administratorii vor fi informați de acest lucru în Builder printr-un punct roșu afișat în pictograma E-mail.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FlYTZzLveOgAVvIig9pF2%2Fimage.png?alt=media&#x26;token=3df97a53-2291-4d07-878f-f37c602d23ef" alt=""><figcaption></figcaption></figure>

În toate secțiunile și ecranele de navigare ulterioare, pe măsură ce aceștia coboară la rubrica Rute de e-mail, vor fi indicate în permanență noile reguli de rutare care trebuie cunoscute.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FnJJDP2N0nFhOx36Du7z7%2Fimage.png?alt=media&#x26;token=d2aaf8ea-d017-4d90-9465-a517a8e6758a" alt=""><figcaption></figcaption></figure>

Odată accesată pagina Rute, un banner va informa utilizatorii cu privire la noile rute de e-mail care trebuie cunoscute, precum și cu privire la numărul acestora. Prin intermediul unui link, aceștia vor putea filtra rutele pentru a le selecta doar pe cele noi de care trebuie să fie la curent.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FrCwfEMyzU7BDe5MEKiZc%2Fimage.png?alt=media&#x26;token=95972c44-f767-4918-aeaa-62b6fb855f78" alt=""><figcaption></figcaption></figure>

În cadrul tabelului de rute, fiecare utilizator va fi avertizat cu privire la aceste rute noi pe care trebuie să le cunoască.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FnHBMhC5QQYYG0fwV0rNF%2Fimage.png?alt=media&#x26;token=112a83c8-656e-4d24-8c29-30a46068f9c7" alt=""><figcaption></figcaption></figure>

Administratorii pot examina aceste noi reguli de rutare (și să vorbească cu agentul care le-a creat\*) pentru a se asigura că acestea funcționează în combinație cu celelalte reguli. Pot alege să le dezactiveze din funcțiune, să efectueze modificări și chiar să le elimine, dacă consideră necesar.

Dacă sunt mulțumiți cu regula respectivă, trebuie debifată opțiunea „a se modifica”. Pot accesa link-ul „Eliminați filtrul de revizuire” din antet pentru a reveni la vizualizarea normală.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2F2hLMr3koQBuFAYDFy4Os%2Fimage.png?alt=media&#x26;token=9ae361e6-1121-4449-acc1-e7323b08b2e8" alt=""><figcaption></figcaption></figure>

\*Puteți vizualiza cine a creat o regulă de rutare a e-mailurilor prin pictograma „Afișare activitate” din partea de sus a ferestrei cu informații privind regula respectivă.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FIO6viSDVdQk5WsjMbdCi%2Fimage.png?alt=media&#x26;token=1b4bcde7-9999-4407-9288-360a833c797d" alt=""><figcaption></figcaption></figure>

Dacă faceți clic pe aceasta, va apărea istoricul de verificare a persoanei care a creat și a actualizat regula respectivă.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FztZ6bBPiwSz9fH2Q6yRX%2Fimage.png?alt=media&#x26;token=6040e208-4832-4a90-9299-6387a6b95325" alt=""><figcaption></figcaption></figure>
