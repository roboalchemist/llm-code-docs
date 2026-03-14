# Source: https://docs.enate.net/enate-help/romana/cautare-rapida/cum-functioneaza-cautare-rapida-specifica.md

# Cum funcționează Căutarea rapidă – particularități

Câteva explicații suplimentare privind modul în care funcționează Căutarea rapidă: Există trei tipuri diferite de căutare, care se desfășoară în paralel atunci când introduceți datele de Căutare rapidă:

**1) Căutare cu un numărul de referință specific.** Aceasta se bazează pe recunoașterea unui format cunoscut al numărului de referință al sistemului pentru articolele de lucru și apoi returnarea rezultatelor referitoare la Tichete, Cazuri, Acțiuni care au această referință. Puteți doar să introduceți referința, de exemplu „17117-T” și sistemul o va recunoaște ca referință. Nu trebuie să introduceți un cod scurt de început.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2Fs7qtEXDYgYCe1N2rQwOI%2Fimage.png?alt=media\&token=0d998f68-236f-41f5-904f-1bc080372f08)

**2) Căutare de Câmp de date personalizate.** După cum este descris anterior. Sistemul este capabil să facă acest tip de căutare atunci când introduceți un cod scurt cunoscut, de exemplu „FN:”. Căutarea se va face pentru un domeniu care conține valoarea specifică pe care o introduceți. Consultați nota de mai jos despre Metacaractere.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FK2dLdQopV1QTY32gD1zn%2Fimage.png?alt=media\&token=fb6b2ece-e10b-486e-8eac-9b509ecd4ff2)

**3) Căutarea de text liber pentru articole de lucru, comunicări și utilizatori** în raport cu orice altă informație introdusă care nu se încadrează în primele două tipuri de date recunoscute. Sistemul caută în textul liber cuvintele individuale în funcție de diverse caracteristici de sistem ale articolelor de lucru, comunicărilor și utilizatorilor (de ex. titlul articolului de lucru, subiectul și corpul e-mailului).

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FJirmKULRdqymDaP5KjNN%2Fimage.png?alt=media\&token=8ae5eb5e-937f-4092-b670-15c01bd7cbeb)

**4) Căutarea "Începe cu" pentru fișiere** - sistemul utilizează logica "începe cu" pentru căutarea fișierelor, în care adaugă un metacaracter la SFÂRȘITUL textelor de căutare. De exemplu, dacă se caută un fișier numit " Procesare factură.docx", căutările pentru "procesare" nu vor găsi fișierul, dar căutările pentru "factură" îl vor găsi.

## Metacaractere pentru căutarea deschisă <a href="#a-metacaractere-pentru-cautarea-deschisa" id="a-metacaractere-pentru-cautarea-deschisa"></a>

În momentul căutării, sistemul va adăuga un metacaracter la SFÂRȘITUL textelor de căutare, dar nu și la început.&#x20;

Pentru Căutările de date personalizate, un exemplu ar fi: dacă se caută, de exemplu, „p:John Smi” se vor găsi articole cu valoarea „John Smith” în domeniul „persoană”, dar dacă se caută doar „p:Smith”, această valoare NU se va găsi.&#x20;

Pe scurt: în cazul căutărilor de Câmpuri de date personalizate, se caută valoarea precisă a câmpului sau începutul valorii respective. Căutările cu text liber nu sunt exact aceleași lucru, deoarece o căutare cu text liber va încerca să se potrivească cu fiecare cuvânt individual în cadrul unei valori de text pentru a obține o potrivire, și nu cu valoarea în ansamblu.

Sunt adăugate și metacaractere la sfârșitul căutărilor cu numere de referință.

### Utilizarea Metacaractere în timp ce tastați <a href="#rulati-metacaractere-in-timp-ce-tastati" id="rulati-metacaractere-in-timp-ce-tastati"></a>

În timp ce tastați în Căutare rapidă, sistemul va efectua o căutare cu metacaracter după ultimul cuvânt. De exemplu, dacă efectuați o căutare cu text liber: „John return prio”, sistemul va căuta cu metacaractere ultimul cuvânt și va afișa rezultate cum ar fi „prioritate”.

