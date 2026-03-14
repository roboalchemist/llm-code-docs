# Source: https://docs.enate.net/enate-help/romana/e-mailuri/e-mailuri-primite-logica-de-procesare.md

# E-mailuri primite - Logica de procesare

## **Cum se atribuie un e-mail primit în Enate?**

La sosirea de noi e-mailuri în Enate, sistemul analizează e-mailul pentru a determina dacă este o cerere nouă sau dacă este asociată uneia deja existente, după care stabilește procesarea acestora.

Astfel, sistemul va examina în ordine mai multe criterii diferite și, dacă va găsi o potrivire, se va opri din căutare (altfel spus, primul rezultat câștigă). Ordinea în care se realizează acest proces este următoarea:

**1) Valoarea datelor furnizate în antetul e-mailului (de răspuns)**. Această valoare are următoarea structură:

<”E-mail unic GUID'.”articol de lucru GUID”@”Serverul Enate care a trimis e-mailul”.enate>.

De exemplu: \<d23a9d57-6006-4ab7-a412-8ca8ece2f3aa.2b8586bb-ef95-4020-9cf8- <ed56a059b47e@TrimitereNumeServer.enate>>

**2) Identificator unic în conținutul mesajului** - Dacă e-mailul primit a fost trimis ca răspuns la un e-mail care a fost trimis prin Enate, acesta va conține probabil un identificator unic ca parte a conținutului de e-mail.

**3) Referința articolului de lucru în subiectul e-mailului**

**4) Referința articolului de lucru în conținutul mesajului de e-mail**

## Atribuirea unui e-mail la un articol de lucru existent, aflat în derulare

Dacă identifică o potrivire cu un Tichet, un Caz sau o Acțiune existentă care se află în stadiul de CIORNĂ, DE FĂCUT sau ÎN DERULARE, sistemul va proceda astfel:

* va anexa e-mailul la articolul de lucru respectiv
* va marca articolul de lucru cu ”informații noi primite”

