# Source: https://docs.enate.net/enate-help/hu/fueggelek/munkatetelek-toemeges-letrehozasa-soran-elofordulo-esetleges-ellenorzesi-hibak.md

# Munkatételek tömeges létrehozása során előforduló esetleges ellenőrzési hibák

| Hibaterület                                                                        | Leírás                                                                                                                  |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Állapothiba                                                                        |                                                                                                                         |
| "not\_valid": "Data not valid or Something went wrong"                             | Az egyik cella helytelen információt tartalmaz, és a munkatételek nem hozhatók létre.                                   |
| "completed": "Completed"                                                           | A munkatételek sikeresen létrehozva.                                                                                    |
| "in\_progress": "In progress"                                                      | A munkatételek létrehozása folyamatban van.                                                                             |
| Hiba                                                                               |                                                                                                                         |
| "1": "Uploaded file is not a \*.xls or \*.xlsx file"                               | A feltöltött fájl formátuma nem .xls vagy .xlsx.                                                                        |
| "3": "Workbook has multiple worksheets. Only first sheet will be processed"        | Egy fájlban több munkalap is tartalmaz feldolgozandó adatokat.                                                          |
| "5": "Master Process Instance not live"                                            | A folyamatpéldány nem élő vagy a verziók vázlatverziók.                                                                 |
| "101": "Worksheet is missing the required column '{{v0}}'"                         | Az Excel-munkalap nem tartalmazza a munkatételek feldolgozásához szükséges egyik oszlopot.                              |
| "102": "Column '{{v0}}' is of type '{{v1}}' which is not supported in Bulk Create" | Nem támogatott adattjpusok használata, mint például entitáskapcsolatoks, táblázat.                                      |
| "103": "No field found to link Column '{{v0}}' to"                                 | A tömeges létrehozást ellenőrző API nem tudja az oszlopadatokat a rendszeradatokhoz társítani.                          |
| "200": "Creation of a schedule-driven Case is not supported"                       | Az ügy ütemezésekhez van kapcsolva, és az ügy szerepel az Excelben.                                                     |
| "300": "Title is not unique in file"                                               | A feltöltött fájlban több munkatételhez is ugyanaz a cím tartozik.                                                      |
| "301": "Title is not unique"                                                       | A feltöltött fájl olyan címmel rendelkezik, amely már létre lett hozva a rendszerben.                                   |
| "302": "Value is blank and column is required"                                     | A kötelező mezők nem tartalmaznak bementi értékeket.                                                                    |
| "303": "Value in not valid for data type '{{v0}}'"                                 | Amikor egy egyéni mezőben nem a megfelelő adat szerepel, vagy az adat nem egyéni mezőre vonatkozik.                     |
| "304": "No person could be found from email address"                               | Amikor rossz e-mai-azonosító lett megadva, vagy az nem szerepel a rendszerben.                                          |
| "305": "Customer not found or you do not have permission to see it"                | Amikor rossz ügyfélnév lett megadva, vagy egy adott ügyfélhez nincs jogosultságunk munkatételek létrehozására.          |
| "306": "Contract not found under Customer or you do not have permission to see it" | Amikor rossz szerződésnév lett megadva, vagy egy adott ügyfélhez nincs jogosultságunk munkatételek létrehozására.       |
| "307": "Service not found under Contract or you do not have permission to see it"  | Amikor rossz szolgáltatásnév lett megadva, vagy egy adott szerződéshez nincs jogosultságunk munkatételek létrehozására. |
| "308": "Process not found under Service or you do not have permission to see it"   | Amikor rossz folyamatnév lett megadva, vagy egy adott szerződéshez nincs jogosultságunk munkatételek létrehozására.     |
| "309": "Ticket Category not found"                                                 | Amikor helytelen jegykategória-érték lett megadva.                                                                      |
| "310": "Value is not valid for list"                                               | Amikor a bemeneti érték nem egyezik meg a konfigurált lista/többszintű lista adataival.                                 |
| UI-HIBA                                                                            |                                                                                                                         |
| "1001": "There are no valid items to process."                                     | Az Excel nem tartalmaz feldolgozható adatokat.                                                                          |
| "1002": "All valid items have been processed."                                     | Az összes érvényes tétel létre lett hozva.                                                                              |
| "file\_upload\_limit": "{{name}} is bigger than the server limit ({{limit}})"      | A feltöltött fájl mérete meghaladja a rendszerben konfigurált feltöltési korlátot.                                      |
| "file\_upload\_failure": "Failed to upload file"                                   | A fájlt nem sikerült feltölteni.                                                                                        |
