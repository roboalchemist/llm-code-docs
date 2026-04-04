# Source: https://www.i18next.com/translation-function/plurals.md

# Plurals

Plural can be combined with interpolation, context, ...

These plurals are streamlined with the one used in the [Intl API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules).\
\=>*You need to* [*polyfill*](https://github.com/eemeli/intl-pluralrules) *the* [*Intl.PluralRules*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/PluralRules) *API.*

{% tabs %}
{% tab title="JavaScript" %}
{% hint style="danger" %}
Note: The variable name must be `count`.\
And it must be present: `i18next.t('key', {count: 1});`\
There will be **no** fallback to the `'key'` value if count is not provided.
{% endhint %}
{% endtab %}

{% tab title="TypeScript" %}
{% hint style="danger" %}
Note: The variable name must be `count`.\
And it must be present: `i18next.t($ => $.key, {count: 1});`\
There will be **no** fallback to the `'key'` property if count is not provided.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you need multiple counts, take a look at [nesting](https://www.i18next.com/nesting#passing-options-to-nestings)
{% endhint %}

{% hint style="info" %}
We provide the ability to have special translation for `{count: 0}`, so that a more natural language can be used. If the count is 0, and a `_zero` entry is present, then it will be used instead of the language plural suffix.
{% endhint %}

{% hint style="info" %}
🎓 Check out this topic in the [i18next crash course video](https://youtu.be/SA_9i4TtxLQ?t=485).
{% endhint %}

## Singular / Plural

keys

```javascript
{
  "key_one": "item",
  "key_other": "items",
  "keyWithCount_one": "{{count}} item",
  "keyWithCount_other": "{{count}} items"
}
```

sample

{% tabs %}
{% tab title="JavaScript" %}

```javascript
i18next.t('key', {count: 0}); // -> "items"
i18next.t('key', {count: 1}); // -> "item"
i18next.t('key', {count: 5}); // -> "items"
i18next.t('key', {count: 100}); // -> "items"
i18next.t('keyWithCount', {count: 0}); // -> "0 items"
i18next.t('keyWithCount', {count: 1}); // -> "1 item"
i18next.t('keyWithCount', {count: 5}); // -> "5 items"
i18next.t('keyWithCount', {count: 100}); // -> "100 items"
```

{% endtab %}

{% tab title="TypeScript" %}

```typescript
i18next.t($ => $.key, {count: 0}); // -> "items"
i18next.t($ => $.key, {count: 1}); // -> "item"
i18next.t($ => $.key, {count: 5}); // -> "items"
i18next.t($ => $.key, {count: 100}); // -> "items"
i18next.t($ => $.keyWithCount, {count: 0}); // -> "0 items"
i18next.t($ => $.keyWithCount, {count: 1}); // -> "1 item"
i18next.t($ => $.keyWithCount, {count: 5}); // -> "5 items"
i18next.t($ => $.keyWithCount, {count: 100}); // -> "100 items"
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
With [v21.0.0](https://www.i18next.com/misc/migration-guide#json-format-v4-pluralization) a new [JSON format v4](https://www.i18next.com/misc/json-format#i-18-next-json-v4) was introduced that changed the suffixes.\
To convert your existing translations to the new v4 format, have a look at [i18next-v4-format-converter](https://github.com/i18next/i18next-v4-format-converter) or [this web tool](https://i18next.github.io/i18next-v4-format-converter-web/).
{% endhint %}

## Languages with multiple plurals

Sample uses arabic which has 5 plural forms beside the singular.

keys

```javascript
{
  "key_zero": "zero",
  "key_one": "singular",
  "key_two": "two",
  "key_few": "few",
  "key_many": "many",
  "key_other": "other"
}
```

sample

{% tabs %}
{% tab title="JavaScript" %}

```javascript
i18next.t('key', {count: 0}); // -> "zero"
i18next.t('key', {count: 1}); // -> "singular"
i18next.t('key', {count: 2}); // -> "two"
i18next.t('key', {count: 3}); // -> "few"
i18next.t('key', {count: 4}); // -> "few"
i18next.t('key', {count: 5}); // -> "few"
i18next.t('key', {count: 11}); // -> "many"
i18next.t('key', {count: 99}); // -> "many"
i18next.t('key', {count: 100}); // -> "other"
```

{% endtab %}

{% tab title="TypeScript" %}

```typescript
i18next.t($ => $.key, {count: 0}); // -> "zero"
i18next.t($ => $.key, {count: 1}); // -> "singular"
i18next.t($ => $.key, {count: 2}); // -> "two"
i18next.t($ => $.key, {count: 3}); // -> "few"
i18next.t($ => $.key, {count: 4}); // -> "few"
i18next.t($ => $.key, {count: 5}); // -> "few"
i18next.t($ => $.key, {count: 11}); // -> "many"
i18next.t($ => $.key, {count: 99}); // -> "many"
i18next.t($ => $.key, {count: 100}); // -> "other"
```

{% endtab %}
{% endtabs %}

## How to find the correct plural suffix?

You can use this small utility to get the correct plural suffixes.

[source code](https://jsfiddle.net/6bpxsgd4)

*Or try* [*translation-check*](https://github.com/locize/translation-check)*, it shows an overview of your translations in a nice UI. It shows also the appropriate plural forms.*

#### Or you use a smart translation management system, like [locize](https://locize.com)

![](https://286188001-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-L9iS6Wm2hynS5H9Gj7j%2F-MX2rpXr6D3UrjwHPOqm%2F-MX2s2PKNH3dqXxCShCx%2Flocize_plurals.png?alt=media\&token=a93a4d64-6c13-4e19-9d1f-c9ae9c898e8f)

## Ordinal plurals

There is also support for ordinal numbers *(referring to the ordering or ranking of things, e.g. "1st", "2nd", "3rd" in English)*. The `ordinal` option (and the \_ordinal suffix) tells the helper to use the ordinal digit to determine the plurality key used. E.g., for "32" the ordinal digit is "2" so `key_two` is used.

keys

```javascript
// i.e. english
{
  "key_ordinal_one": "{{count}}st place", // 1st, 21st, 31st
  "key_ordinal_two": "{{count}}nd place", // 2nd, 22nd, 32nd
  "key_ordinal_few": "{{count}}rd place", // 3rd, 23rd, 33rd
  "key_ordinal_other": "{{count}}th place" // 4th, 5th, 24th, 11th
}
```

sample

{% tabs %}
{% tab title="JavaScript" %}

```javascript
i18next.t('key', { count: 1, ordinal: true }); // -> "1st place"
i18next.t('key', { count: 21, ordinal: true }); // -> "21st place"
i18next.t('key', { count: 2, ordinal: true }); // -> "2nd place"
i18next.t('key', { count: 11, ordinal: true }); // -> "11th place"
i18next.t('key', { count: 32, ordinal: true }); // -> "32nd place"
```

{% endtab %}

{% tab title="TypeScript" %}

```typescript
i18next.t($ => $.key, { count: 1, ordinal: true }); // -> "1st place"
i18next.t($ => $.key, { count: 21, ordinal: true }); // -> "21st place"
i18next.t($ => $.key, { count: 2, ordinal: true }); // -> "2nd place"
i18next.t($ => $.key, { count: 11, ordinal: true }); // -> "11th place"
i18next.t($ => $.key, { count: 32, ordinal: true }); // -> "32nd place"
```

{% endtab %}
{% endtabs %}

## Interval plurals

Want to define phrases expressing the number of items lies in a range. Like *a few items* or *a lot of items*.

You will need to add a post processor: [i18next-intervalplural-postprocessor](https://github.com/i18next/i18next-intervalplural-postprocessor)

```javascript
import i18next from 'i18next';
import intervalPlural from 'i18next-intervalplural-postprocessor';

i18next
  .use(intervalPlural)
  .init(i18nextOptions);
```

keys

```javascript
{
  "key1_one": "{{count}} item",
  "key1_other": "{{count}} items",
  "key1_interval": "(1)[one item];(2-7)[a few items];(7-inf)[a lot of items];",
  "key2_one": "{{count}} item",
  "key2_other": "{{count}} items",
  "key2_interval": "(1)[one item];(2-7)[a few items];"
}
```

sample

{% tabs %}
{% tab title="JavaScript" %}

```javascript
i18next.t('key1_interval', {postProcess: 'interval', count: 1}); // -> "one item"
i18next.t('key1_interval', {postProcess: 'interval', count: 4}); // -> "a few items"
i18next.t('key1_interval', {postProcess: 'interval', count: 100}); // -> "a lot of items"

// not matching into a range it will fallback to
// the regular plural form
i18next.t('key2_interval', {postProcess: 'interval', count: 1}); // -> "one item"
i18next.t('key2_interval', {postProcess: 'interval', count: 4}); // -> "a few items"
i18next.t('key2_interval', {postProcess: 'interval', count: 100}); // -> "100 items"
```

{% endtab %}

{% tab title="TypeScript" %}

```typescript
i18next.t($ => $.key1_interval, {postProcess: 'interval', count: 1}); // -> "one item"
i18next.t($ => $.key1_interval, {postProcess: 'interval', count: 4}); // -> "a few items"
i18next.t($ => $.key1_interval, {postProcess: 'interval', count: 100}); // -> "a lot of items"

// not matching into a range it will fallback to
// the regular plural form
i18next.t($ => $.key2_interval, {postProcess: 'interval', count: 1}); // -> "one item"
i18next.t($ => $.key2_interval, {postProcess: 'interval', count: 4}); // -> "a few items"
i18next.t($ => $.key2_interval, {postProcess: 'interval', count: 100}); // -> "100 items"
```

{% endtab %}
{% endtabs %}

{% hint style="danger" %}
Note: The regex for the interval entry has changed in `v3.0.0` of `i18next-intervalPlural-postProcessor` so if you are using the older versions, you need to use the curly braces instead of the bracketes, e.g.:

```javascript
"key2_interval": "(1){one item};(2-7){a few items};"
```

{% endhint %}
