# Source: https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html

Title: NoSuspiciousCharacters (Symfony Docs)

URL Source: https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/reference/constraints/NoSuspiciousCharacters.rst)

Validates that the given string does not contain characters used in spoofing security attacks, such as invisible characters such as zero-width spaces or characters that are visually similar.

"symfony.com" and "ѕymfony.com" look similar, but their first letter is different (in the second string, the "s" is actually a [cyrillic small letter dze](https://graphemica.com/%D1%95)). This can make a user think they'll navigate to Symfony's website, whereas it would be somewhere else.

This is a kind of [spoofing attack](https://en.wikipedia.org/wiki/Spoofing_attack) (called "IDN homograph attack"). It tries to identify something as something else to exploit the resulting confusion. This is why it is recommended to check user-submitted, public-facing identifiers for suspicious characters in order to prevent such attacks.

Because Unicode contains such a large number of characters and incorporates the varied writing systems of the world, incorrect usage can expose programs or systems to possible security attacks.

That's why this constraint ensures strings or [Stringable](https://secure.php.net/manual/en/class.stringable.php "Stringable")s do not include any suspicious characters. As it leverages PHP's [Spoofchecker](https://secure.php.net/manual/en/class.spoofchecker.php "Spoofchecker"), the intl extension must be enabled to use it.

[Basic Usage](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#basic-usage "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------

The following constraint will use different detection mechanisms to ensure that the username is not spoofed:

Note

As with most of the other constraints, `null` and empty strings are considered valid values. This is to allow them to be optional values. If the value is mandatory, a common solution is to combine this constraint with [NotBlank](https://symfony.com/doc/current/reference/constraints/NotBlank.html).

[Options](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#options "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------

### [`checks`](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#checks "Permalink to this headline")

**type**: `integer`**default**: all

This option is a bitmask of the checks you want to perform on the string:

*   `NoSuspiciousCharacters::CHECK_INVISIBLE` checks for the presence of invisible characters such as zero-width spaces, or character sequences that are likely not to display, such as multiple occurrences of the same non-spacing mark.
*   `NoSuspiciousCharacters::CHECK_MIXED_NUMBERS` (usable with ICU 58 or higher) checks for numbers from different numbering systems.
*   `NoSuspiciousCharacters::CHECK_HIDDEN_OVERLAY` (usable with ICU 62 or higher) checks for combining characters hidden in their preceding one.

You can also configure additional requirements using [locales](https://symfony.com/doc/current/components/intl.html#locales) and [restrictionLevel](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#restrictionlevel).

### [`locales`](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#locales "Permalink to this headline")

**type**: `array`**default**: [framework.enabled_locales](https://symfony.com/doc/current/reference/configuration/framework.html#reference-enabled-locales)

Restrict the string's characters to those normally used with the associated languages.

For example, the character "π" would be considered suspicious if you restricted the locale to "English", because the Greek script is not associated with it.

Passing an empty array, or configuring [restrictionLevel](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#restrictionlevel) to `NoSuspiciousCharacters::RESTRICTION_LEVEL_NONE` will disable this requirement.

### [`restrictionLevel`](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#restrictionlevel "Permalink to this headline")

**type**: `integer`**default**: `NoSuspiciousCharacters::RESTRICTION_LEVEL_MODERATE` on ICU >= 58, otherwise `NoSuspiciousCharacters::RESTRICTION_LEVEL_SINGLE_SCRIPT`

Configures the set of acceptable characters for the validated string through a specified "level":

*   `NoSuspiciousCharacters::RESTRICTION_LEVEL_MINIMAL` requires the string's characters to match [the configured locales](https://symfony.com/doc/current/components/intl.html#locales)'.
*   `NoSuspiciousCharacters::RESTRICTION_LEVEL_MODERATE` also requires the string to be [covered](https://unicode.org/reports/tr39/#def-cover) by Latin and any one other [Recommended](https://www.unicode.org/reports/tr31/#Table_Recommended_Scripts) or [Limited Use](https://www.unicode.org/reports/tr31/#Table_Limited_Use_Scripts) script, except Cyrillic, Greek, and Cherokee.
*   `NoSuspiciousCharacters::RESTRICTION_LEVEL_HIGH` (usable with ICU 58 or higher) also requires the string to be [covered](https://unicode.org/reports/tr39/#def-cover) by any of the following sets of scripts:

    *   Latin + Han + Bopomofo (or equivalently: Latn + Hanb)
    *   Latin + Han + Hiragana + Katakana (or equivalently: Latn + Jpan)
    *   Latin + Han + Hangul (or equivalently: Latn + Kore)

*   `NoSuspiciousCharacters::RESTRICTION_LEVEL_SINGLE_SCRIPT` also requires the string to be [single-script](https://unicode.org/reports/tr39/#def-single-script).
*   `NoSuspiciousCharacters::RESTRICTION_LEVEL_ASCII` (usable with ICU 58 or higher) also requires the string's characters to be in the ASCII range.

You can accept all characters by setting this option to `NoSuspiciousCharacters::RESTRICTION_LEVEL_NONE`.

### [`groups`](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#groups "Permalink to this headline")

**type**: `array` | `string`**default**: `null`

It defines the validation group or groups of this constraint. Read more about [validation groups](https://symfony.com/doc/current/validation/groups.html).

### [`payload`](https://symfony.com/doc/current/reference/constraints/NoSuspiciousCharacters.html#payload "Permalink to this headline")

**type**: `mixed`**default**: `null`

This option can be used to attach arbitrary domain-specific data to a constraint. The configured payload is not used by the Validator component, but its processing is completely up to you.

For example, you may want to use [several error levels](https://symfony.com/doc/current/validation/severity.html) to present failed constraints differently in the front-end depending on the severity of the error.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
