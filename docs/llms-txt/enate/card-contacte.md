# Source: https://docs.enate.net/enate-help/romana/contacte/card-contacte.md

# Etichete de contact

Etichetele de contact se folosesc pentru a asocia contactele cu articolele de lucru.

## Etichete implicite configurate de sistem

Etichetele implicite de contact configurate de sistem sunt următoarele:

* **Contact principal** - utilizatorul principal cu care colaborați referitor la această cerere. Nu poate exista decât un singur Contact principal pentru un articol de lucru. Această rubrică este obligatorie pentru Tichete. În funcție de configurația Cazului în Builder, aceasta poate fi sau nu obligatorie pentru Cazuri (dacă este setată ca obligatorie după tipul de Caz, este obligatorie și pentru Acțiunile acelui Caz).
* **Solicitant inițial** - persoana care a inițiat solicitarea. Nu poate exista decât un singur Solicitant inițial pentru un articol de lucru, iar acesta este independent de eticheta „Solicitant”. Solicitantul inițial va fi setat automat în situația în care o persoană de contact validă trimite e-mailul de inițiere a articolul de lucru; în caz contrar, se va promova la „Solicitant inițial” prima persoană care a fost setată manual ca „Solicitant”. Eticheta de „Solicitant inițial” nu poate fi modificată odată ce este setată și nu puteți elimina persoana de contact etichetată ca „Solicitant inițial” din articolul de lucru.
* **Solicitant** - persoana care solicită cererea aferentă. Nu poate exista decât un singur Solicitant pentru un articol de lucru. Această rubrică este obligatorie pentru Tichete. În funcție de configurația Cazului în Builder, aceasta poate fi sau nu obligatorie pentru Cazuri (dacă este setată ca obligatorie după tipul de Caz, este obligatorie și pentru Acțiunile acelui Caz).
* **Subiect** – utilizatorul la care se referă articolul de lucru (poate fi niciunul dintre articolele menționate anterior). Nu poate exista decât un singur Subiect pentru un articol de lucru.

Deseori, toate trei vor fi aceeași persoană. Dacă etichetați un alt contact cu aceste tipuri de etichete implicite configurate de sistem, eticheta contactului anterior va fi eliminată - deoarece nu poate exista decât un singur titular al contactelor implicite din sistem într-un articol de lucru.

Dacă adăugați manual primul contact la un articol de lucru, acesta va fi setat în mod implicit drept Contact principal, Solicitant și Subiect. Ulterior, puteți reatribui manual aceste etichete altor utilizatori.

* **CC** - orice alte contacte care pot fi incluse în corespondență. Dacă un contact este etichetat doar ca „CC”, acesta va fi afișat în secțiunea separată CC (care va rămâne ascunsă până când vor exista doar contacte CC pentru articolul de lucru).

## Setarea implicită a etichetelor suplimentare la înregistrarea de contacte

Pe lângă etichetele implicite de contact din sistem (Contact principal, Subiect, CC, Solicitant), puteți adăuga o altă etichetă de contact implicită la o înregistrare de contact pentru a facilita și ușura utilizarea acestora pentru articolele de lucru.

De exemplu: Dacă știți că „Jane Smith” va fi întotdeauna Broker-ul pentru fiecare articol de lucru la care este adăugată ca persoană de contact, puteți atribui o etichetă implicită de „Broker” fișei de contact lui Jane, astfel încât aceasta să fie completată automat pentru ea în articolul de lucru, fără a fi nevoie să setați manual această valoare a etichetei de fiecare dată.

Lista etichetelor implicite cu opțiunile disponibile este configurată în Builder, în rubrica [Setări Generale > > Etichete De Contact](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).

Puteți seta etichetarea implicită oricând adăugați un nou contact în sistem.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FgeZ6QbKw9oPfiICmKc7e%2Fimage.png?alt=media&#x26;token=2e824066-1e83-49e6-ad39-da078fd7b242" alt=""><figcaption></figcaption></figure>

Totodată, puteți adăuga etichete la contactele existente și edita eticheta implicită setată pentru un contact în pagina Contacte.

Etichetarea implicită poate fi editată și în masă, respectiv se poate seta pentru mai multe contacte deodată - selectați pur și simplu un număr de fișe de contact din pagina de Contacte și faceți clic pe butonul Editare pentru a accesa opțiunea de editare în masă.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FySpilGjhYUejmbkvxmLu%2Fimage.png?alt=media&#x26;token=27c9e8e8-f9ff-450a-88da-eb7cffa4948b" alt=""><figcaption></figcaption></figure>

### Comportamentul implicit al etichetei de contact dacă nu este setat la „Permiteți mai multe”

Dacă o anumită valoare a etichetei nu a fost setată la „Permiteți mai multe”, doar un singur contact din articolul de lucru poate avea valoarea respectivă. De exemplu: se poate întâmpla să existe un singur contact „Broker” pentru un Tichet. Acest lucru afectează în mod evident etichetarea implicită dacă două contacte care au aceeași etichetă implicită „trebuie să fie unică” sunt adăugate la un articol de lucru, fie manual, fie automat. În acest caz, sistemul va aloca eticheta implicită unui singur contact (și, prin urmare, va elimina eticheta implicită pentru celelalte contacte). Sistemul va aloca persoanei de contact deja etichetate, o *altă* valoare de etichetă existentă, în următoarea ordine de prioritate.

