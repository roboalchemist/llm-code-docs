# Source: https://symfony.com/doc/current/reference/constraints/Length.html

Title: Length (Symfony Docs)

URL Source: https://symfony.com/doc/current/reference/constraints/Length.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/reference/constraints/Length.rst)

Validates that a given string length is _between_ some minimum and maximum value.

[Basic Usage](https://symfony.com/doc/current/reference/constraints/Length.html#basic-usage "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

To verify that the `firstName` field length of a class is between `2` and `50`, you might add the following:

Note

As with most of the other constraints, `null` is considered a valid value. This is to allow the use of optional values. If the value is mandatory, a common solution is to combine this constraint with [NotNull](https://symfony.com/doc/current/reference/constraints/NotNull.html).

[Options](https://symfony.com/doc/current/reference/constraints/Length.html#options "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

### [`charset`](https://symfony.com/doc/current/reference/constraints/Length.html#charset "Permalink to this headline")

**type**: `string`**default**: `UTF-8`

The charset to be used when computing value's length with the [mb_check_encoding](https://secure.php.net/manual/en/function.mb-check-encoding.php "mb_check_encoding") and [mb_strlen](https://secure.php.net/manual/en/function.mb-strlen.php "mb_strlen") PHP functions.

### [`charsetMessage`](https://symfony.com/doc/current/reference/constraints/Length.html#charsetmessage "Permalink to this headline")

**type**: `string`**default**: `This value does not match the expected {{ charset }} charset.`

The message that will be shown if the value is not using the given [charset](https://symfony.com/doc/current/reference/constraints/Length.html#charset).

You can use the following parameters in this message:

| Parameter | Description |
| --- | --- |
| `{{ charset }}` | The expected charset |
| `{{ value }}` | The current (invalid) value |

### [`countUnit`](https://symfony.com/doc/current/reference/constraints/Length.html#countunit "Permalink to this headline")

**type**: `string`**default**: `Length::COUNT_CODEPOINTS`

The character count unit to use for the length check. By default [mb_strlen](https://secure.php.net/manual/en/function.mb-strlen.php "mb_strlen") is used, which counts Unicode code points.

Can be one of the following constants of the [Length](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Constraints/Length.php "Symfony\Component\Validator\Constraints\Length") class:

*   `COUNT_BYTES`: Uses [strlen](https://secure.php.net/manual/en/function.strlen.php "strlen") counting the length of the string in bytes.
*   `COUNT_CODEPOINTS`: Uses [mb_strlen](https://secure.php.net/manual/en/function.mb-strlen.php "mb_strlen") counting the length of the string in Unicode code points. This was the sole behavior until Symfony 6.2 and is the default since Symfony 6.3. Simple (multibyte) Unicode characters count as 1 character, while for example ZWJ sequences of composed emojis count as multiple characters.
*   `COUNT_GRAPHEMES`: Uses [grapheme_strlen](https://secure.php.net/manual/en/function.grapheme-strlen.php "grapheme_strlen") counting the length of the string in graphemes, i.e. even emojis and ZWJ sequences of composed emojis count as 1 character.

### [`exactly`](https://symfony.com/doc/current/reference/constraints/Length.html#exactly "Permalink to this headline")

**type**: `integer`

This option is the exact length value. Validation will fail if the given value's length is not **exactly** equal to this value.

Note

This option is the one being set by default when using the Length constraint without passing any named argument to it. This means that for example, `#[Assert\Length(20)]` and `#[Assert\Length(exactly: 20)]` are equivalent.

### [`exactMessage`](https://symfony.com/doc/current/reference/constraints/Length.html#exactmessage "Permalink to this headline")

**type**: `string`**default**: `This value should have exactly {{ limit }} characters.`

The message that will be shown if min and max values are equal and the underlying value's length is not exactly this value.

You can use the following parameters in this message:

| Parameter | Description |
| --- | --- |
| `{{ limit }}` | The exact expected length |
| `{{ value }}` | The current (invalid) value |
| `{{ value_length }}` | The current value's length |

### [`groups`](https://symfony.com/doc/current/reference/constraints/Length.html#groups "Permalink to this headline")

**type**: `array` | `string`**default**: `null`

It defines the validation group or groups of this constraint. Read more about [validation groups](https://symfony.com/doc/current/validation/groups.html).

### [`max`](https://symfony.com/doc/current/reference/constraints/Length.html#max "Permalink to this headline")

**type**: `integer`

This option is the "max" length value. Validation will fail if the given value's length is **greater** than this max value.

This option is required when the `min` option is not defined.

### [`maxMessage`](https://symfony.com/doc/current/reference/constraints/Length.html#maxmessage "Permalink to this headline")

**type**: `string`**default**: `This value is too long. It should have {{ limit }} characters or less.`

The message that will be shown if the underlying value's length is more than the [max](https://symfony.com/doc/current/reference/constraints/Length.html#max) option.

You can use the following parameters in this message:

| Parameter | Description |
| --- | --- |
| `{{ limit }}` | The expected maximum length |
| `{{ min }}` | The expected minimum length |
| `{{ max }}` | The expected maximum length |
| `{{ value }}` | The current (invalid) value |
| `{{ value_length }}` | The current value's length |

### [`min`](https://symfony.com/doc/current/reference/constraints/Length.html#min "Permalink to this headline")

**type**: `integer`

This option is the "min" length value. Validation will fail if the given value's length is **less** than this min value.

This option is required when the `max` option is not defined.

It is important to notice that `null` values are considered valid no matter if the constraint requires a minimum length. Validators are triggered only if the value is not `null`.

### [`minMessage`](https://symfony.com/doc/current/reference/constraints/Length.html#minmessage "Permalink to this headline")

**type**: `string`**default**: `This value is too short. It should have {{ limit }} characters or more.`

The message that will be shown if the underlying value's length is less than the [min](https://symfony.com/doc/current/reference/constraints/Length.html#min) option.

You can use the following parameters in this message:

| Parameter | Description |
| --- | --- |
| `{{ limit }}` | The expected minimum length |
| `{{ min }}` | The expected minimum length |
| `{{ max }}` | The expected maximum length |
| `{{ value }}` | The current (invalid) value |
| `{{ value_length }}` | The current value's length |

### [`normalizer`](https://symfony.com/doc/current/reference/constraints/Length.html#normalizer "Permalink to this headline")

**type**: a [PHP callable](https://www.php.net/callable)**default**: `null`

This option allows you to define the PHP callable applied to the given value before checking if it is valid.

For example, you may want to pass the `'trim'` string to apply the [trim](https://secure.php.net/manual/en/function.trim.php "trim") PHP function in order to ignore leading and trailing whitespace during validation.

### [`payload`](https://symfony.com/doc/current/reference/constraints/Length.html#payload "Permalink to this headline")

**type**: `mixed`**default**: `null`

This option can be used to attach arbitrary domain-specific data to a constraint. The configured payload is not used by the Validator component, but its processing is completely up to you.

For example, you may want to use [several error levels](https://symfony.com/doc/current/validation/severity.html) to present failed constraints differently in the front-end depending on the severity of the error.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
