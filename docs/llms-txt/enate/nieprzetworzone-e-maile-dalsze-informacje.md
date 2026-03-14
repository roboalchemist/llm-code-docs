# Source: https://docs.enate.net/enate-help/polski/e-maile/nieobsluzone-wiadomosci-e-mail/nieprzetworzone-e-maile-dalsze-informacje.md

# Nieprzetworzone e-maile – dalsze informacje

## Kiedy e-maile pojawiają się w widoku nieprzetworzonych wiadomości?

Wiadomości pojawią się w tym widoku Skrzynki odbiorczej w Work Managerze po spełnieniu jednego z poniższych warunków:

1. Żaden z adresów Do i/albo DW nie ma pasującego przekierowania ustawionego w Builderze;
2. Wiadomość zawiera tylko adresy UDW (brak adresów Do lub DW).

Poniższa tabela zawiera szczegółowe informacje o postępowaniu z nowymi wiadomościami odebranymi przez Enate w zależności od kombinacji adresów e-mail w polach Do, DW i UDW.

| Sytuacja                                                                                                                        | Liczba utworzonych elementów pracy       | Czy pojawią się w widoku „Nieprzetworzone e-maile”?                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------- |
| Tylko jeden adres w polu Do lub DW przychodzącej wiadomości.                                                                    | 1                                        | <mark style="color:orange;">Nie</mark>                                        |
| Dwa lub więcej adresów w polu Do lub DW przychodzącej wiadomości.                                                               | 2 lub więcej                             | <mark style="color:orange;">Nie</mark>                                        |
| Jeden adres w polu Do, jeden w DW i jeden w UDW przychodzącej wiadomości.                                                       | 1 dla każdego adresu Do i DW             | <mark style="color:orange;">Nie</mark>                                        |
| \*Jeden adres w polu Do i jeden w UDW przychodzącej wiadomości.                                                                 | 1 dla adresu Do                          | <mark style="color:orange;">Nie</mark>                                        |
| Jeden lub więcej adresów tylko w polu UDW przychodzącej wiadomości. Pola Do i DW – puste.                                       | 0                                        | <mark style="color:green;">Tak – dla skrzynki pocztowej UDW</mark>            |
| Tylko jeden adres przychodzącej wiadomości, który nie został poprawnie skonfigurowany w Enate.                                  | 0                                        | <mark style="color:green;">Tak – dla nieskonfigurowanego adresu e-mail</mark> |
| Jeden adres przychodzącej wiadomości, który nie został poprawnie skonfigurowany w Enate i jeden adres poprawnie skonfigurowany. | Jeden dla skonfigurowanego adresu e-mail | <mark style="color:orange;">Nie</mark>                                        |

&#x20;
