# Source: https://redocly.com/docs/realm/content/markdoc-functions/includes.md

# `includes` function

The `includes` function checks if an array contains a specific value.
It is commonly used within conditional logic (`{% if %}`) tags.

## Syntax


```markdoc
includes(array, value)
```

## Parameters

| Parameter | Type | Description |
|  --- | --- | --- |
| array | array | **Required.** The array to check.
Often a variable like `$frontmatter.tags` or an array defined directly. |
| value | scalar (string, number, boolean, null) | **Required.** The value to search for within the array. |


## Returns

`true` if the `array` contains the `value`, otherwise `false`.

## Examples

### Check frontmatter tags


```markdoc
---
tags: ["tutorial", "api", "getting-started"]
---

{% if includes($frontmatter.tags, "api") %}
This page is relevant for API users.
{% /if %}

{% if not(includes($frontmatter.tags, "advanced")) %}
This content is suitable for beginners.
{% /if %}
```

### Check user teams membership


```markdoc
{% if includes($rbac.teams, "employee") %}
You are an employee.
{% /if %}
```