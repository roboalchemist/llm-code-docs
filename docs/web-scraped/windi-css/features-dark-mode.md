# Source: https://windicss.org/features/dark-mode

Title: Windi CSS

URL Source: https://windicss.org/features/dark-mode

Markdown Content:
Dark Mode
---------

Windi CSS has out-of-box Dark Mode support.

By prefixing the `dark:` variant to utilities, they will only apply when dark mode is enabled. With the following example, the `Preview` text will be red on the light mode, and green on the dark mode. Try to play with it:

CSS

.text-red-400 {
  --tw-text-opacity: 1;
  color: rgba(248, 113, 113, var(--tw-text-opacity));
}
.dark .dark\:text-green-400 {
  --tw-text-opacity: 1;
  color: rgba(52, 211, 153, var(--tw-text-opacity));
}

We have two modes for enabling dark mode, [class mode](https://windicss.org/features/dark-mode#class-mode) and [media query mode](https://windicss.org/features/dark-mode#media-query-mode). By default, `class` mode is enabled.

Class mode
----------

Class mode gives you better control over when dark mode should enable.

windi.config.js

```
export default {
  darkMode: 'class',
  // ...
}
```

It detects the parent element's `class="dark"`, and usually you can apply it on the `html` element to make it work globally.

```
<html>
<body>
  <!-- Dark mode disabled -->
</body>
</html>

<html class="dark">
<body>
  <!-- Dark mode enabled -->
</body>
</html>
```

You can use the following snippet to make the color scheme match with the user's system preference, or write your own logic to manage it.

```
if (window.matchMedia('(prefers-color-scheme: dark)').matches)
  document.documentElement.classList.add('dark')
else
  document.documentElement.classList.add('light')
```

Config

CSS

.text-white {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}
.dark .dark\:text-white {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}

In media query mode, it uses the built-in `@media (prefers-color-scheme: dark)` query from the browser that always matches with the user's system preference.

windi.config.js

```
export default {
  darkMode: 'media',
  // ...
}
```

Config

CSS

.text-white {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}
@media (prefers-color-scheme: dark) {
  .dark\:text-white {
    --tw-text-opacity: 1;
    color: rgba(255, 255, 255, var(--tw-text-opacity));
  }
}
