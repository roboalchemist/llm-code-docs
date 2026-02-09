# Source: https://ui.nuxt.com/raw/docs/getting-started/integrations/i18n/vue.md

# Source: https://ui.nuxt.com/raw/docs/getting-started/integrations/color-mode/vue.md

# Source: https://ui.nuxt.com/raw/docs/getting-started/integrations/icons/vue.md

# Source: https://ui.nuxt.com/raw/docs/getting-started/installation/vue.md

# Installation

> Learn how to install and configure Nuxt UI in your Vue application, compatible with both plain Vite and Inertia.

> [!NOTE]
> See: /docs/getting-started/installation/nuxt
> Looking for the Nuxt version?

## Setup

### Add to a Vue project

Install the Nuxt UI package
```bash
pnpm add @nuxt/ui tailwindcss

```

```bash
yarn add @nuxt/ui tailwindcss

```

```bash
npm install @nuxt/ui tailwindcss

```

```bash
bun add @nuxt/ui tailwindcss

```
Add the Nuxt UI Vite plugin in your vite.config.ts
```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui()
  ]
})

```

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'
import laravel from 'laravel-vite-plugin'

export default defineConfig({
  plugins: [
    laravel({
      input: ['resources/js/app.ts'],
      refresh: true
    }),
    vue({
      template: {
        transformAssetUrls: {
          base: null,
          includeAbsolute: false
        }
      }
    }),
    ui({
      router: 'inertia'
    })
  ]
})

```

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'
import adonisjs from '@adonisjs/vite/client'
import inertia from '@adonisjs/inertia/client'

export default defineConfig({
  plugins: [
    adonisjs({
      entrypoints: ['inertia/app/app.ts'],
      reload: ['resources/views/**/*.edge']
    }),
    inertia(),
    vue(),
    ui({
      router: 'inertia'
    })
  ]
})

```
> [!TIP]
> Nuxt UI registers `unplugin-auto-import` and `unplugin-vue-components`, which will generate `auto-imports.d.ts` and `components.d.ts` type declaration files. You will likely want to gitignore these, and add them to your `tsconfig`.
> ```json
> {
>   "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.vue", "auto-imports.d.ts", "components.d.ts"]
> }
> 
> ```
> 
> ```bash
> # Auto-generated type declarations
> auto-imports.d.ts
> components.d.ts
> 
> ```

> [!TIP]
> Internally, Nuxt UI relies on custom alias to resolve the theme types. If you're using TypeScript, you should add an alias to your `tsconfig` to enable auto-completion in your `vite.config.ts`.
> ```json
> {
>   "compilerOptions": {
>     "paths": {
>       "#build/ui": [
>         "./node_modules/.nuxt-ui/ui"
>       ]
>     }
>   }
> }
> 
> ```
> 
> ```json
> {
>   "compilerOptions": {
>     "paths": {
>       "#build/ui/*": [
>         "./node_modules/.nuxt-ui/ui/*"
>       ]
>     }
>   }
> }
> 
> ```

Use the Nuxt UI Vue plugin
```ts
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import ui from '@nuxt/ui/vue-plugin'
import App from './App.vue'

const app = createApp(App)

const router = createRouter({
  routes: [],
  history: createWebHistory()
})

app.use(router)
app.use(ui)

app.mount('#app')

```

```ts
import type { DefineComponent } from 'vue'
import { createInertiaApp } from '@inertiajs/vue3'
import ui from '@nuxt/ui/vue-plugin'
import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers'
import { createApp, h } from 'vue'

const appName = import.meta.env.VITE_APP_NAME || 'Laravel x Nuxt UI'

createInertiaApp({
  title: title => (title ? `${title} - ${appName}` : appName),
  resolve: name =>
    resolvePageComponent(
      `./pages/${name}.vue`,
      import.meta.glob<DefineComponent>('./pages/**/*.vue')
    ),
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .use(ui)
      .mount(el)
  }
})

```

