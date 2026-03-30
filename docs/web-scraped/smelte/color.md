# Source: https://smeltejs.com/color

Title: Material design using Tailwind CSS for Svelte

URL Source: https://smeltejs.com/color

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

#### Color helper classes

Right now Smelte adds very little to what Tailwind [has](https://tailwindcss.com/docs/background-color/)[to offer](https://tailwindcss.com/docs/text-color/) dealing with color except for porting the Material design color [palette](https://material.io/design/color/#tools-for-picking-colors) and adding a few extra utilities like caret color on inputs or colored ripple animation effect. Colors themselves are configured in [tailwind.config.js](https://github.com/matyunya/smelte/blob/master/tailwind.config.js) .

##### Background

.bg-{color}-{variant} gives element appropriate background color: 
```javascript
<div class="bg-deep-purple-500 text-white p-4">This div is deep purple.</div>
```

This div is deep purple.

##### Text

.text-{color}-{variant} changes text color accordingly: 
```javascript
<h4 class="text-error-500">This header is error</h4>
```

#### This header is error color

##### Border

 Same principle applies to border, but there are also border width border-{n} and type border-{solid|dashed|dotted|none} helpers. 
```javascript
<div class="border-2 border-secondary-600 p-4">This div has secondary border</div>
```

This div has secondary color border
