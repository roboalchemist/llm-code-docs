# Source: https://lingui.dev/guides/plurals.md

# Pluralization

Pluralization is essential for effective internationalization, allowing applications to display messages or select options based on the number. In this article, we explore various categories of pluralization, see implementation examples, and learn how to customize your application for different languages.

Lingui uses the [CLDR Plural Rules](https://www.unicode.org/cldr/charts/42/supplemental/language_plural_rules.html) to determine the correct plural form for each language.

In general, there are 6 plural forms (taken from the [CLDR Plurals](https://cldr.unicode.org/index/cldr-spec/plural-rules) page):

* zero
* one (singular)
* two (dual)
* few (paucal)
* many (also used for fractions if they have a separate class)
* other (required — general plural form — also used if the language only has a single form)

info

Only the *other* form is required, because it's the only common plural form used in all languages.

All other plural forms depend on the language. For example, English has only two forms: *one* and *other* (1 book vs. 2 books). In Czech, we have four: *one*, *few*, *many* and *other* (1 kniha, 2 knihy, 1,5 knihy, 5 knih). Some languages have even more, such as Arabic.

## Using Plural Forms[​](#using-plural-forms "Direct link to Using Plural Forms")

The good thing is that **as developers, we only need to know the plural forms of the source language**.

When we use English in the source code, we'll only use *one* and *other*:

```
plural(numBooks, {
  one: "# book",
  other: "# books",
});
```

When `numBooks == 1`, this will render as *1 book* and for `numBook == 2` it will be *2 books*. Interestingly, for `numBooks == -1`, it will be *-1 book*. This is because the "one" plural form also applies to -1. It is therefore important to remember that the plural forms (such as "one" or "two") do not represent the numbers themselves, but rather *categories* of numbers.

Under the hood, the [`plural`](/ref/macro.md#plural) macro is replaced with a low-level [`i18n._`](/ref/core.md#i18n._) call. In production, the example will look like this:

```
i18n._({
  id: "d1wX4r",
  // stripped on production
  // message: '{numBooks, plural, one {# book} other {# books}}',
  values: { numBooks },
});
```

When we extract messages from the source code using the [Lingui CLI](/ref/cli.md), we get:

```
{numBooks, plural, one {# book} other {# books}}
```

This is then translated by our Czech translator as:

```
{numBooks, plural, one {# kniha} few {# knihy} many {# knihy} other {# knih}}
```

Important

The important thing is that *we don't have to change our code to support languages with different plural rules*.

## Source Code in Language Other than English[​](#source-code-in-language-other-than-english "Direct link to Source Code in Language Other than English")

As developers, we only need to be aware of the plural forms for the source language. Check the [plural forms](https://www.unicode.org/cldr/charts/42/supplemental/language_plural_rules.html) for your language, and then you can use them accordingly. Here's an example in Czech:

```
plural(numBooks, {
  one: "# kniha",
  few: "# knihy",
  many: "# knihy",
  other: "# knih",
});
```

This makes Lingui also valuable for monolingual projects, meaning that you can benefit from it even if you don't translate your application. Pluralization, along with number and date formatting, is relevant to all languages.
