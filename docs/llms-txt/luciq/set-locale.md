# Source: https://docs.luciq.ai/references/user-interface-design/set-locale.md

# Set Locale

The locale of the SDK can be changed by passing the required locale enum to this method.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.setLocale(.french)
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[Luciq setLocale:LCQLocaleFrench];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.setLocale(new Locale("de"));
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setLocale(Locale("de"))
```

{% endtab %}

{% tab title="RN" %}

```javascript
import Luciq, { Locale } from '@luciq/react-native';

Luciq.setLocale(Locale.french);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.setLocale(LCQLocale.french);
```

{% endtab %}
{% endtabs %}

#### Locale Parameters

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
.arabic
.azerbaijani
.catalan
.catalanSpain
.chineseSimplified
.chineseTaiwan
.chineseTraditional
.czech
.danish
.dutch
.english
.french
.german
.italian
.japanese
.korean
.norwegian
.polish
.portuguese
.portugueseBrazil
.russian
.slovak
.spanish
.swedish
.turkish
.hungarian
.finnish
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQLocaleArabic    
LCQLocaleChineseSimplified    
LCQLocaleChineseTaiwan
LCQLocaleChineseTraditional
LCQLocaleCzech
LCQLocaleDanish
LCQLocaleDutch
LCQLocaleEnglish
LCQLocaleFrench
LCQLocaleGerman
LCQLocaleItalian
LCQLocaleJapanese
LCQLocaleKorean
LCQLocaleNorwegian
LCQLocalePolish
LCQLocalePortugese
LCQLocalePortugueseBrazil
LCQLocaleRussian
LCQLocaleSlovak
LCQLocaleSpanish
LCQLocaleSwedish
LCQLocaleTurkish
```

{% endtab %}

{% tab title="And - Java" %}

```java
Locale("en")
Locale("ar")
Locale("az")
Locale("ca")
Locale("ca","ES")
Locale("cs")
Locale("da")
Locale("de")
Locale("es")
Locale("fa")
Locale("fi")
Locale("fr")
Locale("hu")
Locale("in")
Locale("it")
Locale("ja")
Locale("ko")
Locale("nl")
Locale("pl")
Locale("pt","BR")
Locale("pt","PT")
Locale("ru")
Locale("sk")
Locale("sv")
Locale("tr")
Locale("zh","CN")
Locale("zh","TW")
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Locale("en")
Locale("ar")
Locale("az")
Locale("ca")
Locale("ca","ES")
Locale("cs")
Locale("da")
Locale("de")
Locale("es")
Locale("fa")
Locale("fi")
Locale("fr")
Locale("hu")
Locale("in")
Locale("it")
Locale("ja")
Locale("ko")
Locale("nl")
Locale("pl")
Locale("pt","BR")
Locale("pt","PT")
Locale("ru")
Locale("sk")
Locale("sv")
Locale("tr")
Locale("zh","CN")
Locale("zh","TW")
```

{% endtab %}

{% tab title="RN" %}

```javascript
Locale.arabic
Locale.azerbaijani
Locale.chineseSimplified
Locale.chineseTraditional
Locale.czech
Locale.danish
Locale.dutch
Locale.english
Locale.french
Locale.german
Locale.italian
Locale.japanese
Locale.polish
Locale.portugueseBrazil
Locale.romanian
Locale.russian
Locale.spanish
Locale.swedish
Locale.turkish
Locale.korean
```

{% endtab %}

{% tab title="Flutter" %}

```dart
LCQLocale.arabic
LCQLocale.azerbaijani
LCQLocale.chineseSimplified
LCQLocale.chineseTraditional
LCQLocale.czech
LCQLocale.danish
LCQLocale.dutch
LCQLocale.english
LCQLocale.french
LCQLocale.german
LCQLocale.italian
LCQLocale.japanese
LCQLocale.korean
LCQLocale.polish
LCQLocale.portugueseBrazil
LCQLocale.portuguesePortugal
LCQLocale.romanian
LCQLocale.russian
LCQLocale.spanish
LCQLocale.swedish
LCQLocale.turkish
LCQLocale.indonesian
LCQLocale.slovak
LCQLocale.norwegian
```

{% endtab %}
{% endtabs %}
