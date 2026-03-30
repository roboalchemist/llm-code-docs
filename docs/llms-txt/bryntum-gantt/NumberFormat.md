# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/NumberFormat.md

# [NumberFormat](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat)

This class is an enhancement to `Intl.NumberFormat` that has a more flexible constructor as well as other features such as `parse()`.

All constructor forms take a single argument. The most common is to pass a format [template](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat#config-template) string:

```
 const formatter = new NumberFormat('9,999.99##');
```

The above is equivalent to:

```
 const formatter = new Intl.NumberFormat({
     useGrouping           : true,
     minimumFractionDigits : 2,
     maximumFractionDigits : 4
 });
```

The `formatter` created above is used as follows (in the `en-US` locale):

```
 console.log(formatter.format(12345.54321));
 console.log(formatter.format(42));

 // 12,345.5432
 // 42.00
```

When a format template is insufficient, a config object can be provided, similar to `Intl.NumberFormat`'s `options` parameter. While all options from `Intl.NumberFormat` are valid properties for this class's config object, additional properties are supported.

For example:

```
 new NumberFormat({
     locale      : 'en-US',
     template    : '$9,999',
     currency    : 'USD',
     significant : 5
 });
```

The `locale` option takes the place of the first positional parameter to the `Intl.NumberFormat` constructor. The `template` config is the same string that can be passed by itself.

Another example: custom decimal and group separators

```
 new NumberFormat({
     template         : '9,9.99##',
     decimalSeparator : '#',
     groupSeparator   : ' '
 });
```

This would format the passed number `123456789.87654` as `123 456 789#8765`.

NOTE: These options are not part of `Intl.NumberFormat`.

The shorthand properties `fraction`, `integer`, and `significant` set the standard options `minimumFractionDigits`, `maximumFractionDigits`, `minimumIntegerDigits`, `minimumSignificantDigits`, and `maximumSignificantDigits`.

NOTE: Instances of `NumberFormat` are immutable after construction.

For details about `Intl.NumberFormat` see [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NumberFormat).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[decimalSeparator](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-decimalSeparator)
Set this to a value to apply a custom `decimalSeparator` to the instance of `NumberFormat`. This overrides the localization specific separator and the static `NumberFormat.decimalSeparator`.

Example: set decimal separator on instance

```
const fmt = new NumberFormat({
    template         : '',
    decimalSeparator : '-'
});
fmt.format(12345.54321);

// Result: '12,345-5432'
```

[groupSeparator](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-groupSeparator)
Set this to a value to apply a custom `groupSeparator` to the instance of `NumberFormat`. This overrides the localization specific separator and the static `NumberFormat.groupSeparator`.

Example: set group separator on instance

```
const fmt = new NumberFormat({
    template       : '',
    groupSeparator : ' '
});
fmt.format(12345.54321);

// Result: '12 345.5432'
```

[currency](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-currency)
The currency to use when using `style: 'currency'`. For example, `'USD'` (US dollar) or `'EUR'` for the euro.

If not provided, the [LocaleManager](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleManager) default will be used.

[currencyDisplay](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-currencyDisplay)
The format in which to display the currency value when using `style: 'currency'`.

Valid values are: `'symbol'` (the default), `'code'`, and `'name'`.

[fraction](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-fraction)
Specifies the `minimumFractionDigits` and `maximumFractionDigits` in a compact way. If this value is a `Number`, it sets both the minimum and maximum to that value. If this value is an array, `[0]` sets the minimum and `[1]` sets the maximum.

[integer](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-integer)
An alias for `minimumIntegerDigits`.

[locale](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-locale)
The name of the locale. For example, `'en-US'`. This config is the same as the first argument to the `Intl.NumberFormat` constructor.

Defaults to the browser's default locale.

[maximumFractionDigits](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-maximumFractionDigits)
The maximum number of digits following the decimal.

This is more convenient to specify using the [fraction](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat#config-fraction) config.

[minimumFractionDigits](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-minimumFractionDigits)
The minimum number of digits following the decimal.

This is more convenient to specify using the [fraction](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat#config-fraction) config.

[minimumIntegerDigits](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-minimumIntegerDigits)
The minimum number of digits preceding the decimal.

This is more convenient to specify using the [integer](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat#config-integer) config.

[maximumSignificantDigits](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-maximumSignificantDigits)
The maximum number of significant digits.

This is more convenient to specify using the [significant](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat#config-significant) config.

[minimumSignificantDigits](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-minimumSignificantDigits)
The minimum number of significant digits.

This is more convenient to specify using the [significant](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat#config-significant) config.

[significant](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-significant)
Specifies the `minimumSignificantDigits` and `maximumSignificantDigits` in a compact format. If this value is a `Number`, it sets only the maximum to that value. If this value is an array, `[0]` sets the minimum and `[1]` sets the maximum.

If this value (or `minimumSignificantDigits` or `minimumSignificantDigits`) is set, `integer` (and `minimumIntegerDigits`) and `fraction` (and `minimumFractionDigits` and `minimumFractionDigits`) are ignored.

[style](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-style)
The formatting style.

Valid values are: `'decimal'` (the default), `'currency'`, and `'percent'`.

[template](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-template)
A format template consisting of the following parts:

```
 [$] [\d+:] \d+ [,\d+] [.\d* [#*] | *] [%]
```

If the template begins with a `'$'`, the formatter's `style` option is set to `'currency'`. If the template ends with `'%'`, `style` is set to `'percent'`. It is invalid to include both characters. When using `'$'`, the `currency` symbol defaults to what is provided by the [LocaleManager](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleManager).

To set the `minimumIntegerDigits`, the desired minimum comes before the first digits in the template and is followed by a `'>'` (greater-than). For example:

```
 5>9,999.00
```

The above sets `minimumIntegerDigits` to 5.

The `useGrouping` option is enabled if there is a `','` (comma) present and is disabled otherwise.

If there is a `'.'` (decimal) present, it may be followed by either of:

* Zero or more digits which may then be followed by zero or more `'#'` characters. The number of digits determines the `minimumFractionDigits`, while the total number of digits and `'#'`s determines the `maximumFractionDigits`.
* A single `'*'` (asterisk) indicating any number of fractional digits (no minimum or maximum).

[useGrouping](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#config-useGrouping)
Specify `false` to disable thousands separators.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[decimalSeparator](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#property-decimalSeparator-static)
Set this to a value to apply a default custom `decimalSeparator` to all formatted numbers in the application. This overrides the localization specific separator.

Example: set global decimal separator

```
// App init code
NumberFormat.decimalSeparator = '-';

// All numbers displayed in the application will have the custom decimal separator applied:
const fmt = new NumberFormat('9,9.99##');
fmt.format(12345.54321);

// Result: '12,345-5432'
```

[groupSeparator](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#property-groupSeparator-static)
Set this to a value to apply a default custom `groupSeparator` to all formatted numbers in the application. This overrides the localization specific separator.

Example: set global group separator

```
// App init code
NumberFormat.groupSeparator = ' ';

// All numbers displayed in the application will have the custom decimal separator applied:
const fmt = new NumberFormat('9,9.99##');
fmt.format(12345.54321);

// Result: '12 345.5432'
```

## Functions

Functions are methods available for calling on the class

[as](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#function-as)
Creates a derived `NumberFormat` from this instance, with a different `style`. This is useful for processing currency and percentage styles without the symbols being injected in the formatting.

[format](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#function-format)
Returns the given `value` formatted in accordance with the specified locale and formatting options.

[parse](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#function-parse)
Returns a `Number` parsed from the given, formatted `value`, in accordance with the specified locale and formatting options.

If the `value` cannot be parsed, `NaN` is returned.

Pass `strict` as `true` to require all text to convert. In essence, the default is in line with JavaScript's `parseFloat` while `strict=true` behaves like the `Number` constructor:

```
 parseFloat('1.2xx');  // = 1.2
 Number('1.2xx')       // = NaN
```

[parseStrict](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#function-parseStrict)
Returns a `Number` parsed from the given, formatted `value`, in accordance with the specified locale and formatting options.

If the `value` cannot be parsed, `NaN` is returned.

This method simply passes the `value` to `parse()` and passes `true` for the second argument.

[round](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#function-round)
Returns the given `Number` rounded in accordance with the specified locale and formatting options.

[truncate](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#function-truncate)
Returns the given `Number` truncated to the `maximumFractionDigits` in accordance with the specified locale and formatting options.

[_minMax](https://bryntum.com/docs/gantt/api/Core/helper/util/NumberFormat#function-_minMax)
Expands the provided shorthand into the "minimum_Digits" and "maximum_Digits".