Același lucru este valabil și pentru mesajele de e-mail generate automat care se potrivesc cu un articol de lucru existent în stare de CIORNĂ, DE FĂCUT sau ÎN DERULARE. Vă rugăm să consultați [secțiunea de mai jos](#detalii-suplimentare) pentru mai multe informații despre modul în care sistemul detectează e-mailurile generate automat.

## Atribuirea unui e-mail la un articol de lucru aflat în stare de Așteptare

Dacă  un e-mail primit se potrivește cu un articol de lucru existent care se află în stare de AȘTEPTARE, sistemul va proceda astfel:

* va anexa e-mailul la articolul de lucru respectiv
* va marca articolul de lucru cu ”informații noi primite”

În plus, dacă tipul de Așteptare este ”În așteptare de informații suplimentare”, sistemul va efectua următoarele operațiuni:

* va schimba starea articolului de lucru din AȘTEPTARE în DE FĂCUT.&#x20;
* Ca urmare a modificării stării în DE FĂCUT, se vor seta o Coadă de așteptare și un destinatar pentru articolul de lucru și acesta va reveni în Inbox-ul activității al agentului responsabil, fiind marcat cu „informații noi primite”.
* dacă articolul de lucru este o Acțiune și atât Acțiunea, cât și Cazul principal se află în starea de AȘTEPTARE cu mențiunea de ”În așteptare de informații suplimentare”, starea Cazului principal se va modifica și va deveni ÎN DERULARE

Aceleași reguli se aplică și în cazul e-mailurilor generate automat care corespund unui articol de lucru existent aflat într-o stare de Așteptare sau În așteptare de informații suplimentare. Vă rugăm să consultați [secțiunea de mai jos](#detalii-suplimentare) pentru mai multe informații despre modul în care sistemul detectează e-mailurile generate în mod automat.

## Atribuirea unui e-mail la un articol de lucru Rezolvat (Caz și Tichet)

Dacă un e-mail primit este asociat unui articol de lucru existent care se află în starea de REZOLVAT (rețineți că numai Cazurile și Tichetele pot fi într-o stare de REZOLVAT), sistemul va efectua următoarele operațiuni:

* va anexa e-mailul la articolul de lucru respectiv
* va redeschide articolul de lucru și îl va seta din nou la starea DE FĂCUT.&#x20;
* Ca urmare a schimbării în starea DE FĂCUT, se va stabili o coadă de așteptare și un destinatar pentru articolul de lucru, iar acesta va reveni în Inbox-ul Enate al utilizatorului desemnat, și va fi marcat cu ”informații noi primite”.

Aceleași reguli se aplică și în cazul e-mailurilor generate automat care corespund unui articol de lucru existent aflat în starea de REZOLVAT. Vă rugăm să consultați [secțiunea de mai jos](#detalii-suplimentare) pentru mai multe informații despre modul în care sistemul detectează e-mailurile generate în mod automat.

## Trimiterea unui e-mail către un articol de lucru Închis

Dacă un e-mailul primit este asociat cu un articol de lucru existent care se află în starea de ÎNCHIS, sistemul poate acționa în diferite moduri, în funcție de tipul articolului de lucru:

* • În primul rând, sistemul se va deplasa „ascendent” pentru a căuta un articol de lucru principal, astfel:
  * dacă e-mailul este asociat cu o Acțiune care se află în starea de ÎNCHIS, sistemul va analiza Cazul principal al Acțiunii să verifice dacă acesta este încă deschis.
  * dacă e-mailul este asociat cu un Caz care se află în starea de ÎNCHIS, sistemul va verifica dacă acest Caz are un Caz sau un Tichet principal rămas deschis.
  * odacă e-mailul este asociat cu un Tichet care se află în starea de ÎNCHIS, sistemul va verifica dacă acest Tichet are un Tichet principal rămas deschis.
* ·        Dacă sistemul *identifică* un articol de lucru principal care a rămas deschis, va aplica logica de gestionare a e-mailurilor pentru articolul de lucru principal (și anume, logica descrisă în secțiunile de mai sus referitoare la articolele de lucru în curs de desfășurare).
* Dacă sistemul *nu poate* identifica un articol de lucru principal care să fie încă deschis, e-mailul primit NU va fi anexat la articolul de lucru deja închis. În schimb, se va crea un articol de lucru nou urmând [regulile de mai jos](#ce-se-intampla-daca-nu-se-poate-atribui-un-e-mail-la-un-articol-de-lucru-existent) referitoare la cazurile în care sistemul nu poate asocia un e-mail la un articol de lucru existent, și se vor copia toate informațiile (comunicări, fișiere, contacte etc.) din articolul de lucru închis în noul articol de lucru.

## Ce se întâmplă dacă nu se poate atribui un e-mail la un articol de lucru existent

Dacă nu se poate identifica nicio informație care să stabilească o legătură între un e-mail și un articol de lucru în derulare, sistemul va genera un articol de lucru complet nou (fie Tichet sau Caz) pe baza regulilor de redirecționare configurate pentru e-mailuri. Un e-mail de confirmare va fi înapoiat în mod automat la adresa de e-mail solicitantă, cu numărul de referință, dacă setările de redirecționare a e-mailurilor specificate în Builder au opțiunea ”trimitere răspuns” setată ca ”activată”.

## Detalii suplimentare

* **Tichet Divizat** – dacă un e-mail este asociat unui Tichet divizat, fie că este vorba de Tichetul original care a fost divizat sau de unul dintre Tichetele secundare în care acesta s-a divizat, e-mailul va fi anexat la fiecare dintre Tichetele SECUNDARE. Sistemul va aplica apoi gestionarea inteligentă de procesare a e-mailurilor la fiecare dintre Tichetele secundare, în mod individual.
* **Tichet Fuzionat** - dacă un e-mail este asociat unui Tichet fuzionat, fie că este vorba de unul dintre Tichetele principale care au fost fuzionate sau de Tichetul ”țintă” în care s-au fuzionat, e-mailul va fi anexat la Tichetul ”țintă”. Sistemul va aplica apoi gestionarea inteligentă de procesare a e-mailurilor la Tichetul ”țintă”.
* **Tichet convertit într-un Caz** – dacă un e-mail este asociat unui Tichet care a fost Rezolvat prin conversia într-un Caz, e-mailul va fi anexat la Cazul respectiv. Sistemul va aplica apoi gestionarea inteligentă de procesare a e-mailurilor la acel Caz.&#x20;

## Gestionarea inteligentă de detectare a e-mailurilor generate automat

Sistemul detectează e-mailurile generate automat prin unul sau mai multe dintre următoarele criterii:

* Există un antet de « x-răspuns automat »
* Există un antet de « x-replică automată »
* Există un antet de « trimitere automată iar valoarea este fie « generat automat », fie « răspuns automat»
* Există un antet de « tip conținut », iar valoarea este fie « raport/multipartit », fie « stare livrare »
* Există un antet numit ”Returnează ruta de acces”, a cărui valoare este « <> » sau « <<>> »
