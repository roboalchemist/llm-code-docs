# Source: https://vueform.com/docs/styles-and-layout

Title: Styles and Layout | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/styles-and-layout

Markdown Content:
Learn about the many ways how Vueform styles and layouts can be customized.

Size [​](https://vueform.com/docs/styles-and-layout#size)
---------------------------------------------------------

We can use any element in three different sizes: `sm`, `md` and `lg`. The `md` is the default one, while we can switch to eg. `sm` using `size` prop:

vue

```
<TextElement label="Small" placeholder="Small" size="sm" ... />
<TextElement label="Medium" placeholder="Medium" ... />
<TextElement label="Large" placeholder="Large" size="lg" ... />
```

Small

Small

Medium

Medium

Large

Large

Views [​](https://vueform.com/docs/styles-and-layout#views)
-----------------------------------------------------------

Some elements and components have alternative views, that we can use with `view` option:

vue

```
<!-- Default view -->
<CheckboxgroupElement :items="['Vue.js', 'React', 'AngularJS']" ... />

<!-- Tabs view -->
<CheckboxgroupElement view="tabs" :items="['Vue.js', 'React', 'AngularJS']" ... />

<!-- Blocks view -->
<CheckboxgroupElement view="blocks" :items="[
  { value: 'Vue.js', label: 'Vue.js', description: 'Vue.js framework' },
  { value: 'React', label: 'React', description: 'React framework' },
  { value: 'AngularJS', label: 'AngularJS', description: 'AngularJS framework' },
]" ... />
```

### Views for Children [​](https://vueform.com/docs/styles-and-layout#views-for-children)

The `view` we define for an element will be applied to each of its child components (if the view exist for them with the same name). If we want to change the views of the element's child components, we can use `views` property, which overrides the elements default `view` option:

vue

```
<TextElement :views="{
  ElementLabel: 'highlighted'
}" ... />
```

In this case `ElementLabel_highlighted` template will be used instead of `ElementLabel` for this specific element if it registered as a template.

If a component has multiple available views, they can be found at the Components reference, under the components **Views** section.

Columns [​](https://vueform.com/docs/styles-and-layout#columns)
---------------------------------------------------------------

We can pass an object to `:columns` prop of any element to define its column widths:

vue

`<TextElement label="Label" :columns="{ container: 12, label: 3, wrapper: 12 }" ... />`

Columns add grid classes (like `col-6` or `w-1/2`) to `container`, `label` and `wrapper` of an element, where:

*   `container` is the outermost DOM of the element that contains both `label` and `wrapper`
*   `label` contains the label
*   `wrapper` contains the custom parts of element.

Here they are more visually:

`container: 12`

`label: 3`

`wrapper: 12`

The value of `container` defines the size of the element's container. `12` will result in full width, `6` in half, `4` in third and so on.

The value of `label` defines the amount of space the label should take up **within the container**. If the `container` is `12` and `label` is `6` the label is going to take up half the space and the element's wrapper will the other half (which is calculated automatically). If the `container` is `6` and `label` is `6`, the label will only take up one forth and the element's wrapper the rest. In case the `label` has full width (`12`) the element's wrapper will also take up **full space** instead of being zero.

The value of `wrapper` defines the size of the element's wrapper **within the space left for it in the container after subtracting the size of the label**. If the `container` is `12` and `label` is `4` the space left for the element's wrapper is `8`. In this case if the `wrapper` value is `12` it will take up the full space left for the it (which is `8`) while if it is changed to `6` it will only take up half the space left for it (`4`):

vue

```
<TextElement label="Label" :columns="{ container: 12, label: 4, wrapper: 12 }" />
<TextElement label="Label" :columns="{ container: 12, label: 4, wrapper: 6 }" />
```

Note that while the size of the element's wrapper container changes the size of other _extras_ like a description or error won't be limited to the field's space. Instead it will take up the full space left by the label:

vue

```
<TextElement
  label="Label"
  description="Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  :columns="{ container: 12, label: 4, wrapper: 6 }"
  ...
/>
```

We can set the value of `columns` as a `number` which case the `container` will receive its value without affecting the default `label` and `wrapper` values:

vue

`<TextElement label="Label" :columns="6" ... /> <!-- { container: 6, label: 3, wrapper: 12 } -->`

### Responsive Columns [​](https://vueform.com/docs/styles-and-layout#responsive-columns)

We can also define column values for different **breakpoints** using the theme system's breakpoints like `sm`, `md`, etc. as keys:

vue

```
<TextElement label="Label" :columns="{
  default: { container: 12, label: 12, wrapper: 12 },
  sm: { container: 12, label: 4, wrapper: 12 },
  md: 12,
  lg: { container: 12, label: 2, wrapper: 12 }
}" ... />
```

Vueform is using a **mobile-first** breakpoint system to accomodate most popular CSS frameworks like Bootstrap or Tailwind CSS. The `default` breakpoint is the one that will be used below the lowest breakpoint.

The default breakpoints are (based on [Tailwind CSS breakpoint system](https://tailwindcss.com/docs/responsive-design)):

| Breakpoint prefix | Minimum width | CSS |
| --- | --- | --- |
| `sm` | 640px | `@media (min-width: 640px) { ... }` |
| `md` | 768px | `@media (min-width: 768px) { ... }` |
| `lg` | 1024px | `@media (min-width: 1024px) { ... }` |
| `xl` | 1280px | `@media (min-width: 1280px) { ... }` |
| `2xl` | 1536px | `@media (min-width: 1536px) { ... }` |

### Customizing Breakpoints [​](https://vueform.com/docs/styles-and-layout#customizing-breakpoints)

We can customize the form's breakpoints to fit our project's breakpoints.

#### In Tailwind Theme [​](https://vueform.com/docs/styles-and-layout#in-tailwind-theme)

When using `tailwind` theme we don't have to do anything specific beside customizing the `tailwind.config.js`[to use certain breakpoints](https://tailwindcss.com/docs/responsive-design#customizing-your-theme). Once we done that the same breakpoints can used for column definition.

Eg. customizing the `tailwind.config.js` with the following values:

js

```
// tailwind.config.js

module.exports = {
  theme: {
    screens: {
      'tablet': '640px',
      // => @media (min-width: 640px) { ... }

      'laptop': '1024px',
      // => @media (min-width: 1024px) { ... }

      'desktop': '1280px',
      // => @media (min-width: 1280px) { ... }
    },
  }
}
```

Allows us to use the following breakpoints for columns for any Vueform element:

template

```
<TextElement label="Label" :columns="{
  default: { container: 12, label: 12, wrapper: 12 },
  tablet: { container: 12, label: 4, wrapper: 12 },
  laptop: { container: 12, label: 3, wrapper: 12 },
  desktop: { container: 12, label: 2, wrapper: 12 },
}" ... />
```

#### In Other Themes [​](https://vueform.com/docs/styles-and-layout#in-other-themes)

In other themes like the default `vueform` theme we need to customize the breakpoints via a **scss variable**.

The first step is to replace our original `css` import with the `scss` counterpart:

scss

```
// eg. index.css

// Original import
@import './../node_modules/@vueform/vueform/dist/vueform.css';
```

Instead of using a `css` create an `scss` file and import that somewhere in your project. The `scss` file should contain the following:

scss

```
// eg. index.scss

// New import
@import './../node_modules/@vueform/vueform/themes/vueform/scss/index.scss';
```

Now we can rely on `scss` variables and we can override the breakpoints:

scss

```
// eg. index.scss

$grid-breakpoints: (
  tablet: 640px,
  laptop: 1024px,
  desktop: 1280px,
);

// New import
@import './../node_modules/@vueform/vueform/themes/vueform/scss/index.scss';
```

This will allow us to use our custom breakpoints in any Vueform element:

template

```
<TextElement label="Label" :columns="{
  default: { container: 12, label: 12, wrapper: 12 },
  tablet: { container: 12, label: 4, wrapper: 12 },
  laptop: { container: 12, label: 3, wrapper: 12 },
  desktop: { container: 12, label: 2, wrapper: 12 },
}" ... />
```

Changing Classes [​](https://vueform.com/docs/styles-and-layout#changing-classes)
---------------------------------------------------------------------------------

### Basics [​](https://vueform.com/docs/styles-and-layout#basics)

Each component has a template defined by the theme. The template includes 3 parts:

*   the actual `<template>` of the component
*   the classes that can be used in the template in `defaultClasses` object in `data()`
*   `<style>` if the component is using named classes and not utility classes.

> Themes also include a `classes.js` file that overrides any `defaultClasses` defined by the templates, which is useful if we want to centralize class definitions. Also, the `<template>` part is provided by a theme called `blank` for each theme, so they don't have to be reimplemented in different themes only when something requires structural change.

Let's take a look at the `<template>` part of [`TextElement`](https://vueform.com/reference/text-element) component:

template

```
<!-- From: @vueform/vueform/themes/blank/templates/elements/TextElement.vue -->

<template>
  <ElementLayout class="classes.container">
    <template element>
      <div class="classes.inputContainer">
        <ElementAddon type="before" ... />
        <ElementAddon type="after" ... />
        <ElementLabelFloating ... />
        <ElementLoader ... />
        <input class="classes.input" ... />
      </div>
    </template>
  </ElementLayout>
</template>
```

The template has been simplified for better readability, but what's important for us are the **classes**.

We can see that `TextElement` uses three class names: `container`, `inputContainer` and `input`.

These classes are defined by themes differently, here's how they look like in `vueform` theme:

js

```
// From: @vueform/vueform/themes/vueform/templates/elements/TextElement.vue

{
  container: '',
  inputContainer: 'vf-input-group',
  // ...
  input: 'vf-input',
  input_enabled: '',
  input_disabled: '',
  input_sm: 'vf-input-sm',
  input_md: '',
  input_lg: 'vf-input-lg',
  // ...
  $input: (classes, { isDisabled, Size }) => ([
    classes.input,
    classes[`input_${Size}`],
    isDisabled ? classes.input_disabled : classes.input_enabled
  ])
}
```

And this is how `tailwind` theme defines them:

js

```
// From: @vueform/vueform/themes/tailwind/classes.js

{
  container: '',
  inputContainer: 'w-full flex',
  // ...
  input: 'w-full form-border form-border-color z-1 transition-shadow addon-before:form-rounded-l-none outline-none addon-after:form-rounded-r-none',
  input_enabled: 'focus:form-ring',
  input_disabled: 'form-bg-disabled form-text-disabled',
  input_sm: 'form-p-input-sm form-rounded-sm form-text-sm',
  input_md: 'form-p-input form-rounded',
  input_lg: 'form-p-input-lg form-rounded-lg form-text-lg with-floating:form-p-input-floating-lg',
  // ...
  $input: (classes, { isDisabled, Size }) => ([
    classes.input,
    classes[`input_${Size}`],
    isDisabled ? classes.input_disabled : classes.input_enabled
  ]),
}
```

_(The `TextElement` template changed in `1.2.0`, but it's easier to grasp the concept with this example.)_

We can see that `input` also has conditional classes:

*   `input_enabled` - added when the input is enabled
*   `input_disabled` - added when the input is disabled
*   `input_sm` - added when the input's size is `sm`
*   `input_md` - added when the input's size is `md`
*   `input_lg` - added when the input's size is `lg`.

These classes are only added to `input` if their conditions are fulfilled.

> If a class name is also defined as a `function` and starts with a `$` it can return a dynamic value for the original class name.

Based on this, the actual `<input>` field have different classes in different states.

For example in `tailwind` theme the `TextElement`'s `input` class has `input_md` and `input_enabled` added by default:

js

```
input: `w-full form-border form-border-color z-1 transition-shadow
        addon-before:form-rounded-l-none outline-none
        addon-after:form-rounded-r-none ` // from `input`
     + `form-p-input form-rounded ` // from `input_md`
     + `focus:form-ring` // from `input_enabled`
```

If the element becomes **disabled** and uses **sm** size it'll change to this:

js

```
input: `w-full form-border form-border-color z-1 transition-shadow
        addon-before:form-rounded-l-none outline-none
        addon-after:form-rounded-r-none ` // from `input`
     + `form-p-input-sm form-rounded-sm form-text-sm ` // from `input_sm`
     + `form-bg-disabled form-text-disabled` // from `input_disabled`
```

This is how Vueform manages the different states and appearances of components driven by external parameters like [`Size`](https://vueform.com/reference/text-element#property-size) or [`isDisabled`](https://vueform.com/reference/text-element#property-is-disabled).

### Class Helpers [​](https://vueform.com/docs/styles-and-layout#class-helpers)

This is how `TextElement` gets rendered in the browser using `tailwind` theme:

If we check the source code we'll see it's complete HTML structure:

html

```
<div class="form-col w-full">
  <div class="form-row flex flex-wrap form-mb-gutter">
    <label for="text" class="form-col pr-4 form-py-input-border w-3/12">
      <span>Text</span>
    </label>
    <div class="flex-1 w-9/12">
      <div class="form-col w-full"></div>
      <div class="form-col w-full">
        <div class="w-full flex">
          <input type="text" name="text" id="text" class="w-full form-border form-border-color z-1 transition-shadow addon-before:form-rounded-l-none outline-none addon-after:form-rounded-r-none form-p-input form-rounded focus:form-ring">
        </div>
      </div>
      <div class="form-col w-full"></div>
    </div>
  </div>
</div>
```

_(The `TextElement` template changed in `1.2.0`, but it's easier to grasp the concept with this example.)_

We have a bunch of utility classes assigned to different DOM elements, but we have no idea which component or class name they belong to and makes it hard to customize them.

To make development easier we've introduced **class helpers** in `1.2.0` which prepends descriptive names to the class lists.

Let's enable [`classHelpers`](https://vueform.com/docs/configuration#class-helpers) in `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  classHelpers: true,
  // ...
})
```

And see how our source changes:

html

```
<div class="ElementLayout.container--> form-col ElementLayout.container_md--> w-full TextElement.container-->">
  <div class="ElementLayout.outerWrapper--> form-row flex flex-wrap ElementLayout.outerWrapper_single--> ElementLayout.outerWrapper_single_md--> form-mb-gutter">
    <label for="text" class="ElementLabel.container--> form-col pr-4 ElementLabel.container_md--> form-py-input-border w-3/12">
      <span>Text</span>
    </label>
    <div class="ElementLayout.innerContainer--> flex-1 w-9/12">
      <div class="ElementLayout.innerWrapperBefore--> form-col w-full"></div>
      <div class="ElementLayout.innerWrapper--> form-col w-full">
        <div class="TextElement.inputContainer--> w-full flex">
          <input type="text" name="text" id="text" class="TextElement.input--> w-full form-border form-border-color z-1 transition-shadow addon-before:form-rounded-l-none outline-none addon-after:form-rounded-r-none TextElement.input_md--> form-p-input form-rounded TextElement.input_enabled--> focus:form-ring">
        </div>
      </div>
      <div class="ElementLayout.innerWrapperAfter--> form-col w-full"></div>
    </div>
  </div>
</div>
```

Helper classes were prepended to our class lists which contain information about where the following classes are coming from.

The **first** part of a highlighted class name is the **name of the component**, the **second** is the **name of the class**.

With this knowledge we can identify which class comes from which component's class name and now we're ready to customize them.

### Add Classes [​](https://vueform.com/docs/styles-and-layout#add-classes)

To add classes to the element we can use `addClass` option.

Let's say we want bold letters in our input field, so add `font-bold` utility class to `input`:

vue

```
<TextElement name="text" label="Text" default="value" :add-class="{
  input: 'font-bold'
}" />
```

Result:

The `font-bold` class got appended to the class to `TextElement.input` section and now it is rendered among classes:

vue

```
<input type="text" name="text" id="text" class="TextElement.input--> w-full form-border
form-border-color z-1 transition-shadow addon-before:form-rounded-l-none outline-none
addon-after:form-rounded-r-none font-bold TextElement.input_md--> form-p-input
form-rounded TextElement.input_enabled--> focus:form-ring">
```

When adding classes we need to define them as `string` or `array`. If we want to use [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes), `object` (conditional) values must be wrapped in an `array`.

If we pass a `string` or an `array` directly to `addClass` instead of an `object` it will be appended to the element's outermost DOM.

### Remove Classes [​](https://vueform.com/docs/styles-and-layout#remove-classes)

If we want to remove a class from a class list we can use `removeClass` option.

Let's remove the border related props from the `TextElement`'s `input` class:

vue

```
<TextElement name="text" label="Text" default="value" :remove-class="{
  inputContainer: ['form-border-width-input', 'form-border-color-input']
}" />
```

Result:

> The `form-border-width-input` and `form-border-color-input` utility classes are defined by Vueform's Tailwind CSS plugin and they are responsible form setting border width and color based on [Tailwind](https://vueform.com/themes/tailwind#customization).

When removing classes we need to define the list of classes to be removed in an `array`.

If we pass an `array` directly to `removeClass` instead of an `object` it will be applied to the element's outermost DOM.

### Replace Classes [​](https://vueform.com/docs/styles-and-layout#replace-classes)

We can also replace certain classes in a class list instead of removing and adding ones with `replaceClass` property.

Let's change the original form input border with a thicker black one:

vue

```
<TextElement name="text" label="Text" default="value" :replace-class="{
  inputContainer: {
    'form-border-width-input': 'border-2',
    'form-border-color-input': ['border-black', 'border-opacity-80']
  }
}" />
```

Result:

When replacing classes we must use an object, where the keys are the original class names and the values are the replacements. The keys can only be single classes, while values can contain multiple ones in `string` or an `array`. If we want to use [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes), `object` (conditional) values must be wrapped in an `array`.

If we pass an `object` in an `array` directly to `removeClass` instead of an `object` it will be applied to the element's outermost DOM.

### Override Classes [​](https://vueform.com/docs/styles-and-layout#override-classes)

If we want to replace an element's class completely we can use `overrideClass` options.

Let's get rid of the built-in form input looks and replace it with a simple underlined input field:

vue

```
<TextElement name="text" label="Text" default="value" :override-class="{
  inputContainer: 'border-b-2 bg-transparent w-full transition-all',
  inputContainer_default: 'border-black',
  inputContainer_focused: 'border-red-500',
  inputContainer_md: 'h-10',
}" />
```

Result:

We changed multiple classes in order to get rid of border radius and focus ring as well.

When overriding classes we can use `string` or `array` values. If we want to use [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes), `object` (conditional) values must be wrapped in an `array`.

If we pass an `string` or an `array` directly to `overrideClass` instead of an `object` it will override the element's outermost DOM's class.

### Modify Multiple Components [​](https://vueform.com/docs/styles-and-layout#modify-multiple-components)

We can modify multiple components used by the element at the same time. For example we can add `font-bold` to `TextElement`'s `input` and `ElementLabel`'s `container` field as well:

vue

```
<TextElement name="text" label="Text" default="value" :add-classes="{
  TextElement: {
    input: 'font-bold'
  },
  ElementLabel: {
    container: 'font-bold'
  }
}" />
```

Result:

We can modify multiple classes the same way with `removeClasses`, `replaceClasses` and `overrideClasses` as well.

### Modify FileElement in MultifileElement [​](https://vueform.com/docs/styles-and-layout#modify-fileelement-in-multifileelement)

One thing to note is that these class modifiers will only be applied to **element and its child components**, **but not to its child elements**. So if we want to change classes for eg. `FileElement` in `MultifileElement` (which is like a `ListElement` with multiple `FileElement`s), we have to pass the class modifiers directly to `FileElement` via `file` prop:

vue

```
<MultifileElement name="multifile" label="Multifile" :file="{
  overrideClasses: {
    FilePreview: {
      upload: 'hidden'
    },
  }
}" />
```

### Conditional Classes [​](https://vueform.com/docs/styles-and-layout#conditional-classes)

Conditional classes can be used in all modification types by passing a `function` as the options value which should return an `object`. The first param of the function is the [`form$`](https://vueform.com/reference/vueform) instance:

vue

```
<TextElement :add-classes="(form$, el$, comp$) => ({
  TextElement: {
    container: {
      'text-red-500': form$.el$('age')?.value < 18
    }
  }
})" ... />
```

> The `el$` (second param) can only be used for components that has `el$` (component instance) property available, eg. `TextElement` or `ElementLabel` but not eg. `Vueform` or `FormElements`. If you are referencing custom components make sure they have `el$` available by injecting `el$` in any component used by an element type component.

The `comp$` (third param) is a reference to the component itself. It always takes up the value of the current component when going through child components. Eg. if used for `ElementLayout` the `comp$` will be the instance of `ElementLayout` and `CheckboxgroupCheckbox` when used for that one. Therefore it's important to use optional chaining (`comp$?.something`) in each case.

This can be used for element, form and config level class modifiers.

Replacing Templates [​](https://vueform.com/docs/styles-and-layout#replacing-templates)
---------------------------------------------------------------------------------------

Sometimes, it's not enough to change the classes of the component's existing DOM structure but we need to alter the DOM structure itself. This is when we can replace the template of an existing component.

In this example we are going to replace the template of the [`ElementError`](https://vueform.com/reference/element-error) component and we will add a bold `ERROR:` prefix to all error messages and make all errors align to right.

Here's how `ElementError` looks like by default:

And here's what we will achieve:

### DOM Structure [​](https://vueform.com/docs/styles-and-layout#dom-structure)

In order to replace an existing component's template it's advisable to use its exising counterpart's template as a starting point.

We can do this by checking out [`/themes/blank/templates`](https://github.com/vueform/vueform/tree/main/themes/blank/templates) directory in the [`@vueform/vueform`](https://github.com/vueform/vueform) repo, which is the **basis for every theme's DOM structure**.

Here's how `ElementError`'s template looks like ([source](https://github.com/vueform/vueform/blob/main/themes/blank/templates/ElementError.vue)):

vue

```
<!-- From: @vueform/vueform/themes/blank/templates/ElementError.vue -->

