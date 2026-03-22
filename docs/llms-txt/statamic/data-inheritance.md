# Source: https://statamic.dev/content-modeling/data-inheritance.md

# Data Inheritance

Statamic sets data in a series of scopes that can inherit and override each other in order. We call this data inheritance model **The Cascade**.

## Overview

Statamic provides a unique approach to data inheritance. The value of any given variable in your views can depend on the URL you're on. If a value of a variable doesn't exist on an entry URL, Statamic will check for a fallback value. If that fallback doesn't exist, it will fall back further, and so on. If it never finds anything, the value is `null`.

We call this fallback logic "the cascade", because the value of any given variable "cascades" down from the "top" until it finds where it's defined.

This approach allows you to create views that are less repetitive and are easier to read because a "missing" variable will never throw an error, it will only ever be null.

:::tip
You can easily set variable fallbacks and "catch" the first value that exists without having to write a series of ugly `if/else` conditions.

::tabs

::tab antlers
```antlers
<h1>{{ nav_title ?? breadcrumb_title ?? title }}</h1>
```
::tab blade
```blade
<h1>{{ $nav_title ?? $breadcrumb_title ?? $title }}</h1>
```
::
:::

## Cascade order

Here's the cascading order in which Statamic will look for the value of a given variable:

1. Are we inside a [partial](/tags/partial.md)? If so, has the variable been explicitly passed in?
2. If not, has it been set in a [ViewModel](/view-models.md)?
3. If not, has it been set on the [entry](/collections.md)?
4. If not, and this entry has been translated from another [origin](/multi-site.md), is it set on the origin entry?
5. If not, is it set on the collection via [inject](/collections#inject.md)?
6. If not, is it a [global variable](/globals.md)?
7. If not, is it a [system variable](/variables.md)?
8. Well okay then, `null` it is.
