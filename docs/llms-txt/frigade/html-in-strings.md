# Source: https://docs.frigade.com/platform/html-in-strings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using HTML in Strings

You can use basic HTML tags to format strings in your YAML Flow definitions. The following tags and attributes are supported:

* `<b>`
* `<i>`
* `<u>`
* `<a href="..." target="...">`
* `<br>`
* `<p>`
* `<img src="..." alt="...">`
* `<div>`
* `<span>`

The `style` and `class` attributes can be used to style all of the above elements.

## Example

```yaml  theme={"system"}
title: This title is <b>really</b> important
```
