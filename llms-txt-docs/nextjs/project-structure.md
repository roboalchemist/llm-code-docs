# Source: https://nextjs.org/docs/pages/getting-started/project-structure.md

# Source: https://nextjs.org/docs/app/getting-started/project-structure.md

# Source: https://nextjs.org/docs/pages/getting-started/project-structure.md

# Source: https://nextjs.org/docs/app/getting-started/project-structure.md

# Source: https://nextjs.org/docs/pages/getting-started/project-structure.md

# Project structure and organization
@doc-version: 16.0.3


This page provides an overview of **all** the folder and file conventions in Next.js, and recommendations for organizing your project.

## Folder and file conventions

### Top-level folders

Top-level folders are used to organize your application's code and static assets.

![Route segments to path segments](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/top-level-folders.png)

|                                                                    |                                    |
| ------------------------------------------------------------------ | ---------------------------------- |
| [`app`](/docs/app.md)                                                 | App Router                         |
| [`pages`](/docs/pages/building-your-application/routing.md)           | Pages Router                       |
| [`public`](/docs/app/api-reference/file-conventions/public-folder.md) | Static assets to be served         |
| [`src`](/docs/app/api-reference/file-conventions/src-folder.md)       | Optional application source folder |

### Top-level files

Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.

|                                                                              |                                         |
| ---------------------------------------------------------------------------- | --------------------------------------- |
| **Next.js**                                                                  |                                         |
| [`next.config.js`](/docs/app/api-reference/config/next-config-js.md)            | Configuration file for Next.js          |
| [`package.json`](/docs/app/getting-started/installation.md#manual-installation) | Project dependencies and scripts        |
| [`instrumentation.ts`](/docs/app/guides/instrumentation.md)                     | OpenTelemetry and Instrumentation file  |
| [`proxy.ts`](/docs/app/api-reference/file-conventions/proxy.md)                 | Next.js request proxy                   |
| [`.env`](/docs/app/guides/environment-variables.md)                             | Environment variables                   |
| [`.env.local`](/docs/app/guides/environment-variables.md)                       | Local environment variables             |
| [`.env.production`](/docs/app/guides/environment-variables.md)                  | Production environment variables        |
| [`.env.development`](/docs/app/guides/environment-variables.md)                 | Development environment variables       |
| [`eslint.config.mjs`](/docs/app/api-reference/config/eslint.md)                 | Configuration file for ESLint           |
| `.gitignore`                                                                 | Git files and folders to ignore         |
| `next-env.d.ts`                                                              | TypeScript declaration file for Next.js |
| `tsconfig.json`                                                              | Configuration file for TypeScript       |
| `jsconfig.json`                                                              | Configuration file for JavaScript       |

### File conventions

|                                                                                                             |                     |                   |
| ----------------------------------------------------------------------------------------------------------- | ------------------- | ----------------- |
| [`_app`](/docs/pages/building-your-application/routing/custom-app.md)                                          | `.js` `.jsx` `.tsx` | Custom App        |
| [`_document`](/docs/pages/building-your-application/routing/custom-document.md)                                | `.js` `.jsx` `.tsx` | Custom Document   |
| [`_error`](/docs/pages/building-your-application/routing/custom-error.md#more-advanced-error-page-customizing) | `.js` `.jsx` `.tsx` | Custom Error Page |
| [`404`](/docs/pages/building-your-application/routing/custom-error.md#404-page)                                | `.js` `.jsx` `.tsx` | 404 Error Page    |
| [`500`](/docs/pages/building-your-application/routing/custom-error.md#500-page)                                | `.js` `.jsx` `.tsx` | 500 Error Page    |

### Routes

|                                                                                                |                     |             |
| ---------------------------------------------------------------------------------------------- | ------------------- | ----------- |
| **Folder convention**                                                                          |                     |             |
| [`index`](/docs/pages/building-your-application/routing/pages-and-layouts.md#index-routes)        | `.js` `.jsx` `.tsx` | Home page   |
| [`folder/index`](/docs/pages/building-your-application/routing/pages-and-layouts.md#index-routes) | `.js` `.jsx` `.tsx` | Nested page |
| **File convention**                                                                            |                     |             |
| [`index`](/docs/pages/building-your-application/routing/pages-and-layouts.md#index-routes)        | `.js` `.jsx` `.tsx` | Home page   |
| [`file`](/docs/pages/building-your-application/routing/pages-and-layouts.md)                      | `.js` `.jsx` `.tsx` | Nested page |

### Dynamic routes

|                                                                                                                   |                     |                                  |
| ----------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------------------- |
| **Folder convention**                                                                                             |                     |                                  |
| [`[folder]/index`](/docs/pages/building-your-application/routing/dynamic-routes.md)                                  | `.js` `.jsx` `.tsx` | Dynamic route segment            |
| [`[...folder]/index`](/docs/pages/building-your-application/routing/dynamic-routes.md#catch-all-segments)            | `.js` `.jsx` `.tsx` | Catch-all route segment          |
| [`[[...folder]]/index`](/docs/pages/building-your-application/routing/dynamic-routes.md#optional-catch-all-segments) | `.js` `.jsx` `.tsx` | Optional catch-all route segment |
| **File convention**                                                                                               |                     |                                  |
| [`[file]`](/docs/pages/building-your-application/routing/dynamic-routes.md)                                          | `.js` `.jsx` `.tsx` | Dynamic route segment            |
| [`[...file]`](/docs/pages/building-your-application/routing/dynamic-routes.md#catch-all-segments)                    | `.js` `.jsx` `.tsx` | Catch-all route segment          |
| [`[[...file]]`](/docs/pages/building-your-application/routing/dynamic-routes.md#optional-catch-all-segments)         | `.js` `.jsx` `.tsx` | Optional catch-all route segment |