<template>
  <div
    v-if="error"
    :class="classes.container"
    :id="id"
    aria-live="assertive"
    v-html="error"
  ></div>
</template>

<script>
  export default {
    name: 'ElementError',
    data() {
      return {
        merge: true,
        defaultClasses: {
          container: '',
        }
      }
    }
  }
</script>

<style lang="scss">
</style>
```

We know that we want to prefix all element messages with a bold `ERROR:` string so we want to achieve something like this on the DOM level:

vue

```
<template>
  <div
    v-if="error"
    :class="classes.container"
    :id="id"
    aria-live="assertive"
  >
    <b>ERROR: </b><span v-html="error" />
  </div>
</template>
```

So in order to achieve let's create a copy of the existing template as `CustomElementError.vue` and apply the changes:

vue

```
<!-- CustomElementError.vue -->

<template>
  <div
    v-if="error"
    :class="classes.container"
    :id="id"
    aria-live="assertive"
  >
    <b>ERROR: </b><span v-html="error" />
  </div>
</template>

<script>
  export default {
    name: 'ElementError',
    data() {
      return {
        merge: true,
        defaultClasses: {
          container: '',
        }
      }
    }
  }
</script>

<style lang="scss">
</style>
```

Now we have our custom DOM structure, but we haven't dealt with styles yet.

### Applying Styles [​](https://vueform.com/docs/styles-and-layout#applying-styles)

We can see that our component only uses a single class called `container`:

vue

```
<!-- CustomElementError.vue -->

