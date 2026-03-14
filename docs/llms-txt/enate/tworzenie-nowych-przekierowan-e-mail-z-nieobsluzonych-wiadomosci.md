# Source: https://docs.enate.net/enate-help/polski/e-maile/nieobsluzone-wiadomosci-e-mail/tworzenie-nowych-przekierowan-e-mail-z-nieobsluzonych-wiadomosci.md

# Tworzenie nowych przekierowań        e-mail z nieobsłużonych wiadomości

Przetwarzając nieobsłużone wiadomości, agenci mogą tworzyć nowe przekierowania e-mail bezpośrednio w Work Managerze. Dzięki nim kolejne wiadomości danego typu nie będą klasyfikowane jako nieobsłużone, ponieważ system utworzy dla nich zapytania lub sprawy. Zmniejszy to liczbę nieobsłużonych e-maili i pozwoli szybciej przejść do przetwarzania właściwych elementów pracy. Aby jednak zachować kontrolę nad tą funkcjonalnością, tworzenie nowych przekierowań e-mail w Work Managerze przez agentów to opcja, którą można włączyć lub wyłączyć za pośrednictwem ról użytkowników w Builderze.

Reguły utworzone w ten sposób w Work Managerze są od razu aktywne, ale administratorzy otrzymują w Builderze powiadomienie o każdej z nich. Pozostaną specjalnie oznaczone, dopóki administratorzy ich nie potwierdzą. Po dokonaniu oceny nowych reguł administratorzy mogą również modyfikować ich ustawienia lub zupełnie je wyłączyć.

## Przyznawanie użytkownikom Work Managera uprawnień do tworzenia nowych reguł przekierowań e-mail

Dostęp do funkcji tworzenia nowych przekierowań e-mail w Work Managerze jest kontrolowany za pomocą systemu ról użytkowników, do którego dodana została nowa opcja (w ramach widoków wiadomości e-mail).

{% hint style="info" %}
Uwaga: dostęp do funkcji „Twórz przekierowania e-mail” jest ustawiony na **Wł.** dla standardowej roli członka zespołu.
{% endhint %}

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FyNkwH8IE8SSXY3zcPIXK%252Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_1JbSS8D8arRxmWau5EPQ_image.webp%3Falt%3Dmedia%26token%3D9234507a-2226-4f34-94ec-4f9428481e66&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=354af8f5cd3e6a654163c6aba79d36760a6b9202cb29e41cb79383914e88d4d2" alt=""><figcaption></figcaption></figure>

## Jak utworzyć nowe przekierowanie e-mail w sekcji Nieobsłużone e-maile

Po wybraniu, czy dana wiadomość w sekcji „Nieobsłużone e-maile” Skrzynki odbiorczej ma być dalej przetwarzana jako zapytanie, czy jako sprawa (klikając „Nowy element pracy”), wyświetlone zostanie następujące okienko:

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FrvRXtoAG2LyFHMOwizyT%252FCreate%2520Route1.png%3Falt%3Dmedia%26token%3Ddbf82db2-f0db-46da-abe8-eb4d540dfafb&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=b73a50b08c16793ca2006bc0e54e76300dffe8f6446e5ce8e1c1e207647fb424" alt=""><figcaption></figcaption></figure>

Można wyszukiwać według przekierowania e-mail (które automatycznie podstawi informacje w polach Klient, Kontrakt i Usługa w oparciu o sugestie dotyczące wybranego adresu skrzynki pocztowej) lub ręcznie wybrać określone dane. Kliknięcie „Utwórz” w tym momencie utworzy nam z e-maila określony element pracy, jak zwykle.

Jeśli jednak chcemy, aby te same ustawienia były automatycznie wybierane w przyszłości, przed kliknięciem „Utwórz” należy zaznaczyć opcję „Zastosuj do innych wiadomości e-mail” w dolnej części okienka. Po jej zaznaczeniu i kliknięciu „Utwórz”:

