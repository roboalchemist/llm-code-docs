# Source: https://docs.enate.net/enate-help/romana/tipuri-de-elemente-de-lucru-tichete-cazuri-si-actiuni/previziuni-pentru-cazuri.md

# Previziuni pentru Cazuri

## Prezentare generală

Pentru utilizatorii care folosesc versiunea 2024.1, aceștia vor putea utiliza funcția de Previziuni pentru a furniza o estimare mai precisă a efortului necesar pentru articolele de lucru, ceea ce vă va permite să planificați în mod mai eficient resursele necesare.

Pe termen lung, aceste date pot fi clasate și transmise administratorilor pentru a ajusta intervalele de timp pentru estimarea efortului și pentru a furniza previziuni mai precise pentru volumele de lucru ulterioare.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2Fd8xoKDJZM9YwD6zbNXan%2Fimage.png?alt=media&#x26;token=7de15e5a-23ba-4667-8601-9bd4aab44714" alt=""><figcaption></figcaption></figure>

## Cum se utilizează funcția „Previziuni”

Odată activată această funcție, va apărea o nouă secțiune denumită „Estimare efort” în Cazurile din Work Manager.

Aici veți vedea un raport al estimării efortului pentru întregul Caz, o defalcare a estimării efortului pentru Acțiunile sau Cazurile secundare care formează Cazul și o defalcare a estimării efortului pentru Acțiunile sau Cazurile secundare care nu au fost încă create.

### Sinteza efortului pentru Caz

În secțiunea „Sinteza efortului pentru Caz”, utilizatorul poate modifica timpul estimat alocat Cazului. Aceasta conține și alți parametri utili pentru Cazul respectiv.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FIMPdpAZ2ya6k0ewByk8b%2Fimage.png?alt=media&#x26;token=2d79fa33-eebb-4bba-b312-8d1b885173df" alt=""><figcaption></figcaption></figure>

Efortul „estimat” indică timpul total estimat pentru rezolvarea Cazului. Această valoare poate fi actualizată de către utilizatori cu o estimare mai precisă.

