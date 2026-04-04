# Template Configuration

## Overview

The `template.conf` file serves as the core configuration document for Squarespace templates. It contains metadata about the template and defines essential structural elements. This JSON file is required for all templates.

## File Format

All `.conf` files are written in the JSON format.

## Basic Structure

A minimal template.conf file:

```json
{
  "name": "My Custom Template",
  "author": "Your Name",
  "layouts": {
    "default": {
      "name": "Default",
      "regions": ["site"]
    }
  },
  "stylesheets": [
    "reset.css",
    "site.less"
  ]
}
```

## Required Information

Two mandatory fields must be included:

### name
The name of the template. Displayed in the Template and Developer tabs of the Squarespace interface.

```json
"name": "My Awesome Template"
```

### author
The author of the template. Displayed in the Template and Developer tabs alongside the template name.

```json
"author": "John Doe"
```

## Core Configuration Sections

### Layouts

Site layouts consist of one or more regions. Layouts define the overall HTML markup and page structure. A default layout must always be defined.

Each layout includes:
- A display name for user-facing selection menus
- A list of region files to combine in order

**Basic example:**
```json
"layouts": {
  "default": {
    "name": "Default",
    "regions": ["site"]
  }
}
```

**Multiple layout example:**
```json
"layouts": {
  "default": {
    "name": "Sidebar Layout",
    "regions": ["header", "sidebar", "footer"]
  },
  "homepage": {
    "name": "Full Width",
    "regions": ["header", "full-width", "footer"]
  },
  "archive": {
    "name": "Archive",
    "regions": ["header", "archive", "footer"]
  }
}
```

### Navigations

This section configures the top-level navigation sections visible in the Navigation section of the Squarespace interface. Each navigation entry requires:
- A title for UI display
- A name/ID for accessing navigation data throughout templates

**Example:**
```json
"navigations": [
  {
    "title": "Main Navigation",
    "name": "mainNav"
  },
  {
    "title": "Footer Navigation",
    "name": "footerNav"
  }
]
```

Then in your templates, access navigation data with:
```json
{.section mainNav}
  {navigationMarkup}
{.end}
```

### Stylesheets

List of your stylesheets. Stylesheets will be compiled into `site.css` following the ordering here.

**Example:**
```json
"stylesheets": [
  "reset.css",
  "variables.less",
  "typography.less",
  "layout.less",
  "components.less",
  "responsive.less"
]
```

The stylesheets are concatenated in the order specified and compiled into a single `site.css` file served to the browser. LESS files are processed during compilation.

### Special Note on Reset Styles

If you create a file named `reset.css` in the `/styles/` folder, it automatically appears at the beginning of compiled styles and should not be manually listed in the stylesheet configuration. Squarespace handles this automatically.

## Complete Example Configuration

```json
{
  "name": "Modern Blog Template",
  "author": "Design Studio Inc.",
  "layouts": {
    "default": {
      "name": "Blog with Sidebar",
      "regions": ["header", "sidebar", "footer"]
    },
    "fullwidth": {
      "name": "Full Width",
      "regions": ["header", "full-width", "footer"]
    },
    "homepage": {
      "name": "Homepage",
      "regions": ["header", "homepage", "footer"]
    }
  },

  "navigations": [
    {
      "title": "Main Navigation",
      "name": "mainNav"
    },
    {
      "title": "Footer Links",
      "name": "footerNav"
    }
  ],

  "stylesheets": [
    "reset.css",
    "variables.less",
    "typography.less",
    "layout.less",
    "blog.less",
    "responsive.less"
  ]
}
```

## Collections Configuration

Individual collections have their own configuration files. See the Collections section of the template structure for how to configure collection-specific layouts and behaviors.

**Example collection configuration (blog.conf):**
```json
{
  "name": "Blog",
  "layouts": {
    "default": {
      "name": "Default",
      "regions": ["blog"]
    },
    "fullwidth": {
      "name": "Full Width",
      "regions": ["blog-fullwidth"]
    }
  }
}
```

## Regions Reference

Regions are defined in `.region` files and referenced in layouts. Common region names:

- **site** - Main site wrapper
- **header** - Site header
- **footer** - Site footer
- **sidebar** - Optional sidebar
- **full-width** - Full width content area
- **blog** - Blog-specific layout

Create region files (e.g., `site.region`, `header.region`) in the root template directory, then reference them in `template.conf`.

## Validation

Squarespace requires valid JSON. Common mistakes:
- Missing commas between properties
- Trailing commas (not allowed in JSON)
- Unquoted property names
- Improper nesting of arrays or objects

Use a JSON validator to verify your configuration:
```json
{
  "name": "Template",
  "author": "Author",
  "layouts": {
  }
}
```

## Best Practices

1. **Organize sections logically** - Group related configurations
2. **Use clear naming** - Name layouts and navigations descriptively
3. **Maintain consistent capitalization** - Follow standard naming conventions
4. **Document custom properties** - Add comments about template-specific settings
5. **Start simple** - Begin with one layout, add complexity as needed
6. **Test regularly** - Validate JSON frequently during development
