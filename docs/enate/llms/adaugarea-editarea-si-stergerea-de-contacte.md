# Source: https://docs.enate.net/enate-help/romana/contacte/adaugarea-editarea-si-stergerea-de-contacte.md

# Adăugarea, editarea și ștergerea de contacte

## Adăugarea de contacte

Contactele externe pot fi create în mai multe moduri în Enate.

### 1)  În mod automat, dintr-un e-mail de intrare

Sistemul Enate poate fi setat să creeze automat noi registre de contacte externe la primirea de e-mailuri care conțin adrese de e-mail noi, dacă setarea [„Permiteți crearea automată a contactelor” este configurată ca fiind ACTIVATĂ în Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).

Sistemul va completa automat numele și prenumele persoanei de contact pe baza numelui afișat în e-mail. Mai multe detalii referitoare la acest aspect:

* Dacă numele afișat în e-mail conține un spațiu, valoarea de dinaintea primului spațiu va fi folosită ca prenume a persoanei de contact, iar valoarea de după ultimul spațiu va fi folosită ca nume de familie. De exemplu, dacă numele afișat în e-mail este „John Smith”, persoanei de contact va fi completat automat ca „John”, iar numele de familie va fi completat automat ca „Smith”.
* Dacă numele afișat în e-mail conține o virgulă, valoarea de dinaintea primei virgule va fi folosită ca nume de familie a persoanei de contact, iar valoarea de după virgulă, dar înainte de spațiu, ca prenume. De exemplu, dacă numele afișat în e-mail este „Smith, John”, atunci numele de familie a persoanei de contact va fi completat automat ca „Smith”, iar prenumele va fi completat automat ca „John”.
* Dacă sistemul nu poate completa automat numele și prenumele cu certitudine, atunci contactul va fi creat automat fără nume și prenume, iar utilizatorul va fi invitat să completeze el însuși aceste date când trimite articolul de lucru.