* Reprezintă suma efortului „estimat” al tuturor articolelor create și al Acțiunilor (și al Acțiunilor aferente Cazului secundar) care formează Cazul, precum și din valoarea „Efort pentru activitatea încă necreată”.
  * Acest câmp va afișa inițial valoarea manuală „[Efort inițial estimat pentru înregistrare](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)” din Builder (dacă există) înmulțită cu [numărul de înregistrări](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
  * Dacă se actualizează „numărul de înregistrări”, „efortul estimat” pentru Cazul care nu a fost actualizat de un utilizator din Work Manager se va actualiza pentru a reflecta modificarea numărului de înregistrări.
    * Odată ce Cazul se află în starea „Rezolvat” sau „Închis”, efortul estimat al acestuia nu mai poate fi modificat.
  * Rețineți că mărirea acestei valori va crește estimarea „Efort pentru activitatea încă necreată” și viceversa.
* Efortul „real” indică timpul alocat Efortului pentru activitatea încă necreată din cadrul Cazului.
  * Reprezintă suma efortului „real” al tuturor Acțiunilor și Cazurilor secundare create care formează Cazul, preluate din contoarele de timp respective.
* „Rămas estimat” indică timpul estimat rămas pentru Cazul respectiv.
  * Reprezintă suma efortului estimat rămas pentru toate Acțiunile și Cazurile secundare create care formează Cazul ȘI timpul estimat rămas pentru articole care nu au fost încă create (prin urmare, este posibil să nu fie întotdeauna egal cu efortul „estimat pentru Caz” minus efortul „real al Cazului”).

Modificarea valorii efortului „estimat” pentru un Caz are următoarele consecințe:

* Actualizare automată a [valorii estimate "Efort pentru activitatea încă necreată".](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases#effort-for-work-not-yet-created) Acest lucru se datorează faptului că „Efortul estimat” pentru Caz este o valoare calculată, formată din suma efortului „estimat” al tuturor articolelor create și al Acțiunilor (și al Acțiunilor aferente Cazului secundar) care formează Cazul, precum și din valoarea „Efort pentru activitatea încă necreată”.
  * Dacă se mărește efortul „estimat” pentru un Caz, se mărește valoarea „Efort pentru activitatea încă necreată” cu aceeași valoare
  * Dacă se reduce efortul „estimat” pentru un Caz, se reduce valoarea „Efort pentru activitatea încă necreată” cu aceeași valoare

### Defalcare efort pentru articole create

În secțiunea „Defalcare efort pentru articole create”, utilizatorii pot modifica timpul estimat pentru fiecare dintre Acțiunile create (și Cazurile secundare) care formează Cazul. Aceasta afișează și alți parametri utili pentru toate Acțiunile create (și Cazurile secundare) care formează Cazul.

Rețineți că, odată ce o Acțiune este în starea de „Rezolvat” sau „Închis”, efortul estimat al acesteia nu mai poate fi modificat.

Pe măsură ce se creează Acțiunile (și Cazurile secundare), efortul estimat pentru acestea va fi preluat din valoarea Efortului estimat din secțiunea Articole care nu au fost încă create de mai jos.

### Defalcare Acțiuni

La fiecare Acțiune, veți observa:

* Un link către fiecare Acțiune
* Efortul „estimat” care indică timpul total care se estimează că va dura Acțiunea. Această valoare poate fi actualizată de către utilizatori cu o estimare mai precisă.
  * Acest câmp va afișa inițial valoarea manuală „[Efort inițial estimat pentru înregistrare](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)” din Builder înmulțită cu [numărul de înregistrări](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
    * Dacă se actualizează „numărul de înregistrări”, „efortul estimat” pentru toate Acțiunile în derulare care nu au fost actualizate de un utilizator Work Manager se va actualiza pentru a reflecta modificarea numărului de înregistrări.
  * Mărirea acestei valori va reduce estimarea „Activitatea încă necreată” și viceversa și, prin urmare, ar putea afecta efortul total „estimat pentru Caz”
  * Rețineți că, odată ce o Acțiune este în starea de „Rezolvat” sau „Închis”, efortul estimat al acesteia nu mai poate fi modificat.
* Efortul „real” indică timpul alocat până în prezent Acțiunii respective
  * Valoarea este preluată din contorul de timp al Acțiunii.
* Rămas estimat” indică timpul estimat rămas pentru Acțiunea respectivă.
  * Se calculează prin scăderea efortului „real” alocat Acțiunii din efortul „estimat”.
* Data scadentă a Acțiunii
  * Dacă efortul „real” este zero în momentul de față, veți vedea și o valoare „Începând cu”. Această valoare indică momentul limită până la care se poate iniția Acțiunea pentru a respecta data scadentă.
* Starea Acțiunii

Modificarea valorii efortului „estimat” pentru o Acțiune are următoarele consecințe:

* Actualizare automată a valorii estimate "Efort pentru activitatea încă necreată" pentru Caz.
* O posibilă actualizare automată a efortului „estimat” pentru întregul Caz

Informații detaliate:

* Dacă se reduce efortul „estimat” pentru o Acțiune, se mărește valoarea „Efort pentru activitatea încă necreată” pentru Caz, cu aceeași valoare (lăsând același efort „estimat” pentru întregul Caz).
* Dacă se mărește efortul „estimat” pentru o Acțiune, se reduce valoarea „Efort pentru activitatea încă necreată” pentru Caz, cu aceeași valoare. Această situație poate afecta sau nu efortul „estimat” pentru întregul Caz.
  * Dacă „efortul estimat” actualizat pentru o Acțiune nu crește suficient pentru ca valoarea „Efort pentru activitatea încă necreată” pentru Caz să scadă sub 0, efortul „estimat” pentru Caz nu va fi afectat
    * De exemplu: să presupunem că efortul „estimat” pentru Acțiunea 1 este de 2 ore, estimarea „Efort pentru activitatea încă necreată” este de 1 oră, iar „Efortul estimat” pentru Caz este de 3 ore. Dacă utilizatorul decide că Acțiunea 1 va dura cu 1 oră mai mult, va actualiza efortul „estimat” pentru Acțiunea 1 de la 2 la 3 ore. „Efort pentru activitatea încă necreată” va scădea de la 1 oră la 0 ore, iar efortul „estimat” pentru Caz nu se va modifica - va rămâne la 3 ore.
  * Dacă „efortul estimat” actualizat pentru o Acțiune crește suficient de mult pentru ca valoarea „Efort pentru activitatea încă necreată” pentru Caz să scadă sub 0, diferența trebuie adăugată la „efortul estimat” pentru întregul Caz.
    * De exemplu: să presupunem că un Caz are o singură Acțiune creată pentru el, numită Acțiunea 1. Efortul „estimat” pentru Acțiunea 1 este de 2 ore, estimarea „Efort pentru activitatea încă necreată” este de 0 ore și, prin urmare, „Efortul estimat” pentru întregul Caz este de 2 ore. Dacă utilizatorul decide că Acțiunea 1 va dura cu 1 oră mai mult, va actualiza efortul „estimat” pentru Acțiunea 1 de la 2 la 3 ore. Deoarece valoarea „Efort pentru activitatea încă necreată” este 0, efortul „estimat” pentru întregul Caz va crește cu 1 oră, trecând de la 2 la 3 ore.
    * Exemplul 2: să presupunem că un Caz are o singură Acțiune creată pentru el, numită Acțiunea 1. Efortul „estimat” pentru Acțiunea 1 este de 2 ore, estimarea „Efort pentru activitatea încă necreată” este de 1 oră și, prin urmare, „Efortul estimat” pentru întregul Caz este de 3 ore. Dacă utilizatorul decide că Acțiunea 1 va dura cu 2 ore mai mult, va actualiza efortul „estimat” pentru Acțiunea 1 de la 2 la 4 ore, ceea ce face ca „Efortul pentru activitatea încă necreată” să se reducă cu 1 oră, de la 1 la 0 (se va reduce cât de mult posibil). Ora „rămasă” va fi adăugată la efortul total „estimat” al Cazului, care va crește cu 1 oră pentru a ajunge de la 3 la 4 ore.

### Defalcare Caz secundar

Dacă se creează un Caz secundar, veți observa:

* Un link către Cazul secundar, dacă aveți permisiunea să îl accesați (în caz contrar, veți vizualiza doar numele și numărul de referință ale acestuia, fără link)
* Un rând „total” al Cazului secundar, cu următoarele informații:
  * Efortul „estimat” indică timpul total estimat pentru rezolvarea Cazului secundar. Această valoare poate fi actualizată de către utilizatori cu o estimare mai precisă.
    * Reprezintă suma efortului „estimat” al tuturor Acțiunilor create și viitoare care formează Cazul secundar.
    * Acest câmp va afișa inițial valoarea manuală „[Efort inițial estimat pentru înregistrare](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)” din Builder înmulțită cu [numărul de înregistrări](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
      * Dacă se actualizează „numărul de înregistrări”, „efortul estimat” pentru Cazul secundar care nu a fost actualizat de un utilizator din Work Manager se va actualiza pentru a reflecta modificarea numărului de înregistrări.
    * Odată ce Cazul secundar se află în starea „Rezolvat” sau „Închis”, efortul estimat al acestuia nu mai poate fi modificat.
    * Rețineți că mărirea acestei valori va crește estimarea „Activitatea încă necreată” pentru Cazul secundar și viceversa.
  * Efortul „real” indică timpul alocat până în prezent Cazului secundar.
    * Reprezintă suma efortului „real” al tuturor Acțiunilor care formează Cazul secundar, preluate din contoarele de timp respective.
  * „Rămas estimat” indică timpul estimat rămas pentru Cazul secundar.
    * Reprezintă suma efortului estimat rămas pentru toate Acțiunile care formează Cazul secundar ȘI timpul estimat rămas pentru articole care nu au fost încă create în Cazul secundar (prin urmare, este posibil să nu fie întotdeauna egal cu efortul „estimat pentru Cazul secundar” minus efortul „real al Cazului secundar”)
    * Data scadentă a Cazului secundar
    * Starea Cazului secundar
* Un rând pentru fiecare Acțiune aferentă Cazului secundar, cu următoarele informații:
  * Efortul „estimat” indică timpul total estimat pentru rezolvarea Acțiunii aferente Cazului secundar. Această valoare poate fi actualizată de către utilizatori cu o estimare mai precisă.
    * Acest câmp va afișa inițial valoarea manuală „Efort inițial estimat pentru înregistrare” din Builder înmulțită cu numărul de înregistrări
      * Dacă se actualizează „numărul de înregistrări”, „efortul estimat” pentru toate Acțiunile aferente Cazului secundar care se află în derulare și care nu au fost actualizate de un utilizator Work Manager, se va actualiza pentru a reflecta modificarea numărului de înregistrări.
    * Mărirea acestei valori va reduce estimarea Cazului secundar pentru „Activitatea încă necreată” și viceversa și, prin urmare, ar putea afecta efortul total „estimat pentru Cazul secundar”
    * Odată ce o Acțiune se află în starea „Rezolvat” sau „Închis”, efortul estimat a acesteia nu mai poate fi modificat.
  * Efortul „real” indică timpul alocat până în prezent Acțiunii aferente Cazului secundar
    * Valoarea este preluată din contorul de timp al Acțiunii aferente Cazului secundar.
  * „Rămas estimat” indică timpul estimat rămas pentru Acțiunea aferentă Cazului secundar.
    * Se calculează prin scăderea efortului „real” alocat Acțiunii aferente Cazului secundar din efortul „estimat”.
* Data scadentă a Acțiunii aferente Cazului secundar
  * Dacă efortul „real” este zero în momentul de față, veți vedea și o valoare „Începând cu”. Această valoare indică momentul limită până la care se poate iniția Acțiunea aferentă Cazului secundar, pentru a respecta data scadentă.
    * Starea Acțiunii aferente Cazului secundar
* Un rând pentru „Observație privind activitatea Cazului secundar creat deja”, cu următoarele informații:
  * Efortul „estimat” indică efortul estimat necesar pentru finalizarea Acțiunilor aferente Cazului secundar, care nu au fost încă create pentru respectivul Caz secundar. Această valoare poate fi actualizată de către utilizatori cu o estimare mai precisă.
    * Modificarea acestei estimări va afecta efortul total „Estimat pentru Cazul secundar” și ar putea afecta estimarea efortului pentru întregul Caz

Modificarea valorii efortului „estimat” pentru o Acțiune aferentă Cazului secundar are următoarele consecințe:

* Actualizare automată a valorii estimate "Efort pentru activitatea încă necreată" pentru Cazul secundar.
* O posibilă actualizare automată a efortului „estimat” pentru întregul Caz secundar
* O posibilă actualizare automată a efortului „estimat” pentru întregul Caz principal

Informații detaliate:

* Dacă crește efortul „estimat” pentru o Acțiune aferentă unui Caz secundar, creștere valoarea „Efort pentru activitatea încă necreată” pentru Cazul secundar cu același procent (efortul „estimat” pentru întregul Caz secundar rămâne același și, prin urmare, nu are niciun impact asupra efortului „estimat” pentru întregul Caz principal).
* Dacă se mărește efortul „estimat” pentru o Acțiune aferentă unui Caz secundar, se reduce valoarea „Efort pentru activitatea încă necreată” pentru Cazul secundar, cu aceeași valoare. Această situație poate afecta sau nu efortul „estimat” pentru întregul Caz.
  * Dacă „efortul estimat” actualizat pentru o Acțiune aferentă unui Caz secundar nu crește suficient pentru ca valoarea „Efort pentru activitatea încă necreată” pentru Cazul secundar să scadă sub 0, efortul „estimat” pentru Cazul secundar nu va fi afectat (și, prin urmare, nici efortul „estimat” pentru întregul Caz principal nu va fi afectat).
    * De exemplu: să presupunem că un Caz secundar are o singură Acțiune creată pentru el, numită Acțiunea 1 a Cazului Secundar. Efortul „estimat” pentru Acțiunea 1 a Cazului secundar este de 2 ore, iar estimarea „Efort pentru activitatea încă necreată” pentru Cazul secundar este de 1 oră, prin urmare „efortul estimat” pentru Cazul secundar este de 3 ore. Dacă utilizatorul decide că Acțiunea 1 a Cazului secundar va dura cu 1 oră mai mult, va actualiza efortul „estimat” pentru Acțiunea 1 a Cazului secundar de la 2 la 3 ore, ceea ce face ca „Efortul pentru activitatea încă necreată” al Cazului secundar să se reducă de la 1 oră la 0 ore. Efortul „estimat” pentru Cazul secundar nu se modifică - va fi în continuare de 3 ore (și, prin urmare, efortul „estimat” pentru întregul Caz principal nu va fi afectat).
  * Dacă „efortul estimat” actualizat pentru o Acțiune aferentă unui Caz secundar crește suficient de mult pentru ca valoarea „Efort pentru activitatea încă necreată” pentru Cazul secundar să scadă sub 0, diferența trebuie adăugată la „efortul estimat” pentru întregul Caz secundar (și, prin urmare, ar putea afecta efortul „estimat” pentru întregul Caz principal).
    * De exemplu: să presupunem că un Caz secundar are o singură Acțiune creată pentru el, numită Acțiunea 1 a Cazului Secundar. Efortul „estimat” pentru Acțiunea 1 a Cazului secundar este de 2 ore, iar estimarea „Efort pentru activitatea încă necreată” pentru Cazul secundar este de 0 ore, prin urmare „efortul estimat” pentru întregul Caz secundar este de 2 ore. Dacă utilizatorul decide că Acțiunea 1 a Cazului secundar va dura cu 1 oră mai mult, va actualiza efortul „estimat” pentru Acțiunea 1 de la 2 la 3 ore. Deoarece valoarea „Efort pentru activitatea încă necreată” pentru Cazul secundar este de 0 ore, efortul „estimat” pentru Cazul secundar va crește cu 1 oră, trecând de la 2 la 3 ore.
      * Dacă există suficient timp în „Efortul pentru activitatea încă necreată” al Cazului principal, această majorare de 1 oră ar putea fi extrasă de acolo, astfel încât să nu fie afectat efortul „estimat” pentru întregul Caz principal.
      * Dacă nu există suficient timp în „Efortul pentru activitatea încă necreată” al Cazului principal, această majorare de 1 oră va duce la o creștere a efortului „estimat” pentru întregul Caz principal.
    * Exemplul 2: să presupunem că un Caz secundar are o singură Acțiune creată pentru el, numită Acțiunea 1 a Cazului Secundar. Efortul „estimat” pentru Acțiunea 1 a Cazului secundar este de 2 ore, iar estimarea „Efort pentru activitatea încă necreată” pentru Cazul secundar este de 1 oră, prin urmare „efortul estimat” pentru întregul Caz secundar este de 3 ore. Dacă utilizatorul decide că Acțiunea 1 a Cazului secundar va dura cu 2 ore mai mult, va actualiza efortul „estimat” pentru Acțiunea 1 a Cazului secundar de la 2 la 4 ore, ceea ce face ca „Efort pentru activitatea încă necreată” al Cazului secundar să se reducă cât de mult posibil - acesta se va reduce cu 1 oră, de la 1 la 0. Ora „rămasă” va fi adăugată la efortul total „estimat” al Cazului secundar, care va crește cu 1 oră pentru a ajunge de la 3 la 4 ore.
      * Dacă există suficient timp în „Efortul pentru activitatea încă necreată” al Cazului principal, această majorare de 1 oră ar putea fi extrasă de acolo, astfel încât să nu fie afectat efortul „estimat” pentru întregul Caz principal.
      * Dacă nu există suficient timp în „Efortul pentru activitatea încă necreată” al Cazului principal, această majorare de 1 oră va duce la o creștere a efortului „estimat” pentru întregul Caz principal.

### Efort pentru activitatea încă necreată

Secțiunea „Efort pentru activitatea încă necreată” indică efortul estimat necesar pentru finalizarea Acțiunilor (și Acțiunilor aferente Cazurilor secundare) care nu au fost încă create pentru acest Caz.

Se calculează prin scăderea sumei efortului „estimat” pentru activitatea creată din efortul „estimat” pentru Cazul respectiv. Prin urmare, dacă se mărește „Efortul pentru activitatea încă necreată”, va crește efortul estimat pentru întregul Caz și viceversa.

Pe măsură ce se creează Acțiunile (și Cazurile secundare), efortul estimat pentru acestea va fi preluat din estimarea „Efort pentru activitatea încă necreată”.

Odată ce Cazul se află în starea „Rezolvat” sau „Închis”, „Efortul pentru activitatea încă necreată” nu mai poate fi modificat.
