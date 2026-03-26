# Source: https://www.zuplo.com/docs/dev-portal/zudoku/configuration/site.md


# Branding & Layout

We offer you to customize the main aspects of your Dev Portal site's appearance and behavior.

## Branding

**Title**, **logo** can be configured in under the `site` property:

```tsx title=zudoku.config.tsx
const config = {
  site: {
    title: "My API Documentation",
    logo: {
      src: {
        light: "/path/to/light-logo.png",
        dark: "/path/to/dark-logo.png",
      },
      alt: "Company Logo",
      href: "/",
    },
    // Other options...
  },
};
```

### Available Options

#### Title

Set the title of your site next to the logo in the header:

```tsx title=zudoku.config.tsx
{
  site: {
    title: "My API Documentation",
  }
}
```

#### Logo

Configure the site's logo with different versions for light and dark themes:

```tsx title=zudoku.config.tsx
{
  site: {
    logo: {
      src: {
        light: "/light-logo.png",
        dark: "/dark-logo.png"
      },
      alt: "Company Logo",
      width: "120px", // optional width
      href: "/", // optional link target (defaults to "/")
      reloadDocument: true, // optional, defaults to true
    }
  }
}
```

The `reloadDocument` option controls whether clicking the logo triggers a full page reload (`true`,
the default) or uses client-side SPA navigation (`false`). A full reload is useful when your landing
page is served by a different system (e.g. a CMS) outside of Zudoku.

#### Colors & Theme

We allow you to fully customize all colors, borders, etc - read more about it in
[Colors & Themes](/dev-portal/zudoku/customization/colors-theme)

## Layout

### Banner

Add a banner message to the top of the page:

```tsx title=zudoku.config.tsx
{
  site: {
    banner: {
      message: "Welcome to our beta documentation!",
      color: "info", // "note" | "tip" | "info" | "caution" | "danger" or custom
      dismissible: true
    }
  }
}
```

### Footer

The footer configuration has its own dedicated section. See the [Footer Configuration](./footer) for
details.

## Complete Example

Here's a comprehensive example showing all available page configuration options:

```tsx title=zudoku.config.tsx
{
  site: {
    title: "My API Documentation",
    logo: {
      src: {
        light: "/images/logo-light.svg",
        dark: "/images/logo-dark.svg"
      },
      alt: "Company Logo",
      width: "100px",
    },
    banner: {
      message: "Welcome to our documentation!",
      color: "info",
      dismissible: true
    },
  }
}
```
