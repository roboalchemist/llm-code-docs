# Source: https://docs.enate.net/enate-help/romana/procesarea-unei-actiuni/actiunea-de-extragere-documente.md

# Acțiunea de extragere documente

## Prezentare generală

Extragerea documentelor permite extragerea automată a datelor relevante din fișierele anexate la e-mailurile primite, astfel încât aceste date să poată fi utilizate în procesarea ulterioară a articolelor de lucru, ceea ce reduce considerabil timpul și efortul agenților dvs. Prin urmare, documente precum PDF-urile pot fi scanate și utilizate atât pentru a lansa Cazurile în Enate, cât și pentru a forma parte din activitățile în curs de desfășurare a procesului.

Când se execută o acțiune de extragere a documentelor pentru un Caz, se pot trimite documentele anexate la Cazul respectiv pentru scanare, iar fișierele extrase și procesate vor fi returnate și anexate automat la Caz.

În cazul în care tehnologia utilizată se dovedește a avea o eroare în ceea ce privește rezultatele, pe baza unui prag de confidențialitate pe care îl puteți seta dvs., Enate va transfera instantaneu sarcina către un agent din Work Manager pentru examinare și verificare, oferind astfel un sistem de sprijin „uman”.

Această caracteristică poate fi activată de către admin în secțiunea [Marketplace ](about:blank)din Enate Builder.

Urmăriți acest clip video pentru informații suplimentare:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

## Cum funcționează în momentul execuției

Când Cazul se execută în Work Manager, datele relevante din fișierele anexate la e-mailurile primite aferente acestuia sunt analizate și extrase automat.

Dacă tehnologia utilizată este îndeajuns de sigură de rezultatele extragerii datelor, această Acțiune nu va trebui să fie consultată de un utilizator uman, ea va fi pur și simplu finalizată în mod automat, iar Cazul va trece la următoarea Acțiune. Acțiunea completată de extragere a datelor poate fi vizualizată dacă faceți clic pe ea, însă nu va trebui transferată unui utilizator uman pentru intervenție.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2Fggwv7NUJqjEIYHH47po0%2Fimage.png?alt=media&#x26;token=a3d4ffc3-c1c1-49ca-8229-73a9c386134b" alt=""><figcaption></figcaption></figure>

Totuși, dacă tehnologia de extracție este mai puțin sigură de rezultatele extragerii datelor, Acțiunea va fi transferată unui utilizator uman în momentul în care accesați opțiunea „extragere din Coada de așteptare” de pe pagina principală, pentru a fi preluată și analizată. Astfel, dacă un agent deschide Acțiunea, veți constata că aceasta i-a fost atribuită pentru că sunt necesare unele verificări suplimentare.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2F0xFGlyit6Suzzys4wCqO%2Fimage.png?alt=media&#x26;token=cd8019eb-ed0b-444c-8da5-109d49410faf" alt=""><figcaption></figcaption></figure>

Pentru aceasta, trebuie doar să faceți clic pe opțiunea „Verificați acum” și să derulați la „Stația de validare” din cadrul Acțiunii, în care vor fi afișate documentul scanat și datele extrase din tabelul de valori rezultate. Veți putea observa în acest mod aspectele care evidențiază nivelurile de încredere mai scăzute, să le examinați și să efectuați manual corecțiile necesare. Acestea se pot vizualiza in situ sau se pot extinde într-o fereastră pop-up pentru a fi afișate pe tot ecranul.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FAALQeEyK19UBXnPzRXzI%2Fimage.png?alt=media&#x26;token=784cde5a-a1d3-492d-a03a-2175486291ad" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Notiță: Se poate vizualiza un singur document la un moment dat.
{% endhint %}

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2Fna3di9g3AOIJColO4bpo%2Fimage.png?alt=media&#x26;token=3d0d96ef-2de8-49ea-a862-a737e6879638" alt=""><figcaption></figcaption></figure>

Pe acest ecran de validare, agentul va putea vedea o copie scanată a fișierului, care poate conține mai multe pagini, alături de două file care afișează datele extrase.

* Fila Date extrase afișează perechile de valori cheie ale agentului din datele extrase, împreună cu nivelul de încredere pe care EnateAI le-a atribuit. Valorile pot fi ajustate atunci când este necesar și sunt salvate odată ce agentul face clic pe butonul de actualizare pentru valoarea respectivă. Astfel, valoarea de încredere pentru cheia respectivă va fi setată la 100%.
* Fila Tabele afișează toate datele repetitive care au fost selectate ca tabel. Puteți utiliza butonul Ștergere pentru a șterge rândurile care nu sunt necesare.

Dacă agentul trebuie să părăsească ecranul Stație de validare în orice moment, poate pur și simplu să facă clic pe „Salvare ca schiță” pentru a salva modificările aduse unui anumit document.

{% hint style="info" %}
Notiță: Dacă un agent accesează ecranul de validare pentru o Acțiune care nu îi este atribuită, datele vor fi în modul de citire și nu pot fi editate. Pentru a putea edita datele, agentul trebuie mai întâi să își atribuie Acțiunea.
{% endhint %}

Odată ce un agent este mulțumit de date, tot ce trebuie să facă pentru a trimite datele actualizate este să facă clic pe butonul „Trimite”. EnateAI va finaliza procesarea în fundal și va actualiza ecranul Acțiune pentru a confirma când a terminat. Procesarea în fundal permite agentului să treacă la orice alte documente care necesită verificare.

Odată ce ați făcut clic pe „Trimite” pentru ultimul document care necesită validare, ecranul Acțiune se închide automat. Din nou, EnateAI finalizează procesarea în fundal și va marca Acțiunea ca Rezolvată după un timp scurt, apoi va fi mutată în Închis.

*Notiță: De fiecare dată când revizuiți și actualizați elementele de date, EnateAI va învăța și va deveni puțin mai bun în sugestiile sale de extragere a datelor. Dacă observați că tehnologia greșește în mod regulat sugestiile, discutați cu echipa de administrare despre modificarea pragului de încredere.*
