# Source: https://vueform.com/docs/conditional-rendering

Title: Conditional rendering | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/conditional-rendering

Markdown Content:
Learn how to render almost any part of your forms conditionally.

Element Conditions [​](https://vueform.com/docs/conditional-rendering#element-conditions)
-----------------------------------------------------------------------------------------

We can pass an `array` to `:conditions` prop of any element:

template

```
<template>
  <Vueform>
    <CheckboxElement name="newsletter" text="Subscribe for newsletter" />
    <TextElement
      name="Email"
      placeholder="Email address"
      :conditions="[
        ['newsletter', '==', true]
      ]"
    >
  </Vueform>
</template>
```

If **any** of the conditions are failing the element will be **invisible**, its data will be **excluded** from [`requestData`](https://vueform.com/reference/vueform#property-request-data) and the element's `available` property will become `false`.

When a condition is provided as an `array`, the first value must be the `path` of an other element. The second is an operator that should define the type of comparison. The third is the expected value of the other field.

Available operators:

*   `==` - expect equality
*   `!=` - expect inequality
*   `>` - expect the other element's value(s) to be higher
*   `>=`- expect the other element's value(s) to be higher or equal
*   `<` - expect the other element's value(s) to be lower
*   `<=` - expect the other element's value(s) to be lower or equal
*   `between` - expect the other element's value(s) to be between two numbers (`[x, y]`)
*   `^` - expect the other element's value to start with
*   `$` - expect the other element's value to end with
*   `*` - expect the other element's value to contain
*   `in` - expect to be among an array of values
*   `not_in` - expect not to be among an array of values
*   `today` - expect to be today
*   `before` - expect to be before a date (value can be a `YYYY-MM-DD` date string or `today`)
*   `after` - expect to be after a date (value can be a `YYYY-MM-DD` date string or `today`)

If we are checking for equality we can leave the operator and pass the expected value as the second param:

vue

`<TextElement :conditions="[['newsletter', true]]" ...>`

The expected value can also be defined as an `array` in which case **any** of its values will fulfill the condition:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <TextElement name="phone" :conditions="[
    ['delivery', ['ups', 'fedex']]
  ]" ... />
</template>
```

### AND Conditions [​](https://vueform.com/docs/conditional-rendering#and-conditions)

When multiple conditions are applied they must all be fulfilled:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <CheckboxElement name="ask_call" text="Ask for a call" ... />

  <!-- `delivery` AND `ask_call` need to satisfy the condition -->
  <TextElement name="phone" :conditions="[
    ['delivery', ['ups', 'fedex']],
    ['ask_call', true],
  ]" ... />
</template>
```

### OR Conditions [​](https://vueform.com/docs/conditional-rendering#or-conditions)

To use `or` type conditions or condition groups we need to wrap our conditions in an extra array:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <CheckboxElement name="ask_call" text="Ask for a call" ... />

  <!-- `delivery` OR `ask_call` need to satisfy the condition -->
  <TextElement name="phone" :conditions="[
    [
      ['delivery', ['ups', 'fedex']],
      ['ask_call', true],
    ]
  ]" ... />
</template>
```

In this case either choosing `UPS` or `FedEx` will satisfy the condition OR checking `Ask for a call`.

We might combine _**or**_ conditions with _**and**_:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <SelectElement name="payment_method" :items="{
    credit_card: 'Credit Card',
    wire: 'Wire Transfer',
  }" ... />

  <CheckboxElement name="ask_call" text="Ask for a call" :conditions="[
    [
      ['delivery', ['ups', 'fedex']],
      ['payment_method', 'wire'],
    ]
  ]" ... />

  <!-- `delivery` OR `payment_method` AND `ask_call` need to satisfy the condition -->
  <TextElement name="phone" :conditions="[
    [
      ['delivery', ['ups', 'fedex']],
      ['payment_method', 'wire'],
    ],
    ['ask_call', true],
  ]" ... />
</template>
```

Either selecting `UPS` or `FedEx` as delivery option **or**`Wire Transfer` as payment method **and** checking `Ask for a call` will fulfill our condition. Note that in our example `Ask for a call` also receives a condition.

We can combine multiple `or` condition groups as well:

template

```
<!-- `delivery` OR `payment_method` AND `ask_call` OR `some_other_condition` need to satisfy the condition -->
<TextElement name="phone" :conditions="[
  [
    ['delivery', ['ups', 'fedex']],
    ['payment_method', 'wire'],
  ],
  [
    ['ask_call', true],
    ['some_other_condition', 'expected value'],
  ]
]" ... />
```

We can also use another `AND` group in an `OR` group:

template

```
<!-- `delivery` OR `a` is greater than `10` AND lower than `20` -->
<TextElement name="phone" :conditions="[
  [
    ['delivery', ['ups', 'fedex']],
    [
      ['a', '>', 10], ['a', '<', 20]
    ],
  ],
]" ... />
```

