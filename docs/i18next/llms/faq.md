# Source: https://www.i18next.com/how-to/faq.md

# FAQ

## Misc

### **i18next is awesome. How can I support the project?**

*There are a lot of ways to support us. Make a PR for a feature requested. Improve the documentation. Help others to get started. Spread the word.*

*Further you could try* [*locize.com*](http://locize.com) *- our localization as a service offering. It's like donating to i18next but with additional benefits for you - like saving hours of time translating your project.*

## Loading issues

### **I don't see my translations!!!**

*Try setting* `debug: true` *on init and check the console log. There is rather sure a warning for unable to resolve the loadPath or invalid json. Check if the translation files are accessible via browser.*

## Translation

### **How to translate the resource files?**

<figure><img src="https://286188001-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6Wm2hynS5H9Gj7j%2Fuploads%2FrsjuxiiE9sPvATUOKDz5%2Ftranslate.i18next.jpg?alt=media&#x26;token=68f486fb-146e-4b05-afb4-ab370c4d1c82" alt=""><figcaption><p><a href="https://translate.i18next.com/">https://translate.i18next.com</a></p></figcaption></figure>

For a quick and dirty machine translation you may have a look at [this free translator](https://translate.i18next.com).\
But in general we suggest to use a smart Translation Management Service like [locize](https://locize.com) to translate your i18next resources.

For professional translations we advice you to work with [human translators](https://docs.locize.com/guides-tips-and-tricks/working-with-translators). Or at least proofread the results coming from machine translations.

### **How do i know which plural suffix i have to use?**

*On the* [*plural page*](https://www.i18next.com/translation-function/plurals) *there is a tool to get them.*

*Or try* [*translation-check*](https://github.com/locize/translation-check)*, it shows an overview of your translations in a nice UI. It shows also the appropriate plural forms.*

*Or you use a smart translation management system, like* [*locize*](https://locize.com)*.*

![](https://286188001-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-L9iS6Wm2hynS5H9Gj7j%2F-MX2rpXr6D3UrjwHPOqm%2F-MX2s2PKNH3dqXxCShCx%2Flocize_plurals.png?alt=media\&token=a93a4d64-6c13-4e19-9d1f-c9ae9c898e8f)

### **Why are my plural keys not working?**

*Are you seeing this warning in the development console?*

> i18next::pluralResolver: Your environment seems not to be Intl API compatible, use an Intl.PluralRules polyfill. Will fallback to the compatibilityJSON v3 format handling.

*With v21 we* streamlined the suffix with the one used in the [Intl API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules).

*In environments where the* [*Intl.PluralRules*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/PluralRules) *API  is not available (like older Android devices), you may need to* [*polyfill*](https://github.com/eemeli/intl-pluralrules) *the* [*Intl.PluralRules*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/PluralRules) *API.*\
*In case it is not available it will fallback to the* [*i18next JSON format v3*](https://www.i18next.com/misc/json-format#i-18-next-json-v3) *plural handling. And if your json is already using the new suffixes, your plural keys will probably not be shown.*

*tldr;*

```shell
npm install intl-pluralrules
```

```javascript
import 'intl-pluralrules'
```

### How should the language codes be formatted?

*Theoretically, you're not bound to any specific language code format, but if you want to make use of all the in built language features, like proper* [*pluralization*](https://www.i18next.com/translation-function/plurals) *and correct* [*fallback resolution*](https://www.i18next.com/principles/fallback#language-fallback)*, we strongly suggest to use the following iso norm (BCP 47 language tag):*

`lng-(script)-REGION-(extensions)`\
\
\&#xNAN;*i.e.*

* *en, en-US or en-GB*
* *zh, zh-HK or zh-Hant-HK*

*Other examples are listed here:* [*https://www.iana.org/assignments/language-tags/language-tags.xhtml*](https://www.iana.org/assignments/language-tags/language-tags.xhtml)

*And more information about the format can be found here:* [*https://www.w3.org/International/articles/language-tags/*](https://www.w3.org/International/articles/language-tags/)

{% hint style="info" %}
As soon as you use the dash character `-` the language codes are tried to be formatted with `Intl.getCanonicalLocales`.
{% endhint %}

## Process

### **How do I keep overview over my translation progress?**

*Try* [*translation-check*](https://github.com/locize/translation-check)*, it shows an overview of your translations in a nice UI. Check which keys are not yet translated.*

*If you need more, it might be time to use a* [*translation management tool*](https://locize.com)*.*

### **How to handle with changes in e2e tests?**

*For e2e tests a good tactic is to set language to* `cimode` *on init. This will set i18next to always return the key on calling* `i18next.t`*. Want to add the namespace to returned value change* `appendNamespaceToCIMode: true` *on init.*

### **How to use i18next in serverless environments?**

Due to how serverless functions work, you cannot guarantee that a cached version of your data is available. Serverless functions are short-lived, and can shut down at any time, purging any in-memory or filesystem cache. This may be an acceptable trade-off, but sometimes it isn't acceptable.

Because of this we suggest to not use a remote backend and to download the translations and package them with your serverless function.

{% hint style="success" %}
Read more about this topic, [here](https://locize.com/blog/i18n-serverless/).[<br>](https://locize.com/blog/how-does-server-side-internationalization-look-like/)[![](https://286188001-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6Wm2hynS5H9Gj7j%2Fuploads%2FWlRIcoHBxh3tLr13Gzz9%2Ftitle.jpg?alt=media\&token=7823c353-0215-4c15-ae40-52f9f1b0cd89)](https://locize.com/blog/i18n-serverless/)
{% endhint %}