<template>
  <div
    v-if="error"
    :class="classes.container"
    :id="id"
    aria-live="assertive"
  >
    <b>ERROR: </b><span v-html="error" />
  </div>
</template>
```

> The `classes` object is a computed variable that merges the component's default classes with everything that might manipulate them externally, like the theme's class definition file, global overrides, on the flight overrides, etc. That's all we need to know for now.

#### Utility Based Themes (eg. tailwind) [​](https://vueform.com/docs/styles-and-layout#utility-based-themes-eg-tailwind)

If we are using a utility based theme like `tailwind` classes will be automatically filled in from the theme's [class definition file](https://github.com/vueform/vueform/blob/main/themes/tailwind/classes.js#L1275) as we are using `merge: true` in data export.

So this is what basically gets applied to `ElementError` component:

js

```
// @vueform/vueform/themes/tailwind/classes.js

export default {
  // ...
  ElementError: {
    container: 'form-color-danger block',
    container_sm: 'form-text-small-sm mt-0.5',
    container_md: 'form-text-small mt-1',
    container_lg: 'form-text-small-lg mt-1',
    $container: (classes, { Size }) => ([
      classes.container,
      classes[`container_${Size}`],
    ]),
  },
  // ...
}
```

If we want to customize it in our custom component that we just created, we can copy them to our component and customize them while setting `merge: false`:

vue

```
<!-- CustomElementError.vue -->

<template>
  <div
    v-if="error"
    :class="classes.container"
    :id="id"
    aria-live="assertive"
  >
    <b>ERROR: </b><span v-html="error" />
  </div>
</template>

<script>
  export default {
    name: 'ElementError',
    data() {
      return {
        merge: false, 
        defaultClasses: {
          container: 'form-color-danger block text-right', // <-- we added `text-right`
          container_sm: 'form-text-small-sm mt-0.5',
          container_md: 'form-text-small mt-1',
          container_lg: 'form-text-small-lg mt-1',
          $container: (classes, { Size }) => ([
            classes.container,
            classes[`container_${Size}`],
          ]),
        }
      }
    }
  }
</script>

<style lang="scss">
</style>
```

> The `merge: true` option means that the component's classes should be merge with the ones defined in the theme's _class definition file_ (if any) where the ones in the class definition get merged to the ones defined in the component's `defaultClasses` data prop.
> 
> 
> If it's set to `merge: false` the classes defined in the component will be used.

#### Class Name Based Themes (eg. vueform) [​](https://vueform.com/docs/styles-and-layout#class-name-based-themes-eg-vueform)

If we are using a class name based theme like `vueform` we need to copy the original class names to our component from [ElementError's `defaultClasses`](https://github.com/vueform/vueform/blob/main/themes/vueform/templates/ElementError.vue#L10) and set `merge: false`:

vue

```
<!-- CustomElementError.vue -->

