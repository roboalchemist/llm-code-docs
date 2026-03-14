# Source: https://docs.enate.net/enate-help/romana/e-mailuri/e-mailuri-primite-logica-de-procesare/gestionarea-e-mailurilor-primite-in-afara-biroului.md

# Gestionarea e-mailurilor primite în afara biroului

## Modul în care Enate gestionează e-mailurile din afara biroului

Enate gestionează e-mailurile primite „În afara biroului” în două moduri:

1. Dacă e-mailul „În afara biroului” este generat ca răspuns la primirea unui e-mail scris de un utilizator în Enate, Enate va anexa e-mailul „În afara biroului” la articolul de lucru și va marca articolul de lucru cu „informații noi primite”. Consultați mai jos pentru detalii suplimentare.
2. Dacă e-mailul „În afara biroului”este trimis ca răspuns la un e-mail generat automat de Enate (de exemplu, confirmarea creării unui Tichet), e-mailul „În afara biroului” NU va fi anexat la articolul de lucru și articolul de lucru nu va fi marcat cu „informații noi primite”- acesta va fi efectiv ignorat.

Să dezvoltăm mai departe logica situației 1 de mai sus, în care un e-mail „În afara biroului” este generat ca răspuns la primirea unui e-mail scris de un utilizator în Enate...

## E-mailuri primite în afara biroului, asociate cu un articol de lucru existent în curs de desfășurare

Dacă e-mailul „În afara biroului” care intră aparține unui Tichet, Caz sau unei Acțiuni existente în stare de CIORNĂ, DE FĂCUT sau ÎN PROGRES, sistemul efectuează următoarele operațiuni:

* va anexa e-mailul la articolul de lucru
* va marca articolul de lucru cu „informații noi primite”