```ts
import type { DefineComponent } from 'vue'
import { createInertiaApp } from '@inertiajs/vue3'
import ui from '@nuxt/ui/vue-plugin'
import { resolvePageComponent } from '@adonisjs/inertia/helpers'
import { createApp, h } from 'vue'

const appName = import.meta.env.VITE_APP_NAME || 'AdonisJS x Nuxt UI'

createInertiaApp({
  title: title => (title ? `${title} - ${appName}` : appName),
  resolve: name =>
    resolvePageComponent(
      `../pages/${name}.vue`,
      import.meta.glob<DefineComponent>('../pages/**/*.vue')
    ),
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .use(ui)
      .mount(el)
  }
})

```
Import Tailwind CSS and Nuxt UI in your CSS
```css
@import "tailwindcss";
@import "@nuxt/ui";

```

```css
@import "tailwindcss";
@import "@nuxt/ui";

```

```css
@import "tailwindcss";
@import "@nuxt/ui";

```
> [!TIP]
> Import the CSS file in your entrypoint.
> ```ts
> import './assets/main.css'
> 
> import { createApp } from 'vue'
> import { createRouter, createWebHistory } from 'vue-router'
> import ui from '@nuxt/ui/vue-plugin'
> import App from './App.vue'
> 
> const app = createApp(App)
> 
> const router = createRouter({
>   routes: [],
>   history: createWebHistory()
> })
> 
> app.use(router)
> app.use(ui)
> 
> app.mount('#app')
> 
> ```
> 
> ```ts
> import '../css/app.css'
> import type { DefineComponent } from 'vue'
> import { createInertiaApp } from '@inertiajs/vue3'
> import ui from '@nuxt/ui/vue-plugin'
> import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers'
> import { createApp, h } from 'vue'
> 
> const appName = import.meta.env.VITE_APP_NAME || 'Laravel x Nuxt UI'
> 
> createInertiaApp({
>   title: title => (title ? `${title} - ${appName}` : appName),
>   resolve: name =>
>     resolvePageComponent(
>       `./pages/${name}.vue`,
>       import.meta.glob<DefineComponent>('./pages/**/*.vue')
>     ),
>   setup({ el, App, props, plugin }) {
>     createApp({ render: () => h(App, props) })
>       .use(plugin)
>       .use(ui)
>       .mount(el)
>   }
> })
> 
> ```
> 
> ```ts
> import '../css/app.css'
> import type { DefineComponent } from 'vue'
> import { createInertiaApp } from '@inertiajs/vue3'
> import ui from '@nuxt/ui/vue-plugin'
> import { resolvePageComponent } from '@adonisjs/inertia/helpers'
> import { createApp, h } from 'vue'
> 
> const appName = import.meta.env.VITE_APP_NAME || 'AdonisJS x Nuxt UI'
> 
> createInertiaApp({
>   title: title => (title ? `${title} - ${appName}` : appName),
>   resolve: name =>
>     resolvePageComponent(
>       `../pages/${name}.vue`,
>       import.meta.glob<DefineComponent>('../pages/**/*.vue')
>     ),
>   setup({ el, App, props, plugin }) {
>     createApp({ render: () => h(App, props) })
>       .use(plugin)
>       .use(ui)
>       .mount(el)
>   }
> })
> 
> ```

::

> [!NOTE]
> It's recommended to install the [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) extension for VSCode and add the following settings:
> ```json
> {
>   "files.associations": {
>     "*.css": "tailwindcss"
>   },
>   "editor.quickSuggestions": {
>     "strings": "on"
>   },
>   "tailwindCSS.classAttributes": ["class", "ui"],
>   "tailwindCSS.experimental.classRegex": [
>     ["ui:\\s*{([^)]*)\\s*}", "(?:'|\"|`)([^']*)(?:'|\"|`)"]
>   ]
> }
> 
> ```

#### Wrap your app with App component

```vue
<template>
  <UApp>
    <RouterView />
  </UApp>
