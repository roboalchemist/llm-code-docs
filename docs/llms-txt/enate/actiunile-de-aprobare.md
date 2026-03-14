# Source: https://docs.enate.net/enate-help/romana/actiunile-de-aprobare.md

# Source: https://docs.enate.net/enate-help/romana/procesarea-unei-actiuni/actiunile-de-aprobare.md

# Acțiunile de aprobare

### Ce sunt acțiunile de aprobare? Cum funcționează acestea?

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==>" %}

Adesea, în cadrul fluxurilor de Caz din procesele de afaceri create, intervin momente în care este nevoie ca persoane externe (adică persoane care acționează în afara Enate - poate fi vorba de manageri de afaceri din cadrul companiei dvs. sau al companiei client relevante) să aprobe activitățile înainte ca procesele să poată continua. Procedurile de salarizare sunt un bun exemplu de astfel de procese, în care conducerea companiei client trebuie să aprobe rapoartele de salarizare pentru ca procesul să poată continua.&#x20;

Funcția de aprobare a fost creată cu scopul de a oferi asistență specifică pentru aceste situații în mod integrat, astfel încât „ciclul de aprobare” să se gestioneze în mod riguros și să fie vizibil în cadrul fluxului de activități din Enate.

### Cum funcționează acțiunile de aprobare în momentul execuției

Cererile de aprobare sunt trimise agenților care acționează în mod extern din Enate pentru a fi aprobate sau respinse.&#x20;

Există diferite tipuri de aprobare care influențează modul în care se ia decizia:&#x20;

* Într-un scenariu cu mai multe niveluri, se trimite e-mailul de solicitare la fiecare nivel nou după aprobarea cu succes a nivelului anterior, până la un maxim de 3 niveluri. Dacă este respins de oricare dintre utilizatori, aprobarea este refuzată. &#x20;
* Într-un scenariu paralel, se trimite e-mailul de solicitare tuturor celor care acordă aprobarea și se ia prima decizie. &#x20;
* Într-un scenariu paralel cu toate, se trimite e-mailul de solicitare tuturor celor care acordă aprobarea și TOȚI trebuie să aprobe pentru ca solicitarea să fie aprobată. Dacă oricare dintre ei o respinge, aprobarea este refuzată.&#x20;

Dacă cererea este aprobată de toate părțile necesare, acțiunea de aprobare este rezolvată cu succes și se va închide în mod automat, astfel încât niciun agent din Work Manager nu va trebui să o preia, însă Acțiunea închisă se poate vizualiza în orice moment făcând clic pe aceasta.&#x20;

### Excepții - când sunt gestionate de un agent în Work Manager

Există, totuși, anumite scenarii în care un agent din Work Manager ar putea fi nevoit să efectueze toate activitățile necesare pentru a procesa în continuare o acțiune de aprobare:&#x20;

* Aprobarea a fost refuzată &#x20;
* Nu s-a identificat automat niciun aprobator (sau aprobatori insuficienți)

### Cerere de aprobare refuzată

În cazul în care cererea de aprobare a fost refuzată, Acțiunea va trece în starea „De făcut” și, drept urmare, va trebui gestionată de către un agent în Work Manager. Acesta va trebui să verifice motivul respingerii furnizat de către autorul aprobării și să decidă cum să procedeze. Poate opta între următoarele variante:&#x20;

1. Să actualizeze cererea după cum este necesar și să o retrimită prin setarea Acțiunii în „Așteptare”. Această operațiune va trimite automat e-mailul de cerere a aprobării din nou\*\* și va plasa Acțiunea în starea de „În așteptare de informații suplimentare” - având în vedere că se așteaptă ca informațiile externe (un răspuns de aprobare) să fie înregistrate din nou în sistem înainte ca activitatea să poată continua.  &#x20;
2. Să marcheze Acțiunea drept Imposibil de finalizat. Astfel, proprietarul Cazului va fi notificat și va trebui să decidă cum să procedeze - poate să prelucreze din nou Cazul sau să îl închidă complet.&#x20;
3. Să marcheze Acțiunea ca Rezolvată, care va marca manual cererea ca fiind aprobată. Cazul va trece apoi la următoarea Acțiune.

{% hint style="info" %}
\*\*Rețineți: trimiterea e-mailurilor de cerere de aprobare va fi reluată de la început, adică toți solicitanții vor fi contactați din nou. Dacă aceștia vor face clic pe vreun e-mail trimis anterior, vor întâmpina un mesaj care îi va anunța că cererea de aprobare respectivă nu mai este valabilă (întrucât este posibil să se fi schimbat detaliile cererii).
{% endhint %}

### Număr insuficient de aprobatori

Dacă este necesar ca agentul să adauge aprobatori deoarece unul sau mai mulți aprobatori necesari nu sunt menționați (sau să facă modificări în urma cărora cererile de aprobare trebuie trimise din nou), agentul va prelua Acțiunea de aprobare în starea „De făcut”. Odată ce termină de făcut modificările și/sau de completat numele aprobatorilor care lipsesc, agentul trebuie să plaseze Acțiunea în starea de În așteptare. Imediat ce face acest lucru, se va trimite automat e-mailul de cerere a aprobării, iar apoi Acțiunea va trece în starea de „În așteptare de informații suplimentare”, întrucât se așteaptă informații externe (de aprobare) înainte de a continua.

{% hint style="info" %}
Rețineți: Când o acțiune de aprobare se află în starea „De făcut” sau „În curs de desfășurare”, părțile externe cărora li s-au trimis cereri de aprobare NU vor putea să le aprobe sau să le refuze. În schimb, aceștia vor primi un mesaj care îi va informa că articolul în cauză se află în curs de procesare. Agenții din Work Manager TREBUIE să treacă Acțiunea înapoi la starea „În așteptare de informații suplimentare” dacă doresc să reia activitatea de aprobare.
{% endhint %}

### Dacă cererile de aprobare expiră...

Este posibil ca acțiunea de aprobare să se închidă automat pentru că a expirat, întrucât nu s-au primit răspunsuri suficiente/ nu s-au primit la timp. Acțiunea se va seta automat ca fiind Rezolvată, iar Cazul va fi reluat. În acest context, nu va fi nevoie ca vreun agent din Work Manager să preia o Acțiune, deși Acțiunea închisă poate fi întotdeauna vizualizată printr-un simplu clic manual pe ea.
