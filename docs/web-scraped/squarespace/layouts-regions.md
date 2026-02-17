# Layouts & Regions

## Overview

Site layouts define the HTML "wrapper" for your site—everything from `<!doctype html>` to `</html>`. Layouts control the overall page structure by combining one or more region files that contain specific sections of markup.

## Single Layout Sites

The most straightforward approach uses one file (typically `site.region`) as the main template, similar to `index.php` in WordPress.

### Basic Structure

A basic layout includes:
- HTML document structure (`<!DOCTYPE>`, `<head>`, `<body>`)
- Header with navigation
- Main content area
- Sidebar (optional)
- Footer section

### Minimal Example

**site.region:**
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{websiteTitle}</title>
  <squarespace:head-end/>
</head>
<body>

  <header>
    <h1>{websiteTitle}</h1>
    {.section navigation}
      {navigation}
    {.end}
  </header>

  <main id="main-content">
    {main-content}
  </main>

  <footer>
    <p>&copy; {year} {websiteTitle}</p>
  </footer>

  <squarespace:body-end/>
</body>
</html>
```

### Registration in template.conf

```json
"layouts": {
  "default": {
    "name": "default",
    "regions": ["site"]
  }
}
```

## Multiple Layouts

Advanced sites can support different layouts for different pages. A common use case: full-width homepages with sidebar-based subpages.

### Implementation Steps

#### Create Region Files Separately

Create individual region files for reusable components:

**header.region:**
```html
<header>
  <h1>{websiteTitle}</h1>
  <nav>{.section navigation}{navigation}{.end}</nav>
</header>
```

**footer.region:**
```html
<footer>
  <p>&copy; {year} {websiteTitle}</p>
</footer>
```

**full-width.region:**
```html
<main id="main-content">
  {main-content}
</main>
```

**sidebar.region:**
```html
<div class="container">
  <main id="main-content">
    {main-content}
  </main>
  <aside class="sidebar">
    {sidebar-content}
  </aside>
</div>
```

#### Configure Multiple Layouts in template.conf

```json
"layouts": {
  "default": {
    "name": "Sidebar",
    "regions": ["header", "sidebar", "footer"]
  },
  "homepage": {
    "name": "Full Width",
    "regions": ["header", "full-width", "footer"]
  },
  "minimal": {
    "name": "Minimal",
    "regions": ["header", "footer"]
  }
}
```

### Benefits of Multiple Layouts

- **Homepage differentiation** - Full-width design for impact
- **Content pages** - Sidebar for navigation and related items
- **Landing pages** - Minimal layout with no distractions
- **Blog archives** - Different structure from single posts

## Region Files

Region files (`.region`) contain fragments of HTML and JSON-T code that define specific sections of your site.

### Basic Region File

```html
<div class="featured-section">
  <h2>{headline}</h2>
  <p>{description}</p>
  {.section image}
    <img src="{image}" alt="{headline}" />
  {.end}
</div>
```

### Regions with Collections

```html
<section class="blog-posts">
  <h2>Latest Posts</h2>
  {.repeated section items}
    <article class="post-summary">
      <h3>{title}</h3>
      <time>{datePublished}</time>
      <p>{excerpt}</p>
      <a href="{url}">Read more</a>
    </article>
  {.end}
</section>
```

## Default Layout Hierarchy

Layouts can be set at multiple levels (in priority order):

### 1. Homepage-Specific
Defined as "homepage" in configuration. Takes precedence for the site homepage.

```json
"layouts": {
  "homepage": {
    "name": "Full Width",
    "regions": ["header", "full-width", "footer"]
  }
}
```

### 2. Folder-Specific
Set per folder configuration. Allows different layouts for different section branches.

**In folder.conf:**
```json
{
  "layout": "sidebar"
}
```

### 3. Collection-Specific
Set in individual collection configs. Blog collection can use different layout than gallery.

**In collections/blog.conf:**
```json
{
  "layouts": {
    "default": {
      "name": "Blog Layout",
      "regions": ["blog-header", "blog-content", "sidebar", "footer"]
    }
  }
}
```

### 4. Site-wide Default
The "default" layout applies when no more specific layout is configured.

```json
"layouts": {
  "default": {
    "name": "Default Layout",
    "regions": ["header", "main", "footer"]
  }
}
```

## Complete Example: Multi-Layout Site

### Directory Structure

```
/layouts-example-site/
├── template.conf
├── header.region
├── footer.region
├── sidebar.region
├── main.region
├── full-width.region
└── /collections/
    ├── blog.list
    ├── blog.item
    └── blog.conf
```

### template.conf

```json
{
  "name": "Multi-Layout Blog",
  "author": "Your Name",

  "layouts": {
    "default": {
      "name": "Sidebar Layout",
      "regions": ["header", "sidebar", "main", "footer"]
    },
    "homepage": {
      "name": "Full Width Homepage",
      "regions": ["header", "full-width", "footer"]
    },
    "wide": {
      "name": "Wide Layout",
      "regions": ["header", "main", "footer"]
    }
  },

  "navigations": [
    {
      "title": "Main Navigation",
      "name": "mainNav"
    }
  ],

  "stylesheets": [
    "reset.css",
    "layout.less",
    "responsive.less"
  ]
}
```

### header.region

```html
<header id="header">
  <div class="container">
    <h1 class="site-title">{websiteTitle}</h1>
    <nav class="main-nav">
      {.section mainNav}
        {navigation}
      {.end}
    </nav>
  </div>
</header>
```

### sidebar.region

```html
<div class="main-wrapper">
  <main id="main-content">
    {main-content}
  </main>
  <aside class="sidebar">
    <h3>Recent Posts</h3>
    {.section recentPosts}
      <ul>
        {.repeated section .@}
          <li><a href="{url}">{title}</a></li>
        {.end}
      </ul>
    {.end}
  </aside>
</div>
```

### full-width.region

```html
<main id="main-content" class="full-width">
  {main-content}
</main>
```

### footer.region

```html
<footer id="footer">
  <div class="container">
    <p>&copy; {year} {websiteTitle}. All rights reserved.</p>
    {.section socialLinks}
      <nav class="social-nav">{socialLinks}</nav>
    {.end}
  </div>
</footer>
```

## Best Practices

1. **Keep regions focused** - Each region should handle one logical section
2. **Reuse components** - Share regions across layouts where possible
3. **Use CSS for layout** - Prefer CSS Grid/Flexbox to HTML restructuring
4. **Name clearly** - Use descriptive region names (not "left", "right")
5. **Organize hierarchy** - Structure regions logically in template.conf
6. **Mobile first** - Design regions that work across all screen sizes
7. **Semantic markup** - Use proper HTML5 semantic elements
8. **Comment complex logic** - Help future developers understand region purpose

## Common Patterns

### Three-Column Layout

```html
<div class="three-column">
  <aside class="sidebar-left">{left-content}</aside>
  <main>{main-content}</main>
  <aside class="sidebar-right">{right-content}</aside>
</div>
```

### Header with Hero

```html
<header class="hero">
  <div class="hero-image" style="background-image: url({heroImage})"></div>
  <div class="hero-text">
    <h1>{pageTitle}</h1>
  </div>
</header>
```

### Masonry/Grid Layout

```html
<section class="masonry-grid">
  {.repeated section items}
    <div class="masonry-item">
      <img src="{image}" />
      <h3>{title}</h3>
    </div>
  {.end}
</section>
```