<template>
  <div
    v-if="error"
    :class="classes.container"
    :id="id"
    aria-live="assertive"
  >
    <b>ERROR: </b><span v-html="error" />
  </div>
</template>

<script>
  export default {
    name: 'ElementError',
    data() {
      return {
        merge: false,
        defaultClasses: {
          container: 'vf-element-error',
          container_sm: 'vf-element-error-sm',
          container_md: '',
          container_lg: 'vf-element-error-lg',
          $container: (classes, { Size }) => ([
            classes.container,
            classes[`container_${Size}`],
          ]),
        }
      }
    }
  }
</script>

<style lang="scss">
</style>
```

> We are setting `merge: false` just to keep consistency, because `merge: true` would mean that the classes defined in the component's `defaultClasses` should be merge with the theme's class definition object, but class name based themes like `vueform` does not have any.

Great, now we have the default styles applied to our `ElementError` component, so let's add a new class that positions the error message to the right.

vue

```
<!-- CustomElementError.vue -->

<template>
  <div
    v-if="error"
    :class="classes.container"
    :id="id"
    aria-live="assertive"
  >
    <b>ERROR: </b><span v-html="error" />
  </div>
</template>

<script>
  export default {
    name: 'ElementError',
    data() {
      return {
        merge: false,
        defaultClasses: {
          container: 'vf-element-error vf-element-error-right',
          container_sm: 'vf-element-error-sm',
          container_md: '',
          container_lg: 'vf-element-error-lg',
          $container: (classes, { Size }) => ([
            classes.container,
            classes[`container_${Size}`],
          ]),
        }
      }
    }
  }
</script>

<style lang="scss">
.vf-element-error-right {
  text-align: right;
}
</style>
```

### Sidenote: Using Computed Classes ($classname) [​](https://vueform.com/docs/styles-and-layout#sidenote-using-computed-classes-classname)

You probably noticed that even though `ElementError` only has a single `container` class it has couple of alterations of that and you might be wondering what they are.

Vueform resolve classes dynamically and when it notices that a class name is also defined with a `$` prefix (like `$container`) it treats it as a sort of computed value. What it means is that instead of returning the plain value of `container` it returns the computed value returned by `$container`.

The a computed class method's first argument is the list of classes the component has, which in our case are:

*   `container`
*   `container_sm`
*   `container_md`
*   `container_lg`

The second is the component instance itself, which allows accessing any of properties and methods.

Let's see what `$container` does in our example:

js

```
$container: (classes, { Size }) => ([
  classes.container, // returns 'vf-element-error vf-element-error-right'
  classes[`container_${Size}`], // returns 'vf-element-error-sm' or '' or 'vf-element-error-lg'
]),
```

*   It takes `classes` as the first argument, and deconstructs `Size` from the second
*   It returns the original `container` class
*   And it returns the version of container that is suffixed with the [size](https://vueform.com/docs/styles-and-layout#size), depending on the `Size` of element.

Here's how `container` class is resolved with different sizes:

vue

```
<TextElement size="sm" />
<!-- vf-element-error vf-element-error-right vf-element-error-sm -->

<TextElement size="md" />
<!-- vf-element-error vf-element-error-right -->

<TextElement size="lg" />
<!-- vf-element-error vf-element-error-right vf-element-error-lg -->
```

> To see what properties a component has, check it out in the [Components](https://vueform.com/reference/element-error) reference.

### Registering the Template Globally [​](https://vueform.com/docs/styles-and-layout#registering-the-template-globally)

The last step is to register out component globally, overriding the original `ElementError`'s template:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import CustomElementError from './path/to/CustomElementError.vue'

export default defineConfig({
  templates: {
    ElementError: CustomElementError,
  },
})
```

Now when `ElementError` gets rendered in any component it will use our custom template and styles:

### Single Use [​](https://vueform.com/docs/styles-and-layout#single-use)

If we don't want to globally override the `ElementError` component and just use it for a single form or element, we can do it via `templates` property of `<Vueform>` component or any element like `<TextElement>` component:

Composition API Options API

vue

```
<template>
  <div id="app">
    <!-- Will be applied to all elements -->
    <Vueform :templates="{ ElementError }">
      <TextElement name="text" />
      <TextElement name="text2" />
    </Vueform>

    <Vueform>
      <!-- Will be applied to a single elements -->
      <TextElement name="text" :templates="{ ElementError }" />
    </Vueform>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ElementError from './path/to/CustomElementError.vue'
</script>
```

vue

```
<template>
  <div id="app">
    <!-- Will be applied to all elements -->
    <Vueform :templates="{ ElementError }">
      <TextElement name="text" />
      <TextElement name="text2" />
    </Vueform>

    <Vueform>
      <!-- Will be applied to a single elements -->
      <TextElement name="text" :templates="{ ElementError }" />
    </Vueform>
  </div>
</template>

<script>
import { ref, markRaw } from 'vue'
import ElementError from './path/to/CustomElementError.vue'

export default {
  data: () => ({
    // Make sure to use `markRaw` when passing over components
    // as data to remove unnecessary reactivity.
    ElementError: markRaw(ElementError)
  })
}
</script>
```

Alternative Views [​](https://vueform.com/docs/styles-and-layout#alternative-views)
-----------------------------------------------------------------------------------

In the previous section, [Replacing Templates](https://vueform.com/docs/styles-and-layout#replace-templates), we learned how we can create a custom version of a Vueform component's template. Here, we will learn how we can use it as an **alternative view**, instead of overriding the component's original template.

Sticking to our example from the previous section (make sure to read it first), instead of registering the template as a replacement of `ElementError` let's add an `_errorRight` suffix to it:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import CustomElementError from './path/to/CustomElementError.vue'

export default defineConfig({
  // ...
  templates: {
    ElementError_errorRight: CustomElementError,
  }
})
```

Then, we can use this template as an alternative view anytime by applying `view="errorRight"` on **any parent component** that uses `ElementError`:

html

```
<!-- All elements in the form will use the "ElementError_errorRight" template -->
<Vueform view="errorRight">
  <TextElement ... />
  <TextElement ... />
</Vueform>

<Vueform>
  <!-- Only this element will use the "ElementError_errorRight" template -->
  <TextElement view="errorRight" ... />

  <!-- This will use the original `ElementError` -->
  <TextElement ... />
</Vueform>
```

We can create alternative views for any component the same way. Just remember when `view` is defined for an element (or even [`<Vueform>`](https://vueform.com/reference/vueform#option-view)) it will be [**passed down to children**](https://vueform.com/docs/styles-and-layout#views-for-children) so all of them will try to use the same alternative template for all of their components if available.

Presets [​](https://vueform.com/docs/styles-and-layout#presets)
---------------------------------------------------------------

If we want to apply a set of rules (eg. `addClasses`, `templates`, `size`, etc.) to certain elements or forms we can use **presets**.

Presets can be created at `vueform.config.js` under `presets` property:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  presets: {
    presetName: {
      // preset options
    }
  }
})
```

We can add the same options to a preset that we'd normally add to an element, including:

*   `size` - defines the default size
*   `views` - an object containing key value pairs for component names and their default views
*   `columns` - a columns object
*   `addClasses` - classes to add
*   `removeClasses` - classes to remove
*   `replaceClasses` - classes to replace
*   `overrideClasses` - classes to override
*   `templates` - templates to replace.

For example this would add an extra margin to each `ElementLabel` component where the preset is applied:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  presets: {
    italicLabel: {
      addClasses: {
        ElementLabel: {
          container: 'italic'
        }
      }
    }
  }
})
```

Later we can use the presets for an element using `presets` option:

template

```
<template>
  <Vueform>
    <TextElement label="Normal" ... />
    <TextElement label="Italic" :presets="['italicLabel']" ... />
  <Vueform>
</template>
```

... or even for forms:

template

```
<template>
  <Vueform :presets="['italicLabel']">
    <TextElement label="Italic" ... />
    <TextElement label="Italic"  ... />
  <Vueform>
</template>
```

The presets will be applied in consecutive order **before** the element/form options. This means that if a preset eg. adds a class a class it will be added before classes added with element/form's `addClasses` option.

Form Customization [​](https://vueform.com/docs/styles-and-layout#form-customization)
-------------------------------------------------------------------------------------

Just like for presets, the following options can be also applied on a form level:

*   `size`
*   `views`
*   `columns`
*   `addClass`
*   `addClasses`
*   `removeClass`
*   `removeClasses`
*   `replaceClass`
*   `replaceClasses`
*   `overrideClass`
*   `overrideClasses`
*   `presets`

Options defined on form level will take effect **before** element presets and options. Eg:

vue

```
<template>
  <Vueform size="sm">
    <TextElement ... />
    <TextElement size="md" ... />
  </Vueform>
