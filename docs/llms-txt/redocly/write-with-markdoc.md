# Source: https://redocly.com/learn/markdoc/write-with-markdoc.md

# Write with Markdoc

This guide will teach you how use Markdoc syntax in your technical writing to unlock powerful features for building documentation.

## Markdown refresher

Before diving into Markdoc, let's revisit our shared understanding of Markdown. This section provides a quick refresher on Markdown basics.

[Markdown](https://daringfireball.net/projects/markdown/basics) is a markup language used to format text documents. Markdown forms the foundational syntax that Markdoc builds upon. You should be comfortable writing in Markdown before using Markdoc.

### Basic syntax

The basic syntax for Markdown comes from the original [design document](https://daringfireball.net/projects/markdown/syntax). These elements are widely supported by modern Markdown tooling.

details
summary
See Basic Syntax examples
| Element | Syntax |
|  --- | --- |
| Heading (6 header levels) | 
```markdown
# H1
## H2
```
 |
| Bold | 
```markdown
This text is **bold**.
```
 |
| Italic | 
```markdown
This text uses _italic_.
```
 |
| Link | 
```markdown
[link text](https://redocly.com)
```
 |
| Image | 
```markdown
![Image alt text](cat_with_glasses.png)
```
 |
| Inline code | 
```markdown
This text has `inline_code`.
```
 |
| Blockquote | 
```markdown
> This text is a quote.
```
 |
| Horizontal rule | 
```markdown
---
```
 |
| Unordered list | 
```markdown
- First bullet
- Second bullet
```
 |
| Ordered list | 
```markdown
1. First thing on list
2. Second thing on list
```
 |


### Extended syntax

Support for additional elements is added to Markdown using extended syntax. Some extended elements, like code block, are widely supported while others are tool-specific, like [GitHub Flavored Markdown](https://github.github.com/gfm/).

Ever created a table in Markdown? You've used extended syntax.

details
summary
See Extended Syntax examples
| Element | Syntax |
|  --- | --- |
| Code block (aka "fence") | 
```text
```javascript
console.log('hello world');
```
```
 |
| Table | 
```markdown
| Header 1 | Header 2 |
| -------- | -------- |
| Hello    | World    |
| Foo      | Bar      |
```
 |
| Strikethrough | 
```markdown
This text has a <del>strikethrough</del>.</code>
```
 |
| Task list | 
```markdown
- [x] Completed task
- [ ] Task to do
```
 |
| Footnote | 
```markdown
This text has a footnote. <sup>[4]</sup>

[4] ... the footnote.
```
 |


Attention
This is **not** a comprehensive list of extended syntax. For more examples and information, try this resource: [Extended Syntax](https://www.markdownguide.org/extended-syntax/).

There's **a lot** of different extended syntax out there. This resource compares syntax for the most common extensions: [Extended syntax comparison by Markdown flavor](https://gist.github.com/vimtaai/99f8c89e7d3d02a362117284684baa0f).

## Learn Markdoc syntax

Markdoc is a "superset", which means it builds on top of Markdown to provide enhanced features and capabilities. That means you're still writing using Markdown syntax, but can reach for Markdoc when you need a more complex feature.

This section introduces Markdoc syntax and provides examples. Please keep the following in mind:

- Markdoc features are optional. Only use what adds value.
- You don't need to be a developer to use Markdoc in your writing.


### Markdown plus Markdoc

Markdoc extends Markdown by adding support for a custom syntax that wraps text with `{%` and `%}`. You'll write using a combination of Markdown and Markdoc syntax.


```markdown
# Example guide

Content with _Markdown elements_.

{% markdoc-tag %}
More **Markdown** content.
{% markdoc-tag %}
```

### Tags add elements

Markdoc tags add new elements and capabilities to your document. Use tags to enhance your writing experience with pre-built elements and tools.

details
summary
Learn more about tags

Markdoc includes some [built-in tags](index.md#built-in-markdoc-features), but teams can [define custom tags](index.md#build-your-own-writing-tools) tailored to the needs of their authors and users.

Official Markdoc docs: [Tags](https://markdoc.dev/docs/tags)

Tags are composable, flexible, and play nicely with Markdown syntax. The table below contains common patterns for using Markdoc tags that you'll see in your writing.

| Example  | Syntax |
|  --- | --- |
| Markdown inside tag
 | 
```
{% admonition type="info" %}
  _Markdown_ syntax stays the **same**.
{% /admonition %}
```
 |
| Nested Markdoc tags
 | 
```
{% tabs %}
  {% tab label="First tab"%}
    Content in the first tab
  {% /tab %}
  {% tab label="Second tab"%}
    Second tab content
  {% /tab %}
{% /tabs %}
```
 |
| Self-closing tag
 | 
```
{% code-snippet file="/some-file.md" /%}
```
 |


### Attributes control tags

Attributes allow you to pass values to tags. Use attributes to control the behavior or appearance of an element added by a tag.

details
summary
Learn more about attributes

Attributes are defined in a tag's schema. Custom tags can define custom attributes that control how authors are able to interact with or modify a tag.

Official Markdoc docs: [Attributes](https://markdoc.dev/docs/attributes)

The attributes available for each Markdoc tag are defined as part of the tag's schema. Consider the `admonition` tag below:

Syntax

```
{% admonition type="info" %}
  Hello, friends!
{% /admonition %}
```

Output
Hello, friends!

Passing a `name` attribute adds a header to the admonition.

Syntax

```
{% admonition type="info" name="Header" %}
  Hello, friends!
{% /admonition %}
```

Output
Header
Hello, friends!

Passing a `type` attribute changes to a different pre-defined admonition.

Syntax

```
{% admonition type="success" %}
  Hello, friends!
{% /admonition %}
```

Output
Hello, friends!

### Variables resolve at runtime

Variables define values that resolve when the page loads. Use variables to customize the page with dynamic values accessible at runtime.

details
summary
Learn more about variables

Variables resolve when the page renders. If a variable changes on the server after the page renders, then the page needs to reload for it to be visible.

Official Markdoc docs: [Variables](https://markdoc.dev/docs/variables)

In this guide's Markdown file, I've added the following values to the front matter:


```yaml
example:
  value: world
  days:
    - Monday
    - Tuesday
    - Wednesday
```

I can pass those values to elements using Markdoc variables.

Syntax

```
Hello {% $frontmatter.example.value %}
```

Output
Hello 

Syntax

```
Today is {% $frontmatter.example.days[0] %}.
```

Output
Today is .

Variables can be used to pass values to partials. They're especially useful when combined with function syntax.

### Functions provide logic

Functions are a tool for building "runtime logic" into your content. Use functions and variables to control or transform the content rendered by your document.

details
summary
Learn more about functions

Markdoc includes built-in functions, but you can also build custom functions. Similar to tags, custom functions are built by developers and exposed for writers to use in their content.

Official Markdoc docs: [Functions](https://markdoc.dev/docs/functions)

You can use built-in functions to implement conditional logic. For example, adding a beta disclaimer:


```
{% if equals($frontmatter.product-status, "beta") %}
  **Note** -- This product is still in beta.
{% /if %}
```

### Annotations extend elements

Annotations pass attributes to elements that don't use Markdoc tag syntax. Use annotations to extend specific Markdown elements or elements inside a tag.

details
summary
Learn more about annotations

Annotations allow authors to pass attributes that modify the HTML an element renders on a page.

Official Markdoc docs: [Functions](https://markdoc.dev/docs/functions)

Add classes that apply CSS styling to specific elements.

Syntax

```markdown
- An item {% .list-entry-example %}
- Another item {% .list-entry-example %}
- Item without annotation
```

Output
- An item
- Another item
- Item without annotation


Define an element's `id` to use as an anchor link. [This link](#annotation-example-id) anchors to the bold text in the example below.

Syntax

```markdown
**Example anchor element** {% #annotation-example-id %}
```

Output
**Example anchor element** 

Use annotations to pass styling attributes directly to an element. Setting the `width` of a column in a Markdoc table is a great example.

Syntax

```markdown
{% table %}
  * Heading 1 {% width="20%" %}
  * Heading 2
  ---
  * First cell content
  * Second cell content
{% /table %}
```

Output
| Heading 1  | Heading 2 |
|  --- | --- |
| First cell content | Second cell content |


## Keep learning Markdoc

Markdoc builds on the simplicity of Markdown to unlock powerful new capabilities for writers. This guide provides a foundation to explore Markdoc's advanced features and start using them in your own writing.

Use these resources to more about Markdoc:

- [Markdoc Overview](/learn/markdoc)
- [Evaluating Markdoc](/learn/markdoc/evaluating-markdoc)
- [Markdoc Tag Library](/learn/markdoc/tags/tag-library)