* wyświetlone zostanie okienko z potwierdzeniem utworzenia nowego elementu pracy;
* następnie wyświetlone zostanie następne okienko – „Utwórz nową regułę przekierowania e-mail” – w którym można uzupełnić pozostałe szczegóły przed ostatecznym utworzeniem nowej reguły.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FA5EHkoxNFPiLWZRJoNVx%252Fimage.png%3Falt%3Dmedia%26token%3D85345a14-0474-4d5e-b75f-f5fc449f1748&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=5cd64cbb339d70fe63ca0655260f8d1d81f10d7d172f83d5c0d67a8c24c2c8ec" alt=""><figcaption></figcaption></figure>

Należy wybrać, czy będzie to reguła typu „Do” czy „Od”:

* przetwarzaj w ten sposób wszystkie wiadomości OD tego nadawcy (przychodzące z tego adresu e-mail); ALBO
* przetwarzaj w ten sposób wszystkie wiadomości Do tego odbiorcy (wysyłane na ten adres e-mail).

Następnie wskazujemy, który adres e-mail ma być używany w połączeniu z tą regułą. Enate automatycznie podstawi odpowiedni adres powiązany z nieprzetworzoną wiadomością, którą się zajmowaliśmy.

{% hint style="info" %}
W sekcji „Wskazówki” znajduje się odnośnik prowadzący do strony pomocy Enate z dalszymi informacjami na temat nieobsłużonych wiadomości e-mail.
{% endhint %}

## Stosowanie reguły do wcześniej otrzymanych wiadomości (działanie wstecz)

Poza ustawianiem reguł dla wszystkich przyszłych wiadomości, które odpowiadają określonemu wzorcowi, można również zastosować nowo tworzoną regułę do wszystkich albo niektórych nieobsłużonych wiadomości, które otrzymano wcześniej, a które spełniają wskazane warunki. W tym celu należy kliknąć przełącznik automatycznego stosowania w dolnej części tego okienka.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FqO47hIs4kOOPFQBJfdfM%252Fimage.png%3Falt%3Dmedia%26token%3De2525eb0-5a76-4b71-ba0e-6f6ecc731b47&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=d32a3a2f4a97524f60cba72f538c0b0b714c0bef992816b17e4a7569b3f87ad0" alt=""><figcaption></figcaption></figure>

System wyświetli informację, ile zaległych nieobsłużonych wiadomości pasuje do tej reguły (czyli ile e-maili zostanie ponownie przetworzonych).

### **Wybór zakresu czasowego dla ponownego przetworzenia otrzymanych wcześniej nieobsłużonych wiadomości**

Zaznaczenie tej opcji spowoduje wyświetlenie filtra czasu pozwalającego precyzyjniej wskazać, do których z otrzymanych wcześniej wiadomości ma zostać zastosowana nowa reguła (np. tylko do wiadomości z ostatniego tygodnia lub miesiąca).

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252Fn2eBkAxBuSNOIqf7KJtc%252Fimage.png%3Falt%3Dmedia%26token%3Dff0b2bb8-59b2-4df1-b485-e8dd9dbfca9b&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=f77deaada6ad3e94f5aea7ecb91c9f57e2a70a27928007a3d6a1010d18ce9d05" alt=""><figcaption></figcaption></figure>

Za pomocą suwaka możemy ustawić różne zakresy albo konkretne daty. System będzie reagował na zmiany ustawień, wyświetlając aktualną liczbę wiadomości, dla których ta reguła zostanie uruchomiona.

Po zakończeniu konfiguracji reguły należy nacisnąć „Utwórz”, aby uruchomić powtórne przetwarzanie kwalifikujących się e-maili na określony typ sprawy lub zapytania.

{% hint style="info" %}
Ważne: nowa reguła utworzona w Work Managerze w opisany powyżej sposób będzie od razu aktywna i stosowana do wiadomości przychodzących.
{% endhint %}

### Kontrola administratora w Builderze nad nowymi regułami przekierowania e-mail