</template>
```

Will result in:

Classes modified on a higher level can also be modified on a lower level:

template

```
<template>
  <Vueform :add-classes="{
    TextElement: {
      input: 'font-bold'
    }
  }">
    <TextElement ... />
    <TextElement :replace-class="{
      input: {
        'font-bold': 'italic'
      }
    }" ... />
  </Vueform>
</template>
```

Will result in:

Global Customization [​](https://vueform.com/docs/styles-and-layout#global-customization)
-----------------------------------------------------------------------------------------

We can also define the the options mentioned in this chapter globally in [`vueform.config.js`](https://vueform.com/docs/configuration). In config we can use `usePresets` option to apply presets globally, which will take place before any other setting, global or local.

CSS Vars [​](https://vueform.com/docs/styles-and-layout#css-vars)
-----------------------------------------------------------------

Vueform themes use CSS vars under the hood that makes theme customizations a breeze. The different themes (eg. default, Bootstrap, Material) are in fact identicaly structurally and are using the exact same class names, their only difference is how their CSS vars are configured.

To see the available theme check out [Themes](https://vueform.com/themes/tailwind) page.

### Global Customization [​](https://vueform.com/docs/styles-and-layout#global-customization-1)

If we'd like to override some of the CSS vars globally we can define the following in global scope:

css

```
:root, :before, :after, * {
  --vf-border-color-input: #14b8a6;
  --vf-bg-input: #ccfbf1;
}
```

Then all of our forms will be displayed using the global CSS vars setting:

vue

```
<template>
  <Vueform>
    <TextElement ... /> <!-- Will be teal -->
    <TextElement ... /> <!-- Will be teal -->
  </Vueform>
</template>
```

### Local Customization [​](https://vueform.com/docs/styles-and-layout#local-customization)

We can also override CSS vars only for certain form instance or even element. To do this we need to add a class name to the form or element and apply the CSS vars for those scopes only:

css

```
.form-teal, .element-teal {
  --vf-border-color-input: #14b8a6;
  --vf-bg-input: #ccfbf1;
}
```

Now if we apply those classes to forms or elements only those will be altered:

vue

```
<template>
  <!-- Teal form -->
  <Vueform add-class="form-teal">
    <TextElement ... /> <!-- Will be teal -->
    <TextElement ... /> <!-- Will be teal -->
  </Vueform>

  <!-- Teal element -->
  <Vueform>
    <TextElement ... /> <!-- Will be default -->
    <TextElement add-class="element-teal" ... /> <!-- Will be teal -->
  </Vueform>
</template>
```

### Available CSS Vars [​](https://vueform.com/docs/styles-and-layout#available-css-vars)

The following CSS vars are the default values for `vueform` theme and they can be overriden globally or locally.

#### General Colors [​](https://vueform.com/docs/styles-and-layout#general-colors)

Colors used globally in Vueform components.

scss

```
// Colors

:root, :before, :after, * {
  --vf-primary: #07bf9b;
  --vf-primary-darker: #06ac8b;
  --vf-danger: #ef4444;
  --vf-danger-lighter: #fee2e2;
  --vf-success: #10b981;
  --vf-success-lighter: #d1fae5;

  --vf-gray-50: #f9fafb;
  --vf-gray-100: #f3f4f6;
  --vf-gray-200: #e5e7eb;
  --vf-gray-300: #d1d5db;
  --vf-gray-400: #9ca3af;
  --vf-gray-500: #6b7280;
  --vf-gray-600: #4b5563;
  --vf-gray-700: #374151;
  --vf-gray-800: #1f2937;
  --vf-gray-900: #111827;

  --vf-dark-50: #f9fafb;
  --vf-dark-100: #f3f4f6;
  --vf-dark-200: #e5e7eb;
  --vf-dark-300: #d1d5db;
  --vf-dark-400: #9ca3af;
  --vf-dark-500: #6b7280;
  --vf-dark-600: #4b5563;
  --vf-dark-700: #374151;
  --vf-dark-800: #1f2937;
  --vf-dark-900: #111827;
}
```

#### Ring Settings [​](https://vueform.com/docs/styles-and-layout#ring-settings)

Rings appear as an outline when input elements are focused.

scss

```
// Ring Settings

:root, :before, :after, * {
  --vf-ring-width: 2px;
  --vf-ring-color: #07bf9b66;
}
```

#### Link Settings [​](https://vueform.com/docs/styles-and-layout#link-settings)

Links can be displayed with `tag: 'a'` option with [StaticElements](https://vueform.com/docs/static-element).

scss

```
// Link Settings

:root, :before, :after, * {
  --vf-link-color: var(--vf-primary);
  --vf-link-decoration: inherit;
}
```

#### Text Sizing [​](https://vueform.com/docs/styles-and-layout#text-sizing)

Texts sizes to use through components.

scss

```
// Text Sizing

:root, :before, :after, * {
  --vf-font-size: 1rem;
  --vf-font-size-sm: 0.875rem;
  --vf-font-size-lg: 1rem;

  --vf-font-size-small: 0.875rem;
  --vf-font-size-small-sm: 0.8125rem;
  --vf-font-size-small-lg: 0.875rem;

  --vf-font-size-h1: 2.125rem;
  --vf-font-size-h1-sm: 2.125rem;
  --vf-font-size-h1-lg: 2.125rem;

  --vf-font-size-h2: 1.875rem;
  --vf-font-size-h2-sm: 1.875rem;
  --vf-font-size-h2-lg: 1.875rem;

  --vf-font-size-h3: 1.5rem;
  --vf-font-size-h3-sm: 1.5rem;
  --vf-font-size-h3-lg: 1.5rem;

  --vf-font-size-h4: 1.25rem;
  --vf-font-size-h4-sm: 1.25rem;
  --vf-font-size-h4-lg: 1.25rem;

  --vf-font-size-h1-mobile: 1.5rem;
  --vf-font-size-h1-mobile-sm: 1.5rem;
  --vf-font-size-h1-mobile-lg: 1.5rem;

  --vf-font-size-h2-mobile: 1.25rem;
  --vf-font-size-h2-mobile-sm: 1.25rem;
  --vf-font-size-h2-mobile-lg: 1.25rem;

  --vf-font-size-h3-mobile: 1.125rem;
  --vf-font-size-h3-mobile-sm: 1.125rem;
  --vf-font-size-h3-mobile-lg: 1.125rem;

  --vf-font-size-h4-mobile: 1rem;
  --vf-font-size-h4-mobile-sm: 1rem;
  --vf-font-size-h4-mobile-lg: 1rem;

  --vf-font-size-blockquote: 1rem;
  --vf-font-size-blockquote-sm: 0.875rem;
  --vf-font-size-blockquote-lg: 1rem;

  --vf-line-height: 1.5rem;
  --vf-line-height-sm: 1.25rem;
  --vf-line-height-lg: 1.5rem;

  --vf-line-height-small: 1.25rem;
  --vf-line-height-small-sm: 1.125rem;
  --vf-line-height-small-lg: 1.25rem;

  --vf-line-height-headings: 1.2;
  --vf-line-height-headings-sm: 1.2;
  --vf-line-height-headings-lg: 1.2;

  --vf-line-height-blockquote: 1.5rem;
  --vf-line-height-blockquote-sm: 1.25rem;
  --vf-line-height-blockquote-lg: 1.5rem;

  --vf-letter-spacing: 0;
  --vf-letter-spacing-sm: 0;
  --vf-letter-spacing-lg: 0;

  --vf-letter-spacing-small: 0;
  --vf-letter-spacing-small-sm: 0;
  --vf-letter-spacing-small-lg: 0;

  --vf-letter-spacing-headings: 0;
  --vf-letter-spacing-headings-sm: 0;
  --vf-letter-spacing-headings-lg: 0;

  --vf-letter-spacing-blockquote: 0;
  --vf-letter-spacing-blockquote-sm: 0;
  --vf-letter-spacing-blockquote-lg: 0;
}
```

#### Gutter [​](https://vueform.com/docs/styles-and-layout#gutter)

The space between elements vertically and horizontally.

scss

```
// Gutter

:root, :before, :after, * {
  --vf-gutter: 1rem;
  --vf-gutter-sm: 0.5rem;
  --vf-gutter-lg: 1rem;
}
```

#### Input Spacing [​](https://vueform.com/docs/styles-and-layout#input-spacing)

Spacing within input fields.

scss

```
// Input Spacing

