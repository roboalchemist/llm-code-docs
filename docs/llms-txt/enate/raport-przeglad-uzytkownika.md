# Source: https://docs.enate.net/enate-help/polski/zintegrowane-raportowanie/raport-przeglad-uzytkownika.md

# Raport „Przegląd użytkownika”

Raport „Przegląd użytkownika” pokazuje użytkownikowi informacje o jego pracy.&#x20;

Dostępne zestawy danych:

| Aktywność                        | Łączny czas pracy                 | Całkowity czas (w godzinach) poświęcony przez agenta na wszystkie elementy pracy, którymi zajmował się w wybranym zakresie dat.                        |
| -------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Aktywność                        | Rodzaj aktywności                 | Rodzaj czynności wykonanej przez agenta podczas pracy nad danym elementem („Zapisane” lub „Zakończone”).                                               |
| Aktywność                        | Czas trwania w sek.               | Czas spędzony przez agenta na pracy nad danym elementem. Umożliwia ręczne wprowadzenie czasu, jeśli jest znany.                                        |
| Aktywność                        | DataRozpoczęcia                   | Data rozpoczęcia aktywności elementu pracy w formacie data/godzina.                                                                                    |
| Aktywność                        | DataRozpoczęcia\_data             | Data rozpoczęcia aktywności elementu pracy tylko w formie daty.                                                                                        |
| Aktywność                        | Nazwa użytkownika                 | Użytkownik, który wykonywał daną czynność.                                                                                                             |
| Kontekst                         | Kontrakt                          | Nazwa kontraktu.                                                                                                                                       |
| Kontekst                         | Klient                            | Nazwa klienta.                                                                                                                                         |
| Kontekst                         | Usługa                            | Nazwa usługi.                                                                                                                                          |
| Kontekst                         | Dostawca                          | Nazwa dostawcy.                                                                                                                                        |
| Data                             | Data                              | Zakres dat do filtrowania danych.                                                                                                                      |
| Data                             | Wskazane miesiące                 | Wskazane miesiące.                                                                                                                                     |
| Data                             | Tydzień                           | Wskazane tygodnie.                                                                                                                                     |
| Data                             | Rok                               | Wskazany rok.                                                                                                                                          |
| Błędy                            | Liczba elementów pracy            | Liczba elementów pracy z błędami.                                                                                                                      |
| Błędy                            | Data zgłoszenia                   | Data zgłoszenia błędu elementu pracy.                                                                                                                  |
| Błędy                            | Kategoria błędu                   | Kategoria błędu.                                                                                                                                       |
| Błędy                            | Opis                              | Opis błędu.                                                                                                                                            |
| Błędy                            | Status                            | Wskazuje, czy błąd został usunięty, czy nie.                                                                                                           |
| Proces                           | Proces                            | Nazwa procesu, do którego należy każdy z elementów pracy.                                                                                              |
| Proces                           | Rodzaj elementu pracy             | Rodzaj elementu pracy (zapytanie, czynność lub sprawa).                                                                                                |
| <p> </p><p>Kolejki  </p><p> </p> | <p> </p><p>Kolejka </p><p> </p>   | <p> </p><p>Nazwa kolejki, w której ostatnio znajdował się element pracy.</p><p> </p>                                                                   |
| Status                           | Status                            | Status elementu pracy („Do zrobienia”, „W toku”, „Oczekuje”, „Rozwiązane” albo „Zakończone”).                                                          |
| Powód zmiany statusu             | Powód zmiany statusu              | Powód zmiany statusu elementu pracy („Nowo utworzone”, „Otrzymano nowe informacje”, „Zablokowane przez regułę biznesową” itp.).                        |
| Historia statusu „Oczekuje”      | Oczekiwanie każdego dnia          | Liczba elementów pracy w danym dniu, które zostały ustawione przez agenta jako oczekujące (spośród wszystkich elementów pracy, nad którymi pracował).  |
| Historia statusu „Oczekuje”      | DataZakończenia                   | Koniec okresu (w formacie data/czas), w którym element pracy był ustawiony jako oczekujący.                                                            |
| Historia statusu „Oczekuje”      | DataZakończenia\_data             | Koniec okresu (tylko w formie daty), w którym element pracy był ustawiony jako oczekujący.                                                             |
| Historia statusu „Oczekuje”      | DataRozpoczęcia                   | Początek okresu (w formacie data/czas), w którym element pracy był ustawiony jako oczekujący.                                                          |
| Historia statusu „Oczekuje”      | DataRozpoczęcia\_data             | Początek okresu (tylko w formie daty), w którym element pracy był ustawiony jako oczekujący.                                                           |
| Historia statusu „Oczekuje”      | Nazwa użytkownika                 | Agent, który ustawił status „Oczekuje”.                                                                                                                |
| Elementy pracy                   | Czynność                          | Suma zamkniętych i oczekujących elementów pracy agenta.                                                                                                |
| Elementy pracy                   | Elementy pracy przypisane dzisiaj | Liczba elementów pracy przypisanych do agenta w bieżącym dniu.                                                                                         |
| Elementy pracy                   | Zamknięte elementy pracy          | Łączna liczba elementów pracy zamkniętych przez agenta we wskazanym zakresie dat.                                                                      |
| Elementy pracy                   | Elementy pracy zamknięte dzisiaj  | Liczba elementów pracy zamkniętych przez agenta w bieżącym dniu.                                                                                       |
| Elementy pracy                   | Elementy pracy na dziś            | Liczba elementów pracy do wykonania przez agenta w bieżącym dniu.                                                                                      |
| Elementy pracy                   | Otwarte elementy pracy            | Łączna liczba elementów pracy otwartych przez agenta.                                                                                                  |
| Elementy pracy                   | Elementy pracy opóźnione          | Łączna liczba opóźnionych elementów pracy agenta.                                                                                                      |
| Elementy pracy                   | Elementy pracy ponownie otwarte   | Łączna liczba zapytań ponownie otwartych przez agenta.                                                                                                 |
| Elementy pracy                   | Element pracy rozwiązany          | Łączna liczba elementów pracy rozwiązanych przez agenta we wskazanym zakresie dat.                                                                     |
| Elementy pracy                   | Element pracy rozpoczęte          | Łączna liczba elementów pracy rozpoczętych przez agenta we wskazanym zakresie dat.                                                                     |
| Elementy pracy                   | Wiek w dniach                     | Wiek wyrażony w dniach. Dla zakończonych elementów pracy to (data zakończenia - data rozpoczęcia), a dla otwartych (bieżący dzień - data rozpoczęcia). |
| Elementy pracy                   | Liczba dotkniętych rekordów       | Liczba rekordów dotkniętych błędem.                                                                                                                    |
| Elementy pracy                   | Liczba błędów                     | Liczba błędów każdego elementu pracy (jeśli jakieś posiada).                                                                                           |
| Elementy pracy                   | Liczba przeróbek                  | Liczba przeróbek każdego elementu pracy (jeśli jakieś wystąpiły).                                                                                      |
| Elementy pracy                   | Termin                            | Termin elementu pracy w formacie data/godzina.                                                                                                         |
| Elementy pracy                   | Termin\_data                      | Termin elementu pracy tylko w formie daty.                                                                                                             |
| Elementy pracy                   | DataZakończenia                   | Data zakończenia elementu pracy w formacie data/godzina.                                                                                               |
| Elementy pracy                   | DataZakończenia\_data             | Data zakończenia elementu pracy tylko w formie daty.                                                                                                   |
| Elementy pracy                   | Ma błędy                          | Wskazuje, czy element pracy ma błędy, czy nie („Tak” albo „Nie”).                                                                                      |
| Elementy pracy                   | Numer referencyjny                | Numer referencyjny każdego elementu pracy.                                                                                                             |
| Elementy pracy                   | Ponownie otwarte                  | Zapytania, które zostały ponownie otwarte po ich rozwiązaniu.                                                                                          |
| Elementy pracy                   | SLA                               | Umowa o gwarantowanym poziomie świadczenia usług wskazująca, czy element pracy jest opóźniony, czy nie.                                                |
| Elementy pracy                   | DataRozpoczęcia                   | Data rozpoczęcia elementu pracy w formacie data/godzina.                                                                                               |
| Elementy pracy                   | DataRozpoczęcia\_data             | Data rozpoczęcia elementu pracy tylko w formie daty.                                                                                                   |
| Elementy pracy                   | Tytuł                             | Tytuł elementu pracy.                                                                                                                                  |

sdf
