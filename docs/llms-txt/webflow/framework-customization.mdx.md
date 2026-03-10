# Source: https://developers.webflow.com/webflow-cloud/environment/framework-customization.mdx

***

title: Optimizing your app for Webflow Cloud
slug: environment/framework-customization
description: >-
How to adapt and optimize supported frameworks for deployment on Webflow
Cloud.
max-toc-depth: 3
hidden: false
subtitle: Adapt and optimize supported frameworks for deployment on Webflow Cloud.
----------------------------------------------------------------------------------

Webflow Cloud supports the Next.js and Astro frameworks, though running either on the Workers runtime may require specific configuration or adjustments. This page offers guidance on framework-specific setup, limitations, and best practices to help you get the most out of your deployment.

<Tip title="Environment configuration">
  For general deployment and environment configuration, see the [configuration guide](/webflow-cloud/environment/configuration). This page focuses on requirements and recommendations unique to each supported framework.
</Tip>

## Next.js

Webflow Cloud deploys Next.js apps using the [OpenNext Cloudflare adapter](https://opennext.js.org/cloudflare), an open-source tool that brings Next.js to the edge. It handles translating Next.js's server-side features to the edge runtime, including routing, API routes, static assets, and server functions, enabling modern Next.js apps to run with minimal changes.

To run your Next.js app on Webflow Cloud, you may need to adapt some features and provide custom configuration. See the sections below for details.

### Images

Webflow Cloud automatically optimizes images for better performance and reduced bandwidth usage. Here's how different image types are handled:

#### Next.js Image component with local images

When you use the `<Image />` component with local images Webflow Cloud automatically:

* Resizes images for optimal performance
* Serves images through Webflow's CDN for faster loading
* Reduces bandwidth usage

**Example:**

```jsx
import Image from 'next/image';

// This image will be automatically optimized
<Image
  src="/my-image.jpg"
  alt="Description"
  width={500}
  height={300}
/>
```

<Note>
  Webflow Cloud automatically handles routing through your base path when using the Next.js Image component, so you don't need to manually add `assetPrefix` to your image paths.
</Note>

#### Next.js Image component with external images

When you use the `<Image />` component with external images, including those from your main Webflow site, Webflow Cloud doesn't automatically resize the image. However, you can still benefit from other Image component features like lazy loading.

```jsx
// External images are not automatically optimized
<Image
  src="https://example.com/image.jpg"
  alt="External image"
  width={500}
  height={300}
/>
```

#### Plain `img` tags

When using regular `<img>` tags, no automatic optimization occurs. For assets in your `/public` folder, include `assetPrefix` in the src path to ensure proper CDN caching:

```jsx
// Include assetPrefix for CDN caching
<img src={`${assetPrefix}/my-image.jpg`} alt="Description" />
```

### Limitations

Some Next.js features have limitations when running on Webflow Cloud:

* **Middleware:** [Node.js runtime middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware#runtime) isn't supported. Only Edge runtime middleware works on the Workers runtime
* **ISR & On-demand revalidation:** Incremental Static Regeneration and on-demand revalidation are experimental
* **Composable caching:** The `use cache` directive isn't yet supported

See the [OpenNext Cloudflare adapter documentation](https://opennext.js.org/cloudflare#supported-nextjs-features) for current feature support.

### Additional resources

* [Cloudflare Adapter for Next.js](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/)
* [Next.js Edge Runtime Documentation](https://nextjs.org/docs/pages/api-reference/edge)
* [Cloudflare Workers Next.js Guide](https://developers.cloudflare.com/workers/frameworks/framework-guides/nextjs/)
* [OpenNext x Cloudflare Images](https://opennext.js.org/cloudflare/howtos/image)

## Astro

Webflow Cloud deploys Astro apps using the [@astrojs/cloudflare adapter](https://docs.astro.build/en/guides/integrations-guide/cloudflare/). The adapter supports server-side rendering, API routes, and advanced features like server islands and sessions—translating Astro's server functionality to the Workers runtime for seamless edge deployment.

Most features work out of the box, but some Node.js APIs and integrations may need additional configuration. For details and advanced usage, see the [Astro Cloudflare integration guide](https://docs.astro.build/en/guides/integrations-guide/cloudflare/). However, we've outlined the most common adjustments below.

### Loading React components

Be sure to add the `client:load` directive to your components to load your components.

```astro title="src/pages/index.astro" {6}
---
import HelloWorld from '../components/HelloWorld';
---

<div class="container">
  <HelloWorld client:load />
</div>
```

### Static pages

By default, all Astro routes are server-rendered on the edge. For static routes (such as a custom 404 page or privacy policy), enable pre-rendering to generate and serve them as static assets for faster loading.

```javascript title="src/pages/404.astro" {2}
---
export const prerender = true; // Pre-render the page for best performance
---
<html>
  <body>
    <h1>404: Not Found</h1>
    <p>This page does not exist.</p>
  </body>
</html>
```

### Environment variables

Astro provides several ways to access environment variables, depending on where your code runs:

* Use `import.meta.env` for built-in variables like `BASE_URL` and `ASSETS_PREFIX`, and for any custom variables prefixed with `PUBLIC_`. Using the `PUBLIC` prefix will make the variable available on both the server and the client.
* Use `Astro.locals.runtime.env`  in Astro server-side components to access custom environment variables.
* Use `locals.runtime.env`  in API routes to access custom environment variables.

To use `locals.runtime.env` variables during local development, create a `dev.vars` file in your project root. Use the same format as a standard `.env` file to define your environment variables.

```ts title="Accessing environment variables in Astro"
// 1. Built-in environment variables (available everywhere)
import.meta.env.BASE_URL
import.meta.env.ASSETS_PREFIX

// 2. In Astro components (e.g., src/pages/foo.astro)
Astro.locals.runtime.env.VARIABLE_NAME

// 3. In API routes (e.g., src/pages/api/foo.ts)
import type { APIRoute } from 'astro';

export const GET: APIRoute = async ({ locals }) => {
  const siteId = locals.runtime.env.WEBFLOW_SITE_ID;
  const accessToken = locals.runtime.env.WEBFLOW_SITE_API_TOKEN;
  // Use siteId and accessToken as needed
};
```

### API routes

#### Enable Edge runtime for API routes

To ensure Astro API routes work on the [Edge runtime](/webflow-cloud/environment), add the following line to the top of your route:

```javascript title="src/routes/api/hello.ts" {1-4}
// Add this line to your route to ensure it runs on the Edge runtime
export const config = {
    runtime: "edge",
};

import type { APIRoute } from 'astro';


export const GET: APIRoute = async ({ locals }) => {
  return new Response(JSON.stringify({ message: 'Hello from the edge!', runtime }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};
```

#### Disable Astro's CSRF protection (if needed)

You may encounter issues with POST requests containing form data. Disable Astro's built-in [CSRF protection](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF) and implement your own CSRF handling.

In your `astro.config.mjs` file, add the following:

```javascript title="astro.config.mjs" {10}
{
  security: {
    checkOrigin: false,
  },
}
```

### Assets

Astro serves all static assets (such as images, stylesheets, and icons) from the `public` directory. Be sure to place all static files (images, CSS, fonts, etc.) in the `public` directory at your project root.

```
public/
├── images/
│   └── logo.png
├── styles/
│   └── global.css
└── favicon.ico
```

{/* ### Image optimization

Astro's default image optimization service isn't supported on Webflow Cloud, but you can enable edge image optimization by configuring the [Cloudflare image service](https://docs.astro.build/en/guides/integrations-guide/cloudflare/#imageservice) in your `astro.config.mjs`. This lets you serve optimized images globally via Cloudflare's infrastructure.

```js title="astro.config.mjs" {7-8}
import { defineConfig } from "astro/config";
import cloudflare from "@astrojs/cloudflare";
import cloudflareImages from "@astrojs/image/cloudflare";

export default defineConfig({
  adapter: cloudflare(),
  image: {
    service: cloudflareImages(),
  },
});
``` */}

### Tailwind CSS

To use Tailwind CSS in your Astro project, use the `@tailwindcss/vite` plugin to ensure compatibility. Once you've created your Astro project from the CLI, follow the instructions in the [Tailwind CSS integration for Astro](https://tailwindcss.com/docs/installation/framework-guides/astro) guide to set up Tailwind CSS.

<Warning title="@astrojs/tailwind is not supported on Webflow Cloud">
  `@astrojs/tailwind` is deprecated and not supported on Webflow Cloud.

  Third-party templates and guides may still reference it, but it's not recommended to use it. Instead, upgrade to the latest version of Tailwind CSS and use the `@tailwindcss/vite` plugin to ensure compatibility.
</Warning>

## Additional resources

* [Deploying Astro to Cloudflare](https://docs.astro.build/en/guides/deploy/cloudflare/)
* [Cloudflare Workers framework guide for Astro](https://developers.cloudflare.com/workers/frameworks/framework-guides/astro/)
* [Hybrid rendering in Astro](https://blog.logrocket.com/hybrid-rendering-astro-guide/)
