# Source: https://docs.enate.net/enate-help/romana/appendice/termeni-de-cautare-ignorati-detalii-suplimentare.md

# Termeni de căutare ignorați – detalii suplimentare

Ca parte a caracteristicilor standard pentru optimizarea căutărilor pe care le efectuează utilizatorii, anumiți termeni utilizați în mod frecvent sunt eliminați din căutări dacă au fost introduși manual. Acest lucru are ca scop asigurarea unui răspuns în timp util pentru rezultatele căutărilor și, totodată, evitarea afișării unui volum mare de rezultate eligibile, care ar putea ascunde rezultatele dorite de utilizatori. Una dintre abordările utilizate în acest sens este utilizarea „Listelor de excludere”.

## Lista de excludere

O listă de excludere este o listă standard de cuvinte obișnuite, precum conjuncțiile, articolele, pronumele etc., care sunt ignorate din căutările care ar genera prea multe rezultate.

Aveți mai jos o listă detaliată cu toate cuvintele din lista de excludere care vor fi ignorate de TOATE căutările din Enate – aceasta include nu numai căutările efectuate în Căutare rapidă, ci și căutările efectuate asupra utilizatorilor, căutările de e-mailuri, căutările de Articole de lucru, cum ar fi Tichetele rezultate din urma fuzionării Tichetelor, etc. Dacă introduceți oricare dintre termenii menționați, aceștia vor fi ignorați automat ca termeni pentru care se vor returna rezultatele căutării.

{% file src="<https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FXIRdocmXFwUUfBzuYkmA%2FEnate%20SQL%20Stop%20List.xlsx?alt=media&token=75ba006e-bdb8-4f1e-8349-110cd5a73d4d>" %}

Listele multiple de excludere sunt acceptate în diferite limbi de utilizare.

{% hint style="info" %}
Rețineți că pentru căutarea Utilizatorilor și a E-mailurilor, se utilizează întotdeauna lista de excludere în limba engleză (britanică). Pentru articolele de lucru (Titlu, nume Client, nume Contract, nume Serviciu, nume Caz/Tichet etc.) se utilizează limba utilizatorului conectat pentru a găsi lista de excludere. De asemenea, vă rugăm să rețineți că limba maghiară nu este compatibilă în mod direct cu limbajul SQL (limbaj de interogare structurat), astfel încât lista de excludere aplicată în căutările efectuate de utilizatorii maghiari va fi și ea în limba engleză.
{% endhint %}

## Caractere ignorate în Căutarea rapidă

Anumite caractere suplimentare sunt setate pentru a fi ignorate la efectuarea căutărilor în Căutare rapidă, de exemplu „\*”, „?”, „@” etc. Aceasta înseamnă, de exemplu, că atunci când se caută client.com în Căutarea rapidă, vor fi căutate cuvintele „client” și „com”. Ca atare, este recomandat să includeți astfel de combinații de cuvinte între ghilimele pentru a le căuta ca frază specifică – de exemplu, căutarea „client.com” va genera probabil rezultatele pe care le căutați.

Mai jos găsiți o listă completă a tuturor caracterelor pe care căutările din Căutare rapidă le vor ignora:

{% file src="<https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FriRGG3QGj7df45MVFSgx%2FCharacters%20ignored%20in%20Quickfind.pdf?alt=media&token=f9d54a3f-2b8e-402b-b9ba-f98f193c0960>" %}