:root, :before, :after, * {
  --vf-min-height-input: 2.375rem;
  --vf-min-height-input-sm: 2.125rem;
  --vf-min-height-input-lg: 2.875rem;

  --vf-py-input: 0.375rem;
  --vf-py-input-sm: 0.375rem;
  --vf-py-input-lg: 0.625rem;

  --vf-px-input: 0.75rem;
  --vf-px-input-sm: 0.5rem;
  --vf-px-input-lg: 0.875rem;

  --vf-py-btn: 0.375rem;
  --vf-py-btn-sm: 0.375rem;
  --vf-py-btn-lg: 0.625rem;

  --vf-px-btn: 0.875rem;
  --vf-px-btn-sm: 0.75rem;
  --vf-px-btn-lg: 1.25rem;

  --vf-py-btn-small: 0.25rem;
  --vf-py-btn-small-sm: 0.25rem;
  --vf-py-btn-small-lg: 0.375rem;

  --vf-px-btn-small: 0.625rem;
  --vf-px-btn-small-sm: 0.625rem;
  --vf-px-btn-small-lg: 0.75rem;

  --vf-py-group-tabs: var(--vf-py-input);
  --vf-py-group-tabs-sm: var(--vf-py-input-sm);
  --vf-py-group-tabs-lg: var(--vf-py-input-lg);

  --vf-px-group-tabs: var(--vf-px-input);
  --vf-px-group-tabs-sm: var(--vf-px-input-sm);
  --vf-px-group-tabs-lg: var(--vf-px-input-lg);

  --vf-py-group-blocks: 0.75rem;
  --vf-py-group-blocks-sm: 0.625rem;
  --vf-py-group-blocks-lg: 0.875rem;

  --vf-px-group-blocks: 1rem;
  --vf-px-group-blocks-sm: 1rem;
  --vf-px-group-blocks-lg: 1rem;

  --vf-py-tag: 0;
  --vf-py-tag-sm: var(--vf-py-tag);
  --vf-py-tag-lg: var(--vf-py-tag);

  --vf-px-tag: 0.4375rem;
  --vf-px-tag-sm: var(--vf-px-tag);
  --vf-px-tag-lg: var(--vf-px-tag);

  --vf-py-slider-tooltip: 0.125rem;
  --vf-py-slider-tooltip-sm: 0.0625rem;
  --vf-py-slider-tooltip-lg: 0.1875rem;

  --vf-px-slider-tooltip: 0.375rem;
  --vf-px-slider-tooltip-sm: 0.3125rem;
  --vf-px-slider-tooltip-lg: 0.5rem;

  --vf-py-blockquote: 0.25rem;
  --vf-py-blockquote-sm: 0.25rem;
  --vf-py-blockquote-lg: 0.25rem;

  --vf-px-blockquote: 0.75rem;
  --vf-px-blockquote-sm: 0.75rem;
  --vf-px-blockquote-lg: 0.75rem;

  --vf-py-hr: 0.25rem;

  // Space between addon and text input
  --vf-space-addon: 0;
  --vf-space-addon-sm: var(--vf-space-addon);
  --vf-space-addon-lg: var(--vf-space-addon);

  // Space between checkboxes & radios and their labels
  --vf-space-checkbox: 0.375rem;
  --vf-space-checkbox-sm: var(--vf-space-checkbox);
  --vf-space-checkbox-lg: var(--vf-space-checkbox);

  // Space between tags in `TagsElement`
  --vf-space-tags: 0.1875rem;
  --vf-space-tags-sm: var(--vf-space-tags);
  --vf-space-tags-lg: var(--vf-space-tags);

  // Space between the field's top and floating label
  --vf-floating-top: 0rem;
  --vf-floating-top-sm: 0rem;
  --vf-floating-top-lg: 0.6875rem;

  // Space above `StaticElement` tags
  --vf-space-static-tag-1: 1rem;
  --vf-space-static-tag-2: 2rem;
  --vf-space-static-tag-3: 3rem;
}
```

#### Input Colors [​](https://vueform.com/docs/styles-and-layout#input-colors)

Background, text, shadow and border color of inputs.

scss

```
// Input Colors

:root, :before, :after, * {
  --vf-bg-input: #ffffff;
  --vf-bg-input-hover: var(--vf-bg-input);
  --vf-bg-input-focus: var(--vf-bg-input);
  --vf-bg-input-danger: var(--vf-bg-input);
  --vf-bg-input-success: var(--vf-bg-input);
  --vf-bg-checkbox: var(--vf-bg-input);
  --vf-bg-checkbox-hover: var(--vf-bg-checkbox);
  --vf-bg-checkbox-focus: var(--vf-bg-checkbox);
  --vf-bg-checkbox-danger: var(--vf-bg-checkbox);
  --vf-bg-checkbox-success: var(--vf-bg-checkbox);
  --vf-bg-disabled: var(--vf-gray-200);
  --vf-bg-selected: rgba(17,24,39,0.05); // Used eg. when select option is hovered or a checkbox is selected in `blocks` view
  --vf-bg-passive: var(--vf-gray-300); // Used as a background color for eg. slider, toggle
  --vf-bg-icon: var(--vf-gray-500);
  --vf-bg-danger: var(--vf-danger-lighter);
  --vf-bg-success: var(--vf-success-lighter);
  --vf-bg-tag: var(--vf-primary);
  --vf-bg-slider-handle: var(--vf-primary);
  --vf-bg-toggle-handle: #ffffff;
  --vf-bg-date-head: var(--vf-gray-100);
  --vf-bg-addon: transparent;
  --vf-bg-btn: var(--vf-primary);
  --vf-bg-btn-danger: var(--vf-danger);
  --vf-bg-btn-secondary: var(--vf-gray-200);

  --vf-color-input: var(--vf-gray-800);
  --vf-color-input-hover: var(--vf-color-input);
  --vf-color-input-focus: var(--vf-color-input);
  --vf-color-input-danger: var(--vf-color-input);
  --vf-color-input-success: var(--vf-color-input);
  --vf-color-disabled: var(--vf-gray-400);
  --vf-color-placeholder: var(--vf-gray-300);
  --vf-color-passive: var(--vf-gray-700); // Used when text is displayed on passive background eg. `off` toggle
  --vf-color-muted: var(--vf-gray-500); // Used for helper texts eg. element description, floating label
  --vf-color-floating: var(--vf-color-muted);
  --vf-color-floating-focus: var(--vf-color-floating); // Used when the input is focused
  --vf-color-floating-success: var(--vf-color-floating); // Used when the input is filled with success
  --vf-color-floating-danger: var(--vf-color-floating); // Used when the input has error
  --vf-color-on-primary: #ffffff; // Used when text is displayed on primary color
  --vf-color-danger: var(--vf-danger);
  --vf-color-success: var(--vf-success);
  --vf-color-tag: var(--vf-color-on-primary);
  --vf-color-addon: var(--vf-color-input);
  --vf-color-date-head: var(--vf-gray-700);
  --vf-color-btn: var(--vf-color-on-primary);
  --vf-color-btn-danger: #ffffff;
  --vf-color-btn-secondary: var(--vf-gray-700);

  --vf-border-color-input: var(--vf-gray-300);
  --vf-border-color-input-hover: var(--vf-border-color-input);
  --vf-border-color-input-focus: var(--vf-primary);
  --vf-border-color-input-danger: var(--vf-border-color-input);
  --vf-border-color-input-success: var(--vf-border-color-input);
  --vf-border-color-checkbox: var(--vf-border-color-input);
  --vf-border-color-checkbox-focus: var(--vf-primary);
  --vf-border-color-checkbox-hover: var(--vf-border-color-checkbox);
  --vf-border-color-checkbox-danger: var(--vf-border-color-checkbox);
  --vf-border-color-checkbox-success: var(--vf-border-color-checkbox);
  --vf-border-color-checked: var(--vf-primary);
  --vf-border-color-passive: var(--vf-gray-300); // Used as a border for passive states eg. `off` toggle
  --vf-border-color-slider-tooltip: var(--vf-primary);
  --vf-border-color-tag: var(--vf-primary);
  --vf-border-color-btn: var(--vf-primary);
  --vf-border-color-btn-danger: var(--vf-danger);
  --vf-border-color-btn-secondary: var(--vf-gray-200);
  --vf-border-color-blockquote: var(--vf-gray-300);
  --vf-border-color-hr: var(--vf-gray-300);
}
```

#### Shadows [​](https://vueform.com/docs/styles-and-layout#shadows)

Shadows for different component parts.

scss

```
// Shadows

:root, :before, :after, * {
  --vf-shadow-input: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-input-hover: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-input-focus: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-handles: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-handles-hover: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-handles-focus: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-btn: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-dropdown: 0px 0px 0px 0px rgba(0,0,0,0);
}
```

#### Input Borders [​](https://vueform.com/docs/styles-and-layout#input-borders)

The widths and radiuses of inputs.

scss

```
// Input borders