### Expressions [​](https://vueform.com/docs/conditional-rendering#expressions)

As of `1.13.0` Vueform has introduced [expressions](https://vueform.com/docs/expressions).

We can use an expression as a plain string in a condition:

template

```
<TextElement name="id" :conditions="[
  'AGE(birthday) > 18',
]" ... />
```

Expression conditions **can't** be used in [OR](https://vueform.com/docs/conditional-rendering#or-conditions) type conditions but **can** but used in [AND](https://vueform.com/docs/conditional-rendering#and-conditions) type conditions.

Invalid expressions and expressions that don't return a logical value (`true` or `false`) will be considered **unfulfilled** conditions.

Learn more about [expressions](https://vueform.com/docs/expressions).

### Functional Conditions [​](https://vueform.com/docs/conditional-rendering#functional-conditions)

A condition can also be a `function` that receives [`form$`](https://vueform.com/reference/vueform#property-form$) as a first param and [`el$`](https://vueform.com/reference/text-element#property-el$) as the second if the condition is assigned to an element.

Here's an example of custom functional condition:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <CheckboxElement name="ask_call" text="Ask for a call" ... />

  <TextElement name="phone" :conditions="[
    function(form$) {
      return ['ups', 'fedex'].indexOf(form$.el$('delivery')?.value) !== -1 ||
            form$.el$('ask_call')?.value
    }
  ]" ... />
</template>
```

**Note:** some elements might not be returned the time conditions are checked. Therefore it's recommended to use the [optional chaning operator (?.)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) to avoid errors.

Conditions in Nested Elements [​](https://vueform.com/docs/conditional-rendering#conditions-in-nested-elements)
---------------------------------------------------------------------------------------------------------------

We can also apply conditions that point to nested elements by using their path with `.` syntax:

template

```
<template>
  <Vueform>
    <GroupElement name="registration">
      <CheckboxElement name="newsletter" text="Subscribe for newsletter" />
    </GroupElement>
    <TextElement
      name="Email"
      placeholder="Email address"
      :conditions="[
        ['registration.newsletter', true]
      ]"
    >
  </Vueform>
</template>
```

The same dot `.` syntax can be used for `<ObjectElement>`.

List Conditions [​](https://vueform.com/docs/conditional-rendering#list-conditions)
-----------------------------------------------------------------------------------

We can reference elements in lists within the same instance using `*`:

template

```
<template>
  <Vueform>
    <ListElement name="users">
      <template #default="{ index }">
        <ObjectElement :name="index">
          <TextElement name="name" placeholder="Name" />
          <CheckboxElement name="is_admin" text="Has admin rights" />
          <CheckboxElement name="can_delete" text="Can delete posts" :conditions="[
            ['users.*.is_admin', true]
          ]" />
        </ObjectElement>
      </template>
    </ListElement>
  </Vueform>
</template>
```

Conditions on Form Steps [​](https://vueform.com/docs/conditional-rendering#conditions-on-form-steps)
-----------------------------------------------------------------------------------------------------

We can add conditions to [`FormStep`](https://vueform.com/reference/form-step) components:

template

```
<template>
  <Vueform>
    <template #empty>
      <FormSteps>
        <FormStep label="First" :elements="['first']" />
        <FormStep label="Second" :elements="['second']" :conditions="[
          ['checkbox', true]
        ]" />
        <FormStep label="Third" :elements="['third']" />
      </FormSteps>

      <TextElement name="first" placeholder="First input">
      <TextElement name="second" placeholder="Second input">
      <TextElement name="third" placeholder="Third input">
      <CheckboxElement name="checkbox" text="Check me" />

      <FormStepsControls />
    </template>
  </Vueform>
</template>
```

Any element contained in a step with conditions will only be part of [`requestData`](https://vueform.com/reference/vueform#property-request-data) if the step's conditions are fullfilled.

Conditions on Form Tabs [​](https://vueform.com/docs/conditional-rendering#conditions-on-form-tabs)
---------------------------------------------------------------------------------------------------

We can also add conditions to [`FormTab`](https://vueform.com/reference/form-tab) components:

template

```
<template>
  <Vueform>
    <template #empty>
      <FormTabs>
        <FormTab label="First" :elements="['first']" />
        <FormTab label="Second" :elements="['second']" :conditions="[
          ['checkbox', true]
        ]" />
        <FormTab label="Third" :elements="['third']" />
      </FormTabs>

      <TextElement name="first" placeholder="First input">
      <TextElement name="second" placeholder="Second input">
      <TextElement name="third" placeholder="Third input">
      <CheckboxElement name="checkbox" text="Check me" />
    </template>
  </Vueform>
</template>
```

Any element contained in a tab with conditions will only be part of [`requestData`](https://vueform.com/reference/vueform#property-request-data) if the tab's conditions are fullfilled.

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
