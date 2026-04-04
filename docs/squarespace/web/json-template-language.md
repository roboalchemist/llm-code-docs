# JSON-T Template Language

## Overview

JSON Template (JSON-T) is a minimal but powerful template language, designed to be paired with a JSON dataset. Squarespace uses this language to transform content into web pages through a process called "rendering," which combines CMS data with JSON-T code to produce HTML.

## Core Concepts

### Tags and Syntax

JSON-T employs special markers to designate where data appears on a page. The language contains two primary tag categories:

- **Variables**: Insert data using simple curly braces like `{foo}` to display content from the context
- **Directives**: Command-like instructions prefixed with a period (such as `{.section foo}`) that control how sections render

### Variable Substitution

Variables pull information from JSON context and display it on the page. Nested data is accessible using dot notation:

```json-t
{foo.bar.baz}
```

This references progressively deeper levels within the JSON structure.

## Built-in Directives

### Sections

The `{.section foo}` directive expands only when the corresponding key exists and isn't false. Sections close with `{.end}`.

```json-t
{.section website}
  {siteTitle}
{.end}
```

**Key Points:**
- Content displays only if the section exists
- Sections establish scope for nested data tags

### Repeated Sections

The `{.repeated section bar}` directive iterates over list items. The special variable `{@}` represents the current scope's value.

```json-t
{.repeated section items}
  Item: {.@}
{.end}
```

Use `{@index}` to number items (starting at 0).

### Or Clause

Displays alternate content when conditions aren't met:

```json-t
{.section item}
  Item exists.
{.or}
  Item does not exist.
{.end}
```

### Alternates With Clause

Inserts delimiters between repeated items:

```json-t
{.repeated section items}
  {title}
{.alternates with}
  ------
{.end}
```

### Var Directive

Stores values for later use:

```json-t
{.var @myTitle website.siteTitle}
{@myTitle}
```

### Comment Directive

Single-line and multiline comments that don't render:

```json-t
{# Single line comment}

{##BEGIN}
  Multiline comment
{END##}
```

### If Directive

Checks whether data exists without scoping into it. Useful for conditional rendering:

```json-t
{.if property}
  Property exists
{.or}
  Property does not exist
{.end}
```

## Working with JSON Data

Squarespace stores website content as JSON data. You can view this data structure by appending `?format=json-pretty` to any site URL.

### Accessing Nested Values

Use dot notation to access nested values directly without scoping:

```json-t
{collection.title}
{item.metadata.datePublished}
```

### Scope Reference

The `{@}` symbol references the current scoped key, functioning like `this` in JavaScript:

```json-t
{.repeated section items}
  Current item: {.@}
{.end}
```

## Common Patterns

### Multiple Sections

End one scope and begin another to access different data areas on the same page:

```json-t
{.section header}
  <h1>{title}</h1>
{.end}

{.section content}
  <p>{description}</p>
{.end}
```

### Empty Sections

When a section contains no data, nothing renders between the opening and closing tags.

### Fallback Content

Use `{.or}` syntax to display alternative markup when data is absent or empty:

```json-t
{.section thumbnail}
  <img src="{.@}" />
{.or}
  <img src="default-image.png" />
{.end}
```

## Prerequisites

Understanding JSON key-value pairs is essential before implementing these templating techniques. JSON-T is designed to work seamlessly with JSON data structures provided by Squarespace's CMS.
