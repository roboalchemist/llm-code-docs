# Source: https://docs.enate.net/enate-help/romana/appendice/erori-de-validare-potentiale-pentru-crearea-in-masa-a-articolelor-de-lucru.md

# Erori de validare potențiale pentru crearea în masă a articolelor de lucru

| **Zona de eroare**                                                                         | **Descriere**                                                                                                            |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **Status de eroare**                                                                       |                                                                                                                          |
| "not\_valid": "Datele nu sunt valide sau Ceva nu a mers corect",                           | Când o informație greșită este introdusă în celulă și nu se pot crea articole de lucru                                   |
| "completed": "Efectuat",                                                                   | Când articolele de lucru sunt create cu succes                                                                           |
| "in\_progress": "În derulare"                                                              | Când crearea articolului de lucru este în derulare                                                                       |
| **Eroare**                                                                                 |                                                                                                                          |
| "1": "Fișierul încărcat nu este un fișier \*.xls sau \*.xlsx",                             | Când formatul fișierului de încărcare este altul decât fișier .xls sau .xlsx                                             |
| "3": "Workbook are mai multe fișe de lucru. Doar prima fișă va fi procesată",              | Când același fișier are mai multe foi de date de lucru care urmează să fie procesate                                     |
| "5": "Instanța procesului principal nu este live",                                         | Când instanța procesului nu este live sau versiunile sunt ciorne                                                         |
| "101": "Fișei de lucru îi lipsește coloana necesară '{{v0}}'",                             | Când foaia Excel nu are coloana necesară pentru procesarea articolelor de lucru                                          |
| "102": "Coloana „{{v0}}” este de tipul „{{v1}}” care nu este acceptată în Creare în masă", | Când folosim tipuri de date neacceptate, cum ar fi Relație entitate, Tabel                                               |
| "103": "Nu a fost găsit niciun câmp care să facă legătura cu coloana „{{v0}}”",            | Când Validați API-ul de creare în masă nu poate mapa datele coloanei cu datele de sistem                                 |
| "200": "Crearea unui caz bazat pe program nu este acceptată"                               | Când un caz este legat de programe și utilizați Cazul în Excel                                                           |
| "300": "Titlul nu este unic în fișier",                                                    | Când fișierul încărcat are același titlu pentru mai multe articole de lucru din fișier                                   |
| "301": "Titlul nu este unic",                                                              | Când fișierul încărcat are un titlu care este deja creat în sistem                                                       |
| "302": "Valoarea este goală și coloana este necesară",                                     | Când nu există valori de intrare pentru câmpurile obligatorii                                                            |
| "303": "Valoarea nu este valabilă pentru tipul de date „{{v0}}”",                          | Când câmpul personalizat nu poate introduce datele particulare sau datele nu sunt legate de câmpul personalizat          |
| "304": "Nicio persoană nu a putut fi găsită de la adresa de e-mail",                       | Când introducem un ID de e-mail greșit sau ID-ul de e-mail nu este prezent în sistem                                     |
| "305": "Clientul nu a fost găsit sau nu aveți permisiunea de a-l vedea",                   | Când introducem un nume de Client greșit sau nu îl accesăm pentru a crea articole de lucru pentru un anumit client       |
| "306": "Contractul nu se găsește sub Client sau nu aveți permisiunea de a-l vedea",        | Când introducem un nume de Contract greșit sau nu îl accesăm pentru a crea articole de lucru pentru un anumit client     |
| "307": "Serviciul nu este găsit în Contract sau nu aveți permisiunea de a-l vedea",        | Când introducem un nume de serviciu greșit sau nu-l accesăm pentru a crea articole de lucru în baza unui anumit Contract |
| "308": "Procesul nu se găsește sub Serviciu sau nu aveți permisiunea de a-l vedea",        | Când introducem un nume de proces greșit sau nu-l accesăm pentru a crea articole de lucru în cadrul anumitor servicii    |
| "309": "Categoria de tichete nu a fost găsită",                                            | Când introducem o valoare greșită a categoriei de tichete                                                                |
| "310": "Valoarea nu este valabilă pentru listă"                                            | Când valoarea de intrare nu se potrivește cu lista configurată/datele cu niveluri multiple                               |
| **EROARE IU**                                                                              |                                                                                                                          |
| "1001": "Nu există elemente valabile de procesat.",                                        | Când nu există date de procesat în Excel                                                                                 |
| "1002": "Toate articolele valide au fost procesate.",                                      | Când sunt create toate articolele de lucru valide                                                                        |
| "file\_upload\_limit": "{{name}} este mai mare decât limita serverului ({{limit}})",       | Când dimensiunea fișierului încărcat este mai mare decât limita de încărcare configurată de sistem                       |
| "file\_upload\_failure": "Nu a putut încărca fișierul"                                     | când fișierul nu poate fi încărcat                                                                                       |
