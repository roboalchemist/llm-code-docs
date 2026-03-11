# Source: https://redocly.com/docs/realm/content/markdoc-functions/concat.md

# `concat` function

The `concat` function joins multiple arguments together into a single string.

## Syntax


```markdoc
concat(arg1, arg2, ..., argN)
```

## Parameters

| Parameter | Type | Description |
|  --- | --- | --- |
| arg1, ..., argN | scalar (string, number, boolean, null) | **Required.** One or more values to concatenate.
Non-string values are converted to their string representation (e.g., `true` becomes `"true"`, `123` becomes `"123"`, `null` becomes `"null"`). |


## Returns

A single string resulting from the concatenation of all provided arguments.

## Examples

### Concatenate strings


```markdoc
Full name: {% concat($frontmatter.data.firstName, " ", $frontmatter.data.lastName) %}
```

**Result:**
Full name: 

### Create dynamic image URLs


```markdoc
{% img src=concat("https://picsum.photos/id/", $frontmatter.data.imageId, "/300/200") /%}
```

**Result:**

### Create dynamic card title


```markdoc
{% card title=concat("Author", " ", $frontmatter.data.firstName, " ", $frontmatter.data.lastName) %}
  I'm a **card**.
{% /card %}
```

**Result:**

I'm a **card**.

## Resources

- **[Markdoc functions overview](/docs/realm/content/markdoc-functions)** - Learn about using built-in and custom functions for dynamic content manipulation and processing
- **[Build custom Markdoc functions](/docs/realm/customization/build-custom-function)** - Define and integrate your own custom functions for advanced content processing and dynamic features