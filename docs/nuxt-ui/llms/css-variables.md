# Source: https://ui.nuxt.com/raw/docs/getting-started/theme/css-variables.md

# CSS Variables

> Nuxt UI uses CSS variables as design tokens for flexible, consistent theming with built-in light and dark mode support.

## Colors

Nuxt UI provides Tailwind CSS utility classes for each [semantic color](/docs/getting-started/theme/design-system#semantic-colors) you define, allowing you to use class names like `text-error` or `bg-success`:

```vue
<template>
  <p>
  <span>
  Primary</span>
  <span>
  Secondary</span>
  <span>
  Success</span>
  <span>
  Info</span>
  <span>
  Warning</span>
  <span>
  Error</span></p>
  <template v-slot:code=>
  <pre className=language-vue shiki shiki-themes material-theme-lighter material-theme material-theme-palenight code=<template>
    <span class="text-primary">Primary</span>
    <span class="text-secondary">Secondary</span>
    <span class="text-success">Success</span>
    <span class="text-info">Info</span>
    <span class="text-warning">Warning</span>
    <span class="text-error">Error</span>
  </template>
   language=vue meta= style=>
  <code __ignoreMap=>
  <span class=line>
  <span class=sMK4o>
  <</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-primary</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Primary</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-secondary</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Secondary</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-success</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Success</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-info</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Info</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-warning</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Warning</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-error</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Error</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span></code></pre></template>
</template>
```

Each utility class uses a CSS variable to set its color for light and dark modes:

```css
:root {
  --ui-primary: var(--ui-color-primary-500);
  --ui-secondary: var(--ui-color-secondary-500);
  --ui-success: var(--ui-color-success-500);
  --ui-info: var(--ui-color-info-500);
  --ui-warning: var(--ui-color-warning-500);
  --ui-error: var(--ui-color-error-500);
}

```

```css
.dark {
  --ui-primary: var(--ui-color-primary-400);
  --ui-secondary: var(--ui-color-secondary-400);
  --ui-success: var(--ui-color-success-400);
  --ui-info: var(--ui-color-info-400);
  --ui-warning: var(--ui-color-warning-400);
  --ui-error: var(--ui-color-error-400);
}

```

> [!TIP]
> You can adjust which shade each utility class uses for light and dark mode in your `main.css` file:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> :root {
>   --ui-primary: var(--ui-color-primary-700);
> }
> 
> .dark {
>   --ui-primary: var(--ui-color-primary-200);
> }
> 
> ```

> [!WARNING]
> You can't use `primary: 'black'` in your [config](/docs/getting-started/theme/design-system#runtime-configuration) because `black` doesn't have multiple shades. To use solid black or white as your primary color, set it directly in your `main.css` file:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> :root {
>   --ui-primary: black;
> }
> 
> .dark {
>   --ui-primary: white;
> }
> 
> ```

## Text

Nuxt UI provides Tailwind CSS utility classes for text colors, allowing you to use class names like `text-dimmed` or `text-muted`:

```vue
<template>
  <p>
  <span>
  Dimmed</span>
  <span>
  Muted</span>
  <span>
  Toned</span>
  <span>
  Text</span>
  <span>
  Highlighted</span>
  <span>
  Inverted</span></p>
  <template v-slot:code=>
  <pre className=language-vue shiki shiki-themes material-theme-lighter material-theme material-theme-palenight code=<template>
    <span class="text-dimmed">Dimmed</span>
    <span class="text-muted">Muted</span>
    <span class="text-toned">Toned</span>
    <span class="text-default">Text</span>
    <span class="text-highlighted">Highlighted</span>
    <span class="text-inverted bg-inverted">Inverted</span>
  </template>
   language=vue meta= style=>
  <code __ignoreMap=>
  <span class=line>
  <span class=sMK4o>
  <</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-dimmed</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Dimmed</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-muted</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Muted</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-toned</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Toned</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-default</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Text</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-highlighted</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Highlighted</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  span</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  text-inverted bg-inverted</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Inverted</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  span</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span></code></pre></template>
</template>
```

Each utility class uses a CSS variable to set its color for light and dark modes:

```css
:root {
  --ui-text-dimmed: var(--ui-color-neutral-400);
  --ui-text-muted: var(--ui-color-neutral-500);
  --ui-text-toned: var(--ui-color-neutral-600);
  --ui-text: var(--ui-color-neutral-700);
  --ui-text-highlighted: var(--ui-color-neutral-900);
  --ui-text-inverted: white;
}

```

```css
.dark {
  --ui-text-dimmed: var(--ui-color-neutral-500);
  --ui-text-muted: var(--ui-color-neutral-400);
  --ui-text-toned: var(--ui-color-neutral-300);
  --ui-text: var(--ui-color-neutral-200);
  --ui-text-highlighted: white;
  --ui-text-inverted: var(--ui-color-neutral-900);
}

```

> [!TIP]
> You can customize these CSS variables in your `main.css` file:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> :root {
>   --ui-text: var(--ui-color-neutral-900);
> }
> 
> .dark {
>   --ui-text: white;
> }
> 
> ```

## Background

Nuxt UI provides Tailwind CSS utility classes for background colors, allowing you to use class names like `bg-default` or `bg-muted`:

```vue
<template>
  <p>
  <span>
  Default</span>
  <span>
  Muted</span>
  <span>
  Elevated</span>
  <span>
  Accented</span>
  <span>
  Inverted</span></p>
  <template v-slot:code=>
  <pre className=language-vue shiki shiki-themes material-theme-lighter material-theme material-theme-palenight code=<template>
    <div class="bg-default">Default</div>
    <div class="bg-muted">Muted</div>
    <div class="bg-elevated">Elevated</div>
    <div class="bg-accented">Accented</div>
    <div class="bg-inverted text-inverted">Inverted</div>
  </template>
   language=vue meta= style=>
  <code __ignoreMap=>
  <span class=line>
  <span class=sMK4o>
  <</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  bg-default</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Default</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  bg-muted</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Muted</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  bg-elevated</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Elevated</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  bg-accented</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Accented</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  bg-inverted text-inverted</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Inverted</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span></code></pre></template>
</template>
```

Each utility class uses a CSS variable to set its color for light and dark modes:

```css
:root {
  --ui-bg: white;
  --ui-bg-muted: var(--ui-color-neutral-50);
  --ui-bg-elevated: var(--ui-color-neutral-100);
  --ui-bg-accented: var(--ui-color-neutral-200);
  --ui-bg-inverted: var(--ui-color-neutral-900);
}

```

```css
.dark {
  --ui-bg: var(--ui-color-neutral-900);
  --ui-bg-muted: var(--ui-color-neutral-800);
  --ui-bg-elevated: var(--ui-color-neutral-800);
  --ui-bg-accented: var(--ui-color-neutral-700);
  --ui-bg-inverted: white;
}

```

> [!TIP]
> You can customize these CSS variables in your `main.css` file:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> :root {
>   --ui-bg: var(--ui-color-neutral-50);
> }
> 
> .dark {
>   --ui-bg: var(--ui-color-neutral-950);
> }
> 
> ```

## Border

Nuxt UI provides Tailwind CSS utility classes for border colors, allowing you to use class names like `border-default` or `border-muted`:

```vue
<template>
  <p>
  <span>
  Default</span>
  <span>
  Muted</span>
  <span>
  Accented</span>
  <span>
  Inverted</span></p>
  <template v-slot:code=>
  <pre className=language-vue shiki shiki-themes material-theme-lighter material-theme material-theme-palenight code=<template>
    <div class="border border-default">Default</div>
    <div class="border border-muted">Muted</div>
    <div class="border border-accented">Accented</div>
    <div class="border border-inverted">Inverted</div>
  </template>
   language=vue meta= style=>
  <code __ignoreMap=>
  <span class=line>
  <span class=sMK4o>
  <</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  border border-default</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Default</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  border border-muted</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Muted</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  border border-accented</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Accented</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  border border-inverted</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  Inverted</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span></code></pre></template>
</template>
```

Each utility class uses a CSS variable to set its color for light and dark modes:

```css
:root {
  --ui-border: var(--ui-color-neutral-200);
  --ui-border-muted: var(--ui-color-neutral-200);
  --ui-border-accented: var(--ui-color-neutral-300);
  --ui-border-inverted: var(--ui-color-neutral-900);
}

```

```css
.dark {
  --ui-border: var(--ui-color-neutral-800);
  --ui-border-muted: var(--ui-color-neutral-700);
  --ui-border-accented: var(--ui-color-neutral-700);
  --ui-border-inverted: white;
}

```

> [!TIP]
> You can customize these CSS variables in your `main.css` file:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> :root {
>   --ui-border: var(--ui-color-neutral-100);
> }
> 
> .dark {
>   --ui-border: var(--ui-color-neutral-900);
> }
> 
> ```

## Radius

Nuxt UI overrides Tailwind CSS's default `rounded-*` utilities with a unified border radius system, allowing you to use regular [border radius utilities](https://tailwindcss.com/docs/border-radius) like `rounded-xs` or `rounded-2xl`:

```vue
<template>
  <p>
  <span>
  xs</span>
  <span>
  sm</span>
  <span>
  md</span>
  <span>
  lg</span>
  <span>
  xl</span>
  <span>
  2xl</span>
  <span>
  3xl</span></p>
  <template v-slot:code=>
  <pre className=language-vue shiki shiki-themes material-theme-lighter material-theme material-theme-palenight code=<template>
    <div class="rounded-xs">xs</div>
    <div class="rounded-sm">sm</div>
    <div class="rounded-md">md</div>
    <div class="rounded-lg">lg</div>
    <div class="rounded-xl">xl</div>
    <div class="rounded-2xl">2xl</div>
    <div class="rounded-3xl">3xl</div>
  </template>
   language=vue meta= style=>
  <code __ignoreMap=>
  <span class=line>
  <span class=sMK4o>
  <</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  rounded-xs</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  xs</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  rounded-sm</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  sm</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  rounded-md</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  md</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  rounded-lg</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  lg</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  rounded-xl</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  xl</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  rounded-2xl</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  2xl</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  div</span>
  <span class=spNyl>
   class</span>
  <span class=sMK4o>
  =</span>
  <span class=sMK4o>
  "</span>
  <span class=sfazB>
  rounded-3xl</span>
  <span class=sMK4o>
  "</span>
  <span class=sMK4o>
  ></span>
  <span class=sTEyZ>
  3xl</span>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  div</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span></code></pre></template>
</template>
```

These utility classes are calculated based on a global `--ui-radius` CSS variable, which defines the base radius value applied across all components for a consistent look.

```css
:root {
  --ui-radius: 0.25rem;
}
```

> [!TIP]
> You can customize the base radius value in your `main.css` file:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> :root {
>   --ui-radius: 0.5rem;
> }
> 
> ```

> [!NOTE]
> Try the  theme picker in the header above to change the base radius value.

## Container

Nuxt UI provides a `--ui-container` CSS variable that controls the maximum width of the [Container](/docs/components/container) component.

```css
:root {
  --ui-container: 80rem; /* var(--container-7xl) */
}
```

> [!TIP]
> You can customize this value in your `main.css` file to adjust container widths consistently throughout your application:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> @theme {
>   --container-8xl: 90rem;
> }
> 
> :root {
>   --ui-container: var(--container-8xl);
> }
> 
> ```

## Header

Nuxt UI provides a `--ui-header-height` CSS variable that controls the height of the [Header](/docs/components/header) component.

```css
:root {
  --ui-header-height: --spacing(16);
}
```

> [!TIP]
> You can customize this value in your `main.css` to adjust header height consistently throughout your application:
> ```css
> @import "tailwindcss";
> @import "@nuxt/ui";
> 
> :root {
>   --ui-header-height: --spacing(24);
> }
> 
> ```

## Body

Nuxt UI applies default classes on the `<body>` element of your app for consistent theming across light and dark modes:

```css
body {
  @apply antialiased text-default bg-default scheme-light dark:scheme-dark;
}
```
