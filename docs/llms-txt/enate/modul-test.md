# Source: https://docs.enate.net/enate-help/romana/modul-test.md

# Modul Test

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Comutarea la modul Test <a href="#a-comutarea-la-modul-test" id="a-comutarea-la-modul-test"></a>

Dacă contul dvs. de utilizator este setat pentru a vă permite să accesați datele de testare, puteți trece mediul Work Manager pe „Modul Test”. Acest link este disponibil în meniul vertical din partea dreaptă a barei antetului.

## Test Mode Explanation <a href="#test-mode-explanation" id="test-mode-explanation"></a>

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FrdK8HI1UsiV6nv9UK4KK%2Fimage.png?alt=media\&token=7c08aad6-7f3c-4201-a243-b4b8319b165f)

Odată ce rulați în modul test, veți vedea doar datele de testare; permițându-vă să creați și să rulați elemente de testare prin versiuni de testare a proceselor pentru a le verifica înainte de setarea live, toate fără a afecta datele de producție live.

Ca un memento vizual, bara antetului este setată pe roșu atunci când sunteți în modul Test.

## Definirea diferiților Administratori și Membri ai cozilor în modul Test <a href="#c-definirea-diferitilor-administratori-si-membri-ai-cozilor-in-modul-test" id="c-definirea-diferitilor-administratori-si-membri-ai-cozilor-in-modul-test"></a>

Funcționalitatea modului de testare vă permite acum să setați un manager diferit pentru o Coadă atunci când rulați în modul Test vs. modul Live.

Exemplu: Luați în considerare **Managerul 1** care are acces la modul live și este responsabil de gestionarea a două cozi, **Finanțare** și **Caz Master**.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FI4KfqXPcHFW5F9mKj8vL%2Fimage.png?alt=media\&token=9f642ead-4bef-40a0-a39c-4ce00455f1e7)

În modul Test, aceleași două cozi pot fi gestionate de un alt utilizator care are permisiunea Lider de echipă și Mod Test - a se vedea mai jos un exemplu în care **Manager 2** a fost setat să fie responsabil de Cozi în modul Testare.

![](https://756254039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-3742581798%2Fuploads%2FDS2PVKLIYkcfnnynJQ4j%2Fimage.png?alt=media\&token=03bb38a6-86cc-429d-ac62-47cfdb8a1435)

## Comutați roboți între Live și Test <a href="#d-comutati-roboti-intre-live-si-test" id="d-comutati-roboti-intre-live-si-test"></a>

Acum este posibil să comutați un robot astfel încât să poată rula în modul de testare sau în modul live. Mai exact, două noi activități au fost adăugate la bibliotecile de activități pentru UiPath, Automation Anywhere și BluePrism (și API-urile standard ajustate, astfel încât acestea să poată fi apelate generic) după cum urmează

* Setați Modul Live
* Setați Modul Test

Aceste acțiuni vă permit să treceți un robot între stările de testare și cele live. După ce un robot a fost trecut în modul Test, apelurile de activitate ulterioară pe care robotul le-ar putea face, de ex. „Mai mult de lucru” și „Creare Tichet/Caz etc.” au loc în acel context al modului Test, prin obținerea și crearea numai a elementelor de lucru de testare. Robotul ar trebui să fie schimbat în modul Live odată ce procesul este setat să fie activ, pentru a se asigura că creează apoi elemente de lucru live.

## Contacte de testare separate în sistem <a href="#e-contacte-de-testare-separate-in-sistem" id="e-contacte-de-testare-separate-in-sistem"></a>

Enate acceptă acum crearea de înregistrări de contact separate în Modul Test, adică orice înregistrare de contact pe care o creați în modul Test va fi accesibilă numai pentru utilizatorii din modul Test (iar contactele create în modul live vor fi accesibile doar pentru utilizatorii din modul Live). Acest lucru ajută să vă asigurați că e-mailurile din pachetele de testare nu sunt trimise accidental utilizatorilor de producție și invers.
