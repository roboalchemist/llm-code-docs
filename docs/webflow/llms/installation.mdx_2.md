# Source: https://developers.webflow.com/devlink/docs/component-export/installation.mdx

***

title: Installation
description: Learn how to configure your React project for exported components.
subtitle: Learn how to configure your React project for exported components.
max-toc-depth: 3
----------------

This reference covers the configuration required to export Webflow components into a React project using DevLink.

## Install the Webflow CLI

Install the CLI as a development dependency to your React project to bundle and publish your component library:

```bash
npm i --save-dev @webflow/webflow-cli
```

<Note title="DevLink supports React v16.18.0 and higher">
  The minimum version of React supported to use exported components is v16.18.0.
</Note>

## Create a configuration file

DevLink looks for a `webflow.json` file in the root of your project, which defines settings for DevLink setup and sync.

<CodeBlocks>
  ```json title="webflow.json"
  {
    "devlink": {
      "rootDir": "./devlink",
      "cssModules": true,
      "fileExtensions": {
        "js": "jsx"
      }
    }
  }
  ```

  ```javascript title=".webflowrc.js"
  module.exports = {
    devlink: {
      directory: "./devlink",
      importGlobalCSS: true
    }
  }
  ```
</CodeBlocks>

<Note>
  `webflow.json` is a newer configuration file that supports configuration for Webflow Cloud and DevLink. DevLink also supports the older `.webflowrc.js` file for backwards compatibility.
</Note>

### Configuration options

| Option             | Description                                           | Default                              |
| :----------------- | :---------------------------------------------------- | :----------------------------------- |
| `host`             | Webflow API host URL                                  | `https://api.webflow.com`            |
| `rootDir`          | Directory to export components into                   | `./devlink`                          |
| `siteId`           | Webflow site ID                                       | `process.env.WEBFLOW_SITE_ID`        |
| `authToken`        | Webflow API authentication token                      | `process.env.WEBFLOW_SITE_API_TOKEN` |
| `cssModules`       | Enable CSS modules for component styles               | `true`                               |
| `allowTelemetry`   | Allow anonymous usage analytics                       | `true`                               |
| `envVariables`     | Inject environment variables into exported components | `{}`                                 |
| `components`       | Regex pattern to match components to export           | `.*`                                 |
| `overwriteModule`  | Whether to overwrite the module file                  | `true`                               |
| `fileExtensions`   | File extensions for exported components               | `{ js: ".js", css: ".css" }`         |
| `skipTagSelectors` | Exclude tag/ID/attribute selectors from global CSS    | `false`                              |
| `relativeHrefRoot` | Control how relative `href` attributes are resolved   | `/`                                  |

While DevLink will try to assume reasonable defaults for most of the settings, you can specify certain options to customize the behavior of DevLink management and setup.

#### `skipTagSelectors`

When `true`, DevLink filters out global CSS rules with certain selectors, producing a smaller `global.css` file. Specifically, it removes:

{/* <!-- vale off --> */}

* Tag selectors (e.g., `div`, `p`, `h1`)
* ID selectors (e.g., `#myId`)
* Attribute selectors (e.g., `[type="text"]`)
* Pseudo-class selectors (e.g., `:hover`, `:focus`) - except for `:root`

{/* <!-- vale on --> */}

This is useful when you only want class-based styles from Webflow and prefer to exclude global tag defaults. Empty rules are dropped entirely.

<Tip title="Define height/widths of parent elements">
  When using `skipTagSelectors: true`, ensure parent elements of DevLink components have defined heights/widths, or set height: 100% on your HTML and body elements to allow proper rendering of  components.
</Tip>

#### `relativeHrefRoot`

Controls how relative `href` values are rewritten in exported Link and Image components.

| Value            | Description                                 | Notes               |
| :--------------- | :------------------------------------------ | :------------------ |
| `false`          | No modification (export as-is)              | Default behavior    |
| `/`              | Treat all relative paths as root-relative   |                     |
| **A string URL** | Rewrite all relative paths as absolute URLs | Must be a valid URL |

##### Example:

* With `"/"`:
  * Page link to "About" → `href="/about"`
  * Section link → `href="#contact-section"`
  * CMS page link → `href="/blog/my-blog-post"`

* With `"https://my-site.com"`:
  * Page link to "About" → `href="https://my-site.com/about"`
  * Section link → `href="https://my-site.com#contact-section"`
  * CMS page link → `href="https://my-site.com/blog/my-blog-post"`

#### `envVariables`

Inject environment variables into components. Useful for APIs like Maps or Recaptcha.

```json title="webflow.json"
{
  "devlink": {
    "envVariables": {
      "GOOGLE_MAPS_API_KEY": process.env.MY_GOOGLE_MAPS_API_KEY,
      "GOOGLE_RECAPTCHA_API_KEY": "MY_GOOGLE_RECAPTCHA_API_KEY"
    }
  }
}
```

#### `fileExtensions`

Customize the extensions used for exported component files.

```json title="webflow.json"
{
  "devlink": {
    "fileExtensions": {
      "js": ".jsx",
      "css": ".less"
    }
```

## Next steps

<CardGroup cols={2}>
  <Card title="Styling Components" href="/devlink/usage/styling-and-theming-overrides">
    Learn how to style components for reliable export
  </Card>
</CardGroup>
