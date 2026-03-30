# Source: https://redocly.com/docs/realm/config/banner.md

# `banner`

Display announcement banners at the top of your documentation pages.
Banners are sticky notification bars that appear at the top of pages to communicate important announcements, updates, or information to your users.

Banners support Markdown content, can be configured to appear on specific pages using glob patterns, and can be made dismissible so users can hide them.

## Options

Configure banners as an array of banner objects in your `redocly.yaml` file or in page front matter.

If you ejected the `navbar` component before version `0.128.0`, [update it](/docs/realm/customization/eject-components/eject-components-in-reunite#update-ejected-component) to have the component's full functionality.

| Option | Type | Description |
|  --- | --- | --- |
| content
 | string
 | **REQUIRED.**
The banner content text.
Supports Markdown syntax for formatting, links, tags and emphasis.
Example: `This is **a great announcement.** [Button](https://redocly.com)`
 |
| dismissible
 | boolean
 | Configure whether users can dismiss the banner.
When `true`, a close button appears on the banner.
Dismissed banners are stored in browser's `localStorage` and won't appear again for that user.
Default: `false`
 |
| target
 | string
 | Glob pattern that determines which pages display the banner.
Uses glob pattern matching to target specific pages or sections.
If not specified, matches all pages.
When configuring banners in front matter, the `target` option is not needed.
Front matter banners automatically target the page where they're configured.
**Pattern examples:**
- `blog/**` - matches all pages under the `blog/` path
- `docs/api/**` - matches all pages under `docs/api/`
- `**` - matches all pages (catch-all)
- `getting-started.md` - matches a specific page

**Matching rules:**
- more specific patterns take priority over less specific ones
- exact matches take priority over wildcard patterns
- when multiple banners match a page, only the most specific one is displayed
- patterns are case-insensitive and normalized for matching
- front matter banners take priority over global config banners

 |
| color
 | string
 | The visual style tone of the banner.
Controls the color scheme of the banner.
**Available colors:**
- `info` - blue background
- `success` - green background
- `warning` - yellow background
- `error` - red background

Default: `info`
 |
| rbac
 | object
 | Map of teams to permission levels that determines who can see the banner.
Controls the visibility of the banner based on the user's team membership.
If specified, only users belonging to teams with at least `read` access will see the banner.
See [RBAC configuration](/docs/realm/config/access/rbac) for details.
 |


## Configuration

Add banners to your `redocly.yaml` file:


```yaml redocly.yaml
banner:
  - content: This is **a great announcement.** [Button](https://redocly.com)
    dismissible: true
    target: blog/**
  - content: Important update for all users
    target: '**'
    color: warning
```

## Examples

Configure multiple banners for different sections:


```yaml redocly.yaml
banner:
  - content: Check out our **new blog posts** this week!
    dismissible: true
    target: blog/**
  - content: API documentation has been updated
    target: api/**
  - content: Site maintenance scheduled for this weekend
    dismissible: true
    target: '**'
```

### Role-based visibility

Control banner visibility based on team membership.
In the following example, the banner is only visible to unauthenticated visitors (`anonymous` team).


```yaml redocly.yaml
banner:
  - content: "ð Log in to see all content!"
    color: warning
    rbac:
      anonymous: read
      authenticated: none
```

Configure a banner in the front matter of a specific page:


```md example.md
---
banner:
  - content: Introducing the miracle of documentation
---

# Example page

This is an example page.
```

## Resources

- **[Navigation elements](/docs/realm/navigation)** - Overview of navigation components and patterns
- **[Navbar configuration](/docs/realm/config/navbar)** - Configure the top navigation bar
- **[Footer configuration](/docs/realm/config/footer)** - Configure the footer section
- **[Custom styles](/docs/realm/branding/customize-styles)** - Customize banner appearance with CSS
- **[Configuration options](/docs/realm/config)** - Explore other project configuration options