Po utworzeniu nowej reguły przekierowania e-mail w sekcji „Nieobsłużone e-maile” Work Managera, administratorzy systemu zostaną o tym powiadomieni za pośrednictwem czerwonej kropki na ikonie sekcji „E-mail” w Builderze.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FOCbHGjSKXK8K3BXQeE8U%252Fimage.png%3Falt%3Dmedia%26token%3D50ad60d5-23d6-4297-8582-050b2225df18&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=211ba20ef2b0ac4d20004e4ff858067a6c029fe5a1d1d8cb1f7df1327522e618" alt=""><figcaption></figcaption></figure>

Przechodząc do strony „Przekierowania e-mail”, będą widzieć to oznaczenie we wszystkich sekcjach i na wszystkich ekranach.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FJCXHPvZ5wEdho7smifBp%252Fimage.png%3Falt%3Dmedia%26token%3D32123ad9-aa86-4006-b971-836341ec7707&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=9a1b9f352c2ae3d1bf32762d7e820f1965bd3a6166216a937a8f38791bd32c42" alt=""><figcaption></figcaption></figure>

Na stronie przekierowań zobaczą baner z informacją o nowych regułach, na które powinni zwrócić uwagę, oraz ich liczbie. Odnośnik pozwoli im przefiltrować przekierowania i wyświetlić tylko te, którymi powinni się zająć.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252Fl8VwMLkswDUnG5UA75sv%252FAdminBeAware.png%3Falt%3Dmedia%26token%3D9b87a49a-e13c-4402-a327-76044c2c011d&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=a998b692a34772e9a068939f16eec84ba0c7d0d86f421401b7a0c8bedd76b5fc" alt=""><figcaption></figcaption></figure>

W tabeli przekierowań również oznaczone zostaną te, które wymagają uwagi.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252Fp2hWdi9wYE195t19WGP6%252FAdminBeAware2.png%3Falt%3Dmedia%26token%3Dc9babbfc-327b-4550-9076-6bf588707295&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=f98b2d3d7274ec4463019e1d19ff55a73962e2f177fb061e2543a6299423ee1a" alt=""><figcaption></figcaption></figure>

Administratorzy powinni zweryfikować nowe przekierowania (i skontaktować się z agentem, który je utworzył\*), aby upewnić się, że prawidłowo współpracują z innymi regułami. Mogą je wyłączyć, dostosować, a nawet usunąć, jeśli uznają to za konieczne.

Jeśli nie mają żadnych uwag do działania danej reguły, mogą odznaczyć flagę „do sprawdzenia” na nagłówku, aby powrócić do standardowego widoku.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252F0rpGLXp51E0SByACl6lt%252Fimage.png%3Falt%3Dmedia%26token%3Db780afeb-2af3-45ba-8234-69ba1d3a2f98&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=12b408dc5646881f96429534a10603529919a7f60197bd5cc283ec67127f8f53" alt=""><figcaption></figcaption></figure>

\*Aby sprawdzić, kto utworzył regułę, należy kliknąć ikonę „Pokaż aktywność” w górnej części okienka szczegółów reguły.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252Fw1F9yvhhNVNxt2nS17wH%252FAdminBeAware3.png%3Falt%3Dmedia%26token%3D72939c51-d690-4e09-9457-388374f4ca91&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=ad78e9fa1e72a7d6245823adf251e4ffa1359b58803ee2d33d1a0a89139232ad" alt=""><figcaption></figcaption></figure>

Wyświetlone zostanie podsumowanie, kto i kiedy utworzył lub zaktualizował regułę.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FUXIQugqD0R0gE64poKAD%252FAdminBeAware4.png%3Falt%3Dmedia%26token%3D31d7b1d7-4294-456b-a90c-8863c417dde6&#x26;width=400&#x26;dpr=2&#x26;quality=100&#x26;sign=a3b2e27e105d8728eca1edee2c26c8baace94730221785abc5dd463db5ca50ab" alt=""><figcaption></figcaption></figure>
