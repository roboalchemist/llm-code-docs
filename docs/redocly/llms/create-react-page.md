# Source: https://redocly.com/docs/realm/customization/create-react-page.md

# Create page in React

Markdown is the primary format for creating content in Redocly projects, but React pages offer additional flexibility.
Use React pages for dynamic content, complex layouts, or advanced interactivity.

This guide shows you how to create a React page in your Redocly project (Realm or Revel).

## Before you begin

Make sure you have the following:

- a Revel or Realm project running locally
- basic knowledge of React


## Create a new React page

Render React code as an independent page by adding the `.page.tsx` suffix on the filename.
Similar to Markdown pages, React pages use file-based routing and can be located anywhere in a project.

details
summary
See how React pages are used in a project
It's common for projects to have both Markdown and React pages, as in the following example project structure:


```treeview Project with multiple page types
your-awesome-project/
âââ @theme/
âââ static/
âââ guides/
â   âââ example-guide.md
â   âââ pricing.page.tsx
âââ about/
â   âââ index.page.tsx
â   âââ ContactForm.tsx
âââ index.md
âââ redocly.yaml
âââ ...
```

In this example, the `ContactForm.tsx` file defines a component imported by other pages.
It *doesn't render as a page* because the file doesn't have a `.page.tsx` suffix.

To create a React page, add a new file to the root of your project named `example.page.tsx`.

## Add content to React page

Add content to the new page by creating a React component.
View the page in your local preview.

The following example content is for `example.page.tsx`, which can be viewed at `<your-local-host>/example`:


```javascript example.page.tsx
import React from 'react';
import styled from 'styled-components';

export default function () {
  return (
    <Wrapper>
      <h1>Example React page</h1>
      <p>Hello world!</p>
    </Wrapper>
  );
}

const Wrapper = styled.div`
  padding: 40px;
`;
```

Your IDE may show a `Cannot find module...` linting error for `react` and `styled-components`. You have two options:

- Ignore them; the modules resolve when `npx @redocly/cli preview` runs.
- Remove the errors by installing a local version of your Redocly product -- `@redocly/realm` or `@redocly/revel`.


## Set front matter for a React page

Set the React page's [front matter](/docs/realm/config/front-matter-config) by exporting a `frontmatter` object.

Front matter is used to set page metadata or configure page behavior, as in the following list of examples:

- Hide [navbar](/docs/realm/config/navbar) and [footer](/docs/realm/config/footer) elements:

```javascript
export const frontmatter = {
  navbar: {
    hide: true,
  },
  footer: {
    hide: true,
  }
};
```
- Set [page permissions using RBAC](/docs/realm/access/page-permissions#react-pages):

```javascript
export const frontmatter = {
  rbac: {
    Admin: 'admin',
    Employee: 'read',
  },
};
```
- Add SEO titles and descriptions:

```javascript
export const frontmatter = {
  seo: {
    title: 'Some Amazing Guide',
    description: 'Wow this guide is amazing!',
  },
};
```
- [Block indexing](/docs/realm/config/seo#control-search-indexing) by search engines:

```javascript
export const frontmatter = {
  seo: {
    meta: [
      {
        name: "robots",
        content: "noindex"
      }
    ]
  },
};
```


## Add React page to navigation

Add the page to your site's navigation elements, such as the [sidebar](/docs/realm/navigation/sidebars), [navbar](/docs/realm/config/navbar), or [footer](/docs/realm/config/footer), using the page's relative filepath.

The following example shows a sidebar configuration that includes React pages:


```yaml sidebars.yaml
- separator: Demo sidebar
- page: about/index.page.tsx
  label: About us
- group: Guides
    items:
      - page: guides/pricing.page.tsx
      - page: guides/example-guide.md
```

If needed, you can use `frontmatter` to [add the sidebar to a single page](/docs/realm/config/front-matter-config#front-matter-only-options) without listing it in the sidebars configuration file.

## Landing page examples

Redocly provides a [gallery of example landing pages](https://github.com/Redocly/landing-page-gallery) built with React.
These examples can help you get started creating your own custom React pages.

The following example pages are available in the gallery:

| Screenshot  | Description |
|  --- | --- |
|  | This example shows a sleek, modern landing page for a SaaS product.
**Tools:** React, styled-components
[View source code](https://github.com/Redocly/landing-page-gallery/blob/main/example-saas/index.page.tsx)
 |
|  | This example demonstrates a landing page built for training and onboarding purposes.
**Tools:** React, styled-components
[View source code](https://github.com/Redocly/landing-page-gallery/blob/main/legacy-portal/training.page.tsx)
 |


## Resources

- **[React landing page gallery](https://github.com/Redocly/landing-page-gallery)** - Explore real-world examples and design patterns for creating compelling React-based documentation pages
- **[Custom page templates](/docs/realm/customization/custom-page-templates)** - Use React pages as reusable templates for Markdown content with consistent layouts and functionality
- **[Custom styling guide](/docs/realm/branding)** - Customize the appearance of React pages using CSS variables, custom stylesheets, and component-specific styling
- **[Page permissions](/docs/realm/access/page-permissions)** - Implement role-based access control to restrict React page visibility based on user roles and team membership