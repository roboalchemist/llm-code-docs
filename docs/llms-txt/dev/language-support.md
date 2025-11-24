# Source: https://dev.writer.com/api-reference/translation-api/language-support.md

# View supported languages

The Translation API allows you to translate text from one language to another. Below are the languages supported for the translation API and the [formality](#formality), [length control](#length-control), and [profanity masking](#profanity-masking) parameters.

## Supported languages

To specify a language for the translation API, use the [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) language code. For example, `en` for English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a variant, the code appends the two-digit [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). For example, Mexican Spanish is `es-MX`.

The Translation API supports the following languages:

| Language              | Language code |
| --------------------- | ------------- |
| Afrikaans             | `af`          |
| Albanian              | `sq`          |
| Amharic               | `am`          |
| Arabic                | `ar`          |
| Armenian              | `hy`          |
| Azerbaijani           | `az`          |
| Bengali               | `bn`          |
| Bosnian               | `bs`          |
| Bulgarian             | `bg`          |
| Catalan               | `ca`          |
| Chinese (Simplified)  | `zh`          |
| Chinese (Traditional) | `zh-TW`       |
| Croatian              | `hr`          |
| Czech                 | `cs`          |
| Danish                | `da`          |
| Dari                  | `fa-AF`       |
| Dutch                 | `nl`          |
| English               | `en`          |
| Estonian              | `et`          |
| Farsi (Persian)       | `fa`          |
| Filipino, Tagalog     | `tl`          |
| Finnish               | `fi`          |
| French                | `fr`          |
| French (Canada)       | `fr-CA`       |
| Georgian              | `ka`          |
| German                | `de`          |
| Greek                 | `el`          |
| Gujarati              | `gu`          |
| Haitian Creole        | `ht`          |
| Hausa                 | `ha`          |
| Hebrew                | `he`          |
| Hindi                 | `hi`          |
| Hungarian             | `hu`          |
| Icelandic             | `is`          |
| Indonesian            | `id`          |
| Irish                 | `ga`          |
| Italian               | `it`          |
| Japanese              | `ja`          |
| Kannada               | `kn`          |
| Kazakh                | `kk`          |
| Korean                | `ko`          |
| Latvian               | `lv`          |
| Lithuanian            | `lt`          |
| Macedonian            | `mk`          |
| Malay                 | `ms`          |
| Malayalam             | `ml`          |
| Maltese               | `mt`          |
| Marathi               | `mr`          |
| Mongolian             | `mn`          |
| Norwegian (Bokmål)    | `no`          |
| Pashto                | `ps`          |
| Polish                | `pl`          |
| Portuguese (Brazil)   | `pt`          |
| Portuguese (Portugal) | `pt-PT`       |
| Punjabi               | `pa`          |
| Romanian              | `ro`          |
| Russian               | `ru`          |
| Serbian               | `sr`          |
| Sinhala               | `si`          |
| Slovak                | `sk`          |
| Slovenian             | `sl`          |
| Somali                | `so`          |
| Spanish               | `es`          |
| Spanish (Mexico)      | `es-MX`       |
| Swahili               | `sw`          |
| Swedish               | `sv`          |
| Tamil                 | `ta`          |
| Telugu                | `te`          |
| Thai                  | `th`          |
| Turkish               | `tr`          |
| Ukrainian             | `uk`          |
| Urdu                  | `ur`          |
| Uzbek                 | `uz`          |
| Vietnamese            | `vi`          |
| Welsh                 | `cy`          |

## Formality

Formal translations use language associated with formal, polite communication, such as formal forms of second person pronouns and their verb agreement. Informal translations use language associated with informal, casual communication, such as informal forms of second person pronouns and their verb agreement.

The following languages support formal and informal translations. Set the `formality` parameter to `true` to use a formal translation, and `false` to use an informal translation.

| Language              | Language code |
| --------------------- | ------------- |
| Dutch                 | `nl`          |
| French                | `fr`          |
| French (Canada)       | `fr-CA`       |
| German                | `de`          |
| Hindi                 | `hi`          |
| Italian               | `it`          |
| Japanese              | `ja`          |
| Korean                | `ko`          |
| Portuguese (Portugal) | `pt-PT`       |
| Spanish               | `es`          |
| Spanish (Mexico)      | `es-MX`       |

## Length control

Sometimes, translated text is longer than the original source text. You can use length control to limit the length of the translated text. Set the `length_control` parameter to `true` to enable length control.

Length control is available for the following languages:

| Language            | Language code |
| ------------------- | ------------- |
| French              | `fr`          |
| German              | `de`          |
| Italian             | `it`          |
| Portuguese (Brazil) | `pt`          |
| Spanish             | `es`          |

## Profanity masking

You can choose to mask profanity in the translated text for all languages **except the languages listed in the table below**.

The following languages do not support profanity masking:

| Language   | Language code |
| ---------- | ------------- |
| Bengali    | `bn`          |
| Hindi      | `hi`          |
| Malayalam  | `ml`          |
| Punjabi    | `pa`          |
| Sinhala    | `si`          |
| Vietnamese | `vi`          |