Rețineți: Această logică se aplică tuturor e-mailurilor de intrare generate automat care sunt asociate cu un articol de lucru existent în stare de CIORNĂ, DE FĂCUT sau ÎN PROGRES (e-mailurile primite în afara biroului sunt tratate exact în același mod ca și alte e-mailuri de intrare generate automat în aceste stări). Consultați această [secțiune ](https://docs.enate.net/enate-help/romana/e-mailuri/e-mailuri-primite-logica-de-procesare/..#gestionarea-inteligenta-de-detectare-a-e-mailurilor-generate-automat)pentru mai multe informații despre modul în care sistemul detectează e-mailurile generate automat.

## Email-uri primite în afara biroului, asociate unui articol de lucru în stare de Așteptare

Dacă e-mailul de intrare „În afara biroului” este asociat cu un articol de lucru existent care se află în starea de AȘTEPTARE, sistemul va realiza următoarele operațiuni:

* va anexa e-mailul la articolul de lucru
* va marca articolul de lucru cu „informații noi primite”

În plus, dacă tipul de așteptare este „În așteptare de informații suplimentare”, sistemul acționează astfel:

* va schimba starea articolului de lucru din AȘTEPTARE în DE FĂCUT
* Ca urmare a schimbării stării în DE FĂCUT, se va seta o Coadă de așteptare și un destinatar pentru articolul de lucru, iar acesta va reveni în Inbox-ul agentului responsabil, care va fi marcat cu „informații noi primite”
* Dacă articolul de lucru este o Acțiune și atât Acțiunea, cât și Cazul principal se află în starea de AȘTEPTARE având tipul de așteptare „În așteptare de informații suplimentare”, starea Cazului principal se va modifica ÎN PROGRES

Aceleași reguli se aplică și în cazul altor e-mailuri de intrare generate automat care sunt asociate cu un articol de lucru existent aflat în starea de Așteptare sau În așteptare de informații suplimentare (e-mailurile primite în afara biroului sunt tratate exact în același mod ca și alte e-mailuri primite generate automat în această stare). Consultați această [secțiune ](https://docs.enate.net/enate-help/romana/e-mailuri/e-mailuri-primite-logica-de-procesare/..#gestionarea-inteligenta-de-detectare-a-e-mailurilor-generate-automat)pentru mai multe informații despre modul în care sistemul detectează e-mailurile generate automat.

## E-mailuri primite în afara biroului, asociate unui articol de lucru în stare de Rezolvat (Cazuri și Tichete)

Dacă e-mailul primit „În afara biroului” este asociat cu un articol de lucru existent care se află în starea de REZOLVAT (rețineți că numai Cazurile și Biletele se pot afla în starea de REZOLVAT), sistemul va realiza următoarele operațiuni:

* Va anexa e-mailul la articolul de lucru
* Va redeschide articolul de lucru și îl va reseta în starea DE FĂCUT
* Ca urmare a schimbării stării în DE FĂCUT, se va seta o Coadă de așteptare și un destinatar pentru articolul de lucru, iar acesta va reveni în Inbox-ul agentului responsabil, care va fi marcat cu „informații noi primite”

Aceleași reguli se aplică și în cazul altor e-mailuri de intrare generate automat care sunt asociate cu un articol de lucru existent aflat în starea de REZOLVAT (e-mailurile primite în afara biroului sunt tratate exact în același mod ca și alte e-mailuri primite generate automat în această stare). Consultați această [secțiune ](https://docs.enate.net/enate-help/romana/e-mailuri/e-mailuri-primite-logica-de-procesare/..#gestionarea-inteligenta-de-detectare-a-e-mailurilor-generate-automat)pentru mai multe informații despre modul în care sistemul detectează e-mailurile generate automat.

## E-mailuri primite în afara biroului, asociate unui articol de lucru în stare de Închis

Dacă e-mailul primit „În afara biroului” este asociat cu un articol de lucru existent care se află în starea de ÎNCHIS, sistemul poate acționa în diferite moduri, în funcție de tipul articolului de lucru:

* În primul rând, sistemul se va deplasa „ascendent” pentru a căuta un articol de lucru principal, de ex.
  * dacă e-mailul este asociat cu o Acțiune care se află în starea de ÎNCHIS, sistemul va analiza Cazul principal al Acțiunii să verifice dacă acesta este încă deschis.
  * dacă e-mailul este asociat cu un Caz care se află în starea de ÎNCHIS, sistemul va verifica dacă acest Caz are un Caz sau un Tichet principal rămas deschis.
* dacă e-mailul este asociat cu un Tichet care se află în starea de ÎNCHIS, sistemul va verifica dacă acest Tichet are un Tichet principal rămas deschis.
* Dacă există un articol de lucru principal care a rămas deschis, sistemul va aplica logica de gestionare a e-mailurilor pentru articolul de lucru principal (și anume, logica descrisă în secțiunile de mai sus referitoare la articolele de lucru în curs de desfășurare).
* Dacă sistemul nu identifică un articol de lucru principal care să fie încă deschis, e-mailul primit NU va fi anexat la articolul de lucru deja închis. În schimb, se va crea un nou articol de lucru, [respectând regulile de mai jos](#cazuri-in-care-nu-se-poate-stabili-o-legatura-intre-un-e-mail-primit-in-afara-biroului-si-un-articol) cu privire la situațiile în care sistemul nu reușește să asocieze un e-mail cu un articol de lucru existent.

Aceleași reguli se aplică și în cazul altor e-mailuri de intrare generate automat care sunt asociate cu un articol de lucru existent aflat în starea de ÎNCHIS (e-mailurile primite în afara biroului sunt tratate exact în același mod ca și alte e-mailuri primite generate automat în această stare). Consultați această [secțiune ](https://docs.enate.net/enate-help/romana/e-mailuri/e-mailuri-primite-logica-de-procesare/..#gestionarea-inteligenta-de-detectare-a-e-mailurilor-generate-automat)pentru mai multe informații despre modul în care sistemul detectează e-mailurile generate automat.

## Cazuri în care nu se poate stabili o legătură între un e-mail primit în afara biroului și un articol de lucru existent

În cazul în care nu se poate identifica nicio informație care să facă legătura între e-mailul primit „În afara biroului” și un articol de lucru în curs de desfășurare, sistemul va genera un articol de lucru complet nou ( Tichet sau Caz) pe baza regulilor de direcționare configurate pentru e-mail.

La crearea unui Tichet, chiar dacă setările de direcționare a e-mailurilor specificate în Builder au opțiunea de „Trimitere răspuns” activată, NU se va trimite automat un e-mail de confirmare la adresa de e-mail de la care a provenit e-mailul „În afara biroului”, deoarece opțiunea „Dezactivare e-mailuri automate” va fi activată automat.