În plus, [compania configurată](#numele-companiei-domeniul-de-aplicare-a-contactului-extern) pentru un contact creat automat va depinde de setarea domeniului de [aplicare a contactului din Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope). Dacă este configurată pentru „Global” sau „Global și local”, contactul creat automat va avea un domeniu de aplicare global, deci nu va fi asociat cu nicio companie specifică. Dacă este configurată pentru „Local”, contactul creat automat va fi creat în cadrul companiei din care face parte articolul de lucru corespunzător.

### 2)  Adăugarea unui contact individual din Pagina de gestionare contacte

Puteți adăuga contacte din [Pagina de gestionare contacte](https://docs.enate.net/enate-help/romana/contacte/pagina-de-gestionare-a-contactelor) făcând clic pe pictograma Creare contact și completând detaliile contactului în fereastra pop-up rezultantă.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2Fvmk2y2Vz5X0LKRXQvTE6%2F7A%20Adding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=440c5fbd-7b89-4ad5-aae9-5fddc614f935" alt=""><figcaption></figcaption></figure>

### 3)  Importarea contactelor în Pagina de gestionare contacte dintr-un fișier Excel

Puteți importa o listă de contacte dintr-o foaie de calcul Excel în [Pagina de gestionare contacte](https://docs.enate.net/enate-help/romana/contacte/pagina-de-gestionare-a-contactelor). Se furnizează un model, care este compatibil cu toate limbile oferite de Enate.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FHLKbRLzJjoGWakDLs5nz%2F7A%20Bulk-Adding-Contacts.gif?alt=media&#x26;token=46266e64-ee22-40d6-9fd6-433c8b42d795" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Este absolut necesar să completați adresa de e-mail atunci când importați contacte dintr-un fișier Excel. Dacă nu specificați o companie, contactul va fi setat automat la nivel global. Consultați aici pentru mai multe informații despre domeniul de [aplicare al companiei](#numele-companiei-domeniul-de-aplicare-a-contactului-extern).
{% endhint %}

### 4)  Adăugarea unui contact prin funcția de Căutare rapidă

În cazul în care căutați un nou contact care încă nu există în sistem, puteți crea un contact nou prin intermediul funcției de [Căutare rapidă](https://docs.enate.net/enate-help/romana/cautare-rapida). Accesați funcția de căutare a persoanelor din Căutare rapidă și faceți clic pe „Adăugare contact”.

În momentul în care faceți clic pe „Adaugare contact”, sistemul va decoda și va completa automat numele, prenumele și adresa de e-mail. După ce completați toate informațiile și faceți clic pe Creare, veți fi direcționat către [Pagina De Activitate ](https://docs.enate.net/enate-help/romana/contacte/pagina-activitate-de-contact)a noului contact.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXb0zH-DMnI1hDDpqYh%2F-MXbLFVyVHS1XoH7OEUQ%2FAdd-External-Contact-from-Quickf.gif?alt=media\&token=670bf5e6-48a3-4e3f-89d5-69d370bc529c)

{% hint style="info" %}
Notă: adresa de e-mail a contactului trebuie să fie unică în sistem.
{% endhint %}

### 5)  Adăugarea unui contact din Fișa de contacte a unui articol de lucru

De asemenea, puteți crea un contact nou din fișa de contacte a unui articol de lucru. Dacă în Fișa de contacte căutați un utilizator care nu există în sistem, puteți crea un nou contact făcând clic pe opțiunea „Creare contact” și introducând detaliile contactului.

Conform adresei de e-mail a persoanei de contact, sistemul va decoda și va completa automat numele și prenumele persoanei de contact. După ce introduceți toate informațiile și faceți clic pe „creați contactul”, sistemul vă va redirecționa înapoi la articolul de lucru.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FmPXh7cHU4pa3z2A5pjj1%2F7A-Create-Contact-from-Work-Item.gif?alt=media&#x26;token=2afe00d1-75d8-4d3f-8c69-d5016b26941a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Vă rugăm să rețineți că, dacă creați un contact nou în modul de testare, acel contact va fi disponibil numai pentru executarea pachetelor de testare în sistem.
{% endhint %}

## Crearea automată vs. crearea manuală a contactelor

Puteți vedea dacă un contact extern a fost creat automat de către sistem sau dacă a fost creat manual de către un utilizator, consultând rubrica de „Creare automată” din Pagina de gestionare contacte.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FNo0lcXIwissrudvWXJh3%2Fimage.png?alt=media\&token=d6d9dd4d-3664-403f-88af-26c87c3f468a)

{% hint style="info" %}
Vă rugăm să rețineți că, odată ce un contact creat automat este editat, acesta nu va mai fi afișat ca un contact creat automat în coloana din Pagina de gestionare contacte.
{% endhint %}

## Numele companiei - Domeniul de aplicare a contactului extern

În funcție de modul în care acestea au fost configurate în Builder, veți avea la dispoziție diverse opțiuni pentru a atribui o companie unui contact extern:

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FR8OUfR91aqvZg52zEHrC%2F7A%20Company-Scope.gif?alt=media&#x26;token=148254ed-0688-4590-bba8-64bf4d023613" alt=""><figcaption></figcaption></figure>

* Toate companiile/Global
  * Dacă configurați compania la această valoare, contactul extern poate crea și accesa articolele de lucru din toate companiile.
  * Asta înseamnă, de asemenea, că utilizatorii managerului de lucru pot căuta toate contactele externe legate de un articol de lucru.

{% hint style="info" %}
Vă rugăm să rețineți că această opțiune este disponibilă numai dacă domeniul de aplicare al contactului extern este setat la „Global” sau „Global și local” în Builder. Consultați [aici ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#contact-scope)pentru mai multe informații.
{% endhint %}

* O companie anume (locală)
  * Dacă setați domeniul de aplicare al contactului la o anumită companie, contactul extern va putea crea și accesa doar articolele de lucru pentru compania la care este asociat.
  * De asemenea, utilizatorii vor putea adăuga un contact la un pachet de interfață pentru programarea aplicației numai dacă contactul aparține aceleiași companii (sau dacă face parte dintr-o companie generică).

{% hint style="info" %}
Vă rugăm să rețineți că:

1. Puteți schimba compania asociată a unui contact extern din Toate companiile/Global la o anumită companie (locală) numai în cazul în care contactul extern nu este asociat cu articole de lucru de la mai multe companii diferite. Puteți schimba această opțiune prin realocarea contactului la un articol de lucru.
2. Pentru a atribui contactele externe la Toate companiile/Global, este necesar ca rubrica Companie din fișierul de Creare în masă să rămână necompletată, astfel încât, în mod implicit, contactele vor fi atribuite la Global.
3. Compania configurată pentru un contact creat automat va depinde de setarea domeniului de aplicare a contactului. Dacă este configurată pentru „Global” sau „Global și local”, contactul creat automat va avea un domeniu de aplicare global, deci nu va fi asociat cu nicio companie specifică. Dacă este configurată pentru „Local”, contactul creat automat va fi creat în cadrul companiei din care face parte articolul de lucru corespunzător.
   {% endhint %}

### **Impactul delimitării globale/locale a domeniului de aplicare cu privire la asocierea contactelor la un articol de lucru**

{% hint style="warning" %}
Vă rugăm să rețineți că, dacă un contact extern este delimitat la nivel local (cu alte cuvinte, este asociat unei anumite companii), nu îl puteți adăuga ca persoană de contact pentru un articol de lucru care există în cadrul unei alte companii. Acest lucru este valabil și pentru conturile de Agent (care trebuie să existe *întotdeauna* în cadrul unei anumite companii). NUMAI conturile externe cu domeniu de aplicare global au flexibilitatea de a fi asociate ca și contacte la articolele de lucru ale oricărui Client.
{% endhint %}

## Editarea unui contact

Pentru a edita un contact, accesați [Pagina de gestionare contacte](https://docs.enate.net/enate-help/romana/contacte/pagina-de-gestionare-a-contactelor) și faceți dublu clic pe contact pentru a deschide fereastra pop-up de Editare contact.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FNM1D3WnS4JWu5PWWUCCP%2F7A%20Editing-a-Contact-in-Contact-Management%20Page.gif?alt=media&#x26;token=350e71cc-2a53-4bfb-9acf-63c4ad08216f" alt=""><figcaption></figcaption></figure>

Puteți edita în masă compania, fusul orar, locația biroului, limba preferată și eticheta implicită a contactelor dvs. prin selectarea căsuțelor din contactele respective - faceți clic pe butonul de Editare rezultant și se va afișa fereastra de editare în masă. Setați informațiile dorite și apăsați butonul de Confirmare pentru a salva modificările în masă.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FHh7XFzDz1eRduz3aVcFh%2F7A%20Bulk-Editing-Contacts-in-Conta.gif?alt=media&#x26;token=2509b29c-b2fa-4a75-95d9-b9c14873af99" alt=""><figcaption></figcaption></figure>

## Ștergerea unui contact

Pentru a șterge un contact, accesați [Pagina de gestionare contacte](https://docs.enate.net/enate-help/romana/contacte/pagina-de-gestionare-a-contactelor) și faceți clic pe căsuța de selectare a contactului, unde va apărea butonul de ștergere. Aveți posibilitatea de a șterge mai multe contacte simultan.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FmY1kj9ryFcmEQTtA7xgU%2F7A%20Deleting-Conacts-from-Contact.gif?alt=media&#x26;token=9386d642-d630-4f45-9c30-64d13b5408f4" alt=""><figcaption></figcaption></figure>
