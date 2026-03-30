# Source: https://docs.enate.net/enate-help/romana/procesarea-unei-actiuni/actiunile-trimiteti-email-si-trimiteti-email-si-asteptati.md

# Acțiunile de „Trimitere e-mail” și de „Trimitere e-mail și Așteptare”

## Prezentare generală

Acțiunile de „Trimitere e-mail” implică trimiterea automată a unui e-mail prin Enate, după care Acțiunea se închide automat. Utilizatorii din Work Manager nu vor fi nevoiți să efectueze nicio activitate pentru acest tip de Acțiune.

Acțiunile de „Trimitere e-mail și Așteptare” implică trimiterea automată a unui e-mail prin Enate. Acțiunea va trece apoi în starea de Așteptare până la primirea unui răspuns. Odată ce se primește un răspuns, Acțiunea trece în starea De făcut pentru a fi procesată în continuare.

Destinatarul și orice adresă CC sau BCC din e-mail vor fi configurate în Builder - consultați acest articol referitor la modul de configurare a Acțiunilor de „Trimitere e-mail” în Builder:

{% embed url="<https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab>" %}

Odată ce e-mailul este trimis, va apărea o intrare în cronologie care va indica data la care a fost trimis, expeditorul și destinatarul, orice adresă CC sau BCC, subiectul e-mailului și, dacă faceți clic pentru a-l extinde, întregul conținut al e-mailului.

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FDY4uNKPN6Lk8Io7SM4gF%2Fimage.png?alt=media&#x26;token=73f8ff72-28ad-4c89-a8a2-5963e3890887" alt=""><figcaption></figcaption></figure>

## &#x20;**Excepții**

Dacă se utilizează o adresă de e-mail Către, CC sau BCC invalidă, nu se va efectua trimiterea automată a e-mailului pentru Acțiunea de Trimitere e-mail/ Trimitere e-mail și Așteptare, iar Acțiunea va fi mutată înapoi în Coada de așteptare.

Se va afișa un avertisment în cronologie, cu mesajul:

<figure><img src="https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FPT4iKS10CMwvjEH0tnRb%2Fimage.png?alt=media&#x26;token=46d1851b-7a74-4ef2-aba3-58104f6b9324" alt=""><figcaption></figcaption></figure>

Titularul Cazului va putea astfel decide să trimită manual e-mailul și va trebui să rectifice adresa de e-mail și să adauge manual conținutul acestuia. Totodată, va trebui să contacteze administratorul de sistem pentru a-l alerta cu privire la această eroare, astfel încât acesta să poată corecta adresa de e-mail în scopul prevenirii unor viitoare erori de e-mail.
