# Source: https://docs.enate.net/enate-help/ru/obrabotka-deistviya/deistviya-abbyy-flexicapture.md

# Действия ABBYY FlexiCapture

Enate может обеспечить интеграцию с [ABBYY FlexiCapture](https://www.abbyy.com/flexicapture/) — это достигается посредством использования действия, интегрированного с ABBYY FlexiCapture (см. [здесь ](https://docs.enate.net/enate-help/integrations/enate-integrations/ocr-integration/abbyy-integration)для просмотра руководства по созданию и настройке этого нового типа действий).

При запуске Действия ABBYY для любого Случая документы, прикрепленные к Случаю, могут быть отправлены в ABBYY FlexiCapture для распознавания сканирования, а обработанные выходные файлы будут возвращены и автоматически прикреплены к Случаю.

{% hint style="info" %}
Примечание: Могут обрабатываться только типы файлов, поддерживаемые ABBYY v12 и выше. Нажмите [здесь](https://help.abbyy.com/en-us/flexicapture/12/standalone_operator/input_formats), чтобы посмотреть следующую ссылку для списка форматов, поддерживаемых ABBYY.
{% endhint %}

Вы увидите подтверждение того, что документы были успешно отправлены в ABBYY для обработки:

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1956395681%2Fuploads%2FV8EBgUsJcM99OleTOAKk%2Fimage.png?alt=media\&token=d49a2269-9541-4706-9831-4cd01f0c77af)

Вы увидите подтверждение, когда документы будут успешно отправлены в ABBYY для обработки:

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1956395681%2Fuploads%2Fv3SmxmDGES4RNKoQP7MF%2Fimage.png?alt=media\&token=37dc6897-a62a-4116-921a-0521d8b9221e)

Последняя попытка обозначает время, когда документ(ы) был(и) отправлен(ы) в ABBYY FlexiCapture для обработки.

Если отправленные документы были недопустимого формата или если возникли проблемы с определением формата самого документа, то система покажет следующее сообщение:

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1956395681%2Fuploads%2FtPXDUbWfpvhFQN8auVt1%2Fimage.png?alt=media\&token=69d19417-fffc-4077-9a46-0edceb0b7012)

### **Автоматические повторные попытки**

Если возникла проблема с оправкой документа, то система определенное количество раз автоматически повторно попробует отправить, в зависимости от того, как Ваша система была сконфигурирована в Конструкторе ([смотрите подробную информацию тут](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern)).

Если по-прежнему остается проблема после автоматических попыток отправки (например, если в настройках установлено 5 попыток и после 5 автоматических попыток система так и не сможет установить связь), то действие ABBYY перейдет в состояние «Закрыто».

{% hint style="info" %}
В таких обстоятельствах, действие, которое не смогло установить связь с внешней системой, будет переведено к Владельцу случая, помеченное в секции «Действие» на экране случая, что это действие «Закрыто – Выполнено неуспешно».
{% endhint %}

## Валидация

После сканирования документа ABBYY выставляет оценку в зависимости от того, насколько имеется уверенность в качестве сканирования. Если показатель доверия выше заданного порога, то проверка не требуется, данные обрабатываются и задача выполняется. Если показатель доверия ниже определенного порога, требуется проверка человеком.

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### Проверка не требуется <a href="#no-verification-required" id="no-verification-required"></a>

Сообщение о состоянии подтвердит, что проверка человеком не требуется:

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-1956395681%2Fuploads%2F3FfoIKwm4LAka9KlnrZK%2Fimage.png?alt=media\&token=32ff4f10-a62d-4bb2-bfe3-746a8ab47226)

После завершения обработки Действие ABBYY закроется. Экспортированные файлы будут прикреплены к случаю и видны в карточке файлов.

{% hint style="info" %}
Примечание: если явно установлены теги «Теги выходного файла», то ABBYY применит теги «Теги выходного файла» ко всем файлам, которые были обработаны, готовым к использованию в последующих действиях.
{% endhint %}

### Требуется проверка человеком <a href="#human-verification-required" id="human-verification-required"></a>

Система предупредит Вас о необходимости проверки человеком:

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsusO6eKdgoonewdT2%2Fimage.png?alt=media\&token=92610229-5480-4882-896c-4bda4b286600)

Кроме того, рядом со статусом Действия будет отображен текст напоминания, подтверждающий, что ручная верификация должна быть завершена в ABBYY, прежде чем продолжить:

Нажав на кнопку "Проверить", вы попадете на станцию верификации ABBYY, где сможете проверить сканы документов и при необходимости скорректировать информацию.

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsuykc2DFaOX6-GsPY%2Fimage.png?alt=media\&token=27953730-e342-4885-9206-fae88572b769)

{% hint style="info" %}
Примечание: для получения полного доступа к выбранному проекту потребуется действующая учетная запись ABBYY FlexiCapture с правами доступа для проведения проверки.
{% endhint %}

Как только Вы войдете в систему, перед Вами откроется экран ABBY FlexiCapture "Станция верификации", где Вы сможете просмотреть и скорректировать информацию при необходимости.

Станция верификации состоит из трех разделов:

1. Отдельные страницы сканируемого документа.
2. Крупный план оригинального документа, который необходимо отсканировать.
3. Извлеченный результат — это отсканированная версия исходного документа.

Текст, выделенный желтым цветом на вкладке исходного документа, — это данные, которые ABBYY не может прочитать. Он выделен красным цветом в извлеченном выводе.

Некоторые символы, такие как "i", могут быть выделены в разделе «Извлеченный результат», если ABBYY не уверен в отсканированной копии

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx6MLiLXtXFAmC00W%2Fimage.png?alt=media\&token=adebd784-bdf7-4f4c-b696-4832e40c4ec2)

После завершения ручной проверки на экране будет подтверждено ее выполнение, но при этом будет отмечено, что существовала ошибка, требующая ручного вмешательства:

![](https://3327152148-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWsx95C9X78E90Y1xnJ%2Fimage.png?alt=media\&token=a8a3caa8-f99e-46d1-8e4a-711769917f69)

‌После завершения обработки экспортированные файлы будут прикреплены к случаю и видны на [карточке "Файлы"](https://docs.enate.net/enate-help/ru/tipy-rabochikh-elementov-zayavki-sluchai-i-deistviya/karta-failov).

Затем Вы можете отметить действие как завершенное.

{% hint style="info" %}
Примечание: если явно установлены теги «Теги выходного файла», то ABBYY применит теги «Теги выходного файла» ко всем файлам, которые были обработаны, готовым к использованию в последующих действиях.
{% endhint %}
