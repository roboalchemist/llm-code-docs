# Templating Basics

## Core Concepts

Squarespace stores website content as JSON data. You can view this data structure by appending `?format=json-pretty` to any site URL.

## Key Techniques

### Rendering Data

To display content, scope into the appropriate JSON section using curly bracket syntax around keys:

```json-t
{.section collection}
  <h1>{title}</h1>
{.end}
```

### Working with Arrays

Use `{.repeated section key}` to iterate through multiple items. The code repeats for each array element.

```json-t
{.repeated section items}
  <div class="item">
    <h3>{title}</h3>
    <p>{description}</p>
  </div>
{.end}
```

### Multiple Sections

End one scope and begin another to access different data areas on the same page.

```json-t
{.section header}
  <header>
    <h1>{siteTitle}</h1>
  </header>
{.end}

{.section main}
  <main>
    {content}
  </main>
{.end}

{.section footer}
  <footer>
    {copyright}
  </footer>
{.end}
```

### Empty Sections

When a section contains no data, nothing renders between the opening and closing tags. This allows for clean templates that gracefully handle missing content.

```json-t
{.section sidebarContent}
  <aside>
    {sidebarContent}
  </aside>
{.end}
```

If `sidebarContent` doesn't exist, nothing renders—no empty aside tag.

### Fallback Content

Use `{.or}` syntax to display alternative markup when data is absent or empty.

```json-t
{.section thumbnail}
  <img src="{thumbnail}" alt="Featured image" />
{.or}
  <img src="default-thumbnail.png" alt="Default image" />
{.end}
```

### Dot Notation

Access nested values directly without scoping:

```json-t
{collection.title}
{item.metadata.datePublished}
{author.profile.email}
```

This is useful for accessing deeply nested properties without multiple scoping levels.

### Scope Reference

The `{@}` symbol references the current scoped key, functioning like `this` in JavaScript.

```json-t
{.repeated section items}
  Current item: {.@}
{.end}
```

When you repeat over an array of strings, `{.@}` gives you the string value directly. For objects, it gives you access to the entire object.

### Conditional Logic

`{.if property}` checks whether data exists without scoping into it. Pair with `{.or}` for alternative content when conditions fail.

```json-t
{.if isPublished}
  <p class="published">This post is published</p>
{.or}
  <p class="draft">This post is in draft mode</p>
{.end}
```

## Template Structure

### Basic Template File

A typical collection list template might look like:

```html
<div class="articles-list">
  {.repeated section articles}
    <article class="article-preview">
      <h2>{title}</h2>
      {.if excerpt}
        <p>{excerpt}</p>
      {.or}
        <p>{body|truncate:200}</p>
      {.end}
      <a href="{fullUrl}">Read more</a>
    </article>
  {.end}
</div>
```

### Organization

- Use consistent indentation for readability
- Keep scope opening and closing tags clearly paired
- Comment complex template logic
- Separate CSS and JavaScript into their own files

## Filters and Modifiers

Some Squarespace data supports filters for formatting:

```json-t
{datePublished|date %m/%d/%Y}
{body|truncate:200}
{title|uppercase}
```

Check the specific data field documentation for available filters.

## Collections and Pages

### Collection List View

The `.list` template displays multiple items from a collection:

```json-t
{.repeated section items}
  <article>
    <h2>{title}</h2>
    <p>{excerpt}</p>
  </article>
{.end}
```

### Collection Item View

The `.item` template displays a single item with full details:

```html
<article>
  <h1>{title}</h1>
  <div class="meta">
    <span>{author}</span>
    <time>{datePublished}</time>
  </div>
  <div class="content">
    {body}
  </div>
</article>
```

### Static Pages

Static pages don't use JSON-T syntax—they're pure HTML that end users can edit.

## Prerequisites

Understanding JSON key-value pairs is essential before implementing these templating techniques. A basic example:

```json
{
  "title": "My Blog",
  "articles": [
    {
      "title": "First Post",
      "excerpt": "This is my first post"
    },
    {
      "title": "Second Post",
      "excerpt": "This is my second post"
    }
  ]
}
```

In your template, you'd access this data with JSON-T syntax to display the content.

## Debugging

### View Raw JSON Data

Append `?format=json-pretty` to any Squarespace page URL to see the underlying JSON structure:

```text
https://your-site.squarespace.com/blog?format=json-pretty
```

This is invaluable for understanding what data is available and how it's structured.

### Common Data Fields

Most collections provide these fields:

- `title` - Item title
- `excerpt` - Short summary
- `body` - Full content
- `datePublished` - Publication date
- `author` - Author name
- `url` - Item permalink
- `thumbnail` - Featured image

Specific collection types may add custom fields.

## Best Practices

1. **Keep templates simple** - Complex logic belongs in CSS or JavaScript
2. **Use semantic HTML** - Ensure accessibility
3. **Plan for missing data** - Always provide fallbacks with `{.or}`
4. **Use consistent naming** - Match JSON structure in templates
5. **Comment your code** - Help future developers understand template logic
