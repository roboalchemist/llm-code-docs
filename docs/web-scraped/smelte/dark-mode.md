# Source: https://smeltejs.com/dark-mode

Title: Material design using Tailwind CSS for Svelte

URL Source: https://smeltejs.com/dark-mode

Markdown Content:
Smelte: Material design using Tailwind CSS for Svelte
===============

[Text fields](https://smeltejs.com/components/text-fields)[Buttons](https://smeltejs.com/components/buttons)[Selection controls](https://smeltejs.com/components/selection-controls)[Lists](https://smeltejs.com/components/lists)[Selects](https://smeltejs.com/components/selects)[Snackbars](https://smeltejs.com/components/snackbars)[Dialogs](https://smeltejs.com/components/dialogs)[Navigation drawers](https://smeltejs.com/components/navigation-drawers)[Progress indicators](https://smeltejs.com/components/progress-indicators)[Chips](https://smeltejs.com/components/chips)[Tabs](https://smeltejs.com/components/tabs)[Cards](https://smeltejs.com/components/cards)[Menus](https://smeltejs.com/components/menus)[Images](https://smeltejs.com/components/images)[Sliders](https://smeltejs.com/components/sliders)[Data tables](https://smeltejs.com/components/data-tables)[Tooltips](https://smeltejs.com/components/tooltips)[Treeviews](https://smeltejs.com/components/treeviews)[Date pickers](https://smeltejs.com/components/date-pickers)[Typography](https://smeltejs.com/typography)[Color](https://smeltejs.com/color)[Breakpoints](https://smeltejs.com/breakpoints)[Dark mode](https://smeltejs.com/dark-mode)[![Image 1: Smelte logo](https://smeltejs.com/logo.svg) ###### SMELTE](https://smeltejs.com/)

[Components](https://smeltejs.com/components)[Typography](https://smeltejs.com/typography)[Color](https://smeltejs.com/color)[Breakpoints](https://smeltejs.com/breakpoints)[Dark mode](https://smeltejs.com/dark-mode)

_wb\_sunny_

_menu_

[![Image 2: Github Smelte](https://smeltejs.com/github.png)](https://github.com/matyunya/smelte)

###### Components

[* Text fields](https://smeltejs.com/components/text-fields)[* Buttons](https://smeltejs.com/components/buttons)[* Selection controls](https://smeltejs.com/components/selection-controls)[* Lists](https://smeltejs.com/components/lists)[* Selects](https://smeltejs.com/components/selects)[* Snackbars](https://smeltejs.com/components/snackbars)[* Dialogs](https://smeltejs.com/components/dialogs)[* Navigation drawers](https://smeltejs.com/components/navigation-drawers)[* Progress indicators](https://smeltejs.com/components/progress-indicators)[* Chips](https://smeltejs.com/components/chips)[* Tabs](https://smeltejs.com/components/tabs)[* Cards](https://smeltejs.com/components/cards)[* Menus](https://smeltejs.com/components/menus)[* Images](https://smeltejs.com/components/images)[* Sliders](https://smeltejs.com/components/sliders)[* Data tables](https://smeltejs.com/components/data-tables)[* Tooltips](https://smeltejs.com/components/tooltips)[* Treeviews](https://smeltejs.com/components/treeviews)[* Date pickers](https://smeltejs.com/components/date-pickers)

* * *

###### Utilities

[* Typography](https://smeltejs.com/typography)[* Color](https://smeltejs.com/color)[* Breakpoints](https://smeltejs.com/breakpoints)[* Dark mode](https://smeltejs.com/dark-mode)

* * *

#### Dark mode

Smelte uses css pseudo-class variant [feature](https://tailwindcss.com/docs/configuring-variants/) of Tailwind to enable dark mode. Basic dark mode switch looks like this:

`<button bind:value={$darkMode}>Toggle dark mode</button>`
This will append mode-dark class to the document body which will enable all generated classes preceded by pseudo-class "dark:". By default smelte generates following variants:

```
backgroundColor: ["dark", "dark-hover", "hover"],
borderColor: ["dark", "dark-focus"],
textColor: ["dark", "dark-hover", "dark-active"]
```

Now you can use dark theme classes like dark:bg-white (try using the theme toggle on the top right).

I am a light div.

```
<div class="duration-200 ease-in p-10 my-10 bg-black dark:bg-white text-white dark:text-black">
  I am a {$darkMode ? "dark" : "light"} div.
</div>
```

If you don't need dark mode at all, you can pass darkMode: false to the smelte-rollup-plugin and it will generate no extra CSS.
