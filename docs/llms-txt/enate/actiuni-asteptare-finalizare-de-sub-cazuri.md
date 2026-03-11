# Source: https://docs.enate.net/enate-help/romana/procesarea-unei-actiuni/actiuni-asteptare-finalizare-de-sub-cazuri.md

# Acțiunea "Așteptați finalizarea Cazurilor secundare"

Acțiunea "Așteptați finalizarea Cazurilor secundare" va aștepta ca un anumit caz secundar să se finalizeze înainte de a permite Cazului să treacă la următoarea acțiune.

Vă puteți da seama că o acțiune este una de tip "Așteptați finalizarea cazurilor secundare" deoarece în fișa informativă a acesteia se va menționa "Acțiunea așteaptă finalizarea cazurilor secundare".

Odată ce acțiunea "Așteptați finalizarea Cazurilor secundare" a fost inițiată ȘI cazul secundar pentru care a fost setată în așteptare a fost inițiat (fie manual, fie prin intermediul unei acțiuni "Începeți cazul"), acțiunea "Așteptați finalizarea cazurilor secundare" va trece în starea de "Așteptare".

Odată ce cazul secundar este finalizat, acțiunea "Așteptați finalizarea cazurilor secundare" se va închide automat.

Veți fi informat despre acest lucru și în cronologie.

Dacă cazul secundar pentru care acțiunea "Așteptați finalizarea cazurilor secundare" este setată să aștepte nu este disponibil - fie pentru că nu a fost inițiat, fie pentru că a fost rezolvat înainte ca acțiunea "Așteptați finalizarea cazurilor secundare" să fie inițiată, acțiunea respectivă va intra în starea "De făcut" și va fi atribuită unei cozi de așteptare, din care va fi preluată de un utilizator ce va decide cum să procedeze.

Dacă ulterior încercați să configurați acțiunea din "Așteptați finalizarea cazurilor secundare" ca fiind "În așteptare", acțiunea se va închide, deoarece cazul secundar pentru care a fost configurată să aștepte nu a fost inițiat.

Dacă acțiunea nu se află în starea de "Așteptați finalizarea cazurilor secundare" și cazul secundar pe care îl așteaptă a fost finalizat, în fișa informativă va apărea un mesaj cu mențiunea "Cazul secundar este finalizat".

Dacă rezolvați manual o acțiune "Așteptați finalizarea cazului secundar", acțiunea va fi marcată ca fiind rezolvată, deși cazul secundar nu a fost finalizat.

{% hint style="info" %}
Rețineți că, dacă sistemul este configurat să închidă automat o acțiune "Așteptați finalizarea cazului secundar" (consultați aici pentru mai multe informații despre cum să faceți acest lucru) și cazul secundar pe care acțiunea "Așteptați finalizarea cazurilor secundare" este setată să îl aștepte nu este disponibil, fie pentru că nu a fost inițiat, fie pentru că a fost rezolvat înainte ca acțiunea "Așteptați finalizarea cazurilor secundare" să fie inițiată, acțiunea va trece automat în starea Închis. Veți fi informat despre acest lucru în cronologie.
{% endhint %}
