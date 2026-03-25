# Source: https://vueform.com/reference/vueform

Title: Vueform | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/reference/vueform

Markdown Content:
Renders the form.

Basic Usage [​](https://vueform.com/reference/vueform#basic-usage)
------------------------------------------------------------------

`<Vueform>` component can be used globally and serves as a container for elements and form components:

vue

```
<template>
  <Vueform size="lg">
    <StaticElement name="head">
      <h3>Login</h3>
    </StaticElement>
    <TextElement
      name="email"
      placeholder="Email"
      default="john@doe.com"
    />
    <TextElement
      name="password"
      input-type="password"
      placeholder="Password"
      default="********"
    />
    <ButtonElement name="submit" submits>
      Submit
    </ButtonElement>
  </Vueform>
</template>
```

Login

Email

Password

Configuration options can be passed over as regular component **props**. Check out [Options](https://vueform.com/reference/vueform#options) section for available configuration options.

Options [​](https://vueform.com/reference/vueform#options)
----------------------------------------------------------

Find below the list of options that can use to configure `Vueform` component. Options can be passed to the component via **props**.

### schema [​](https://vueform.com/reference/vueform#option-schema)

*   Type: `object`

vue

```
<Vueform :schema="{
  name: {
    type: 'text',
    label: 'Name',
    placeholder: 'Your name'
  },
  email: {
    type: 'text',
    label: 'Email',
    placeholder: 'Your work email'
  },
}" ... />
```

This option can be used to define form elements in an object instead of inline templates. This method also allows storing form elements in JSON objects that can be stored in databases.

The object keys are the `name`s of the elements while the values define the element options (same as props in inline templates).

Elements defined in `schema` will be rendered in [`FormElements`](https://vueform.com/reference/form-elements) component within the form which serves as a wrapper.

### tabs [​](https://vueform.com/reference/vueform#option-tabs)

*   Type: `object`

vue

```
<Vueform
  :tabs="{
    profile: {
      label: 'Profile',
      elements: ['name', 'email', 'bio'],
    },
    gallery: {
      label: 'Gallery',
      elements: ['images'],
    },
  }"
  :schema="{
    name: { ... },
    email: { ... },
    bio: { ... },
    images: { ... },
  }"
/>
```

Similarly to [`schema`](https://vueform.com/reference/vueform#option-schema) and [`steps`](https://vueform.com/reference/vueform#option-steps) this option can be used to define form tabs in an object instead of inline templates.

The object keys are the `name` of the tabs while the values contain the tab [options](https://vueform.com/reference/form-tab#options) (same as props in inline templates).

Tabs are rendered in [`FormTabs`](https://vueform.com/reference/form-tabs) component with a [`FormTab`](https://vueform.com/reference/form-tab) component for each.

### steps [​](https://vueform.com/reference/vueform#option-steps)

*   Type: `object`

vue

```
<Vueform
  :steps="{
    profile: {
      label: 'Profile',
      elements: ['name', 'bio'],
    },
    contact: {
      label: 'Contact',
      elements: ['email', 'phone'],
    },
    gallery: {
      label: 'Gallery',
      elements: ['images'],
    },
  }"
  :schema="{
    name: { ... },
    bio: { ... },
    email: { ... },
    phone: { ... },
    images: { ... },
  }"
/>
```

Similarly to [`schema`](https://vueform.com/reference/vueform#option-schema) and [`steps`](https://vueform.com/reference/vueform#option-steps) this option can be used to define form steps in an object instead of inline templates.

The object keys are the `name` of the steps while the values contain the step [options](https://vueform.com/reference/form-step#options) (same as props in inline templates).

Steps are rendered in [`FormSteps`](https://vueform.com/reference/form-steps) component with a [`FormStep`](https://vueform.com/reference/form-step) component for each.

### stepsControls [​](https://vueform.com/reference/vueform#option-steps-controls)

*   Type: `boolean`
*   Default: `true`

vue

`<Vueform :steps-controls="false" ... />`

Whether [`FormStepsControls`](https://vueform.com/reference/form-steps-controls) component should be displayed when [`steps`](https://vueform.com/reference/vueform#option-steps) are defined.

### scrollOnNext [​](https://vueform.com/reference/vueform#option-scroll-on-next)

*   Type: `boolean`

vue

`<Vueform :scroll-on-next="false" ... />`

Whether to scroll to the top of the form on hitting **Next** button when using [steps](https://vueform.com/docs/breaking-forms-into-steps#using-form-steps).

Can also be set on [config](https://vueform.com/docs/configuration#scrollonnext) level.

### validateOn [​](https://vueform.com/reference/vueform#option-validate-on)

*   Type: `string`

vue

`<Vueform validate-on="change|step" ... />`

Determines when the form should trigger validation. Values must be concatenated with `|`. Possible values: `change` and `step`.

If `change` is present, an element will be validated when its value is changed.

If `step` is present, all the elements within a step will be validated when the user tries to navigate to the next step using the Next form step control.

The form always validates unvalidated elements before submitting data to the server.

### scrollToInvalid [​](https://vueform.com/reference/vueform#option-scroll-to-invalid)

*   Type: `boolean`

vue

`<Vueform :scroll-to-invalid="false" ... />`

Whether to scroll to the first invalid element when the form gets submitted.

Can also be set on [config](https://vueform.com/docs/configuration#scrolltoinvalid) level.

### showRequired [​](https://vueform.com/reference/vueform#option-show-required)

*   Type: `array`

vue

`<Vueform rules="required" :show-required="['label', 'placeholder', 'floating']" ... />`

The list of element assets where an asterisk `*` should be shown if the element has `required` validation rule. The possible items are `label`, `placeholder` and `floating`.

Can also be set on [config](https://vueform.com/docs/configuration#showrequired) level.

### displayErrors [​](https://vueform.com/reference/vueform#option-display-errors)

*   Type: `boolean`

vue

`<Vueform :display-errors="false" ... />`

Whether error messages from [`messageBag`](https://vueform.com/reference/vueform#property-message-bag) should be displayed above the form in [`FormErrors`](https://vueform.com/reference/form-errors) component.

### displayMessages [​](https://vueform.com/reference/vueform#option-display-messages)

*   Type: `boolean`

vue

`<Vueform :display-errors="false" ... />`

Whether messages from [`messageBag`](https://vueform.com/reference/vueform#property-message-bag) should be displayed above the form in [`FormMessages`](https://vueform.com/reference/form-messages) component.

### messages [​](https://vueform.com/reference/vueform#option-messages)

*   Type: `object`

vue

`<Vueform :messages="{ required: 'Please fill in' }" ... />`

Overrides the default messages for each elements' validation rules within the form. The value is an `object` where each key is a name of a validation rule and the value is the error message that will be displayed when the rule fails.

> You can override validation messages on element level with `messages`.

### endpoint [​](https://vueform.com/reference/vueform#option-endpoint)

*   Type: `string|boolean|function|promise`

vue

`<Vueform endpoint="/user/create" ... />`

The endpoint where the form should be submitted on [`submit()`](https://vueform.com/reference/vueform#method-submit).

It can also be a named endpoint, referencing an endpoint in [`vueform.config.js`](https://vueform.com/reference/configuration#endpoints):

js

```
// vueform.config.js

export default {
  endpoints: {
    create_user: {
      url: '/users',
      method: 'post'
    }
  }
}
```

vue

```
<!-- Using a named endpoint -->
<Vueform endpoint="create_user" ... />
```

If set to `false` submitting to endpoint will be disabled and it can be handled manually on [`@submit`](https://vueform.com/reference/vueform#event-submit) event:

vue

```
<!-- Disabling endpoint -->
<Vueform :endpoint="false" ... />
```

Alternatively, it can be an `async function` that receives [`formData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) and [`form$`](https://vueform.com/reference/vueform#property-form_) params and handles the submit:

vue

```
<!-- Using a function to upload file -->
<Vueform :endpoint="async function(FormData, form$){
  const formData = FormData // FormData instance
  const data = form$.data // form data including conditional data
  const requestData = form$.requestData // form data excluding conditional data

  // handle form submission
}" ... />
```

### method [​](https://vueform.com/reference/vueform#option-method)

*   Type: `string`

vue

`<Vueform method="POST" ... />`

The request method that should be used to send data on [`submit()`](https://vueform.com/reference/vueform#method-submit).

### prepare [​](https://vueform.com/reference/vueform#option-prepare)

*   Type: `function`

vue

```
<Vueform :prepare="async (form$) => {
  try {
    // async request
  } catch (error) {
    throw error // cancels form submit
  }
}" ... />
```

An `async function` that is called before data is submitted to the server. It receives [`form$`](https://vueform.com/reference/vueform#property-form) as its form param which is the Vue component instance of the form. It can cancel the submit process by throwing an error.

### formKey [​](https://vueform.com/reference/vueform#option-form-key)

*   Type: `string|number`

vue

`<Vueform form-key="nE8e4wY5mcn5q1nTNakf" ... />`

A unique key that is sent to the backend along with form data on [`submit()`](https://vueform.com/reference/vueform#method-submit). Its primary purpose is to help identify a form if you are using a single endpoint to process all your forms.

### formData [​](https://vueform.com/reference/vueform#option-form-data)

*   Type: `function`

vue

`<Vueform :form-data="form$ => form$.convertFormData(form$.requestData)"... />`

This function can be used to choose which one of the form's data set should be sent to the server on [`submit()`](https://vueform.com/reference/vueform#method-submit). The form has two different objects that contain form data:

*   [`data`](https://vueform.com/reference/vueform#property-data) - contains the full form data, including data from elements which conditions aren't met or submit is disabled for them
*   [`requestData`](https://vueform.com/reference/vueform#property-request-data) - contains only form data from elements which conditions are met and submit is not disabled for them (this is the default).

The function receives a `form$` prop, which is the Vue component instance of the form and expects to return the form data that should be submitted to the server on [`submit()`](https://vueform.com/reference/vueform#method-submit).

The [`convertFormData()`](https://vueform.com/reference/vueform#method-convert-form-data) method converts the data object to [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData). This might be left out if you don't want to send `multipart/form-data` request.

### value [​](https://vueform.com/reference/vueform#option-value)

*   Type: `object`

vue

`<Vueform v-model="data" ... /> <!-- same as :value="data" @input="data = $event.target.value" -->`

This property allows you to store the form data in an external object (similarly to regular inputs) and used by `v-model`**Vue 2**.

The `v-model` directive [does two things](https://vuejs.org/v2/guide/forms.html#Basic-Usage) in **Vue 2**:

*   assigns `:value` prop to the component
*   listens to the `@input` event of the component and updates the value when emitted.

If you want to use it, you either have to define a `v-model` or `:value` prop and listening to [`@input`](https://vueform.com/reference/vueform#event-input) event as well.

By default the form stores its data internally so you don't have to provide `:value` or `v-model`, unless you want to.

> **IMPORTANT:** contrary to regular `v-model`, two-way data binding is optional in Vueform and have to be manually enabled using [`sync`](https://vueform.com/reference/vueform#option-sync) option.

### modelValue [​](https://vueform.com/reference/vueform#option-model-value)

*   Type: `object`

vue

`<Vueform v-model="data" ... /> <!-- same as :model-value="data" @update:model-value="data = $event" -->`

The same as [`value`](https://vueform.com/reference/vueform#option-value) option except that `modelValue` should be used with `@update:model-value` event instead of `value`&`@input` in **Vue 3**.

### sync [​](https://vueform.com/reference/vueform#option-sync)

*   Type: `boolean`

vue

`<Vueform v-model="data" :sync="true" ... />`

Two-way data binding is optional in Vueform and can be enabled with this option.

When `sync: true` the `v-model` object will be updated when the form data is changed (eg. by user input) and direct changes made to the object outside of Vueform will also be reflected in the form.

If `sync: false` the `v-model` object will be still updated when the form data is changed (eg. by user input) but direct changes made to it outside of Vueform will not be reflected in the form.

> When using a lot elements or deeply nested elements the performance can be affected if `sync` is enabled. Make sure to only use `sync` if you actually need two-way data binding.

### default [​](https://vueform.com/reference/vueform#option-default)

*   Type: `object`

template

```
<Vueform :default="{ name: 'John Doe', email: 'john@doe.com' }" ...>
  <TextElement name="name" />
  <TextElement name="email" />
</Vueform>
```

Sets the default data for the form.

### forceNumbers [​](https://vueform.com/reference/vueform#option-force-numbers)

*   Type: `boolean`

html

```
<!-- Form `data` & `requestData` will be string -->
<Vueform>
  <TextElement default="123" />
  <TextElement default="123.456" />
  <TextElement default="123,456" />
</Vueform>

<!-- Form `data` & `requestData` will be number -->
<Vueform force-numbers>
  <TextElement default="123" />
  <TextElement default="123.456" />
  <TextElement default="123,456" />
  <TextElement default="123a" />
</Vueform>
```

Whether text input values should be transformed to a `number` in form [`data`](https://vueform.com/reference/vueform#property-data) and [`requestData`](https://vueform.com/reference/vueform#property-request-data). If the input value contains any non-numeric character (except for `.` and `,`) it will be kept as `string`.

It can be also set on [element level](https://vueform.com/reference/text-element#option-force-numbers) or [config level](https://vueform.com/docs/configuration#forcenumbers).

### formatData [​](https://vueform.com/reference/vueform#option-format-data)

*   Type: `function`

vue

`<Vueform :format-data="(requestData) => ({ /* transformed value */ })" ... />`

Formats the form's [`requestData`](https://vueform.com/reference/vueform#property-request-data) before submitting it to the server.

It receives the original `requestData` as its first param and expects to have a `return` with converted/transformed form data.

This value will only be used when the form is submitted and it does not affect the form's actual [`data`](https://vueform.com/reference/vueform#property-data).

### formatLoad [​](https://vueform.com/reference/vueform#option-format-load)

*   Type: `function`

vue

`<Vueform :format-load="(data) => /* transformed value */" ... />`

Formats the data being loaded to the form with [`load(data, format: true)`](https://vueform.com/reference/vueform#method-load). It receives `data` as its first param which is the original data being loaded. It expects to return a transformed/converted data that will be loaded to elements.

### loading [​](https://vueform.com/reference/vueform#option-loading)

*   Type: `boolean`

vue

`<Vueform :loading="true" ... />`

Manually triggers the loading state of the form. When the form is in loading state it cannot be submitted and submit button will display a loader while becoming disabled.

### disabled [​](https://vueform.com/reference/vueform#option-disabled)

*   Type: `boolean|function|object|array`

vue

```
<Vueform :disabled="true" ... />
<VueformElement :disabled="prop" ... /> <!-- computed / data (ref) prop -->
<VueformElement :disabled="[['text', 'value']]" ... /> <!-- conditional -->
<VueformElement :disabled="(form$) => { return /* boolean */ }" ... />
```

Prevents the form from being submitted.

If can be a `boolean` value.

It can be a computed / data (ref) prop.

It can be an `array` of [conditions](https://vueform.com/docs/conditional-rendering#element-conditions). When all conditions are met the form submission will be disabled.

It can be a function that receives the [`form$`](https://vueform.com/reference/vueform#property-form_) form instance param and expected to return a `boolean`.

### columns [​](https://vueform.com/reference/vueform#option-columns)

*   Type: `object`

template

```
<Vueform :columns="{ container: 12, label: 3, wrapper: 12 }" ...>
  <TextElement label="Label" ... />
</Vueform>
```

Sets the size of the `container`, `label` and `wrapper` of **each element in the form** using the theme's grid system, where the:

*   `container` is the outermost DOM that contains both `label` and `wrapper`
*   `label` contains the label
*   `wrapper` contains the element.

`container: 12`

`label: 3`

`wrapper: 12`

The value of `container` defines the size of the element's container. `12` will result in full width, `6` in half, `4` in third and so on.

The value of `label` defines the amount of space the label should take up **within the container**. If the `container` is `12` and `label` is `6` the label is going to take up half the space and the element's wrapper will the other half (which is calculated automatically). If the `container` is `6` and `label` is `6`, the label will only take up one forth and the element's wrapper the rest. In case the `label` has full width (`12`) the element's wrapper will also take up **full space** instead of becoming zero.

The value of `wrapper` defines the size of the element's wrapper **within the space left for it in the container after subtracting the size of the label**. If the `container` is `12` and `label` is `4` the space left for the element's wrapper is `8`. In this case if the `wrapper` value is `12` it will take up the full space left for the it (which is `8`) while if it is changed to `6` it will only take up half the space left for it (`4`):

template

```
<Vueform :columns="{ container: 12, label: 4, wrapper: 12 }" ...>
  <TextElement label="Label" ... />
</Vueform>

<Vueform :columns="{ container: 12, label: 4, wrapper: 6 }" ...>
  <TextElement label="Label" ... />
</Vueform>
```

Note that while the size of the element's wrapper container changes the size of other _extras_ like a description or error won't be limited to the wrapper's space. Instead it will take up the full space in the container left after subtracting the size of the label:

template

```
<Vueform :columns="{ container: 12, label: 4, wrapper: 6 }" ...>
  <TextElement
    label="Label"
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    ...
  />
</Vueform>
```

You can set the value of `columns` as a `number` which case the `container` will receive its value without affecting the default settings of `label` and `wrapper`:

template

```
<Vueform :columns="6" ... > <!-- { container: 6, label: 3, wrapper: 12 } -->
  <TextElement label="Label" ... />
</Vueform>
```

You can as well define column values for different **breakpoints** using the theme system's breakpoints like `sm`, `md`, etc. as keys:

template

```
<Vueform :columns="{
  xs: { container: 12, label: 12, wrapper: 12 },
  sm: { container: 12, label: 4, wrapper: 12 },
  md: 12,
  lg: { container: 12, label: 2, wrapper: 12 }
}" ... >
  <TextElement label="Label" ... />
</Vueform>
```

> Column sizes can be defined globally in [`vueform.config.js`](https://vueform.com/reference/configuration#columns) or uniquely for each element using the element's `columns` option.

### forceLabels [​](https://vueform.com/reference/vueform#option-force-labels)

*   Type: `boolean`

vue

`<Vueform :force-labels="true" />`

Whether empty labels should be displayed for elements.

### floatPlaceholders [​](https://vueform.com/reference/vueform#option-float-placeholders)

*   Type: `boolean`

vue

`<Vueform :float-placeholders="true" />`

Whether floating labels should be automatically created from placeholders (unless they are explicitly defined).

### size [​](https://vueform.com/reference/vueform#option-size)

*   Type: `string`

template

```
<Vueform size="sm">
  <TextElement ... />
  <TextareaElement ... />
</Vueform>
```

The default size of the elements.

### view [​](https://vueform.com/reference/vueform#option-view)

*   Type: `string`

vue

`<Vueform view="alt" ... />`

The name of the view to be used for the component. If `undefined` the default view will be used. Child component default views can be set with [`views`](https://vueform.com/reference/vueform#option-views) option.

Learn more about views [here](https://vueform.com/docs/styles-and-layout#views).

### views [​](https://vueform.com/reference/vueform#option-views)

*   Type: `object`

vue

```
<Vueform :views="{
  ComponentName: 'alt'
}" ... />
```

The name of the default views for the child components.

Learn more about views [here](https://vueform.com/docs/styles-and-layout#views).

### addClasses [​](https://vueform.com/reference/vueform#option-add-classes)

*   Type: `object|function`

vue

```
<Vueform :add-classes="{
  ComponentName: {
    classname: 'class-value',
    classname: ['class-value'],
    classname: [{'class-value': true}],
  }
}" ... />
```

Adds classes to any component's class names. The classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :add-classes="(form$) => ({
  ComponentName: {
    classname: [
      { 'class-value': form$.el$('other_field')?.value === 'some_value' }
    ],
  }
})" ... />
```

Learn more about adding classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### addClass [​](https://vueform.com/reference/vueform#option-add-class)

*   Type: `array|object|string|function`

vue

```
<Vueform :add-class="{
  classname: 'class-value',
  classname: ['class-value'],
  classname: [{'class-value': true}],
}" ... />
```

Adds classes to any of `Vueform` component's class names. Classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :add-class="(form$) => ({
  classname: [
    { 'class-value': form$.el$('other_field')?.value === 'some_value' }
  ],
})" ... />
```

Learn more about adding classes [here](https://vueform.com/docs/styles-and-layout#add-classes).

### removeClasses [​](https://vueform.com/reference/vueform#option-remove-classes)

*   Type: `object|function`

vue

```
<Vueform :remove-classes="{
  ComponentName: {
    classname: ['class-value-1', 'class-value-2']
  }
}" ... />
```

Removes classes from any class names of any components. The classes to be removed must be listed in an `array`.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :remove-classes="(form$) => ({
  ComponentName: {
    classname: form$.el$('other_field')?.value === 'some_value'
      ? ['class-value-1', 'class-value-2']
      : [],
  }
})" ... />
```

Learn more about removing classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### removeClass [​](https://vueform.com/reference/vueform#option-remove-class)

*   Type: `array|object|function`

vue

```
<Vueform :remove-class="{
  classname: ['class-value-1', 'class-value-2']
}" ... />
```

Removes classes from any of `Vueform` component's class names. The classes to be removed must be listed in an `array`.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :remove-class="(form$) => ({
  classname: form$.el$('other_field')?.value === 'some_value'
    ? ['class-value-1', 'class-value-2']
    : [],
})" ... />
```

Learn more about removing classes [here](https://vueform.com/docs/styles-and-layout#remove-classes).

### replaceClasses [​](https://vueform.com/reference/vueform#option-replace-classes)

*   Type: `object|function`

vue

```
<Vueform :replace-classes="{
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

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :replace-classes="(form$) => ({
  ComponentName: {
    classname: form$.el$('other_field')?.value === 'some_value' ? {
      'from-class': 'to-class'
    } : {},
  }
})" ... />
```

Learn more about replacing classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### replaceClass [​](https://vueform.com/reference/vueform#option-replace-class)

*   Type: `object|function`

vue

```
<VueformElement :replace-class="{
  classname: {
    'from-class': 'to-class',
    'from-class': ['to-class'],
    'from-class': [{'to-class': true}],
  }
}" ... />
```

Replaces the classes of any class names of `Vueform` component. The keys are the original class names and the values are the replacements. The keys can only be single classes, while values can contain multiple ones in `string` or an `array`. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :replace-class="(form$) => ({
  classname: form$.el$('other_field')?.value === 'some_value' ? {
    'from-class': 'to-class'
  } : {},
})" ... />
```

Learn more about replacing classes [here](https://vueform.com/docs/styles-and-layout#replace-classes).

### overrideClasses [​](https://vueform.com/reference/vueform#option-override-classes)

*   Type: `object|function`

vue

```
<Vueform :override-classes="{
  ComponentName: {
    classname: 'class-value',
    classname: ['class-value'],
    classname: [{'class-value': true}],
  }
}" ... />
```

Overrides the classes of any component's class names. The classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :override-classes="(form$) => ({
  ComponentName: form$.el$('other_field')?.value === 'some_value' ? {
    classname: 'class-value'
  } : {}
})" ... />
```

Learn more about overriding classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### overrideClass [​](https://vueform.com/reference/vueform#option-override-class)

*   Type: `array|object|string|function`

vue

```
<Vueform :override-classes="{
  ComponentName: {
    classname: 'class-value',
    classname: ['class-value'],
    classname: [{'class-value': true}],
  }
}" ... />
```

Overrides the classes of any of `Vueform` component's class names. The classes can have `string` or `array` values. When [Vue style classes](https://v3.vuejs.org/guide/class-and-style.html#binding-html-classes) are used `object` values must be wrapped in an array.

Conditional classes can be passed as a `function` with [`form$`](https://vueform.com/reference/vueform#property-form) param, eg.:

vue

```
<Vueform :override-class="(form$) => (form$.el$('other_field')?.value === 'some_value' ? {
  classname: 'class-value'
} : {})" ... />
```

Learn more about overriding classes [here](https://vueform.com/docs/styles-and-layout#override-classes).

### templates [​](https://vueform.com/reference/vueform#option-templates)

*   Type: `object`

vue

```
<template>
  <div id="app">
    <Vueform :templates="{ ElementError }">
      <Textlement ... />
      <Textarealement ... />
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

Overrides the default templates used within the form.

Learn more about overriding templates [here](https://vueform.com/docs/styles-and-layout#templates).

### presets [​](https://vueform.com/reference/vueform#option-presets)

*   Type: `array`

vue

`<Vueform :presets="['preset1', 'preset2']" ... />`

The presets to be applied on a form level.

Learn more about presets classes [here](https://vueform.com/docs/styles-and-layout#presets).

### multilingual [​](https://vueform.com/reference/vueform#option-multilingual)

*   Type: `boolean`

template

```
<Vueform :multilingual="true" ...>
  <TTextElement name="title" placeholder="Title">
</Vueform>
```

Whether a language selector for multilingual elements (eg. [`TTextElement`](https://vueform.com/reference/t-text-element) or [`TTextareaElement`](https://vueform.com/reference/t-textarea-element)) should be displayed above the form.

### languages [​](https://vueform.com/reference/vueform#option-languages)

*   Type: `object`

vue

```
<Vueform :languages="{
  en: 'English',
  zh: 'Chinese',
}" />
```

The object of available languages when using [`multilingual: true`](https://vueform.com/reference/vueform#option-multilingual). If not defined and [`multilingual`](https://vueform.com/reference/vueform#option-multilingual) is used the default `languages` will be used from [`vueform.config.js`](https://vueform.com/reference/configuration#languages).

### language [​](https://vueform.com/reference/vueform#option-language)

*   Type: `string`

vue

`<Vueform language="zh" ... />`

The default language that should be selected when using [`multilingual: true`](https://vueform.com/reference/vueform#option-multilingual).

### locale [​](https://vueform.com/reference/vueform#option-locale)

*   Type: `string`

vue

`<Vueform locale="zh" ... />`

Overrides the global [`locale`](https://vueform.com/reference/configuration#locale) for this form only.

### providers [​](https://vueform.com/reference/vueform#option-providers)

*   Type: `object`

### useProviders [​](https://vueform.com/reference/vueform#option-use-providers)

*   Type: `object`

### providerOptions [​](https://vueform.com/reference/vueform#option-provider-options)

*   Type: `object`

Properties [​](https://vueform.com/reference/vueform#properties)
----------------------------------------------------------------

All the `data`, `computed` and `inject` properties of the component.

### validation [​](https://vueform.com/reference/vueform#property-validation)

*   Type: `boolean`
*   Default: `true`
*   Group: `data`

Enables/disables validation for the form globally.

### conditions [​](https://vueform.com/reference/vueform#property-conditions)

*   Type: `boolean`
*   Default: `true`
*   Group: `data`

Enables/disables conditions for the form globally.

### selectedLanguage [​](https://vueform.com/reference/vueform#property-selected-language)

*   Type: `string`
*   Default: `config.language`
*   Group: `data`

The code of the currently selected language (eg. `en`).

### submitting [​](https://vueform.com/reference/vueform#property-submitting)

*   Type: `boolean`
*   Default: `false`
*   Group: `data`

Whether the async process of submitting the form is currently in progress.

### cancelToken [​](https://vueform.com/reference/vueform#property-cancel-token)

*   Type: `boolean`
*   Default: `false`
*   Group: `data`

The axios cancel token when a request is in progress.

### formErrors [​](https://vueform.com/reference/vueform#property-form-errors)

*   Type: `array`
*   Group: `computed`

Form errors including element errors and the ones added to [`messageBag`](https://vueform.com/reference/vueform#property-message-bag) manually.

### formMessages [​](https://vueform.com/reference/vueform#property-form-messages)

*   Type: `array`
*   Group: `computed`

Form messages including element messages and the ones added to [`messageBag`](https://vueform.com/reference/vueform#property-message-bag) manually.

### hasTabs [​](https://vueform.com/reference/vueform#property-has-tabs)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any tabs.

### hasErrors [​](https://vueform.com/reference/vueform#property-has-errors)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any errors.

### hasMessages [​](https://vueform.com/reference/vueform#property-has-messages)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any messages.

### isMultilingual [​](https://vueform.com/reference/vueform#property-is-multilingual)

*   Type: `boolean`
*   Group: `computed`

Whether the form is multilingual and should show [`FormLanguages`](https://vueform.com/reference/form-languages) component. Returns `true` if [`multilingual`](https://vueform.com/reference/vueform#option-multilingual) is enabled.

### showErrors [​](https://vueform.com/reference/vueform#property-show-errors)

*   Type: `boolean`
*   Group: `computed`

Whether the form should display errors above the form with [`FormErrors`](https://vueform.com/reference/form-errors) component. Can be disabled by [`displayErrors`](https://vueform.com/reference/vueform#option-display-errors) or in `config.displayErrors`.

### showMessages [​](https://vueform.com/reference/vueform#property-show-messages)

*   Type: `boolean`
*   Group: `computed`

Whether the form should display messages above the form with [`FormMessages`](https://vueform.com/reference/form-messages) component. Can be disabled by [`displayMessages`](https://vueform.com/reference/vueform#option-display-messages) or in `config.displayMessages`.

### showLanguages [​](https://vueform.com/reference/vueform#property-show-languages)

*   Type: `boolean`
*   Group: `computed`

Whether the form should show langauge selectors.

### showSteps [​](https://vueform.com/reference/vueform#property-show-steps)

*   Type: `boolean`
*   Group: `computed`

Whether the form should show [`FormSteps`](https://vueform.com/reference/form-steps) component. Returns `true` if [`steps`](https://vueform.com/reference/vueform#option-steps) has value.

### showTabs [​](https://vueform.com/reference/vueform#property-show-tabs)

*   Type: `boolean`
*   Group: `computed`

Whether the form should show [`FormTabs`](https://vueform.com/reference/form-tabs) component. Returns `true` if [`tabs`](https://vueform.com/reference/vueform#option-tabs) has value.

### showStepsControls [​](https://vueform.com/reference/vueform#property-show-steps-controls)

*   Type: `boolean`
*   Group: `computed`

Whether the form should display steps controls below form with [`FormStepsControls`](https://vueform.com/reference/form-steps-control) component when it has [`steps`](https://vueform.com/reference/vueform#option-steps). Can be disabled with [`stepsControls`](https://vueform.com/reference/vueform#option-steps-controls).

### extendedTheme [​](https://vueform.com/reference/vueform#property-extended-theme)

*   Type: `object`
*   Group: `computed`

The selected theme, extended by local template and class overrides, using [`templates`](https://vueform.com/reference/vueform#option-replace-templates), [`addClasses`](https://vueform.com/reference/vueform#option-add-classes) and [`replaceClasses`](https://vueform.com/reference/vueform#option-replace-classes).

### tree [​](https://vueform.com/reference/vueform#property-tree)

*   Type: `array`
*   Group: `computed`

The tree representation of the form schema.

### flatTree [​](https://vueform.com/reference/vueform#property-flat-tree)

*   Type: `array`
*   Group: `computed`

The flat tree representation of the form schema.

### translations [​](https://vueform.com/reference/vueform#property-translations)

*   Type: `object`
*   Group: `computed`

The translation tags of the current locale.

### locale$ [​](https://vueform.com/reference/vueform#property-locale_)

*   Type: `string`
*   Group: `computed`

The active locale of the form.

### steps$ [​](https://vueform.com/reference/vueform#property-steps_)

*   Type: `FormSteps`
*   Group: `data`

### tabs$ [​](https://vueform.com/reference/vueform#property-tabs_)

*   Type: `FormTabs`
*   Group: `data`

### preparing [​](https://vueform.com/reference/vueform#property-preparing)

*   Type: `boolean`
*   Default: `false`
*   Group: `data`

Whether the async process of preparing the elements for submit is currently in progress.

### data [​](https://vueform.com/reference/vueform#property-data)

*   Type: `object`
*   Group: `computed`

The form data including the data of all elements even the ones with `available: false` and `submit: false`.

### requestData [​](https://vueform.com/reference/vueform#property-request-data)

*   Type: `object`
*   Group: `computed`

The form data excluding elements with `available: false` and `submit: false`. This one gets submitted by default, but can be changed with [`formData`](https://vueform.com/reference/vueform#option-form-data)

### validated [​](https://vueform.com/reference/vueform#property-validated)

*   Type: `boolean`
*   Group: `computed`

Whether each element in the form has been validated at least once.

### invalid [​](https://vueform.com/reference/vueform#property-invalid)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any invalid elements.

### dirty [​](https://vueform.com/reference/vueform#property-dirty)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any elements which were modified.

### pending [​](https://vueform.com/reference/vueform#property-pending)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any elements with pending async validation.

### debouncing [​](https://vueform.com/reference/vueform#property-debouncing)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any elements with active debounce process.

### busy [​](https://vueform.com/reference/vueform#property-busy)

*   Type: `boolean`
*   Group: `computed`

Whether the form has any elements with `busy: true` or the [`isLoading`](https://vueform.com/reference/vueform#property-is-loading), [`preparing`](https://vueform.com/reference/vueform#property-preparing) or [`submitting`](https://vueform.com/reference/vueform#property-submitting) property is `true`.

### messageBag [​](https://vueform.com/reference/vueform#property-message-bag)

*   Type: `MessageBag`
*   Default: `MessageBag`
*   Group: `data`

### isDisabled [​](https://vueform.com/reference/vueform#property-is-disabled)

*   Type: `boolean`
*   Group: `computed`

Whether submitting the form is disabled. Returns `true` if:\n* the form has any invalid elements and [`validateOn`](https://vueform.com/reference/vueform#option-validate-on) contains `change`\n* the form is [`busy`](https://vueform.com/reference/vueform#property-busy)\n* manually disabled with [`disabled`](https://vueform.com/reference/vueform#option-disabled) option.

### isLoading [​](https://vueform.com/reference/vueform#property-is-loading)

*   Type: `boolean`
*   Group: `computed`

Whether loading state is triggered manually via [`loading`](https://vueform.com/reference/vueform#option-loading) option.

### Size [​](https://vueform.com/reference/vueform#property-size)

*   Type: `string`
*   Group: `computed`

The resolved default size for each element and component within the form.

### View [​](https://vueform.com/reference/vueform#property-view)

*   Type: `string`
*   Group: `computed`

The name of the resolved view for Vueform component. This one should be used to determine the component's view in class functions.

### template [​](https://vueform.com/reference/vueform#property-template)

*   Type: `object`
*   Group: `computed`

The component's template.

### classes [​](https://vueform.com/reference/vueform#property-classes)

*   Type: `object`
*   Group: `computed`

The component's classes.

### form$ [​](https://vueform.com/reference/vueform#property-form_)

*   Type: `Vueform`
*   Group: `computed`

The form component instance (self).

Methods [​](https://vueform.com/reference/vueform#methods)
----------------------------------------------------------

The `methods` of the component.

### clearMessages [​](https://vueform.com/reference/vueform#method-clear-messages)

*   Returns: `void`

Clears the manually added messages from the form's and each element's `messageBag`.

### convertFormData [​](https://vueform.com/reference/vueform#method-convert-form-data)

*   Arguments: 
    *   `{object} data*` - the data to be converted

*   Returns: `FormData`

### resolveExpression [​](https://vueform.com/reference/vueform#method-resolve-expression)

*   Arguments: 
    *   `{string} exp*` - the expression to resolve
    *   `{string} dataPath*` - the dataPath of the element (required to resolve * in nested paths relative to the element)

*   Returns: `string`

Resolves an expression.

### send [​](https://vueform.com/reference/vueform#method-send)

*   Returns: `Promise`

Sends form data to [`endpoint`](https://vueform.com/reference/vueform#option-endpoint) with the selected [`method`](https://vueform.com/reference/vueform#option-method) (async).

### cancel [​](https://vueform.com/reference/vueform#method-cancel)

*   Returns: `void`

Cancels the form request in progress.

### disableValidation [​](https://vueform.com/reference/vueform#method-disable-validation)

*   Returns: `void`

Disabled form validation globally.

### enableValidation [​](https://vueform.com/reference/vueform#method-enable-validation)

*   Returns: `void`

Enables form validation globally.

### enableConditions [​](https://vueform.com/reference/vueform#method-enable-conditions)

*   Returns: `void`

Enables conditions globally.

### disableConditions [​](https://vueform.com/reference/vueform#method-disable-conditions)

*   Returns: `void`

Disables conditions globally.

### setLanguage [​](https://vueform.com/reference/vueform#method-set-language)

*   Arguments: 
    *   `{string} code*` - the language code to be selected

*   Returns: `void`

Sets current language when using [`multilingual`](https://vueform.com/reference/vueform#option-multilingual).

### handleSubmit [​](https://vueform.com/reference/vueform#method-handle-submit)

*   Returns: `void`

Handles `submit` event.

### el$ [​](https://vueform.com/reference/vueform#method-el_)

*   Arguments: 
    *   `{string} path*` - path of the element
    *   `{object} elements` - the object of elements to look into (defaults to elements$)

*   Returns: `VueformElement|null`

Returns an element by its path.

### siblings$ [​](https://vueform.com/reference/vueform#method-siblings_)

*   Arguments: 
    *   `{string} path*` - path of the element

*   Returns: `void`

Returns the siblings of an element.

### submit [​](https://vueform.com/reference/vueform#method-submit)

*   Returns: `Promise`

Validates and prepares elements then submits the form (async).

### load [​](https://vueform.com/reference/vueform#method-load)

*   Arguments: 
    *   `{string} value*` - the value to be loaded
    *   `{boolean} format` - whether the loaded value should be formatted with [`formatLoad`](https://vueform.com/reference/vueform#option-format-load) (default: `false`)

*   Returns: `Promise`

Loads data to the form using optional [`formatLoad`](https://vueform.com/reference/vueform#option-format-load) formatter.

### update [​](https://vueform.com/reference/vueform#method-update)

*   Arguments: 
    *   `{object} data*` - data to update with
    *   `{object} path` - the `path` of the element to update (default: `null`)

*   Returns: `void`

Updates the form data. Can be used to update a single element by providing the element's `path` as second option.

### clear [​](https://vueform.com/reference/vueform#method-clear)

*   Returns: `void`

Clears the forms data.

### reset [​](https://vueform.com/reference/vueform#method-reset)

*   Returns: `void`

Resets the form's data to default state. Also resets all the validation state for the elements.

### on [​](https://vueform.com/reference/vueform#method-on)

*   Arguments: 
    *   `{string} event*` - name of the event to listen for
    *   `{function} callback*` - callback to run when the event is triggered

*   Returns: `void`

Adds a listener for an event.

### off [​](https://vueform.com/reference/vueform#method-off)

*   Arguments: 
    *   `{string} event*` - name of the event to remove

*   Returns: `void`

Removes all listeners for an event.

### fire [​](https://vueform.com/reference/vueform#method-fire)

*   Arguments: 
    *   `{any} args` - list of arguments to pass over to the event callback

*   Returns: `void`

Fires and emits an event.

### validate [​](https://vueform.com/reference/vueform#method-validate)

*   Returns: `Promise`

Validates all elements (async) which weren't validated before. If [`validateOn`](https://vueform.com/reference/vueform#option-validate-on) does not contain `change` it will validate all elements on each call.

### clean [​](https://vueform.com/reference/vueform#method-clean)

*   Returns: `void`

Sets all elements' `dirty` to `false`.

### resetValidators [​](https://vueform.com/reference/vueform#method-reset-validators)

*   Returns: `void`

Sets all element validators to default state.

Events [​](https://vueform.com/reference/vueform#events)
--------------------------------------------------------

Events emitted by the component.

### change [​](https://vueform.com/reference/vueform#event-change)

*   Params: 
    *   `{string} newValue` - the new value
    *   `{string} oldValue` - the old value
    *   `{component} form$` - the form's component

Triggered when the forms data is changed.

### reset [​](https://vueform.com/reference/vueform#event-reset)

Triggered when the form is reseted using [`reset()`](https://vueform.com/reference/vueform#method-reset).

### clear [​](https://vueform.com/reference/vueform#event-clear)

Triggered when the form is cleared using [`clear()`](https://vueform.com/reference/vueform#method-clear).

### submit [​](https://vueform.com/reference/vueform#event-submit)

*   Params: 
    *   `{component} form$` - the form's component

Triggered when the form is being submitted, after validation is checked and elements are prepared.

### success [​](https://vueform.com/reference/vueform#event-success)

*   Params: 
    *   `{Response} response` - axios [Response](https://axios-http.com/docs/res_schema) object
    *   `{component} form$` - the form's component

Triggered when the server returns 2XX response after submitting the form.

### error [​](https://vueform.com/reference/vueform#event-error)

*   Params: 
    *   `{Error} error` - the Error object
    *   `{object} details` - additional information for the error, including `stage` property (`"prepare|submit"`) which indicates when the error was thrown.
    *   `{component} form$` - the form's component

Triggered when an error is thrown when preparing elements or submitting the form.

### response [​](https://vueform.com/reference/vueform#event-response)

*   Params: 
    *   `{Response} response` - axios [Response](https://axios-http.com/docs/res_schema) object
    *   `{component} form$` - the form's component

Triggered when the server returns a response after submitting the form.

### language [​](https://vueform.com/reference/vueform#event-language)

*   Params: 
    *   `{string} language` - the selected language

Triggered when a language is selected.

### beforeCreate [​](https://vueform.com/reference/vueform#event-before-create)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in beforeCreate hook.

### created [​](https://vueform.com/reference/vueform#event-created)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in created hook.

### beforeMount [​](https://vueform.com/reference/vueform#event-before-mount)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in beforeMount hook.

### mounted [​](https://vueform.com/reference/vueform#event-mounted)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in mounted hook.

### beforeUpdate [​](https://vueform.com/reference/vueform#event-before-update)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in beforeUpdate hook.

### updated [​](https://vueform.com/reference/vueform#event-updated)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in updated hook.

### beforeUnmount [​](https://vueform.com/reference/vueform#event-before-unmount)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in beforeUnmount (or beforeDestroy in Vue 2) hook.

### unmounted [​](https://vueform.com/reference/vueform#event-unmounted)

*   Params: 
    *   `{component} form$` - the form's component

Triggered in unmounted (or destroyed in Vue 2) hook.

Slots [​](https://vueform.com/reference/vueform#slots)
------------------------------------------------------

The slots of the component.

### default [​](https://vueform.com/reference/vueform#slot-default)

Can be used to render elements. When using `default` slot other form components (like [`FormSteps`](https://vueform.com/reference/form-steps) or [`FormErrors`](https://vueform.com/reference/form-errors)) are automatically added to the form and elements are rendered in [`FormElements`](https://vueform.com/reference/form-elements) component. If you want to use inline form components (eg. [`FormSteps`](https://vueform.com/reference/form-steps)) [`#empty`](https://vueform.com/reference/vueform#slots-empty) slot should be used.

vue

```
<Vueform>
  <TextElement name="name" ... />
  <TextareaElement name="bio" ... />
</Vueform>
```

### empty [​](https://vueform.com/reference/vueform#slot-empty)

Can be used to render form components. When using `empty` slot no form components are being added to the form. If you want to display form errors for example you need to add [`FormErrors`](https://vueform.com/reference/form-errors) component. Elements should be put into a [`FormElements`](https://vueform.com/reference/form-elements) component.

vue

```
<Vueform>
  <template #empty>
    <FormSteps>
      <!-- ... --->
    </FormSteps>
    <FormMessages v-if="showErrors" />
    <FormElements>
      <TextElement name="name" ... />
      <TextareaElement name="bio" ... />
    </FormElements>
  </template>
</Vueform>
```

Here's the default template for Vueform component:

vue

```
<!-- From: @vueform/vueform/themes/blank/templates/Vueform.vue -->

<template>
  <form
    :class="classes.form"
    @submit.prevent="submit"
  >
    <slot name="empty">
      <FormMessages v-if="showMessages"/>
      <FormErrors v-if="showErrors"/>
      <FormLanguages v-if="showLanguages"/>
      <FormTabs v-if="showTabs"/>
      <FormSteps v-if="showSteps"/>
      <FormElements><slot/></FormElements>
      <FormStepsControls v-if="showStepsControls"/>
    </slot>
  </form>
</template>
```

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
