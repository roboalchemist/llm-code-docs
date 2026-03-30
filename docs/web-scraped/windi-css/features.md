# Source: https://windicss.org/features/

Title: Windi CSS

URL Source: https://windicss.org/features/

Markdown Content:
Features
--------

[Windi CSS](https://github.com/windicss/windicss) is fully compatible with [Tailwind CSS](https://tailwindcss.com/docs) v2. On top of that, we have many additional features that boost your workflow further and open up many more possibilities.

Value Auto-infer
----------------

Use arbitrary values in your classes and generate corresponding styles.

```
<!-- sizes and positions -->
<div class="p-5px mt-[0.3px]"></div>

<!-- colors -->
<button class="bg-hex-b2a8bb"></button>
<button class="bg-[hsl(211.7,81.9%,69.6%)]"></button>

<!-- grid template -->
<div class="grid-cols-[auto,1fr,30px]"></div>
```

[Learn more](https://windicss.org/features/value-auto-infer)

Variant Groups
--------------

Apply utilities to the same variant by grouping them with parentheses.

```
<div class="bg-white dark:hover:(bg-gray-800 font-medium text-white)"/>
```

```
<div class="bg-white dark:hover:bg-gray-800 dark:hover:font-medium dark:hover:text-white"/>
```

[Learn more](https://windicss.org/features/variant-groups)

Responsive Design
-----------------

Extended responsive breakpoint control.

```
<div class="p-1 md:p-2 <lg:p-3"></div>
```

[Learn more](https://windicss.org/features/responsive-design)

Important Prefix
----------------

Prefix any utility classes with `!` to set them as `!important`.

```
<div class="text-red-400 !text-green-300">Green</div>
```

[Learn more](https://windicss.org/features/important-prefix)

Shortcuts
---------

Quickly combine utilities to create reusable components.

windi.config.js

```
export default {
  theme: {
    /* ... */
  },
  shortcuts: {
    'btn': 'py-2 px-4 font-semibold rounded-lg shadow-md',
    'btn-green': 'text-white bg-green-500 hover:bg-green-700',
  },
}
```

```
<div class="btn hover:btn-green"></div>
```

[Learn more](https://windicss.org/features/shortcuts)

Dark Mode
---------

```
<div class="text-black dark:text-white"></div>
```

[Learn more](https://windicss.org/features/dark-mode)

RTL
---

```
<div class="text-green-400 rtl:(text-red-400 text-right)"></div>
```

[Learn more](https://windicss.org/features/rtl)

Directives
----------

Tailwind-like `@apply`, `@screen` directives are fully supported.

```
.btn {
  @apply font-bold py-2 px-4 rounded;
}
.btn-blue {
  @apply bg-blue-500 hover:bg-blue-700 text-white;
  padding-top: 1rem;
}
```

[Learn more](https://windicss.org/features/directives)

Visual Analyzer
---------------

We provided a visual analyzer for you to have an overview of your utility usage and design system.

[Learn more](https://windicss.org/features/analyzer)