După ce ați apăsat bara de spațiu, sistemul va concluziona că ați terminat tastarea acestui cuvânt și îl va căuta fără un metacaracter.

## Alți termeni de căutare ignorați <a href="#alti-termeni-de-cautare-ignorati" id="alti-termeni-de-cautare-ignorati"></a>

Pentru a asigura funcționarea corectă a sistemului, următorii termeni sunt ignorați din căutări:

* Cuvinte de 1 sau 2 caractere.
* Cuvinte din „Lista de excludere” a sistemului. Acestea sunt cuvinte comune standard, cum ar fi conjuncții și prepoziții, pronume etc., care ar genera prea multe rezultate. Consultați aici [lista completă  a cuvintelor care sunt ignorate în căutări](https://docs.enate.net/enate-help/romana/appendice/termeni-de-cautare-ignorati-detalii-suplimentare) (atât în funcția de Căutare rapidă, cât și în orice altă căutare efectuată în sistem).
* Caracterele specifice setate pentru a fi ignorate, în special în Căutarea rapidă, sunt:„\*”, „?”, „@” etc. Consultați aici pentru a vedea [lista completă a caracterelor care sunt ignorate](file://enate-help/work-manager/work-manager-2021.1/appendix/search-terms-ignored-further-details#characters-ignored-in-quickfind). Astfel, când se caută, de exemplu, client.com în Căutarea rapidă, se vor căuta cuvintele „client” și „com”. Prin urmare, este recomandat să includeți astfel de combinații de cuvinte între ghilimele pentru a le căuta ca expresii specifice - de exemplu, dacă veți căuta „client.com”, veți obține probabil rezultatele pe care le căutați.

## Alte lucruri de reținut cu privire la Căutarea rapidă

Căutarea rapidă se efectuează pe bază de text. Introducerea datelor în rândurile de text poate duce la rezultate incoerente. Folosiți „ghilimele” când este posibil, pentru a facilita căutarea de șiruri întregi de cuvinte, în cazul în care o astfel de căutare este necesară.&#x20;

Folosiți cursoarele de date pentru a căuta rezultate în intervale de date specifice.

Când căutați mai multe cuvinte, căutarea se va face folosind o formulă bazată pe „ȘI” mai degrabă decât pe „SAU”, de exemplu, se vor găsi articole cu Măr ȘI Banană ȘI Pară.

## Particularități ale căutărilor în raport cu articolele de lucru și cu e-mailurile

Este important să rețineți că funcția de Căutare rapidă efectuează trei căutări independente:&#x20;

* una pentru articolele de lucru (Cazuri, Acțiuni, Tichete)
* una pentru e-mailurile care pot fi asociate cu acestea și&#x20;
* una pentru persoane.&#x20;

O posibilă consecință a acestui fapt este că, dacă efectuați, de exemplu, o căutare în funcție de o combinație de trei cuvinte (de exemplu, măr și banană și pară), Căutarea rapidă va afișa toate rezultatele referitoare la articolele de lucru în care apar toate cele trei cuvinte și, de asemenea, orice e-mail în care apar toate cele trei cuvinte. Situațiile în care două dintre cuvinte apar în articolul de lucru, iar cel de-al treilea doar într-un e-mail asociat, nu ar fi recuperate de niciuna dintre căutări.

Caracteristicile pe baza cărora se efectuează căutările articolelor de lucru sunt următoarele:

* Numărul de referință al articolului de lucru
* Titlul
* Numele clientului
* Numele furnizorului
* Denumirea contractului o Denumirea serviciului
* Numele companiei de servicii
* Denumirea serviciului sau numele tipului de proces&#x20;

Caracteristicile pe baza cărora se efectuează căutările Comunicațiilor sunt următoarele:

* Titlul e-mailului
* Conținutul e-mailului
* Contacte de e-mail (De la, Către, CC, BCC)
* Conținutul notiței interne (pentru notițele adăugate în Enate / Autoservire).
