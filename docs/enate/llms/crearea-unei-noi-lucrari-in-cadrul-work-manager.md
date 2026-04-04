# Source: https://docs.enate.net/enate-help/romana/crearea-unei-noi-lucrari-in-cadrul-work-manager.md

# Creare articol nou

Lucrarea poate fi creată de utilizatori în cadrul Work Manager în două moduri:

1. **Din „Creați articol de lucru nou”.** Acesta este un meniu derulant disponibil din bara de instrumente, agentul selectează un Caz sau un Tichet de început într-un context specific de afaceri.
2. **Din pagina „Activitate de contact”** , adesea denumită și Pagina de gestionare a apelurilor. Din această pagină, agentul de asistență caută mai întâi și găsește o persoană (adesea cineva care apelează la centrul de asistență) și apoi începe o lucrare directă pentru aceasta, adică un Tichet sau un Caz.

## Crearea de noi articole de lucru din lista derulantă „Creare articole de lucru noi”

Pentru a crea un articol de lucru, faceți clic pe link-ul „Creare” din bara de antet (imaginea în formă de cub). Se va afișa o secțiune a ecranului care permite crearea unui articol de lucru nou. În fereastra derulantă apare ordinea ierarhiei: Companie, Contract, Serviciu, Grupa de procese (dacă a fost configurată), apoi Cazurile care se pot crea.

Link-urile de intrare apar automat aici pentru Tichete și Cazuri atunci când ați creat un proces de Tichet sau Caz în Builder și l-ați setat pe Live. Făcând clic pe un link se va crea noul element de lucru într-o filă separată.

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEhH-dnBbM95bUBf0z%2F-MYEk7maY3OWhZPPG154%2FCreate-Work-Item.gif?alt=media\&token=1d97d13f-88ec-4b2f-b505-dd88d3156538)

{% hint style="info" %}
Notă: Când se rulează în Modul test, se vor afișa aici procesele care sunt în stare de „Ciornă validată”.
{% endhint %}

## Meniul derulant „ Începeți activitatea nouă” în pagina Activitate de contact <a href="#b-meniul-derulant-incepeti-activitatea-noua-in-pagina-activitate-de-contact" id="b-meniul-derulant-incepeti-activitatea-noua-in-pagina-activitate-de-contact"></a>

Link-urile de intrare generate automat vor apărea pe [pagina Activitate de contact](https://docs.enate.net/enate-help/romana/contacte/pagina-activitate-de-contact).

![](https://gblobscdn.gitbook.com/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEkWZ6buBtuWBZ8N3r%2F-MYEmC7zXzcavCD1pAwt%2FCreate-work-from-contact-activit.gif?alt=media\&token=c4cd6836-a55a-47fb-b302-d94716f09670)

Dacă sunteți pe o pagină de contact pentru cineva aflat într-o companie cunoscută (adică orientată la nivelul clientului), informațiile despre client nu vor fi afișate în acest nume de link. Căutare de text liber vă va permite să filtrați această listă de link-uri.

Administratorii pot controla dacă doriți să vedeți link-ul de intrare pentru un anumit proces de Tichet/Caz prin setările în Builder.

Crearea unui element de lucru din pagina de activitate a contactului va atribui automat contactul ca persoană de contact principală a elementului de lucru.

## Metode „Început prin/de” <a href="#metode-inceput-prin-de" id="metode-inceput-prin-de"></a>

Există diverse metode prin care poate fi creat un articol de lucru. Acestea pot fi văzute pe articolele de lucru și utilizate în scopuri diferite de afișare - de exemplu, pentru a fi afișate în coloanele grilei sau pentru a le căuta în ecranul Vizualizare. Posibilele metode „început de/prin” sunt după cum urmează:

* Flux de lucru - început de un alt articol de lucru ca parte a unui flux, de exemplu o Acțiune începută de un Caz.
* Manual - început de Agent în Work Manager
* Serviciu independent - început de o cerere de serviciu independent primită
* Robotică - Început de RPA Robot
* E-mail - început poștă primită
* Tichet – început de Tichet
* Creare în masă - fișier excel încărcat în masă
* Program - încărcat automat la data/ora specificată de un program de sistem.
