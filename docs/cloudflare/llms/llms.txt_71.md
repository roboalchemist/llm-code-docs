# Source: https://developers.cloudflare.com/pages/llms.txt

# Pages

Build full-stack, serverless applications globally with minimal configuration

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/pages/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Pages llms-full.txt](https://developers.cloudflare.com/pages/llms-full.txt) for the complete Pages documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Pages](https://developers.cloudflare.com/pages/index.md)

## Functions

- [Functions](https://developers.cloudflare.com/pages/functions/index.md)
- [Advanced mode](https://developers.cloudflare.com/pages/functions/advanced-mode/index.md)
- [API reference](https://developers.cloudflare.com/pages/functions/api-reference/index.md): Learn about the APIs used within Pages Functions.
- [Bindings](https://developers.cloudflare.com/pages/functions/bindings/index.md)
- [Debugging and logging](https://developers.cloudflare.com/pages/functions/debugging-and-logging/index.md)
- [A/B testing with middleware](https://developers.cloudflare.com/pages/functions/examples/ab-testing/index.md): Set up an A/B test by controlling what page is served based on cookies. This version supports passing the request through to test and control on the origin.
- [Adding CORS headers](https://developers.cloudflare.com/pages/functions/examples/cors-headers/index.md): A Pages Functions for appending CORS headers.
- [Get started](https://developers.cloudflare.com/pages/functions/get-started/index.md)
- [Local development](https://developers.cloudflare.com/pages/functions/local-development/index.md)
- [Metrics](https://developers.cloudflare.com/pages/functions/metrics/index.md)
- [Middleware](https://developers.cloudflare.com/pages/functions/middleware/index.md)
- [Module support](https://developers.cloudflare.com/pages/functions/module-support/index.md)
- [Pages Plugins](https://developers.cloudflare.com/pages/functions/plugins/index.md)
- [Cloudflare Access](https://developers.cloudflare.com/pages/functions/plugins/cloudflare-access/index.md)
- [Community Plugins](https://developers.cloudflare.com/pages/functions/plugins/community-plugins/index.md)
- [Google Chat](https://developers.cloudflare.com/pages/functions/plugins/google-chat/index.md)
- [GraphQL](https://developers.cloudflare.com/pages/functions/plugins/graphql/index.md)
- [hCaptcha](https://developers.cloudflare.com/pages/functions/plugins/hcaptcha/index.md)
- [Honeycomb](https://developers.cloudflare.com/pages/functions/plugins/honeycomb/index.md)
- [Sentry](https://developers.cloudflare.com/pages/functions/plugins/sentry/index.md)
- [Static Forms](https://developers.cloudflare.com/pages/functions/plugins/static-forms/index.md)
- [Stytch](https://developers.cloudflare.com/pages/functions/plugins/stytch/index.md)
- [Turnstile](https://developers.cloudflare.com/pages/functions/plugins/turnstile/index.md)
- [vercel/og](https://developers.cloudflare.com/pages/functions/plugins/vercel-og/index.md)
- [Pricing](https://developers.cloudflare.com/pages/functions/pricing/index.md)
- [Routing](https://developers.cloudflare.com/pages/functions/routing/index.md)
- [Smart Placement](https://developers.cloudflare.com/pages/functions/smart-placement/index.md)
- [Source maps and stack traces](https://developers.cloudflare.com/pages/functions/source-maps/index.md): Adding source maps and generating stack traces for Pages.
- [TypeScript](https://developers.cloudflare.com/pages/functions/typescript/index.md)
- [Configuration](https://developers.cloudflare.com/pages/functions/wrangler-configuration/index.md)

## Tutorials

- [Tutorials](https://developers.cloudflare.com/pages/tutorials/index.md)
- [Add a React form with Formspree](https://developers.cloudflare.com/pages/tutorials/add-a-react-form-with-formspree/index.md): Learn how to add a React form with Formspree, a back-end service that handles form processing and storage.
- [Add an HTML form with Formspree](https://developers.cloudflare.com/pages/tutorials/add-an-html-form-with-formspree/index.md): Learn how to add an HTML form with Formspree, a back-end service that handles form processing and storage.
- [Build a blog using Nuxt.js and Sanity.io on Cloudflare Pages](https://developers.cloudflare.com/pages/tutorials/build-a-blog-using-nuxt-and-sanity/index.md): Build a blog application using Nuxt.js and Sanity.io and deploy it on Cloudflare Pages.
- [Build an API for your front end using Pages Functions](https://developers.cloudflare.com/pages/tutorials/build-an-api-with-pages-functions/index.md): This tutorial builds a full-stack Pages application using the React framework.
- [Create a HTML form](https://developers.cloudflare.com/pages/tutorials/forms/index.md): This tutorial will briefly touch upon the basics of HTML forms. This tutorial will make heavy use of Cloudflare Pages and its Workers integration.
- [Localize a website with HTMLRewriter](https://developers.cloudflare.com/pages/tutorials/localize-a-website/index.md): This tutorial uses the HTMLRewriter functionality in the Cloudflare Workers platform to overlay an i18n layer, automatically translating the site based on the userâs language.
- [Use R2 as static asset storage with Cloudflare Pages](https://developers.cloudflare.com/pages/tutorials/use-r2-as-static-asset-storage-for-pages/index.md): This tutorial will teach you how to use R2 as a static asset storage bucket for your Pages app.

## Demos and architectures

- [Demos and architectures](https://developers.cloudflare.com/pages/demos/index.md)

## configuration

- [REST API](https://developers.cloudflare.com/pages/configuration/api/index.md)
- [Branch deployment controls](https://developers.cloudflare.com/pages/configuration/branch-build-controls/index.md)
- [Build caching](https://developers.cloudflare.com/pages/configuration/build-caching/index.md)
- [Build configuration](https://developers.cloudflare.com/pages/configuration/build-configuration/index.md)
- [Build image](https://developers.cloudflare.com/pages/configuration/build-image/index.md)
- [Build watch paths](https://developers.cloudflare.com/pages/configuration/build-watch-paths/index.md)
- [Custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/index.md)
- [Debugging Pages](https://developers.cloudflare.com/pages/configuration/debugging-pages/index.md)
- [Deploy Hooks](https://developers.cloudflare.com/pages/configuration/deploy-hooks/index.md)
- [Early Hints](https://developers.cloudflare.com/pages/configuration/early-hints/index.md)
- [Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/index.md)
- [GitHub integration](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/index.md)
- [GitLab integration](https://developers.cloudflare.com/pages/configuration/git-integration/gitlab-integration/index.md)
- [Troubleshooting builds](https://developers.cloudflare.com/pages/configuration/git-integration/troubleshooting/index.md)
- [Headers](https://developers.cloudflare.com/pages/configuration/headers/index.md)
- [Monorepos](https://developers.cloudflare.com/pages/configuration/monorepos/index.md)
- [Preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/index.md)
- [Redirects](https://developers.cloudflare.com/pages/configuration/redirects/index.md)
- [Rollbacks](https://developers.cloudflare.com/pages/configuration/rollbacks/index.md)
- [Serving Pages](https://developers.cloudflare.com/pages/configuration/serving-pages/index.md)

## framework-guides

- [Blazor](https://developers.cloudflare.com/pages/framework-guides/deploy-a-blazor-site/index.md)
- [Brunch](https://developers.cloudflare.com/pages/framework-guides/deploy-a-brunch-site/index.md)
- [Docusaurus](https://developers.cloudflare.com/pages/framework-guides/deploy-a-docusaurus-site/index.md)
- [Gatsby](https://developers.cloudflare.com/pages/framework-guides/deploy-a-gatsby-site/index.md)
- [Gridsome](https://developers.cloudflare.com/pages/framework-guides/deploy-a-gridsome-site/index.md)
- [Hexo](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hexo-site/index.md)
- [Hono](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hono-site/index.md)
- [Hugo](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/index.md)
- [Jekyll](https://developers.cloudflare.com/pages/framework-guides/deploy-a-jekyll-site/index.md)
- [Nuxt](https://developers.cloudflare.com/pages/framework-guides/deploy-a-nuxt-site/index.md): Web framework making Vue.js-based development simple and powerful.
- [Pelican](https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/index.md)
- [Preact](https://developers.cloudflare.com/pages/framework-guides/deploy-a-preact-site/index.md)
- [Qwik](https://developers.cloudflare.com/pages/framework-guides/deploy-a-qwik-site/index.md)
- [React](https://developers.cloudflare.com/pages/framework-guides/deploy-a-react-site/index.md)
- [Remix](https://developers.cloudflare.com/pages/framework-guides/deploy-a-remix-site/index.md)
- [SolidStart](https://developers.cloudflare.com/pages/framework-guides/deploy-a-solid-start-site/index.md)
- [Sphinx](https://developers.cloudflare.com/pages/framework-guides/deploy-a-sphinx-site/index.md)
- [SvelteKit](https://developers.cloudflare.com/pages/framework-guides/deploy-a-svelte-kit-site/index.md): Learn how to create and deploy a SvelteKit application to Cloudflare Pages using the create-cloudflare CLI
- [Vite 3](https://developers.cloudflare.com/pages/framework-guides/deploy-a-vite3-project/index.md)
- [VitePress](https://developers.cloudflare.com/pages/framework-guides/deploy-a-vitepress-site/index.md)
- [Vue](https://developers.cloudflare.com/pages/framework-guides/deploy-a-vue-site/index.md)
- [Zola](https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/index.md)
- [Analog](https://developers.cloudflare.com/pages/framework-guides/deploy-an-analog-site/index.md): Fullstack meta-framework for Angular, powered by Vite and Nitro.
- [Angular](https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/index.md)
- [Astro](https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/index.md)
- [Elder.js](https://developers.cloudflare.com/pages/framework-guides/deploy-an-elderjs-site/index.md)
- [Eleventy](https://developers.cloudflare.com/pages/framework-guides/deploy-an-eleventy-site/index.md)
- [Ember](https://developers.cloudflare.com/pages/framework-guides/deploy-an-emberjs-site/index.md)
- [MkDocs](https://developers.cloudflare.com/pages/framework-guides/deploy-an-mkdocs-site/index.md)
- [Static HTML](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/index.md)
- [Next.js](https://developers.cloudflare.com/pages/framework-guides/nextjs/index.md): React framework for building full-stack web applications.
- [Static site](https://developers.cloudflare.com/pages/framework-guides/nextjs/deploy-a-static-nextjs-site/index.md): Deploy a static site built using Next.js to Cloudflare Pages

## get-started

- [C3 CLI](https://developers.cloudflare.com/pages/get-started/c3/index.md): Use C3 (`create-cloudflare` CLI) to set up and deploy new applications using framework-specific setup guides to ensure each new application follows Cloudflare and any third-party best practices for deployment.
- [Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/index.md): Upload your prebuilt assets to Pages and deploy them via the Wrangler CLI or the Cloudflare dashboard.
- [Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/index.md): Connect your Git provider to Pages.

## how-to

- [Add custom HTTP headers](https://developers.cloudflare.com/pages/how-to/add-custom-http-headers/index.md)
- [Set build commands per branch](https://developers.cloudflare.com/pages/how-to/build-commands-branches/index.md)
- [Add a custom domain to a branch](https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/index.md)
- [Deploy a static WordPress site](https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/index.md): Learn how to deploy a static WordPress site using Cloudflare Pages.
- [Enable Zaraz](https://developers.cloudflare.com/pages/how-to/enable-zaraz/index.md)
- [Install private packages](https://developers.cloudflare.com/pages/how-to/npm-private-registry/index.md)
- [Preview Local Projects with Cloudflare Tunnel](https://developers.cloudflare.com/pages/how-to/preview-with-cloudflare-tunnel/index.md)
- [Redirecting *.pages.dev to a Custom Domain](https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/index.md)
- [Refactor a Worker to a Pages Function](https://developers.cloudflare.com/pages/how-to/refactor-a-worker-to-pages-functions/index.md)
- [Use Direct Upload with continuous integration](https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/index.md)
- [Use Pages Functions for A/B testing](https://developers.cloudflare.com/pages/how-to/use-worker-for-ab-testing-in-pages/index.md)
- [Enable Web Analytics](https://developers.cloudflare.com/pages/how-to/web-analytics/index.md)
- [Redirecting www to domain apex](https://developers.cloudflare.com/pages/how-to/www-redirect/index.md)

## Migrate to Workers

- [Migrate to Workers](https://developers.cloudflare.com/pages/migrate-to-workers/index.md)

## migrations

- [Migrating from Firebase](https://developers.cloudflare.com/pages/migrations/migrating-from-firebase/index.md): This tutorial explains how to migrate an existing Firebase application to Cloudflare Pages.
- [Migrating from Netlify to Pages](https://developers.cloudflare.com/pages/migrations/migrating-from-netlify/index.md): Learn how to migrate from Netlify to Cloudflare. This guide includes instructions for migrating redirects and headers.
- [Migrating from Vercel to Pages](https://developers.cloudflare.com/pages/migrations/migrating-from-vercel/index.md): In this tutorial, you will learn how to deploy your Vercel application to Cloudflare Pages.
- [Migrating from Workers Sites to Pages](https://developers.cloudflare.com/pages/migrations/migrating-from-workers/index.md): Learn how to migrate from Workers Sites to Cloudflare Pages.
- [Migrating a Jekyll-based site from GitHub Pages](https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/index.md): Learn how to migrate a Jekyll-based site from GitHub Pages to Cloudflare Pages.

## platform

- [Changelog](https://developers.cloudflare.com/pages/platform/changelog/index.md)
- [Known issues](https://developers.cloudflare.com/pages/platform/known-issues/index.md)
- [Limits](https://developers.cloudflare.com/pages/platform/limits/index.md)
- [Choose a data or storage product](https://developers.cloudflare.com/pages/platform/storage-options/index.md)