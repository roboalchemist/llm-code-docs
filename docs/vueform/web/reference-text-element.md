# Source: https://vueform.com/reference/text-element

Title: TextElement | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/reference/text-element

Markdown Content:
Renders a native HTML text input.

Basic Usage [​](https://vueform.com/reference/text-element#basic-usage)
-----------------------------------------------------------------------

`<TextElement>` component can be used in a `<Vueform>` component:

vue

```
<template>
  <Vueform>
    <TextElement name="text" />
  </Vueform>
</template>
```

Configuration options can be passed over as regular component **props**. Check out [Options](https://vueform.com/reference/text-element#options) section for available configuration options.

Options [​](https://vueform.com/reference/text-element#options)
---------------------------------------------------------------

Find below the list of options that can use to configure `TextElement` component. Options can be passed to the component via **props** in inline templates, or in the element's object when using [`schema`](https://vueform.com/reference/vueform#option-schema).

### inputType [​](https://vueform.com/reference/text-element#option-input-type)

*   Type: `string`
*   Default: `text`

vue

```
<TextElement input-type="password" ... />
<TextElement input-type="date" ... />
<TextElement input-type="number" ... />
```

Sets the `type` attribute of the input field.

### expression [​](https://vueform.com/reference/text-element#option-expression)

*   Type: `string|object`
*   Default: `undefined`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

```
<TextElement name="qty" input-type="number" default="10" />
<TextElement name="price" input-type="number" default="5" />
<TextElement name="total" expression="{qty * price}" readonly ... />
```

The [expression](https://vueform.com/docs/expressions) that should be used as the element value. Recommended to be used in conjunction with [`readonly`](https://vueform.com/reference/text-element#option-readonly) or [`disabled`](https://vueform.com/reference/text-element#option-disabled).

### addons [​](https://vueform.com/reference/text-element#option-addons)

*   Type: `object`
*   Default: `{}`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

```
<TextElement :addons="{ before: { template: `<app-icon :icon="['fas', 'pen']" />` } }" ... />
<TextElement :addons="{ after: '...' }" ... />
```

Adds an addon before or after the input field. Can be defined in an object with `before` and `after` keys. The value can either be a `string` or a Vue `component` object with a render function.

> **Note:** Can also be defined via [`#addon-before`](https://vueform.com/reference/text-element#slot-addon-before)&[`#addon-after`](https://vueform.com/reference/text-element#slot-addon-after) slots.

### mask [​](https://vueform.com/reference/text-element#option-mask)

*   Type: `string|object|array|function`
*   Default: `undefined`

vue

`<Text mask="{+1} (000)-000-0000" default="+1 650-253-0000" ... />`

> **IMPORTANT:** Using this option requires [@vueform/plugin-mask](https://vueform.com/docs/input-mask) plugin.

### autocomplete [​](https://vueform.com/reference/text-element#option-autocomplete)

*   Type: `string|number`
*   Default: `null`

vue

`<TextElement autocomplete="off" ... />`

Sets the `autocomplete` attribute of the input field.

> **Hint:** the value `'off'` might not disable autocomplete - read more about it [here](https://stackoverflow.com/questions/12374442/chrome-ignores-autocomplete-off). Alternatively you can also set [`inputType`](https://vueform.com/reference/text-element#option-input-type) to `'search'`.

### loading [​](https://vueform.com/reference/text-element#option-loading)

*   Type: `boolean`
*   Default: `false`

vue

`<TextElement :loading="true" ... />`

Manually triggers the loading state and displays a spinner on the right.

### name [​](https://vueform.com/reference/text-element#option-name)

*   Type: `string|number`
*   Default: `undefined`
*   Required: `true`

vue

`<TextElement name="element" ... />`

Sets the element's name and the `name` attribute of the input field.

### id [​](https://vueform.com/reference/text-element#option-id)

*   Type: `string`
*   Default: `null`

vue

`<TextElement id="field-id" ... />`

Sets the `id` attribute of the input field.

### readonly [​](https://vueform.com/reference/text-element#option-readonly)

*   Type: `boolean|function|array|object`
*   Default: `false`

vue

```
<TextElement :readonly="true" ... />
<TextElement :readonly="prop" ... /> <!-- computed / data (ref) prop -->
<TextElement :readonly="[['text', 'value']]" ... /> <!-- conditional -->
<TextElement :readonly="(el$, form$) => { return /* boolean */ }" ... />
```

Sets the `readonly` attribute of the input field.

If can be a `boolean` value.

It can be a computed / data (ref) prop.

It can be an `array` of [conditions](https://vueform.com/docs/conditional-rendering#element-conditions). When all conditions are met the element will become readonly.

It can be a function that receives the [`el$`](https://vueform.com/reference/text-element#property-el_) element instance and [`form$`](https://vueform.com/reference/text-element#property-form_) form instance params and expected to return a `boolean`.

### disabled [​](https://vueform.com/reference/text-element#option-disabled)

*   Type: `boolean|function|array|object`
*   Default: `false`

vue

```
<TextElement :disabled="true" ... />
<TextElement :disabled="prop" ... /> <!-- computed / data (ref) prop -->
<TextElement :disabled="[['text', 'value']]" ... /> <!-- conditional -->
<TextElement :disabled="(el$, form$) => { return /* boolean */ }" ... />
```

Disables the input field.

If can be a `boolean` value.

It can be a computed / data (ref) prop.

It can be an `array` of [conditions](https://vueform.com/docs/conditional-rendering#element-conditions). When all conditions are met the element will become disabled.

It can be a function that receives the [`el$`](https://vueform.com/reference/text-element#property-el_) element instance and [`form$`](https://vueform.com/reference/text-element#property-form_) form instance params and expected to return a `boolean`.

### attrs [​](https://vueform.com/reference/text-element#option-attrs)

*   Type: `object`
*   Default: `{}`

vue

`<TextElement :attrs="{ autofocus: true }" ... />`

Assigns HTML attributes to the container / input field.

### label [​](https://vueform.com/reference/text-element#option-label)

*   Type: `string|object|function`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

Sets a label for the element. Can be defined as a `string`, a Vue `component` object with a render function or as a `function` that receives [`el$`](https://vueform.com/reference/text-element#property-el) as its first a param.

> Can also be defined via [`#label`](https://vueform.com/reference/text-element#slot-label) slot.

### placeholder [​](https://vueform.com/reference/text-element#option-placeholder)

*   Type: `string|object`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement placeholder="Placeholder" ... />`

Sets the `placeholder` attribute of the input field.

The value of `placeholder` is automatically set as [`floating`](https://vueform.com/reference/text-element#option-floating) if that's not defined. This behavior can be disabled on form level with [`floatPlaceholders: false`](https://vueform.com/reference/vueform#option-float-placeholders) or globally in [`vueform.config.js`](https://vueform.com/reference/configuration#float-placeholders).

### floating [​](https://vueform.com/reference/text-element#option-floating)

*   Type: `string|boolean|object`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement floating="Text" ... />`

Renders a floating label above the input field if that has value.

If [`floatPlaceholders`](https://vueform.com/reference/vueform#option-float-placeholders) is enabled it can be disabled for this element by using `:floating="false"`.

### info [​](https://vueform.com/reference/text-element#option-info)

*   Type: `string|object`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement label="Info" info="Info" ... />`

Renders an [`ElementInfo`](https://vueform.com/reference/element-info) component next to the element's label. By default the icon shows the value of `info` when hovered, which can contain plain text or HTML. The element needs to have a [`label`](https://vueform.com/reference/text-element#option-label) defined in order for info to be rendered.

> Can be also defined via [`#info`](https://vueform.com/reference/text-element#slot-info) slot.

### infoPosition [​](https://vueform.com/reference/text-element#option-info-position)

*   Type: `string`
*   Default: `right`

vue

```
<TextElement label="Top" info="Top" info-position="top" ... />
<TextElement label="Right" info="Right" info-position="right" ... />
<TextElement label="Left" info="Left" info-position="left" ... />
<TextElement label="Bottom" info="Bottom" info-position="bottom" ... />
```

Sets the position of the [`info`](https://vueform.com/reference/text-element#option-info) tooltip.

> Can be also defined via [`#info`](https://vueform.com/reference/text-element#slot-info) slot.

### description [​](https://vueform.com/reference/text-element#option-description)

*   Type: `string|object`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement description="Lorem ipsum dolor sit amet" ... />`

Renders the contents of `description` prop in the [`ElementDescription`](https://vueform.com/reference/element-description) component below the input field. It can contain plain text or HTML.

> Can be also defined via [`#description`](https://vueform.com/reference/text-element#slot-description) slot.

### before [​](https://vueform.com/reference/text-element#option-before)

*   Type: `object|string|number`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement before="Before" ... />`

Renders the contents of `before` in a [`ElementText`](https://vueform.com/reference/element-text) component before the **input field**. It can contain plain text or HTML.

> Can be also defined via [`#before`](https://vueform.com/reference/text-element#slot-before) slot.

### between [​](https://vueform.com/reference/text-element#option-between)

*   Type: `object|string|number`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement description="Description" between="Between" ... />`

Renders the contents of `between` in a [`ElementText`](https://vueform.com/reference/element-text) component between the **input field** and the **description**. It can contain plain text or HTML.

> Can be also defined via [`#between`](https://vueform.com/reference/text-element#slot-between) slot.

### after [​](https://vueform.com/reference/text-element#option-after)

*   Type: `object|string|number`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement description="Description" rules="required" after="After" ... />`

Renders the contents of `after` in a [`ElementText`](https://vueform.com/reference/element-text) component after the **description** and **error**. It can contain plain text or HTML.

> Can be also defined via [`#after`](https://vueform.com/reference/text-element#slot-after) slot.

### default [​](https://vueform.com/reference/text-element#option-default)

*   Type: `string|number|object`
*   Default: `null`
*   [Localizable](https://vueform.com/docs/i18n#translating-element-properties): `true`

vue

`<TextElement default="Default" ... />`

Sets the default value for the input field.

### forceNumbers [​](https://vueform.com/reference/text-element#option-force-numbers)

*   Type: `boolean`
*   Default: `null`

vue

```
<!-- Form `data` & `requestData` will be string -->
<TextElement default="123" />
<TextElement default="123.456" />
<TextElement default="123,456" />

<!-- Form `data` & `requestData` will be number -->
<TextElement default="123" force-numbers />
<TextElement default="123.456" force-numbers />
<TextElement default="123,456" force-numbers />
<TextElement default="123a" force-numbers />
```

Whether the input value should be transformed to a `number` in form [`data`](https://vueform.com/reference/vueform#property-data) and [`requestData`](https://vueform.com/reference/vueform#property-request-data). If the input value contains any non-numeric character (except for `.` and `,`) it will be kept as `string`.

It can be also set on [form level](https://vueform.com/reference/vueform#option-force-numbers) or [config level](https://vueform.com/docs/configuration#forcenumbers).

### formatData [​](https://vueform.com/reference/text-element#option-format-data)

*   Type: `function`
*   Default: `null`

vue

`<TextElement :format-data="(n, v) => ({[n]: /* transformed value */ })" ... />`

Formats the element's [`requestData`](https://vueform.com/reference/text-element#property-request-data).

The first param is the element's `name`, the second is the `value`. The return value should be an `object`, which only contains one item with the element's `name` as key and the transformed `value` as value.

### formatLoad [​](https://vueform.com/reference/text-element#option-format-load)

*   Type: `function`
*   Default: `null`

vue

`<TextElement :format-load="(v) => /* transformed value */" ... />`

Formats the data being loaded to the element when using [`load(data, format: true)`](https://vueform.com/reference/text-element#method-load). It receives the value being loaded to the element as its first param and should return the formatted value of the element.

### submit [​](https://vueform.com/reference/text-element#option-submit)

*   Type: `boolean`
*   Default: `true`

vue

`<TextElement :submit="false" ... />`

If set to `false` the element's data will not be included in [`requestData`](https://vueform.com/reference/text-element#property-request-data) and will not be submitted.

### rules [​](https://vueform.com/reference/text-element#option-rules)

*   Type: `array|string|object`
*   Default: `null`

vue

```
<TextElement rules="required|min:2" ... />
<TextElement :rules="['required', 'min:2']" ... />
```

The validation rules to be applied for the element.

The list of rules can be defined as a `string` separated by `|` or as an `array`, where each item should be a single validation rule.

### fieldName [​](https://vueform.com/reference/text-element#option-field-name)

*   Type: `string|object`
*   Default: `name|label`

vue

`<TextElement field-name="Field name" rules="required" ... />`

Sets the name of the field in validation rule messages.

### debounce [​](https://vueform.com/reference/text-element#option-debounce)

*   Type: `number`
*   Default: `null`

vue

```
<TextElement floating="Without debounce" rules="required" ... />
<TextElement floating="With debounce" :debounce="500" rules="required" ... />
```

The `milliseconds` to wait before the validation triggers after the user changed the value (unless the value is empty). Applies to each validation rule.

> If you only want debounce for a specific rule, you can use: `rules="required|email:debounce=500"`

### messages [​](https://vueform.com/reference/text-element#option-messages)

*   Type: `object`
*   Default: `{}`

vue

`<TextElement rules="required" :messages="{ required: 'Please fill in' }" ... />`

Overrides the default messages for the element's validation rules. The value is an `object` where each key is the name of a validation rule and the value is the error message that will be displayed when the rule fails.

> You can override validation messages on form level with [`messages`](https://vueform.com/reference/vueform#option-messages).

### displayErrors [​](https://vueform.com/reference/text-element#option-display-errors)

*   Type: `boolean`
*   Default: `true`

vue

`<TextElement :display-errors="false" ... />`

Whether element errors should be displayed.

### conditions [​](https://vueform.com/reference/text-element#option-conditions)

*   Type: `array`
*   Default: `[]`

vue

```
<TextElement :conditions="[
  ['foo', 'bar'],
  'AGE(birthday) > 18',
  (form$) => !!form$?.el$('terms').value
]" ... />
```

Shows or hides an element based on the provided [conditions](https://vueform.com/docs/conditional-rendering).

### columns [​](https://vueform.com/reference/text-element#option-columns)

*   Type: `object|string|number`
*   Default: `null`

vue

`<TextElement label="Label" :columns="{ container: 12, label: 3, wrapper: 12 }" ... />`

Sets the size of the `container`, `label` and `wrapper` using the theme's grid system, where the:

*   `container` is the outermost DOM that contains both `label` and `wrapper`
*   `label` contains the label
*   `wrapper` contains the input field.

`container: 12`

`label: 3`

`wrapper: 12`

The value of `container` defines the size of the element's container. `12` will result in full width, `6` in half, `4` in third and so on.

The value of `label` defines the amount of space the label should take up **within the container**. If the `container` is `12` and `label` is `6` the label is going to take up half the space and the input field will the other half (which is calculated automatically). If the `container` is `6` and `label` is `6`, the label will only take up one forth and the input field the rest. In case the `label` has full width (`12`) the input field will also take up **full space** instead of becoming zero.

The value of `wrapper` defines the size of the input field wrapper **within the space left for it in the container after subtracting the size of the label**. If the `container` is `12` and `label` is `4` the space left for the input field is `8`. In this case if the `wrapper` value is `12` it will take up the full space left for it (which is `8`) while if it is changed to `6` it will only take up half the space left for it (`4`):

vue

```
<TextElement label="Label" :columns="{ container: 12, label: 4, wrapper: 12 }" ... />
<TextElement label="Label" :columns="{ container: 12, label: 4, wrapper: 6 }" ... />
```

Note that while the size of the input field wrapper changes, the size of _extras_ like a description or error won't be limited to the wrapper's space. Instead it will take up the full space in the container left after subtracting the size of the label:

vue

```
<TextElement
  label="Label"
  :columns="{ container: 12, label: 4, wrapper: 6 }" 
  description="Lorem ipsum dolor sit amet, consectetur adipiscing elit"
... />
```

You can set the value of `columns` as a `number` in which case the `container` will receive its value without affecting the default settings of `label` and `wrapper`:

vue

`<TextElement label="Label" :columns="6" ... /> <!-- { container: 6, label: 3, wrapper: 12 } -->`

You can as well define column values for different **breakpoints** using the theme system's breakpoints like `sm`, `md`, etc. as keys:

vue

```
<TextElement label="Label" :columns="{
  xs: { container: 12, label: 12, wrapper: 12 },
  sm: { container: 12, label: 4, wrapper: 12 },
  md: 12,
  lg: { container: 12, label: 2, wrapper: 12 }
}" ... />
```

> Default column sizes can be defined globally in [`vueform.config.js`](https://vueform.com/reference/configuration#columns) or on form level using [`columns`](https://vueform.com/reference/vueform#option-columns).

### inline [​](https://vueform.com/reference/text-element#option-inline)

*   Type: `boolean`
*   Default: `false`

vue

`<TextElement :inline="true" ... />`

Renders the element and all of its components in a single `<span>` without applying [`columns`](https://vueform.com/reference/text-element#option-columns).

### size [​](https://vueform.com/reference/text-element#option-size)

*   Type: `string`
*   Default: `undefined`

vue

```
<TextElement size="sm" ... />
<TextElement ... /> <!-- Default size: 'md' -->
<TextElement size="lg" ... />
```

The size of the element and its child components.

### view [​](https://vueform.com/reference/text-element#option-view)

*   Type: `string`
*   Default: `undefined`

vue

`<TextElement view="alt" ... />`

The name of the view to be used for the element and by default for its child components. If `undefined` the default view will be used. Child component views can be overridden with [`views`](https://vueform.com/reference/text-element#option-views) option.

Learn more about views [here](https://vueform.com/docs/styles-and-layout#views).

### views [​](https://vueform.com/reference/text-element#option-views)

*   Type: `object`
*   Default: `{}`

vue

```
<TextElement :views="{
  ComponentName: 'alt'
}" ... />
```

The name of the views for the child components.

Learn more about views [here](https://vueform.com/docs/styles-and-layout#views).

### addClasses [​](https://vueform.com/reference/text-element#option-add-classes)

*   Type: `object|function`
*   Default: `{}`

vue

```
<TextElement :add-classes="{
  ComponentName: {
    classname: 'class-value',
    classname: ['class-value'],
    classname: [{'class-value': true}],
  }
}" ... />
```

Adds classes to any component's class names. The classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :add-classes="(form$) => ({
  ComponentName: {
    classname: [
      { 'class-value': form$.el$('other_field')?.value === 'some_value' }
    ],
  }
})" ... />
```

Learn more about adding classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### addClass [​](https://vueform.com/reference/text-element#option-add-class)

*   Type: `array|object|string|function`
*   Default: `null`

vue

```
<TextElement :add-class="{
  classname: 'class-value',
  classname: ['class-value'],
  classname: [{'class-value': true}],
}" ... />
```

Adds classes to any of `TextElement` component's class names. Classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :add-class="(form$) => ({
  classname: [
    { 'class-value': form$.el$('other_field')?.value === 'some_value' }
  ],
})" ... />
```

Learn more about adding classes [here](https://vueform.com/docs/styles-and-layout#add-classes).

### removeClasses [​](https://vueform.com/reference/text-element#option-remove-classes)

*   Type: `object|function`
*   Default: `{}`

vue

```
<TextElement :remove-classes="{
  ComponentName: {
    classname: ['class-value-1', 'class-value-2']
  }
}" ... />
```

Removes classes from any class names of any components. The classes to be removed must be listed in an `array`.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :remove-classes="(form$) => ({
  ComponentName: {
    classname: form$.el$('other_field')?.value === 'some_value'
      ? ['class-value-1', 'class-value-2']
      : [],
  }
})" ... />
```

Learn more about removing classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### removeClass [​](https://vueform.com/reference/text-element#option-remove-class)

*   Type: `array|object|function`
*   Default: `null`

vue

```
<TextElement :remove-class="{
  classname: ['class-value-1', 'class-value-2']
}" ... />
```

Removes classes from any of `TextElement` component's class names. The classes to be removed must be listed in an `array`.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :remove-class="(form$) => ({
  classname: form$.el$('other_field')?.value === 'some_value'
    ? ['class-value-1', 'class-value-2']
    : [],
})" ... />
```

Learn more about removing classes [here](https://vueform.com/docs/styles-and-layout#remove-classes).

### replaceClasses [​](https://vueform.com/reference/text-element#option-replace-classes)

*   Type: `object|function`
*   Default: `{}`

vue

```
<TextElement :replace-classes="{
  ComponentName: {
    classname: {
      'from-class': 'to-class',
      'from-class': ['to-class'],
      'from-class': [{'to-class': true}],
    }
  }
}" ... />
```

Replaces classes of any class names of any component. The keys are the original class names and the values are the replacements. The keys can only be single classes, while values can contain multiple ones in `string` or an `array`. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :replace-classes="(form$) => ({
  ComponentName: {
    classname: form$.el$('other_field')?.value === 'some_value' ? {
      'from-class': 'to-class'
    } : {},
  }
})" ... />
```

Learn more about replacing classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### replaceClass [​](https://vueform.com/reference/text-element#option-replace-class)

*   Type: `object|function`
*   Default: `null`

vue

```
<TextElement :replace-class="{
  classname: {
    'from-class': 'to-class',
    'from-class': ['to-class'],
    'from-class': [{'to-class': true}],
  }
}" ... />
```

Replaces the classes of any class names of `TextElement` component. The keys are the original class names and the values are the replacements. The keys can only be single classes, while values can contain multiple ones in `string` or an `array`. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :replace-class="(form$) => ({
  classname: form$.el$('other_field')?.value === 'some_value' ? {
    'from-class': 'to-class'
  } : {},
})" ... />
```

Learn more about replacing classes [here](https://vueform.com/docs/styles-and-layout#replace-classes).

### overrideClasses [​](https://vueform.com/reference/text-element#option-override-classes)

*   Type: `object|function`
*   Default: `{}`

vue

```
<TextElement :override-classes="{
  ComponentName: {
    classname: 'class-value',
    classname: ['class-value'],
    classname: [{'class-value': true}],
  }
}" ... />
```

Overrides the classes of any component's class names. The classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :override-classes="(form$) => ({
  ComponentName: form$.el$('other_field')?.value === 'some_value' ? {
    classname: 'class-value'
  } : {}
})" ... />
```

Learn more about overriding classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### overrideClass [​](https://vueform.com/reference/text-element#option-override-class)

*   Type: `array|object|string|function`
*   Default: `null`

vue

```
<TextElement :override-classes="{
  ComponentName: {
    classname: 'class-value',
    classname: ['class-value'],
    classname: [{'class-value': true}],
  }
}" ... />
```

Overrides the classes of any of `TextElement` component's class names. The classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/text-element#property-form) param, eg.:

vue

```
<TextElement :override-class="(form$) => (form$.el$('other_field')?.value === 'some_value' ? {
  classname: 'class-value'
} : {})" ... />
```

Learn more about overriding classes [here](https://vueform.com/docs/styles-and-layout#override-classes).

### templates [​](https://vueform.com/reference/text-element#option-templates)

*   Type: `object`
*   Default: `{}`

vue

```
<template>
  <div id="app">
    <Vueform>
      <TextElement :templates="{ ElementError }" ... />
    </Vueform>
  </div>
</template>

<script>
import { markRaw } from 'vue'
import CustomElementError from './CustomElementError.vue'

export default {
  data() {
    return {
      ElementError: markRaw(CustomElementError),
    }
  }
}
</script>
```

Overrides templates used by the component.

Learn more about overriding templates [here](https://vueform.com/docs/styles-and-layout#templates).

### presets [​](https://vueform.com/reference/text-element#option-presets)

*   Type: `array`
*   Default: `[]`

vue

`<TextElement :presets="['preset1', 'preset2']" ... />`

The presets to be applied for the component.

Learn more about presets classes [here](https://vueform.com/docs/styles-and-layout#presets).

### slots [​](https://vueform.com/reference/text-element#option-slots)

*   Type: `object`
*   Default: `{}`

vue

```
<script>
import { Vueform, useVueform } from '@vueform/vueform';
import CustomDescriptionSlot from 'path/to/CustomDescriptionSlot.vue';

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      schema: {
        element: {
          type: 'text',
          slots: {
            label: '<span>Label</span>',
            description: CustomDescriptionSlot,
          }
        }
      }
    }
  })
}
</script>
```

With this option you can define [slot values](https://vueform.com/reference/text-element#slots) in a schema based form that you would normally just write inline. The value of a slot can be a plain string, HTML or a component with render function.

> While this option can be also used in inline forms, it's primarily intended for schema based forms.

Properties [​](https://vueform.com/reference/text-element#properties)
---------------------------------------------------------------------

Properties include `data`, `computed` and `inject` properties of the component. You can use them by reaching the element's Vue component instance via [`form$`](https://vueform.com/reference/text-element#property-form)'s [`el$(path)`](https://vueform.com/reference/vueform#method-el) method or directly via `this` in options API or [`el$`](https://vueform.com/reference/text-element#property-el) in Composition API.

### aria [​](https://vueform.com/reference/text-element#property-aria)

*   Type: `object`
*   Group: `computed`

The `aria-*` attributes of the input.

### Placeholder [​](https://vueform.com/reference/text-element#property-placeholder)

*   Type: `string`
*   Group: `computed`

The localized placeholder of the element.

### isReadonly [​](https://vueform.com/reference/text-element#property-is-readonly)

*   Type: `boolean`
*   Group: `computed`

Whether the element is readonly.

### isRequired [​](https://vueform.com/reference/text-element#property-is-required)

*   Type: `boolean`
*   Group: `computed`

Whether the element is required (has required rule).

### useCustomFilled [​](https://vueform.com/reference/text-element#property-use-custom-filled)

*   Type: `boolean`
*   Group: `computed`

Whether the element should use a custom logic for checking if it is filled when validating.

### isFilled [​](https://vueform.com/reference/text-element#property-is-filled)

*   Type: `boolean`
*   Group: `computed`

Whether the element is filled is `useCustomFilled` is `true`.

### isDefault [​](https://vueform.com/reference/text-element#property-is-default)

*   Type: `boolean`
*   Group: `computed`

Whether the element has its default value.

### value [​](https://vueform.com/reference/text-element#property-value)

*   Type: `any`
*   Group: `computed`

The value of the element.

### model [​](https://vueform.com/reference/text-element#property-model)

*   Type: `any`
*   Group: `computed`

Intermediary value between element's value and field's `v-model`. It is required when we need to transform the value format between the element and its field.

### data [​](https://vueform.com/reference/text-element#property-data)

*   Type: `object`
*   Group: `computed`

The value of the element in `{[name]: value}` value format. This gets merged with the parent component's data.

### requestData [​](https://vueform.com/reference/text-element#property-request-data)

*   Type: `object`
*   Group: `computed`

Same as `data` property except that it only includes the element's value if [`submit`](https://vueform.com/reference/text-element#option-submit) is not disabled and [`available`](https://vueform.com/reference/text-element#property-available) is `true` (has no [`conditions`](https://vueform.com/reference/text-element#option-conditions) or they are fulfilled).

### empty [​](https://vueform.com/reference/text-element#property-empty)

*   Type: `boolean`
*   Group: `computed`

Whether the element has no value filled in.

### path [​](https://vueform.com/reference/text-element#property-path)

*   Type: `string`
*   Group: `computed`

The path of the element using dot `.` syntax.

### dataPath [​](https://vueform.com/reference/text-element#property-data-path)

*   Type: `string`
*   Group: `computed`

The path of the element's data using dot `.` syntax.

### parent [​](https://vueform.com/reference/text-element#property-parent)

*   Type: `VNode`
*   Group: `computed`

The parent component of the element.

### validated [​](https://vueform.com/reference/text-element#property-validated)

*   Type: `boolean`
*   Group: `computed`

Whether the element was already validated at least once.

### invalid [​](https://vueform.com/reference/text-element#property-invalid)

*   Type: `boolean`
*   Group: `computed`

Whether the element has any failing rules.

### dirty [​](https://vueform.com/reference/text-element#property-dirty)

*   Type: `boolean`
*   Group: `computed`

Whether the element's value was modified.

### pending [​](https://vueform.com/reference/text-element#property-pending)

*   Type: `boolean`
*   Group: `computed`

Whether the element has any async rules in progress.

### debouncing [​](https://vueform.com/reference/text-element#property-debouncing)

*   Type: `boolean`
*   Group: `computed`

Whether the element has a validation rule with pending debounce.

### busy [​](https://vueform.com/reference/text-element#property-busy)

*   Type: `boolean`
*   Group: `computed`

Whether the element is `pending` or `debouncing`.

### messageBag [​](https://vueform.com/reference/text-element#property-message-bag)

*   Type: `MessageBag`
*   Default: `MessageBag`
*   Group: `data`

Instance of MessageBag service. Custom errors and messages [can be added](https://vueform.com/docs/validating-elements#custom-errors-and-messages).

### errors [​](https://vueform.com/reference/text-element#property-errors)

*   Type: `array`
*   Group: `computed`

All the errors of `MessageBag`.

### error [​](https://vueform.com/reference/text-element#property-error)

*   Type: `string`
*   Group: `computed`

The first error of `MessageBag`.

### available [​](https://vueform.com/reference/text-element#property-available)

*   Type: `boolean`
*   Group: `computed`

Whether no [`conditions`](https://vueform.com/reference/text-element#option-conditions) are defined or they are all fulfilled.

### hidden [​](https://vueform.com/reference/text-element#property-hidden)

*   Type: `boolean`
*   Default: `false`
*   Group: `data`

Whether the element was hidden programmatically with [`show()`](https://vueform.com/reference/text-element#method-show) or [`hide()`](https://vueform.com/reference/text-element#method-hide) methods.

### visible [​](https://vueform.com/reference/text-element#property-visible)

*   Type: `boolean`
*   Group: `computed`

Whether the element is visible. It's `false` when `available` or `active` is `false` or `hidden` is `true`.

### focused [​](https://vueform.com/reference/text-element#property-focused)

*   Type: `boolean`
*   Group: `data`

Whether the element is focused.

### isDisabled [​](https://vueform.com/reference/text-element#property-is-disabled)

*   Type: `boolean`
*   Group: `computed`

Whether the element is disabled.

### isLoading [​](https://vueform.com/reference/text-element#property-is-loading)

*   Type: `boolean`
*   Group: `computed`

Whether the element is in loading state.

### isSuccess [​](https://vueform.com/reference/text-element#property-is-success)

*   Type: `boolean`
*   Group: `computed`

Whether the element has been filled in successfully.

### isDanger [​](https://vueform.com/reference/text-element#property-is-danger)

*   Type: `boolean`
*   Group: `computed`

Whether the element has errors.

### container [​](https://vueform.com/reference/text-element#property-container)

*   Type: `HTMLElement`
*   Group: `data`

The ref to the outermost DOM of the element.

### input [​](https://vueform.com/reference/text-element#property-input)

*   Type: `HTMLElement`
*   Group: `data`

The main input field of the element.

### fieldId [​](https://vueform.com/reference/text-element#property-field-id)

*   Type: `string`
*   Group: `computed`

The `id` of the input field. If [`id`](https://vueform.com/reference/text-element#option-id) is not provided [`path`](https://vueform.com/reference/text-element#option-path) will be used.

### hasLabel [​](https://vueform.com/reference/text-element#property-has-label)

*   Type: `boolean`
*   Group: `computed`

Whether the element has a [`label`](https://vueform.com/reference/text-element#option-label) option, a [#label](https://vueform.com/reference/text-element#slot-label) slot or `Vueform` component's [`forceLabels`](https://vueform.com/reference/vueform#option-force-labels) option is `true`.

### hasFloating [​](https://vueform.com/reference/text-element#property-has-floating)

*   Type: `boolean`
*   Group: `computed`

Whether the element floating label.

### Size [​](https://vueform.com/reference/text-element#property-size)

*   Type: `string`
*   Group: `computed`

The resolved size of the element and all of its child components.

### View [​](https://vueform.com/reference/text-element#property-view)

*   Type: `string`
*   Group: `computed`

The name of the resolved view for the component and the default view for its child components. Child component views can be overridden with [`views`](https://vueform.com/reference/text-element#option-views) option. This one should be used to determine the component's view in class functions.

### template [​](https://vueform.com/reference/text-element#property-template)

*   Type: `object`
*   Group: `computed`

The component's template.

### classes [​](https://vueform.com/reference/text-element#property-classes)

*   Type: `object`
*   Group: `computed`

The component's classes.

### theme [​](https://vueform.com/reference/text-element#property-theme)

*   Type: `object`
*   Group: `inject`

The global theme object, which contains all the default templates and classes.

### form$ [​](https://vueform.com/reference/text-element#property-form_)

*   Type: `Vueform`
*   Group: `inject`

The root form's component.

### el$ [​](https://vueform.com/reference/text-element#property-el_)

*   Type: `VueformElement`
*   Group: `computed`

The element's component.

### mounted [​](https://vueform.com/reference/text-element#property-mounted)

*   Type: `boolean`
*   Default: `true`
*   Group: `data`

Whether the element has been already mounted.

Methods [​](https://vueform.com/reference/text-element#methods)
---------------------------------------------------------------

The `methods` of the component that you can use by reaching the element's Vue component instance via [`form$`](https://vueform.com/reference/text-element#property-form)'s [`el$(path)`](https://vueform.com/reference/vueform#method-el) method or directly via `this` in options API or [`el$`](https://vueform.com/reference/text-element#property-el) in Composition API.

### clearMessages [​](https://vueform.com/reference/text-element#method-clear-messages)

*   Returns: `void`

Clears the manually added messages from the [`messageBag`](https://vueform.com/reference/text-element#property-message-bag).

### load [​](https://vueform.com/reference/text-element#method-load)

*   Arguments: 
    *   `{any} value*` - the value to be loaded
    *   `{boolean} format*` - whether the loaded value should be formatted with [`formatLoad`](https://vueform.com/reference/text-element#option-format-load) before setting the value of the element (default: `false`)

*   Returns: `void`

Loads value to the element using optional [`formatLoad`](https://vueform.com/reference/text-element#option-format-load) formatter. This is the method that gets called for each element when loading data to the form with `format: true`.

### update [​](https://vueform.com/reference/text-element#method-update)

*   Arguments: 
    *   `{any} value*` - the value to be set

*   Returns: `void`

Updates the value of the element similarly to [`load`](https://vueform.com/reference/text-element#method-load), only that it can't format data.

### clear [​](https://vueform.com/reference/text-element#method-clear)

*   Returns: `void`

Clears the element's value.

### reset [​](https://vueform.com/reference/text-element#method-reset)

*   Returns: `void`

Resets the element's value to [`default`](https://vueform.com/reference/text-element#option-default) (or empty if `default` is not provided). Also resets all the validation state for the element.

### disable [​](https://vueform.com/reference/text-element#method-disable)

*   Returns: `void`

Disables the element.

### enable [​](https://vueform.com/reference/text-element#method-enable)

*   Returns: `void`

Enables the element even if it is disabled by [`disabled`](https://vueform.com/reference/text-element#disabled) option.

### on [​](https://vueform.com/reference/text-element#method-on)

*   Arguments: 
    *   `{string} event*` - name of the event to listen for
    *   `{function} callback*` - callback to run when the event is triggered

*   Returns: `void`

Adds a listener for an event.

### off [​](https://vueform.com/reference/text-element#method-off)

*   Arguments: 
    *   `{string} event*` - name of the event to remove

*   Returns: `void`

Removes all listeners for an event.

### fire [​](https://vueform.com/reference/text-element#method-fire)

*   Arguments: 
    *   `{any} args*` - list of arguments to pass over to the event callback

*   Returns: `void`

Fires and emits an event.

### validate [​](https://vueform.com/reference/text-element#method-validate)

*   Returns: `Promise`

Checks each validation rule for the element (async).

### clean [​](https://vueform.com/reference/text-element#method-clean)

*   Returns: `void`

Removes the element's `dirty` state.

### resetValidators [​](https://vueform.com/reference/text-element#method-reset-validators)

*   Returns: `void`

Sets the validators to default state.

### reinitValidation [​](https://vueform.com/reference/text-element#method-reinit-validation)

*   Returns: `void`

Re-initializes validators when rules have changed.

### hide [​](https://vueform.com/reference/text-element#method-hide)

*   Returns: `void`

Hides the element.

### show [​](https://vueform.com/reference/text-element#method-show)

*   Returns: `void`

Shows the element if it was hidden with [`hide()`](https://vueform.com/reference/text-element#method-hide) method.

Events [​](https://vueform.com/reference/text-element#events)
-------------------------------------------------------------

With events you can subscribe to different events broadcasted by the element. It can be used inline as regular Vue event listeners with `@event` format. In [`schema`](https://vueform.com/reference/vueform#option-schema) it can be used in PascalCase format prefixed with `on` (eg. `onChange`).

Inline  Schema

vue

```
<template>
  <Vueform>
    <TextElement @{eventName}="handler" ... />
  </Vueform>
</template>
```

vue

```
<script>
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      schema: {
        element: {
          type: 'text',
          on{EventName}() {
            // ...
          }
        }
      }
    }
  })
}
</script>
```

You can also use [`on(event, callback)`](https://vueform.com/reference/text-element#method-on) method to subscribe to events.

### reset [​](https://vueform.com/reference/text-element#event-reset)

*   Params: 
    *   `{component} el$` - the element's component

Triggered when the input is resetted.

### clear [​](https://vueform.com/reference/text-element#event-clear)

*   Params: 
    *   `{component} el$` - the element's component

Triggered when the input is cleared.

### change [​](https://vueform.com/reference/text-element#event-change)

*   Params: 
    *   `{string} newValue` - the new value
    *   `{string} oldValue` - the old value
    *   `{component} el$` - the element's component

Triggered when the element's value is changed.

### blur [​](https://vueform.com/reference/text-element#event-blur)

*   Params: 
    *   `{component} el$` - the element's component

Triggered when the input is blurred.

### focus [​](https://vueform.com/reference/text-element#event-focus)

*   Params: 
    *   `{component} el$` - the element's component

Triggered when the input is focused.

### keydown [​](https://vueform.com/reference/text-element#event-keydown)

*   Params: 
    *   `{Event} Event` - the Event object
    *   `{component} el$` - the element's component

Triggered on keydown.

### keyup [​](https://vueform.com/reference/text-element#event-keyup)

*   Params: 
    *   `{Event} Event` - the Event object
    *   `{component} el$` - the element's component

Triggered on keyup.

### keypress [​](https://vueform.com/reference/text-element#event-keypress)

*   Params: 
    *   `{Event} Event` - the Event object
    *   `{component} el$` - the element's component

Triggered on keypress.

### beforeCreate [​](https://vueform.com/reference/text-element#event-before-create)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in beforeCreate hook.

### created [​](https://vueform.com/reference/text-element#event-created)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in created hook.

### beforeMount [​](https://vueform.com/reference/text-element#event-before-mount)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in beforeMount hook.

### mounted [​](https://vueform.com/reference/text-element#event-mounted)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in mounted hook.

### beforeUpdate [​](https://vueform.com/reference/text-element#event-before-update)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in beforeUpdate hook.

### updated [​](https://vueform.com/reference/text-element#event-updated)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in updated hook.

### beforeUnmount [​](https://vueform.com/reference/text-element#event-before-unmount)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in beforeUnmount (or beforeDestroy in Vue 2) hook.

### unmounted [​](https://vueform.com/reference/text-element#event-unmounted)

*   Params: 
    *   `{component} el$` - the element's component

Triggered in unmounted (or destroyed in Vue 2) hook.

Slots [​](https://vueform.com/reference/text-element#slots)
-----------------------------------------------------------

Slots can be used inline or in [`slots`](https://vueform.com/reference/text-element#option-slots) option object when used in [`schema`](https://vueform.com/reference/vueform#option-schema):

Inline  Schema

vue

```
<template>
  <Vueform>
    <TextElement ... >
      <template #{slot-name}="scope">
        <!-- ... --->
      </template>
    </TextElement>
  </Vueform>
</template>
```

vue

```
<script>
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      schema: {
        element: {
          type: 'text',
          slots: {
            {slotName}: // implementation
          }
        }
      }
    }
  })
}
</script>
```

### label [​](https://vueform.com/reference/text-element#slot-label)

*   Scope: 
    *   `{component} el$` - the element's component

Renders a label for the element in [`ElementLabel`](https://vueform.com/reference/element-label) component.

### info [​](https://vueform.com/reference/text-element#slot-info)

*   Scope: 
    *   `{component} el$` - the element's component

Renders an info icon in [`ElementInfo`](https://vueform.com/reference/element-info) component next the the element label. When the icon is hovered it shows the content of this slot. The element needs to have a label to render this.

### required [​](https://vueform.com/reference/text-element#slot-required)

### description [​](https://vueform.com/reference/text-element#slot-description)

*   Scope: 
    *   `{component} el$` - the element's component

### before [​](https://vueform.com/reference/text-element#slot-before)

*   Scope: 
    *   `{component} el$` - the element's component

Renders an [`ElementText`](https://vueform.com/reference/element-text) component before the input field.

### between [​](https://vueform.com/reference/text-element#slot-between)

*   Scope: 
    *   `{component} el$` - the element's component

Renders an [`ElementText`](https://vueform.com/reference/element-text) component after the input field and before description.

### after [​](https://vueform.com/reference/text-element#slot-after)

*   Scope: 
    *   `{component} el$` - the element's component

Renders an [`ElementText`](https://vueform.com/reference/element-text) component after the description and error.

### addon-before [​](https://vueform.com/reference/text-element#slot-addon-before)

*   Scope: 
    *   `{component} el$` - the element's component

Prepends an addon to the input field.

### addon-after [​](https://vueform.com/reference/text-element#slot-addon-after)

*   Scope: 
    *   `{component} el$` - the element's component

Appends an addon to the input field.

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
