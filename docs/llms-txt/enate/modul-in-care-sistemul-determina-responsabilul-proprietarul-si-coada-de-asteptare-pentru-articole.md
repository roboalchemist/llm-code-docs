# Source: https://docs.enate.net/enate-help/romana/appendice/modul-in-care-sistemul-determina-responsabilul-proprietarul-si-coada-de-asteptare-pentru-articole.md

# Modul în care sistemul determină Responsabilul, Proprietarul și Coada de așteptare pentru articole

Ca parte a gestionării Tichetelor, Cazurilor și Acțiunilor din cadrul fluxului de lucru în Enate, sistemul va verifica în mod regulat cui este atribuită activitatea, cine este proprietarul și la ce Coadă de așteptare este asociat articolul de lucru. Pentru a determina acest lucru, se respectă o serie de reguli foarte precise.

Înainte de a analiza aceste reguli, este important să înțelegem tiparul superior al procesului de repartizare a articolelor de lucru și când sunt evaluate acestea. Modalitatea de funcționare este următoarea:

* În primul rând, [stabilim CÂND au loc astfel de reevaluări](#cum-se-determina-cand-au-loc-reevaluarile) - în principiu, acest lucru se întâmplă când se produc modificări în „Statusul” articolului de lucru.&#x20;
* Dacă sistemul identifică necesitatea unei astfel de evaluări, inițial luăm în considerare starea/situația articolului de lucru pentru a [determina valorile Responsabil, Proprietar și Coadă de așteptare](#se-stabileste-daca-trebuie-setate-sau-eliminate-valorile-responsabil-proprietar-si-coada-de-asteptar) care trebuie să fie setate și care trebuie să fie eliminate complet.
* [În cazul celor care necesită o astfel de setare](#cum-se-stabilesc-responsabilul-proprietarul-si-coada-de-asteptare):
  * Dacă trebuie setată o Coadă de așteptare, este simplu - trebuie doar să selectați Coada de așteptare la care se face referire în regula de alocare (există doar două tipuri de reguli de alocare a Cozii de așteptare care trebuie respectate).
  * Pentru Responsabil și Proprietar, situația este mai complexă - trebuie parcurse o serie de reguli succesive care trebuie îndeplinite și care se termină cu selectarea unei ținte valide\*.

\*[Control de validitate](#controale-de-validitate) - Ca parte a verificării regulii de alocare a Responsabilului/Proprietarului, trebuie stabilit dacă ținta este validă (există o serie de reguli de control al validității pe care trebuie să le îndeplinească). În caz contrar, se continuă cu regulile din secțiunea a 3-a până când se găsește o țintă validă.

Odată ce tiparul superior este identificat, se poate analiza fiecare serie de reguli parcurse pentru secțiunile 1-3 de mai sus și pentru controlul de validitate al țintei.

## **Cum se determină CÂND au loc reevaluările**

Sistemul va reevalua Utilizatorul atribuit, Proprietarul și Coada de așteptare ori de câte ori se modifică informațiile din Status, mai exact când:

* se modifică Statusul
* se modifică Tipul de așteptare
* se modifică Data de monitorizare
* se modifică data din opțiunea „În așteptare de informații suplimentare până la”
* se modifică opțiunea „În așteptare de” (doar pentru Cazuri)
* se modifică contextul Tichetului
* se modifică categoria Tichetului
* se modifică statusul „Evaluare inter pares în desfășurare”
* se primesc informații noi cu privire la articolul de lucru
* un Caz întâmpină o problemă

## **Se stabilește dacă trebuie setate sau eliminate valorile Responsabil, Proprietar și Coadă de așteptare**

Dacă sistemul identifică necesitatea unei astfel de evaluări, inițial luăm în considerare STAREA articolului de lucru pentru a determina valorile Responsabil, Proprietar și Coadă de așteptare care trebuie să fie setate și care trebuie să fie eliminate complet. Puteți consulta aceste informații în tabelul de mai jos:

| <p><strong>Starea/Situația articolului de lucru</strong></p><p> </p>  | <p><strong>Responsabil</strong></p><p> </p> | <p><strong>Proprietar</strong></p><p> </p> | <p><strong>Coadă de așteptare</strong></p><p> </p> |
| --------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------ | -------------------------------------------------- |
| <p>Închis</p><p> </p>                                                 | <p>Ștergeți valoarea</p><p> </p>            | <p>Ștergeți valoarea</p><p> </p>           | <p>Ștergeți valoarea</p><p> </p>                   |
| <p>Schiță</p><p> </p>                                                 | <p>Setați o valoare</p><p> </p>             | <p>Ștergeți valoarea</p><p> </p>           | <p>Ștergeți valoarea</p><p> </p>                   |
| <p>Noi informații primite</p><p> </p>                                 | <p>Setați o valoare</p><p> </p>             | <p>Ștergeți valoarea</p><p> </p>           | <p>Setați o valoare</p><p> </p>                    |
| <p>Necesită atenție (relevant doar pentru Cazuri)</p><p> </p>         | <p>Setați o valoare</p><p> </p>             | <p>Ștergeți valoarea</p><p> </p>           | <p>Setați o valoare</p><p> </p>                    |
| <p>„De făcut” sau „În progres” pentru Acțiuni sau Tichete</p><p> </p> | <p>Setați o valoare</p><p> </p>             | <p>Ștergeți valoarea</p><p> </p>           | <p>Setați o valoare</p><p> </p>                    |
| <p>„De făcut” sau „În progres” pentru Cazuri</p><p> </p>              | <p>Ștergeți valoarea</p><p> </p>            | <p>Setați o valoare</p><p> </p>            | <p>Ștergeți valoarea</p><p> </p>                   |
| <p>„Rezolvat” sau „În așteptare”</p><p> </p>                          | <p>Ștergeți valoarea</p><p> </p>            | <p>Setați o valoare</p><p> </p>            | <p>Ștergeți valoarea</p><p> </p>                   |

&#x20;

## **Cum se stabilesc Responsabilul, Proprietarul și Coada de așteptare**

* **Cozi de așteptare** - Dacă trebuie setată o coadă de așteptare, este simplu - se aplică [Metoda de alocare a Cozilor de așteptare](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method).
* **Responsabil și Proprietar** - Dacă trebuie setat un Responsabil sau un Proprietar, procedura este mai complexă. Trebuie îndeplinite o serie de reguli succesive, iar procesul se oprește când regula este îndeplinită și se selectează o [țintă validă](file://o/-MMRJw5Faehepj28yGyJ/s/-MWYnDNwe3Cuo4zlGbs5-887967055/~/changes/1591/work-manager/work-manager-2021.1/appendix/system-behaviour-for-determining-assignee-owner-and-queue-for-work-items#validity-checks).

Înainte de a parcurge lista de reguli, se face o verificare sporită: dacă este setat deja un Responsabil/Proprietar, aceștia **nu se modifică decât dacă a fost modificată Categoria Tichetului**.

În caz contrar, se aplică următoarele reguli succesive, iar procesul se oprește în momentul în care este identificată o țintă validă:

1. Dacă a fost setată opțiunea „Păstrează cu mine” pentru un articol de lucru, se stabilește Responsabilul/Proprietarul ca fiind utilizatorul care a selectat această opțiune. Dacă nu se întâmplă acest lucru, sau dacă utilizatorul rezultat nu este valid, atunci
2. Dacă utilizatorul Proprietar nu este incomplet, atunci setați Responsabilul la aceeași valoare. Dacă nu se întâmplă acest lucru, sau dacă utilizatorul rezultat nu este valid, atunci
3. Dacă articolul de lucru nu este un Tichet SAU dacă e vorba de un Tichet (în cazul în care categoria Tichetului nu s-a schimbat ȘI dacă au fost create mai mult de 2 rânduri de istoric al stării - adică nu se află în prima stare de neprocesare), atunci:
4. Dacă articolul de lucru nu este un Tichet SAU dacă e vorba de un Tichet (în cazul în care categoria Tichetului nu s-a schimbat ȘI dacă au fost create mai mult de 2 rânduri de istoric al statusului - adică nu se află în prima stare de ciornă), atunci:
   1. Setați Responsabil și Proprietar pentru ultimul utilizator/robot care a actualizat articolul de lucru. Dacă nu se găsește niciun utilizator sau dacă utilizatorul rezultat nu este valid, atunci
   2. Setați Responsabil/Proprietar pentru orice utilizator/robot atribuit anterior, în ordinea descrescătoare a momentului de atribuire. Dacă nu se găsește niciun utilizator sau dacă utilizatorul rezultat nu este valid, atunci
   3. Dacă Acțiunea a fost inițiată de un flux de lucru (nu manual și într-un mod ad-hoc), selectați Responsabilul/Proprietarul ca fiind ultimul utilizator/robot care a efectuat aceeași Acțiune finalizată anterior în cadrul Cazului (sau în Evaluarea inter pares a Acțiunii, dacă s-a efectuat o Evaluare inter pares). Dacă nu se găsește niciun utilizator sau dacă utilizatorul rezultat nu este valid, atunci
5. Aplicați [Regula de alocare](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) pentru acest articol de lucru:
   1. Dacă alocarea principală de împingere este configurată pentru un anumit utilizator, stabiliți Responsabil/Proprietar pentru utilizatorul respectiv. Dacă nu se găsește niciun utilizator sau dacă utilizatorul rezultat nu este valid, atunci
   2. Dacă alocarea secundară este configurată pentru un anumit utilizator, stabiliți Responsabil/Proprietar pentru acel utilizator. Dacă nu se întâmplă acest lucru, sau dacă utilizatorul rezultant nu este valid, atunci
   3. Dacă alocarea principală de împingere este configurată la Poziție, dintre utilizatorii care ocupă această poziție, setați Responsabil/Proprietar drept utilizatorul cu cele mai puține articole de lucru în Inbox. Dacă nu se găsește niciun utilizator sau dacă utilizatorul rezultat nu este valid, atunci
   4. Dacă alocarea secundară de împingere este configurată la Poziție, dintre utilizatorii care ocupă această poziție, setați Responsabil/Proprietar drept utilizatorul cu cele mai puține articole de lucru în Inbox. Dacă nu se găsește niciun utilizator sau dacă utilizatorul rezultat nu este valid, atunci
6. Dacă articolul de lucru este un Caz, setați Responsabilul/Proprietarul ca fiind utilizatorul/robotul care a inițiat acel Caz.

## **Controale de validitate**

Ca parte a verificării regulii de alocare a Responsabilului/Proprietarului, trebuie stabilit dacă ținta este validă. Pentru ca aceasta să fie validă, există o serie de reguli de verificare a validității pe care trebuie să le îndeplinească. În caz contrar, se continuă cu regulile de stabilire a unui Responsabil/Proprietar până când se găsește o țintă validă. Controalele de validitate care se parcurg sunt următoarele:

* Dacă utilizatorul/robotul nu are permisiunea de a lucra la articole de lucru de acest tip (de exemplu, în modul Live/Test), trebuie blocat
* Dacă utilizatorul/robotul este în retragere, trebuie blocat
* Dacă utilizatorul nu are autorizație, trebuie blocat (nu se verifică autorizația pentru roboți)
* Dacă robotul este suspendat, trebuie blocat
* Dacă robotul a operat funcția de „Obținere mai multe sarcini” de mai mult de 3 ori pentru acest articol de lucru, trebuie blocat
* Dacă utilizatorul selectat este un robot și articolul de lucru este o Acțiune care se află în etapa de Evaluare inter pares, trebuie blocat (roboții nu pot efectua Evaluări inter pares).
* Dacă utilizatorul selectat este un robot, iar articolul de lucru este o Acțiune și nu s-a configurat nicio fermă de roboți pentru această Acțiune, trebuie blocat
* Dacă utilizatorul selectat este un robot și articolul de lucru este o Acțiune, iar robotul nu este membru al fermei de roboți configurate pentru această Acțiune, trebuie blocat
* Dacă utilizatorul selectat este un robot și articolul de lucru este un Caz, trebuie blocat (roboților nu li se pot atribui Cazuri)
* Dacă articolul de lucru este un manual cu Acțiune de Evaluare inter pares care se află în etapa de Evaluare inter pares, iar utilizatorul a efectuat una sau mai multe actualizări în timp ce se afla în etapa de Efectuare, trebuie blocat (utilizatorii nu își pot evalua propria activitate)
* Dacă articolul de lucru este un manual cu Acțiune de Evaluare inter pares care se află în etapa de Efectuare, iar utilizatorul a efectuat una sau mai multe actualizări în timp ce se afla în etapa de Evaluare inter pares, trebuie blocat (nu se poate solicita utilizatorilor să efectueze o activitate dacă aceștia au efectuat anterior o Evaluare inter pares)