</template>

```

```vue
<template>
  <UApp>
    <!-- Your content goes here -->
  </UApp>
</template>

```

```vue
<template>
  <UApp>
    <!-- Your content goes here -->
  </UApp>
</template>

```

> [!NOTE]
> See: /docs/components/app
> The `App` component sets up global config and is required for Toast, Tooltip and programmatic overlays.

#### Add the `isolate` class to your root container

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Nuxt UI</title>
  </head>
  <body>
    <div id="app" class="isolate"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>

```

```blade
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    @inertiaHead
    @vite('resources/js/app.ts')
  </head>
  <body>
    <div class="isolate">
        @inertia
    </div>
  </body>
</html>

```

```edge
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    @inertiaHead()
    @vite(['inertia/app/app.ts', `inertia/pages/${page.component}.vue`])
  </head>
  <body>
    @inertia({ class: 'isolate' })
  </body>
</html>

```

> [!NOTE]
> This ensures styles are scoped to your app and prevents issues with overlays and stacking contexts.

::

### Use a Vue template

To quickly get started with Nuxt UI, you can use the [starter template](https://github.com/nuxt-ui-templates/starter-vue) by running:

```bash [Terminal]
npm create nuxt@latest -- --no-modules -t ui-vue
```

You can also get started with one of our [official templates](/templates):

**Starter**
A minimal template to get started with Nuxt UI.

**Dashboard**
A dashboard template with multi-column layout for building sophisticated admin interfaces.

**Starter Adonis**
A minimal Nuxt UI template for AdonisJS using Inertia.js.

**Starter Laravel**
A minimal Nuxt UI template for Laravel using Inertia.js.

You can use the `Use this template` button on GitHub to create a new repository or use the CLI:

```bash
npm create nuxt@latest -- --no-modules -t ui-vue

```

```bash
npm create nuxt@latest -- --no-modules -t ui-vue/dashboard

```

## Options

You can customize Nuxt UI by providing options in your `vite.config.ts`.

### `prefix`

Use the `prefix` option to change the prefix of the components.

- Default: `U`

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      prefix: 'Nuxt'
    })
  ]
})
```

### `ui`

Use the `ui` option to provide configuration for Nuxt UI.

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      ui: {
        colors: {
          primary: 'green',
          neutral: 'slate'
        }
      }
    })
  ]
})
```

### `colorMode`

Use the `colorMode` option to enable or disable the color mode integration from `@vueuse/core`.

- Default: `true`

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      colorMode: false
    })
  ]
})
```

### `theme.colors`

Use the `theme.colors` option to define the dynamic color aliases used to generate components theme.

- Default: `['primary', 'secondary', 'success', 'info', 'warning', 'error']`

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      theme: {
        colors: ['primary', 'error']
      }
    })
  ]
})
```

> [!TIP]
> See: /docs/getting-started/theme/design-system#colors
> Learn more about color customization and theming in the Theme section.

### `theme.transitions`

Use the `theme.transitions` option to enable or disable transitions on components.

- Default: `true`

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      theme: {
        transitions: false
      }
    })
  ]
})
```

> [!NOTE]
> This option adds the `transition-colors` class on components with hover or active states.

### `theme.defaultVariants`

Use the `theme.defaultVariants` option to override the default `color` and `size` variants for components.

- Default: `{ color: 'primary', size: 'md' }`

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      theme: {
        defaultVariants: {
          color: 'neutral',
          size: 'sm'
        }
      }
    })
  ]
})
```

### `theme.prefix` `4.2+`

Use the `theme.prefix` option to configure the same prefix you set on your Tailwind CSS import. This ensures Nuxt UI components use the correct prefixed utility classes and CSS variables.

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      theme: {
        prefix: 'tw'
      }
    })
  ]
})

```

```css
@import "tailwindcss" prefix(tw);
@import "@nuxt/ui";