:root, :before, :after, * {
  --vf-border-width-input-t: 1px;
  --vf-border-width-input-r: 1px;
  --vf-border-width-input-b: 1px;
  --vf-border-width-input-l: 1px;

  --vf-border-width-radio-t: var(--vf-border-width-input-t);
  --vf-border-width-radio-r: var(--vf-border-width-input-r);
  --vf-border-width-radio-b: var(--vf-border-width-input-b);
  --vf-border-width-radio-l: var(--vf-border-width-input-l);

  --vf-border-width-checkbox-t: var(--vf-border-width-input-t);
  --vf-border-width-checkbox-r: var(--vf-border-width-input-r);
  --vf-border-width-checkbox-b: var(--vf-border-width-input-b);
  --vf-border-width-checkbox-l: var(--vf-border-width-input-l);

  --vf-border-width-dropdown: 1px;
  --vf-border-width-btn: 1px;
  --vf-border-width-toggle: 0.125rem;
  --vf-border-width-tag: 1px;
  --vf-border-width-blockquote: 3px;

  --vf-radius-input: 0.25rem;
  --vf-radius-input-sm: var(--vf-radius-input);
  --vf-radius-input-lg: var(--vf-radius-input);

  --vf-radius-btn: var(--vf-radius-input);
  --vf-radius-btn-sm: var(--vf-radius-input-sm);
  --vf-radius-btn-lg: var(--vf-radius-input);

  // Used for eg. list button, slider tooltip, info tooltip
  --vf-radius-small: var(--vf-radius-input);
  --vf-radius-small-sm: var(--vf-radius-input-sm);
  --vf-radius-small-lg: var(--vf-radius-input);

  // Used for larger inputs eg. textarea, editor, drag and drop, checkbox/radio blocks
  --vf-radius-large: var(--vf-radius-input);
  --vf-radius-large-sm: var(--vf-radius-input-sm);
  --vf-radius-large-lg: var(--vf-radius-input);

  --vf-radius-tag: var(--vf-radius-input);
  --vf-radius-tag-sm: var(--vf-radius-input-sm);
  --vf-radius-tag-lg: var(--vf-radius-input);

  --vf-radius-checkbox: var(--vf-radius-input);
  --vf-radius-checkbox-sm: var(--vf-radius-input-sm);
  --vf-radius-checkbox-lg: var(--vf-radius-input);

  --vf-radius-slider: var(--vf-radius-input);
  --vf-radius-slider-sm: var(--vf-radius-input-sm);
  --vf-radius-slider-lg: var(--vf-radius-input);

  --vf-radius-image: var(--vf-radius-input);
  --vf-radius-image-sm: var(--vf-radius-input-sm);
  --vf-radius-image-lg: var(--vf-radius-input);

  --vf-radius-gallery: var(--vf-radius-input);
  --vf-radius-gallery-sm: var(--vf-radius-input-sm);
  --vf-radius-gallery-lg: var(--vf-radius-input);
}
```

#### Input Sizes [​](https://vueform.com/docs/styles-and-layout#input-sizes)

Sizes of different input fields and their components.

scss

```
// Input Sizes

:root, :before, :after, * {
  --vf-checkbox-size: 1rem;
  --vf-checkbox-size-sm: 0.875rem;
  --vf-checkbox-size-lg: 1rem;

  --vf-gallery-size: 6rem;
  --vf-gallery-size-sm: 5rem;
  --vf-gallery-size-lg: 7rem;

  --vf-toggle-width: 3rem;
  --vf-toggle-width-sm: 2.75rem;
  --vf-toggle-width-lg: 3rem;

  --vf-toggle-height: 1.25rem;
  --vf-toggle-height-sm: 1.125rem;
  --vf-toggle-height-lg: 1.25rem;

  --vf-slider-height: 0.375rem;
  --vf-slider-height-sm: 0.3125rem;
  --vf-slider-height-lg: 0.5rem;

  --vf-slider-height-vertical: 20rem;
  --vf-slider-height-vertical-sm: var(--vf-slider-height-vertical);
  --vf-slider-height-vertical-lg: var(--vf-slider-height-vertical);

  --vf-slider-handle-size: 1rem;
  --vf-slider-handle-size-sm: 0.875rem;
  --vf-slider-handle-size-lg: 1.25rem;

  --vf-slider-tooltip-distance: 0.5rem;
  --vf-slider-tooltip-distance-sm: 0.375rem;
  --vf-slider-tooltip-distance-lg: 0.5rem;

  --vf-slider-tooltip-arrow-size: 0.3125rem;
  --vf-slider-tooltip-arrow-size-sm: var(--vf-slider-tooltip-arrow-size);
  --vf-slider-tooltip-arrow-size-lg: var(--vf-slider-tooltip-arrow-size);
}
```

Themes [​](https://vueform.com/docs/styles-and-layout#themes)
-------------------------------------------------------------

Vueform has a couple of themes tailored to popular CSS frameworks. Themes can be installed out of the box and furhter configured with [CSS vars](https://vueform.com/docs/styles-and-layout#css-vars).

Check out [available themes](https://vueform.com/themes/tailwind).

Tailwind Prefix [​](https://vueform.com/docs/styles-and-layout#tailwind-prefix)
-------------------------------------------------------------------------------

> Please note that Vueform is only compatible with Tailwind 2 & 3.

If we want to use [Tailwind Prefix](https://tailwindcss.com/docs/configuration#prefix) we need to make some changes to our theme setup.

First we need to import `prefix` instead of `default` from Vueform's `tailwind` or `tailwind-material` theme and use it as a function with the prefix we want to use:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import { prefix as tailwind } from '@vueform/vueform/dist/tailwind'

export default defineConfig({
  theme: tailwind('tw-'),
  // ...
})
```

After that we need set `prefix` option in `tailwind.config.js`:

js

```
// tailwind.config.js

module.exports = {
  // ...
  prefix: 'tw-',
  plugins: [
    require('@vueform/vueform/tailwind')
  ]
}
```

#### Tailwind 2.x [​](https://vueform.com/docs/styles-and-layout#tailwind-2-x)

In Tailwind CSS 2.x we need to import `@vueform/vueform/tailwind-prefixer` and add is as a `transform` in `purge` block:

js

```
// tailwind.config.js

const prefixer = require('@vueform/vueform/tailwind-prefixer')

module.exports = {
  purge: {
    // ...
    content: [
      // ... your existing 
      './vueform.config.js', // or where `vueform.config.js` is located
      './node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
      './node_modules/@vueform/vueform/themes/tailwind/**/*.js',
    ],
    transform: {
      js: (content) => {
        return prefixer(content, 'tw-')
      }
    }
  },
  prefix: 'tw-',
  plugins: [
    require('@vueform/vueform/tailwind')
  ]
}
```

#### Tailwind 3.x [​](https://vueform.com/docs/styles-and-layout#tailwind-3-x)

In Tailwind CSS 3.x we need to import `@vueform/vueform/tailwind-prefixer` adn change the `content` block to an object and add `files` and `transform` with the prefixer:

js

```
// tailwind.config.js

const prefixer = require('@vueform/vueform/tailwind-prefixer')

module.exports = {
  content: {
    files: [
      // ... your existing 
      './vueform.config.js', // or where `vueform.config.js` is located
      './node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
      './node_modules/@vueform/vueform/themes/tailwind/**/*.js',
    ],
    transform: {
      js: (content) => {
        return prefixer(content, 'tw-')
      }
    }
  },
  prefix: 'tw-',
  plugins: [
    require('@vueform/vueform/tailwind')
  ]
}
```

#### Screen Sizes [​](https://vueform.com/docs/styles-and-layout#screen-sizes)

If we are using different screen sizes than the default ones (`sm`, `md`, `lg`, `xl`, `2xl`) we can pass those as a third argument to `prefixer()`:

js

```
js: (content) => {
  return prefixer(
    content,
    'tw-',
    ['xs', 'sm', 'md', 'lg', 'xl', 'xxl']
  )
}
```