* Contact principal
* Solicitant
* Subiect
* CC
* Orice alt contact asociat cu articolul de lucru

### **Informații suplimentare privind incompatibilitățile dintre societatea furnizoare și etichetele de contact:**

* Nu veți putea adăuga o etichetă implicită unui contact dacă societatea căreia îi este atribuită are o societate furnizoare diferită de cea a etichetei implicite.
* Nu veți putea trimite un articol de lucru cu un contact a cărui etichetă implicită este setată la o companie furnizoare diferită de cea a articolului de lucru.

## Etichetarea automată a contactelor în articolele de lucru

### Contacte completate dintr-un e-mail inițial

#### Contacte cunoscute

La sosirea unui e-mail de la o adresă care este asociată cu un contact care se află deja în sistem și contactul respectiv:

* are o setare Globală a domeniului de aplicare, sau
* are o setare Locală a domeniului de aplicare, dar aparține aceleiași companii la care va aparține articolul de lucru pe baza regulilor de direcționare a e-mailurilor,

se completează automat detaliile sale în Cardul de contacte la crearea articolului de lucru de către sistem, iar acesta va fi etichetat automat ca fiind Contactul principal, Solicitantul inițial și Solicitantul articolului de lucru. În cazul în care îi este atribuită o etichetă implicită, contactul respectiv va fi etichetat ca atare. Rețineți însă că puteți oricând să editați manual etichetele după ce articolul de lucru a fost creat.

La sosirea unui e-mail de la o adresă asociată cu un contact care se află deja în sistem, dar care are o setare Locală a domeniului de aplicare și care aparține unei companii *diferite* de cea căreia îi va aparține articolul de lucru, pe baza regulilor de direcționare a e-mailurilor, detaliile sale NU vor fi completate automat în Cardul de contacte la crearea articolului de lucru de către sistem (și, prin urmare, nu va putea fi etichetat automat pentru articolul de lucru). Rețineți că puteți oricând să editați manual etichetele după ce articolul de lucru a fost creat.

#### Contacte necunoscute

*Domeniul de aplicare implicit pe „Global” sau „Global și local”*

La sosirea unui e-mail de la o adresă necunoscută, dacă:

* [setarea „Activare creare automată a contactelor” este ACTIVATĂ în Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) și
* sistemul dvs. este configurat să seteze domeniul de aplicare al contactelor externe la **Global**, sau **Global și Local**,

contactul va fi creat automat, va avea un domeniu de aplicare Global (adică nu va fi asociat cu nicio companie specifică) și detaliile sale vor fi completate automat în Cardul de contacte la crearea articolului de lucru de către sistem. În plus, acesta va fi etichetat automat ca și Contact principal, Solicitant inițial și Solicitant al articolului de lucru. Deoarece anterior acesta nu exista în sistem, nu va avea o etichetă implicită. Rețineți că puteți oricând să editați manual etichetele după ce articolul de lucru a fost creat.

*Domeniul de aplicare implicit pe „Local”*

La sosirea unui e-mail de la o adresă necunoscută, dacă

* [setarea „Activare creare automată a contactelor” este ACTIVATĂ în Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) și
* sistemul dvs. este configurat să seteze domeniul de aplicare al contactelor externe la **Local**,

contactul respectiv va fi creat automat, va avea un domeniu de aplicare Local (adică va fi asociat unei companii specifice) și va fi creat în cadrul companiei din care face parte articolul de lucru. Detaliile sale vor fi completate automat în Cardul de contacte la crearea articolului de lucru de către sistem și va fi etichetat automat drept Contact principal, Solicitant inițial și Solicitant al articolului de lucru. Deoarece anterior acesta nu exista în sistem, nu va avea o etichetă implicită. Rețineți că puteți oricând să editați manual etichetele după ce articolul de lucru a fost creat.

*Crearea automată a contactelor este DEZACTIVATĂ*

La sosirea unui e-mail de la o adresă necunoscută, dacă

* [setarea „Activare creare automată a contactelor” este DEZACTIVATĂ în Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation),

articolul de lucru va fi creat pe baza regulilor de direcționare a e-mailurilor, dar detaliile expeditorului e-mailului NU vor fi completate automat în Cardul de contacte la crearea articolului de lucru de către sistem (și, prin urmare, acesta nu poate fi etichetat automat la articolul de lucru). Rețineți că puteți oricând să editați manual etichetele după ce articolul de lucru a fost creat.

### Etichete de contact completate din Pagina de activitate a contactelor

Când se creează un articol de lucru de la butonul „Începeți articolul de lucru” de pe [Pagina de activitate](https://docs.enate.net/enate-help/romana/contacte/pagina-activitate-de-contact) a unui contact, contactul respectiv va fi etichetat automat ca Solicitant inițial, Solicitant, Subiect și Contact principal al articolului de lucru, iar eticheta implicită va fi și ea inclusă (dacă are una).