```

This will automatically prefix all Tailwind utility classes and CSS variables in Nuxt UI component themes:

```html
<!-- Without prefix -->
<button class="px-2 py-1 text-xs hover:bg-primary/75">Button</button>

<!-- With prefix: tw -->
<button class="tw:px-2 tw:py-1 tw:text-xs tw:hover:bg-primary/75">Button</button>
```

> [!NOTE]
> See: https://tailwindcss.com/docs/styling-with-utility-classes#using-the-prefix-option
> Learn more about using a prefix in the Tailwind CSS documentation.

### `router` `4.3+`

Use the `router` option to configure routing integration. This is useful for applications that don't use `vue-router`, such as Electron apps, MPAs, or frameworks like [Inertia.js](https://inertiajs.com/) or [Hybridly](https://hybridly.dev/).

- Default: `true`

<table>
<thead>
  <tr>
    <th>
      Value
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code className="language-ts-type shiki shiki-themes material-theme-lighter material-theme material-theme-palenight" language="ts-type" style="">
        <span class="sBMFI">
          true
        </span>
      </code>
    </td>
    
    <td>
      Uses <code>
        vue-router
      </code>
      
       for navigation with <code>
        RouterLink
      </code>
      
       component.
    </td>
  </tr>
  
  <tr>
    <td>
      <code className="language-ts-type shiki shiki-themes material-theme-lighter material-theme material-theme-palenight" language="ts-type" style="">
        <span class="sBMFI">
          false
        </span>
      </code>
    </td>
    
    <td>
      Disables routing integration, links render as plain <code>
        <a>
      </code>
      
       tags.
    </td>
  </tr>
  
  <tr>
    <td>
      <code className="language-ts-type shiki shiki-themes material-theme-lighter material-theme material-theme-palenight" language="ts-type" style="">
        <span class="sMK4o">
          '
        </span>
        
        <span class="sfazB">
          inertia
        </span>
        
        <span class="sMK4o">
          '
        </span>
      </code>
    </td>
    
    <td>
      Uses Inertia.js for navigation with its <code>
        Link
      </code>
      
       component.
    </td>
  </tr>
</tbody>
</table>

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      router: false
    })
  ]
})
```

> [!TIP]
> You can provide custom navigation logic for frameworks like Hybridly by setting `router: false` in the Vite config and passing a function when installing the Vue plugin:
> ```ts
> import ui from '@nuxt/ui/vue-plugin'
> import { router } from 'hybridly'
> 
> app.use(ui, {
>   router: (event, { href, external }) => {
>     if (external) {
>       return
>     }
> 
>     event.preventDefault()
> 
>     router.navigate({ url: href })
>   }
> })
> 
> ```

> [!NOTE]
> When set to `false` or `'inertia'`, `vue-router` is not required as a dependency.

### `scanPackages` `4.3+`

Use the `scanPackages` option to specify additional npm packages that should be scanned for components using Nuxt UI. This is useful when you have a shared component library that uses Nuxt UI components internally.

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      scanPackages: ['@my-org/ui-components']
    })
  ]
})
```

> [!NOTE]
> By default, only `@nuxt/ui` is scanned. Use this option when your external packages contain Vue components that use Nuxt UI.

## Continuous releases

Nuxt UI uses [pkg.pr.new](https://github.com/stackblitz-labs/pkg.pr.new) for continuous preview releases, providing developers with instant access to the latest features and bug fixes without waiting for official releases.

Automatic preview releases are created for all commits and PRs to the `v4` branch. Use them by replacing your package version with the specific commit hash or PR number.

```diff [package.json]
{
  "dependencies": {
-   "@nuxt/ui": "^4.0.0",
+   "@nuxt/ui": "https://pkg.pr.new/@nuxt/ui@4c96909",
  }
}
```

> [!NOTE]
> pkg.pr.new will automatically comment on PRs with the installation URL, making it easy to test changes.
