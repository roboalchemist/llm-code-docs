# Source: https://windicss.org/features/directives

Title: Windi CSS

URL Source: https://windicss.org/features/directives

Markdown Content:
Directives
----------

You can use a combination of directives and CSS to take advantage of the available utilities.

@apply
------

Use `@apply` to inline any existing utility classes into your style block.

This is useful when you find a common utility pattern in your HTML that you'd like to extract to a new component.

Generated CSS

```
.btn {
  border-radius: 0.25rem;
  font-weight: 700;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-left: 1rem;
  padding-right: 1rem;
}
.btn-blue {
  --tw-bg-opacity: 1;
  background-color: rgba(59, 130, 246, var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
  padding-top: 1rem;
}
.btn-blue:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(29, 78, 216, var(--tw-bg-opacity));
}
```

If you'd like to `@apply` an existing class and make it `!important`, simply add `!important` to the end of the declaration:

Generated CSS

```
.btn {
  border-radius: 0.25rem !important;
  font-weight: 700 !important;
  padding-top: 0.5rem !important;
  padding-bottom: 0.5rem !important;
  padding-left: 1rem !important;
  padding-right: 1rem !important;
}
```

@variants
---------

You can generate [screen variants, state variants, theme variants](https://windicss.org/utilities/general/variants) of your own utilities by wrapping their definitions in the `@variants` directive.

Generated CSS

```
.rotate-0:focus {
  transform: rotate(0deg);
}
.rotate-90:focus {
  transform: rotate(90deg);
}
.rotate-0:hover {
  transform: rotate(0deg);
}
.rotate-90:hover {
  transform: rotate(90deg);
}
.dark .bg-color {
  background-color: #1c1c1e;
}
```

@screen
-------

The `@screen` directive allows you to create media queries that reference your breakpoints by name instead of duplicating their values in your own CSS.

Generated CSS

```
@media (min-width: 640px) {
  .custom {
    font-size: 1.125rem;
    line-height: 1.75rem;
  }
}
```

@layer
------

The `@layer` directive sets the order of how each class is applied. Valid layers are `base`, `components`, and `utilities`.

Generated CSS

```
.components {
  --tw-bg-opacity: 1;
  background-color: rgba(239, 68, 68, var(--tw-bg-opacity));
}
.utilities {
  max-width: 768px;
}
base {
  margin-left: auto;
}
.normal {
  margin-right: auto;
}
```

theme()
-------

The `theme()` function allows you to access your config values using dot notation.

Generated CSS

```
.btn-blue {
  background-color: #3b82f6;
}
```