Dark Mode [​](https://vueform.com/docs/styles-and-layout#dark-mode)
-------------------------------------------------------------------

Vueform themes support dark mode out of the box.

By default the dark mode is applied:

*   according to [`darkMode`](https://tailwindcss.com/docs/dark-mode) settings in `tailwind.config.js` when using Tailwind CSS
*   when `.dark` class is present earlier in the HTML tree when using class name based themes.

> Vueform's does not set text colors, so make sure to apply dark themes text colors for form elements as well (eg. define `color: white` for any parent HTML element).

Dark mode is applied by default from version `1.8.0` and can [be disabled](https://vueform.com/docs/styles-and-layout#disabling-dark-mode) or [configured](https://vueform.com/docs/styles-and-layout#configuring-dark-mode).

### Dark Mode Customization [​](https://vueform.com/docs/styles-and-layout#dark-mode-customization)

The dark mode is only an overwrite of certain [CSS vars](https://vueform.com/docs/styles-and-layout#css-vars) that affect colors.

Colors can be customized by overwriting `--vf-dark-*` variables **after** the Vueform theme CSS file or Tailwind CSS is imported.

#### vueform, material, bootstrap [​](https://vueform.com/docs/styles-and-layout#vueform-material-bootstrap)

Customization for `vueform`, `material` and `bootstrap` themes:

css

```
/* @vueform/vueform/dist/vueform|material|bootstrap.css is imported before */

.dark, .dark *, .dark :before, .dark :after {
  --vf-dark-50: #efefef;
  --vf-dark-100: #dcdcdc;
  --vf-dark-200: #bdbdbd;
  --vf-dark-300: #a0a0a0;
  --vf-dark-400: #848484;
  --vf-dark-500: #737373;
  --vf-dark-600: #393939;
  --vf-dark-700: #323232;
  --vf-dark-800: #262626;
  --vf-dark-900: #191919;
}
```

#### tailwind [​](https://vueform.com/docs/styles-and-layout#tailwind)

Customization for `tailwind` theme:

css

```
@tailwind base;
@tailwind components;
@tailwind utilities;

.dark, .dark *, .dark :before, .dark :after {
  --vf-dark-50: #efefef;
  --vf-dark-100: #dcdcdc;
  --vf-dark-200: #bdbdbd;
  --vf-dark-300: #a0a0a0;
  --vf-dark-400: #848484;
  --vf-dark-500: #737373;
  --vf-dark-600: #393939;
  --vf-dark-700: #323232;
  --vf-dark-800: #262626;
  --vf-dark-900: #191919;
}
```

#### Detailed Customization [​](https://vueform.com/docs/styles-and-layout#detailed-customization)

If we want to further customize colors we can use more specific overrides of CSS vars (applies for all themes):

css

```
/* You might use a customized CSS selector */
.dark, .dark *, .dark :before, .dark :after {
  --vf-bg-input: var(--vf-dark-800);
  --vf-bg-input-hover: var(--vf-bg-input);
  --vf-bg-input-focus: var(--vf-bg-input);
  --vf-bg-input-danger: var(--vf-bg-input);
  --vf-bg-input-success: var(--vf-bg-input);
  --vf-bg-checkbox: var(--vf-dark-700);
  --vf-bg-checkbox-hover: var(--vf-bg-checkbox);
  --vf-bg-checkbox-focus: var(--vf-bg-checkbox);
  --vf-bg-checkbox-danger: var(--vf-bg-checkbox);
  --vf-bg-checkbox-success: var(--vf-bg-checkbox);
  --vf-bg-disabled: var(--vf-dark-700);
  --vf-bg-selected: var(--vf-dark-700); /* Used eg. when select option is hovered or a checkbox is selected in `blocks` view */
  --vf-bg-passive: var(--vf-dark-700); /* Used as a background color for eg. slider, toggle */
  --vf-bg-icon: var(--vf-dark-400);
  --vf-bg-danger: var(--vf-danger-lighter);
  --vf-bg-success: var(--vf-success-lighter);
  --vf-bg-addon: transparent;
  --vf-bg-tag: var(--vf-primary);
  --vf-bg-slider-handle: var(--vf-primary);
  --vf-bg-toggle-handle: #ffffff;
  --vf-bg-date-head: var(--vf-dark-700);
  --vf-bg-btn: var(--vf-primary);
  --vf-bg-btn-danger: var(--vf-danger);
  --vf-bg-btn-secondary: var(--vf-dark-700);

  --vf-color-on-primary: #ffffff; /* Used when text is displayed on primary color */
  --vf-color-input: var(--vf-dark-100);
  --vf-color-input-hover: var(--vf-color-input);
  --vf-color-input-focus: var(--vf-color-input);
  --vf-color-input-danger: var(--vf-color-input);
  --vf-color-input-success: var(--vf-color-input);
  --vf-color-placeholder: var(--vf-dark-500);
  --vf-color-disabled: var(--vf-dark-500);
  --vf-color-passive: var(--vf-dark-900); /* Used when text is displayed on passive background eg. `off` toggle */
  --vf-color-muted: var(--vf-dark-500); /* Used for helper texts eg. element description, floating label */
  --vf-color-floating: var(--vf-color-muted);
  --vf-color-floating-focus: var(--vf-color-floating); /* Used when the input is focused */
  --vf-color-floating-success: var(--vf-color-floating); /* Used when the input is filled with success */
  --vf-color-floating-danger: var(--vf-color-floating); /* Used when the input has error */
  --vf-color-danger: var(--vf-danger);
  --vf-color-success: var(--vf-success);
  --vf-color-addon: initial;
  --vf-color-tag: var(--vf-color-on-primary);
  --vf-color-date-head: var(--vf-dark-200);
  --vf-color-btn: var(--vf-color-on-primary);
  --vf-color-btn-danger: #ffffff;
  --vf-color-btn-secondary: var(--vf-dark-300);

  --vf-border-color-input: var(--vf-dark-800);
  --vf-border-color-input-focus: var(--vf-primary);
  --vf-border-color-input-hover: var(--vf-border-color-input);
  --vf-border-color-input-danger: var(--vf-border-color-input);
  --vf-border-color-input-success: var(--vf-border-color-input);
  --vf-border-color-checkbox: var(--vf-border-color-input);
  --vf-border-color-checkbox-focus: var(--vf-primary);
  --vf-border-color-checkbox-hover: var(--vf-border-color-checkbox);
  --vf-border-color-checkbox-danger: var(--vf-border-color-checkbox);
  --vf-border-color-checkbox-success: var(--vf-border-color-checkbox);
  --vf-border-color-checked: var(--vf-primary);
  --vf-border-color-btn: var(--vf-primary);
  --vf-border-color-tag: var(--vf-primary);
  --vf-border-color-slider-tooltip: var(--vf-primary);
  --vf-border-color-passive: var(--vf-dark-700); /* Used as a border for passive states eg. `off` toggle */
  --vf-border-color-btn-danger: var(--vf-danger);
  --vf-border-color-btn-secondary: var(--vf-dark-700);
  --vf-border-color-blockquote: var(--vf-dark-700);
  --vf-border-color-hr: var(--vf-dark-700);

  --vf-shadow-input: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-input-hover: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-input-focus: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-handles: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-handles-hover: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-handles-focus: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-btn: 0px 0px 0px 0px rgba(0,0,0,0);
  --vf-shadow-dropdown: 0px 0px 0px 0px rgba(0,0,0,0);
}
```

These are all the color related CSS variables in Vueform, but we might change others if we see fit.

### Disabling Dark Mode [​](https://vueform.com/docs/styles-and-layout#disabling-dark-mode)

Dark mode is only available from version `1.8.0` but can be disabled.

#### vueform, bootstrap, material [​](https://vueform.com/docs/styles-and-layout#vueform-bootstrap-material)

In class name based themes the dark theme can be disabled by importing the `css` without dark mode variables:

js

```
// eg. vueform.config.js

import '@vueform/vueform/dist/{THEME_NAME}.nodark.css'
```

#### tailwind [​](https://vueform.com/docs/styles-and-layout#tailwind-1)

The dark theme can be disabled in `tailwind` theme by setting `vfDarkMode` to `false` in `tailwind.config.js`:

js

```
// tailwind.config.js

export default {
  // ...
  vfDarkMode: false,
}
```

### Configuring Dark Mode [​](https://vueform.com/docs/styles-and-layout#configuring-dark-mode)

We can configure how and when dark mode should be enabled.

#### vueform, bootstrap, material [​](https://vueform.com/docs/styles-and-layout#vueform-bootstrap-material-1)

When using a class name based theme by default the `.dark` class must is present earlier in the HTML tree (eg. `<body>` or `<html>`).

The class name can be customized by importing the theme's `.scss` file instead of `.css` and using the `vf-dark-vars` mixin to load CSS vars:

html

```
<!-- Eg. App.vue -->

<style lang="scss">
  @import '@vueform/vueform/themes/vueform/scss/index.scss';

  @media (prefers-color-scheme: dark) {
    :root, :before, :after, * {
      @include vf-dark-vars;
    }
  }
</style>
```

#### tailwind [​](https://vueform.com/docs/styles-and-layout#tailwind-2)

When using Tailwind CSS the dark mode will be automatically detected based on the settings in `tailwind.config.js`.

If `darkMode` is:

*   not set, user preferences will be used using `@media (prefers-color-scheme: dark)` query.
*   set to `class` the `.dark` class must is present earlier in the HTML tree.
*   an array the second item will be the class selector.

Learn more about Tailwind CSS dark mode configuration [here](https://tailwindcss.com/docs/dark-mode).
