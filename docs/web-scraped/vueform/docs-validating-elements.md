# Source: https://vueform.com/docs/validating-elements

Title: Validation | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/validating-elements

Markdown Content:
Learn how to validate elements and create custom rules in Vueform.

Validation Rules [​](https://vueform.com/docs/validating-elements#validation-rules)
-----------------------------------------------------------------------------------

We can pass an `array` of rules to an element or a `string` where rules are separated by `|`:

vue

```
<TextElement :rules="['required', 'email']" />
<TextElement rules="required|email" />
```

### Validate On [​](https://vueform.com/docs/validating-elements#validate-on)

To decide when to validate elements we can set `validate-on` prop on form level:

vue

```
<template>
  <Vueform validate-on="">
    <TextElement :rules="['required', 'email']" ... />
    <ButtonElement button-label="Submit" submits ...  />
  </Vueform>
</template>
```

The form only validates on submit if `validate-on` is empty.

It can contain to other values joined with `|`. Possible values: `change` and `step`:

vue

`<Vueform validate-on="change|step">`

If `change` is present the elements will be validated when their values are changed.

If `step` is present they will be validated when using form steps before moving to the next step.

The `validateOn` option can be set globally in [`vueform.config.js`](https://vueform.com/docs/configuration#validate-on):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  validateOn: 'change|step',
  // ...
})
```

### Debounce [​](https://vueform.com/docs/validating-elements#debounce)

Certain rules should not be checked instantly as the user inputs data. For example when an element has `email` rule it's better to display an error message only a second after the user has stopped writing. This can be achieved by passing the number of _milliseconds_ that should elapse after the last user input to `:debounce` prop:

vue

`<TextElement :debounce="1000" rules="required|email" />`

Passing `debounce` as a prop will apply delay to all validation rules. If we want to apply it only for one, we can pass it directly to the rule:

vue

`<TextElement rules="required|email:debounce=1000" />`

If the element value is empty the debounce value will be **ignored**.

### Nullable [​](https://vueform.com/docs/validating-elements#nullable)

We can use the `nullable` rule to ignore further rules if the element's value is empty.

Here's `email` rule without `nullable`:

vue

`<TextElement rules="email" />`

And with `nullable`:

vue

`<TextElement rules="nullable|email" />`

### Asnyc Rules [​](https://vueform.com/docs/validating-elements#asnyc-rules)

Validation rules can asynchronous. For example `unique` rules sends a request to and endpoint and waits for the answer before deciding if the element's value is valid:

vue

`<TextElement rules="nullable|unique:users" />`

Validation rule endpoints can be configured in [`vueform.config.js`](https://vueform.com/docs/configuration#endpoints). See configuration options at [`unique`](https://vueform.com/docs/validating-elements#rule-unique) and [`exists`](https://vueform.com/docs/validating-elements#rule-exists) rules.

### Dependent Rules [​](https://vueform.com/docs/validating-elements#dependent-rules)

Validation rules can compare an element's value with an other and trigger validation check when any of them changes. For example `confirmed` rule needs to have an other element with the same name, suffixed with `_confirmation` to have the same value:

vue

```
<TextElement name="password" rules="required|confirmed" ... />
<TextElement name="password_confirmation" rules="required" ... />
```

Conditional Rules [​](https://vueform.com/docs/validating-elements#conditional-rules)
-------------------------------------------------------------------------------------

Sometimes we only want to apply a validation rule to an element under certain conditions. To do that we must define rules as an `array` and set the rule as an object:

vue

```
<CheckboxElement name="newsletter" ... />
<TextElement name="email" :rules="[
  {
    required: [['newsletter', '==', true]]
  }
]" ... />
```

The key of the object is the name of the rule and the value is an array. The first item of the array must be the `path` of the other element. The second is an operator that should define the type of comparison. The third is the expected value of the other element.

If you want to check for equality you can leave the operator and pass the expected value as the second param:

js

`required: [['newsletter', true]]`

Available operators:

*   `==` - expect equality
*   `!=` - expect inequality
*   `>` - expect the other element's value(s) to be higher
*   `>=`- expect the other element's value(s) to be higher or equal
*   `<` - expect the other element's value(s) to be lower
*   `<=` - expect the other element's value(s) to be lower or equal
*   `^` - expect the other element's value to start with
*   `$` - expect the other element's value to end with
*   `*` - expect the other element's value to contain
*   `in` - expect to be among an array of values
*   `not_in` - expect not to be among an array of values
*   `today` - expect to be today
*   `before` - expect to be before a date (value can be a `YYYY-MM-DD` date string or `today`)
*   `after` - expect to be after a date (value can be a `YYYY-MM-DD` date string or `today`)

The expected value can also be defined as an `array` in which case any of its values will fulfill the condition:

vue

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <TextElement name="phone" :rules="[
    {
      required: [
        ['delivery', ['ups', 'fedex']]
      ]
    }
  ]" ... />
</template>
```

### AND Conditions [​](https://vueform.com/docs/validating-elements#and-conditions)

Multiple conditions can be applied by wrapping conditions in an array:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <TextElement name="phone" :rules="[
    {
      required: [
        ['delivery', ['ups', 'fedex']],
        ['other_condition', 'expected value'],
      ]
    }
  ]" ... />
</template>
```

In this case **both**`delivery` and `other_condition` need to satisfy their conditions.

### OR Conditions [​](https://vueform.com/docs/validating-elements#or-conditions)

To create **or** conditions you might wrap the conditions in an other array:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <!-- Either `delivery` OR `other_condition` need to satisfy the condition -->
  <TextElement name="phone" :rules="[
    {
      required: [
        [
          ['delivery', ['ups', 'fedex']],
        ],
        [
          ['other_condition', 'expected value'],
        ]
      ]
    }
  ]" ... />
</template>
```

In this case **either**`delivery` or `other_condition` need to satisfy their conditions.

In or condition groups multiple conditions can be wrapped and they can be combined with single conditions:

template

```
<template>
  <SelectElement name="delivery" :items="{
    ups: 'UPS',
    fedex: 'FedEx',
    shop: 'In person'
  }" ... />

  <TextElement name="phone" :rules="[
    {
      required: [
        [
          ['condition_1', 'expected value'],
          ['condition_2', 'expected value'],
        ],
        [
          ['condition_3', 'expected value'],
          ['condition_4', 'expected value'],
        ],
        ['condition_5', 'expected value']
      ]
    }
  ]" ... />
</template>
```

In this case `condition_1` or `condition_2` AND `condition_3` or `condition_4` AND `condition_5` need to fulfill their condition.

### Expressions [​](https://vueform.com/docs/validating-elements#expressions)

As of `1.13.0` Vueform has introduced [expressions](https://vueform.com/docs/expressions).

We can use an expression as a plain string in a condition:

template

```
<TextElement name="phone" :rules="[
  {
    required: [
      'create_account == true and AGE(birthday) > 18'
    ]
  }
]" ... />
```

When an expression is used in a rule condition it must be **either the only condition** in the array (as above) or each expression has to be wrapped in an array.

This **will** work:

template

```
<TextElement name="phone" :rules="[
  {
    required: [ // WORKS
      ['create_account == true'],
      ['AGE(birthday) > 18'],
    ]
  }
]" ... />
```

This **will not** work:

template

```
<TextElement name="phone" :rules="[
  {
    required: [ // DOESN'T WORK
      'create_account == true',
      'AGE(birthday) > 18',
    ]
  }
]" ... />
```

It does work with regular [AND](https://vueform.com/docs/validating-elements#and-conditions) type conditions:

template

```
<TextElement name="phone" :rules="[
  {
    required: [
      ['AGE(birthday) > 18'],
      ['create_account', true],
    ]
  }
]" ... />
```

It will not work with [OR](https://vueform.com/docs/validating-elements#or-conditions) type conditions.

Invalid expressions and expressions that don't return a logical value (`true` or `false`) will be considered **unfulfilled** conditions.

Learn more about [expressions](https://vueform.com/docs/expressions).

### Functional Conditions [​](https://vueform.com/docs/validating-elements#functional-conditions)

We can also pass a function as a condition for more complex use-cases:

template

```
<template>
  <CheckboxElement name="support" ... />
  <SelectElement name="delivery" :items="{ ... }" ... />

  <TextElement name="phone" :rules="[
    {
      required: (form$, Validator) => {
        Validator.watch(['support', 'delivery'])
        
        return form$.el$('support')?.value === true ||
              ['ups', 'fedex'].indexOf(form$.el$('delivery')?.value) !== -1
      }
    }
  ]" ... />
</template>
```

The condition function receives `form$` as its first param, which is the instance of [`Vueform`](https://vueform.com/reference/vueform) component and `Validator` as second.

We can use `Validator.watch` method to automatically revalidate the current element when another element changes. The `Validator.watch` accepts an array of element paths or a single element `path`.

Functional conditions can also wrapped in _arrays_ or used in _or_ condition groups.

Multilingual Rules [​](https://vueform.com/docs/validating-elements#multilingual-rules)
---------------------------------------------------------------------------------------

Certain elements can have multiple values in different languages. For example for [`TTextElement`](https://vueform.com/reference/t-text-element) we can set different rules for different languages:

vue

```
<TTextElement name="title" :rules="{
  en: 'required|max:255',
  zh: 'max:255',
}" />
```

Error Messages [​](https://vueform.com/docs/validating-elements#error-messages)
-------------------------------------------------------------------------------

When an element has failing rules the first one's error message will be displayed under the element:

vue

```
<template>
  <Vueform>
    <TextElement rules="required|email" />
  </Vueform>
</template>
```

If the element has `label`, `floating` or a `placeholder` those will be used as element names in the error message (in this order).

We can explicitly define the name we want to use in the error message with `field-name` option:

vue

```
<template>
  <Vueform>
    <TextElement rules="required|email" field-name="Email address" />
  </Vueform>
</template>
```

If none of the above ones are defined, the `name` will be transformed to element name, using uppercase first letter and replacing `_` and `-` with spaces.

### Form Errors [​](https://vueform.com/docs/validating-elements#form-errors)

The form collects all validation errors from elements in [`FormErrors`](https://vueform.com/reference/form-errors) component which is displayed above the form by default:

It can be disabled locally with `:display-errors` prop:

vue

```
<template>
<Vueform :display-errors="false">
```

It can also be disabled globally in [`vueform.config.js`](https://vueform.com/docs/configuration#display-errors):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  displayErrors: false,
  // ...
})
```

### Custom Error Messages [​](https://vueform.com/docs/validating-elements#custom-error-messages)

By default validation messages come from the locale file's `validation` object entry. Error messages can be replaced by passing an object to `:messages` prop:

template

```
<template>
  <Vueform>
    <TextElement rules="required" :messages="{
      required: 'Please fill in this field'
    }" />
  </Vueform>
</template>
```

The object key is the name of the validator, and the value is the custom message.

We can use `:attribute` to reference the element's name in the error message:

js

`{ required: 'Please fill in :attribute field' }`

Error messages can also be replaced on form level:

template

```
<template>
  <Vueform :messages="{
    required: 'Please fill in this field'
  }" />
</template>
```

Or globally when importing the locale in [`vueform.config.js`](https://vueform.com/docs/configuration):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import en from '@vueform/vueform/locales/en'

en.validation.required = 'Please fill in :attribute field'

export default defineConfig({
  locales: { en },
  // ...
})
```

Custom Errors and Messages [​](https://vueform.com/docs/validating-elements#custom-errors-and-messages)
-------------------------------------------------------------------------------------------------------

We can add custom errors and messages to our form using the `append` and `prepend` methods of the form's `messageBag`:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.messageBag.append('Appended error')
  form$.value.messageBag.prepend('Prepended error')

  form$.value.messageBag.append('Appended message', 'message')
  form$.value.messageBag.prepend('Prepended message', 'message')
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" />
  </Vueform>
</template>

<script>
export default {
  mounted() {
    this.$refs.form$.messageBag.append('Appended error')
    this.$refs.form$.messageBag.prepend('Prepended error')

    this.$refs.form$.messageBag.append('Appended message', 'message')
    this.$refs.form$.messageBag.prepend('Prepended message', 'message')
  }
}
</script>
```

Appended and prepended form errors are displayed before and after form errors in [`FormErrors`](https://vueform.com/reference/form-errors) component. Messages are displayed in [`FormMessages`](https://vueform.com/reference/form-messages) component.

Messages and errors can be removed and cleared:

js

```
messageBag.clear() // clears all errors and messages
messageBag.clear('errors') // clears all errors
messageBag.clear('messages') // clears all messages

messageBag.clearPrepended() // clears all prepended errors and messages
messageBag.clearPrepended('errors') // clears prepended errors
messageBag.clearPrepended('messages') // clears prepended messages

messageBag.clearAppended() // clears all appended errors and messages
messageBag.clearAppended('errors') // clears appended errors
messageBag.clearAppended('messages') // clears appended messages

messageBag.remove('Lorem ipusm') // removes 'Lorem ipsum' entry from errors and messages
messageBag.remove('Lorem ipusm', 'errors') // removes 'Lorem ipsum' entry from errors
messageBag.remove('Lorem ipusm', 'messages') // removes 'Lorem ipsum' entry from messages
```

Errors and messages can be added to an element's `messageBag` as well:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.el$('name').messageBag.append('Appended error')
  form$.value.el$('name').messageBag.prepend('Prepended error')

  form$.value.el$('name').messageBag.append('Appended message', 'message')
  form$.value.el$('name').messageBag.prepend('Prepended message', 'message')
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" />
  </Vueform>
</template>

<script>
export default {
  mounted() {
    this.$refs.form$.el$('name').messageBag.append('Appended error')
    this.$refs.form$.el$('name').messageBag.prepend('Prepended error')

    this.$refs.form$.el$('name').messageBag.append('Appended message', 'message')
    this.$refs.form$.el$('name').messageBag.prepend('Prepended message', 'message')
  }
}
</script>
```

When errors and messages are added to an element only the first appears under the element from each group. Errors manually added to elements' `messageBag` will be collected in form errors, while messages will not be included in form messages.

Manual Validation [​](https://vueform.com/docs/validating-elements#manual-validation)
-------------------------------------------------------------------------------------

Form validation can be manually triggered with [`validate()`](https://vueform.com/reference/vueform#method-validate) method:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" ... />
    <TextElement name="email" rules="required" ... />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.validate()
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" ... />
    <TextElement name="email" rules="required" ... />
  </Vueform>
</template>

<script>
export default {
  mounted() {
    this.$refs.form$.validate()
  }
}
</script>
```

It can be also triggered for elements:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" ... />
    <TextElement name="email" rules="required" ... />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.el$('name').validate()
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" ... />
    <TextElement name="email" rules="required" ... />
  </Vueform>
</template>

<script>
export default {
  mounted() {
    this.$refs.form$.el$('name').validate()
  }
}
</script>
```

Validation can be reset with `resetValidators()`:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" ... />
    <TextElement name="email" rules="required" ... />
    <ButtonElement name="reset" button-label="Reset Name validators" @click="resetNameValidators">
    <ButtonElement name="reset" button-label="Reset all validators" @click="resetAllValidators">
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const resetNameValidators = () => {
  form$.value.el$('name').resetValidators()
}

const resetAllValidators = () => {
  form$.value.resetValidators()
}

onMounted(() => {
  form$.value.validate()
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" rules="required" ... />
    <TextElement name="email" rules="required" ... />
    <ButtonElement name="reset" button-label="Reset Name validators" @click="resetNameValidators">
    <ButtonElement name="reset" button-label="Reset all validators" @click="resetAllValidators">
  </Vueform>
</template>

<script>
export default {
  methods: {
    resetNameValidators() {
      this.$refs.form$.el$('name').resetValidators()
    },
    resetAllValidators() {
      this.$refs.form$.resetValidators()
    }
  },
  mounted() {
    this.$refs.form$.validate()
  }
}
</script>
```

Available Validation Rules [​](https://vueform.com/docs/validating-elements#available-validation-rules)
-------------------------------------------------------------------------------------------------------

Here's the list of available validator rules:

### accepted

The value must be `true`, `'true'`, `'yes'`, `'on'`, `'1'` or `1`.

### active_url

The value must be an URL with active A or AAAA type DNS record. The validator must be implemented on the backend which should return a `true` or `false` response.

The endpoint must be set in [`vueform.config.js`](https://vueform.com/docs/configuration#endpoints):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    activeUrl: {
      url: '/validators/active-url',
      method: 'POST'
    }
  },
  // ...
})
```

Alternatively we can specify it as an `async function` that returns a `true` or `false` value:

js

```
// vueform.config.js

import axios from 'axios'
import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    activeUrl: async (value, el$, form$) => {
      const res = await axios.post('/my-active-url-checker', {
        value,
      })

      return res.data // should be `true` or `false`
    }
  },
  // ...
})
```

### after:date

The value must be after a given date. The `date` parameter can be an exact date like `2020-01-01`, a relative date which is either `today`, `tomorrow` or `yesterday` or the `path` to an other element.

js

```
// being an exact date
'after:2018-01-01'

// being a relative date
'after:today'

// being an other elements's path
'after:checkin_date'
```

### after_or_equal:date

It's the same as [after](https://vueform.com/docs/validating-elements#rule-after) rule, except that the value must be after or equal to a given date.

### alpha

The value can only contain alphabetic characters.

### alpha_dash

The value can only contain numbers, alphabetic characters, dash `-` and underscore `_`.

### alpha_num

The value can only contain numbers and alphabetic characters.

### array

The value must be an array.

### before:date

It's the same as [after](https://vueform.com/docs/validating-elements#rule-after) rule, except that the value must be before a given date.

### before_or_equal:date

It's the same as [after](https://vueform.com/docs/validating-elements#rule-after) rule, except that the value must be before or equal to a given date.

### between:min,max

The value must be between the size of _min_ and _max_. The size is evaluated the same way as described at [size](https://vueform.com/docs/validating-elements#rule-size) rule.

### boolean

The value must be some form of a boolean which is either `true`, `false`, `1`, `0`, `'1'` or `'0'`.

### captcha

Validates if the captcha challenge has been passed. Automatically assigned to each captcha elements - no need to assign manually.

### completed

Validates if the phone number is completed when masks are enabled (used only in `PhoneElement`).

### confirmed

The value must identical to an other element's value which has the same name ending with `_confirmation`.

js

```
password: {
  type: 'text',
  inputType: 'password',
  rules: 'confirmed'
},
password_confirmation: {
  type: 'text',
  inputType: 'password',
  label: 'Password Again'
}
```

### date

The value must be a valid date.

### date_equals:date

The value must match an exact date.

### date_format:format

The value must match a given date format using [Date Formatting Tokens](https://vueform.com/docs/i18n#date-formatting-tokens).

### different:path

The value must be different from an other element's value.

### digits:value

The value must be **numeric** and have an exact length of **value**.

### digits_between:min,max

The value must be **numeric** and have a length between **min** and **max**.

### dimensions

The value must be an image with dimension constraints. Available constraints:

*   min_width
*   min_height
*   max_witdth
*   max_height
*   height
*   width
*   ratio

The ratio can be a float, like `0.66` or a statement like `2/3` which represents **width / height** ratio.

js

```
'dimensions:min_width=768'
'dimensions:min_height=1024'
'dimensions:min_width=768,ratio=2/3'
```

### distinct

The value must be a unique item of an array.

js

```
favorite_numbers: {
  type: 'list',
  label: 'Favorite numbers:',
  element: {
    type: 'text',
    placeholder: 'Number',
    rules: 'distinct'
  }
}
```

### email

The value must be a valid email format.

### exists:param1,param2,...

The value must be confirmed by an endpoint that exist in database. It does not specify any required params, but we can use them to identify a validation request in the backend.

For example, let's take the following rule definition: `exists:users`. The `users` param is just a string that the backend receives in the `params` (request) param:

php

```
$params = $_REQUEST['params'];
$type = $params[0]; // will be 'users'
```

Params can be used to identify requests:

php

```
$value = $_REQUEST['value']; // the value of the input field
$name = $_REQUEST['name']; // the name of the input field
$params = $_REQUEST['params'];
$type = $params[0];

switch($type) {
  case 'users':
    return ... // check value against users

  case 'product_identifiers':
    return ... // check value against product identifiers

  case 'slugs':
    return ... // check value against slugs
}
```

The backend should return `true` if the given `value`**exist** in the database and therefore the field value should be considered **valid**.

If a param's name equals to the name of a field in the form, the value of that will be sent instead of the param name. So for example if `exists:users,id` is the rule and the form has a field with `id` name, the request params will be sent:

js

```
// request params sent to `exists` endpoint

requestParams: {
  value: 'john@doe.com',
  name: 'email',
  params: [
    'users',
    5984
  ]
}
```

And you can access the value of `id` field using the `params` object:

php

```
$value = $_REQUEST['value']; // the value of the input field - 'john@doe.com'
$name = $_REQUEST['name']; // the name of the input field - 'email'
$params = $_REQUEST['params'];
$type = $params[0]; // will be 'users'
$id = $params[1]; // will be the value of the 'id' field in the same form - 5984
```

This way we can send field values dynamically to the backend to validate requests (eg. excluding the user's ID from the database check).

The endpoint where all the `exists` requests submitted can be configured in [`vueform.config.js`](https://vueform.com/docs/configuration#endpoints)'s `endpoints.exists` section:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    exists: {
      url: '/validators/exists',
      method: 'POST'
    }
  },
  // ...
})
```

Alternatively we can specify it as an `async function` that returns a `true` or `false` value:

js

```
// vueform.config.js

import axios from 'axios'
import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    exists: async (value, name, params, el$, form$) => {
      const res = await axios.post('/my-exists-checker', {
        value,
        name,
        params,
      })

      return res.data // should be `true` or `false`
    }
  },
  // ...
})
```

### file

The value must be an instance of [File](https://developer.mozilla.org/hu/docs/Web/API/File).

### filled

The value must be not empty.

### gt:path

The value must be greater than the **size** of a given element. The size is evaluated the same way as described at [size](https://vueform.com/docs/validating-elements#rule-size) rule.

### gte:path

The value must be greater than or equal to the **size** of a given element. The size is evaluated the same way as described at [size](https://vueform.com/docs/validating-elements#rule-size) rule.

### image

The value must a file with `jpg`, `jpeg`, `png`, `bmp`, `gif`, `svg` or `webp` extension.

### in:foo,bar,...

The value must be one of the provided values.

js

```
role: {
  type: 'select',
  label: 'Role',
  items: {
    admin: 'Admin',
    editor: 'Editor'
  },
  rules: 'in:admin,editor'
}
```

### in_array:path.*

The value must be present in an other element's array value.

### integer

The value must be an **integer**.

### ip

The value must be a valid IP address.

### ipv4

The value must be a valid IPv4 address.

### ipv6

The value must be a valid IPv6 address.

### json

The value must be a valid JSON string.

### lt:path

The value must be lower than the **size** of a given element. The size is evaluated the same way as described at [size](https://vueform.com/docs/validating-elements#rule-size) rule.

### lte:path

The value must be lower than or equal to the **size** of a given element. The size is evaluated the same way as described at [size](https://vueform.com/docs/validating-elements#rule-size) rule.

### max:value

The size of the value must be lower than or equal to **max**. The size is evaluated the same way as described at [size](https://vueform.com/docs/validating-elements#rule-size) rule.

### mimetypes:text/plain,...

The value must be an instance of [File](https://developer.mozilla.org/hu/docs/Web/API/File) and have one of the listed **mime-type**.

### mimes:zip,rar,...

The value must be an instance of [File](https://developer.mozilla.org/hu/docs/Web/API/File) and have one of the listed **extensions**.

### min:value

The size of the value must be at least **value**. The size is evaluated the same way as described at [size](https://vueform.com/docs/validating-elements#rule-size) rule.

### not_in:foo,bar,...

The value must **not** be one of the provided values.

### not_regex:pattern

The value must **not** match the provided regex **pattern**.

js

`'not_regex:/^.+$/i'`

> When using pipe `|` in the pattern it's recommended to define the rules as array instead of a string.

### nullable

Certain rules should only execute if the input has value, otherwise it should be ignored. For example if the user can optionally fill in his birthday, the date format should only be validated if the input is filled:

js

```
birthday: {
  type: 'date',
  label: 'Birthday',
  rules: 'nullable|date_format:YYYY-MM-DD'
}
```

### numeric

The value must be numeric.

### regex:pattern

The value must match the provided regex **pattern**.

js

`'regex:/^.+$/i'`

> When using pipe `|` in the pattern it's recommended to define the rules as array instead of a string.

### required

The value must not be empty. The value is considered empty as the following:

*   the value is `null`
*   the value is `undefined`
*   if the value is a string it's `''`
*   if the value is an array it contains no items
*   if the value is a File object it's `name` is empty.

### same:path

The value must be the same as the given element's value.

js

```
password: {
  type: 'password',
  rules: 'same:password_again'
},
password_again: {
  type: 'password',
  label: 'Password Again'
}
```

If used in nested elements like `GroupElment` or `ObjectElement` the reference must include the full path using `.` dot syntax (eg. `parent.password_again`).

### size:value

The size of the value must be exactly as a given _value_. Size is calculated as the following:

*   if the value is **string** then it's the **length of the string**
*   if the value is **numeric** then it's the actual **numeric value**
*   if the value is **array** then it's the **length of the array**
*   if the value is **File** then it's the **size of the file in KB**.

> If you expect numeric comparison make sure to add [`numeric`](https://vueform.com/docs/validating-elements#rule-numeric) to the list of rules.

### string

The value must be a string.

### timezone

The value must be a valid timezone, eg. `'America/Los_Angeles'`.

### unique:param1,param2,...

The value must be confirmed by an endpoint that doesn't exist in database. It does not specify any required params, but we can use them to identify a validation request in the backend.

For example, let's take the following rule definition: `unique:users`. The `users` param is just a string that the backend receives in the `params` (request) param:

php

```
$params = $_REQUEST['params'];
$type = $params[0]; // will be 'users'
```

Params can be used to identify requests:

php

```
$value = $_REQUEST['value']; // the value of the input field
$name = $_REQUEST['name']; // the name of the input field
$params = $_REQUEST['params'];
$type = $params[0];

switch($type) {
  case 'users':
    return ... // check value against users

  case 'product_identifiers':
    return ... // check value against product identifiers

  case 'slugs':
    return ... // check value against slugs
}
```

The backend should return `true` if the given `value`**does not exist** (unique) in the database and therefore the field value should be considered **valid**.

If a param's name equals to the name of a field in the form, the value of that will be sent instead of the param name. So for example if `unique:users,id` is the rule and the form has a field with `id` name, the request params will be sent:

js

```
// request params sent to `unique` endpoint

requestParams: {
  value: 'john@doe.com',
  name: 'email',
  params: [
    'users',
    5984
  ]
}
```

And you can access the value of `id` field using the `params` object:

php

```
$value = $_REQUEST['value']; // the value of the input field - 'john@doe.com'
$name = $_REQUEST['name']; // the name of the input field - 'email'
$params = $_REQUEST['params'];
$type = $params[0]; // will be 'users'
$id = $params[1]; // will be the value of the 'id' field in the same form - 5984
```

This way we can send field values dynamically to the backend to validate requests (eg. excluding the user's ID from the database check).

The endpoint where all the `unique` requests submitted can be configured in [`vueform.config.js`](https://vueform.com/docs/configuration#endpoints)'s `endpoints.unique` section:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    unique: {
      url: '/validators/unique',
      method: 'POST'
    }
  },
  // ...
})
```

Alternatively we can specify it as an `async function` that returns a `true` or `false` value:

js

```
// vueform.config.js

import axios from 'axios'
import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    unique: async (value, name, params, el$, form$) => {
      const res = await axios.post('/my-unique-checker', {
        value,
        name,
        params,
      })

      return res.data // should be `true` or `false`
    }
  },
  // ...
})
```

### url

The value must be a valid URL format.

### uuid

The value must be a valid UUID format.

Custom Validation Rules [​](https://vueform.com/docs/validating-elements#custom-validation-rules)
-------------------------------------------------------------------------------------------------

We can create custom validation rules by extending `Validator` class:

Composition API Options API

vue

```
<template>
  <Vueform>
    <TextElement :rules="[uppercase]" name="code" />
  </Vueform>
</template>

<script setup>
import { Validator } from '@vueform/vueform'

const uppercase = class extends Validator {
  check(value) {
    return /^[A-Z]*$/.test(value)
  }
}
</script>
```

vue

```
<template>
  <Vueform>
    <TextElement :rules="[uppercase]" />
  </Vueform>
</template>

<script>
import { Validator } from '@vueform/vueform'

const uppercase = class extends Validator {
  check(value) {
    return /^[A-Z]*$/.test(value)
  }
}

export default {
  data() {
    return {
      uppercase,
    }
  }
}
</script>
```

The `check` method validates whether the value only contains uppercase letters.

### Custom Error Message [​](https://vueform.com/docs/validating-elements#custom-error-message)

If the value is invalid a generic error message will be displayed from locale's `vueform.defaultMessage`. We can replace this by adding a custom message to the rule:

js

```
const uppercase = class extends Validator {
  get msg() {
    return 'The text must only contain uppercase letters'
  }

  check(value) {
    return /^[A-Z]*$/.test(value)
  }
}
```

#### Message Params [​](https://vueform.com/docs/validating-elements#message-params)

We can use `:attribute` param in our error message that will be replaced by the element's name. By default the element's name equals to its `label` or if there's no label then the `placeholder` or if that's not defined either then the element's `name`, uppercasing its first letter:

js

```
const uppercase = class extends Validator {
  get msg() {
    return 'The :attribute must only contain uppercase letters'
  }

  check(value) {
    return /^[A-Z]*$/.test(value)
  }
}
```

We can add other params to the error message by defining `get messageParams`:

js

```
const uppercase = class extends Validator {
  get msg() {
    return 'The :attribute must only contain :type letters'
  }

  get messageParams () {
    return {
      attribute: this.attributeName,
      type: 'UPPERCASE'
    }
  }

  check(value) {
    return /^[A-Z]*$/.test(value)
  }
}
```

### Rule Params [​](https://vueform.com/docs/validating-elements#rule-params)

We can add params to our rule by wrapping it in an `array` and pass params as the second second item. Then we can get them via `attributes`.

Let's say we only want to allow character between `A-H`:

Composition API Options API

vue

```
<template>
  <Vueform>
    <TextElement :rules="[
      [uppercase, ['A', 'H']]
    ]" />
  </Vueform>
</template>

<script setup>
import { Validator } from '@vueform/vueform'

const uppercase = class extends Validator {
  get from () {
    return this.attributes[0] || 'A'
  }

  get to () {
    return this.attributes[1] || 'Z'
  }

  check(value) {
    let regexp = new RegExp(`^[${this.from}-${this.to}]*$`)
    
    return regexp.test(value)
  }
}
</script>
```

vue

```
<template>
  <Vueform>
    <TextElement :rules="[
      [uppercase, ['A', 'H']]
    ]" />
  </Vueform>
</template>

<script>
import { Validator } from '@vueform/vueform'

const uppercase = class extends Validator {
  get from () {
    return this.attributes[0] || 'A'
  }

  get to () {
    return this.attributes[1] || 'Z'
  }

  check(value) {
    let regexp = new RegExp(`^[${this.from}-${this.to}]*$`)
    
    return regexp.test(value)
  }
}

export default {
  data() {
    return {
      uppercase,
    }
  }
}
</script>
```

Once the rule is [registered globally](https://vueform.com/docs/validating-elements#registering-rule-globally) we can provide params after the rule name using a colon `:`, separated by commas `,`:

vue

`<TextElement rules="uppercase:A,H" ... />`

#### Using Rule Params in Message [​](https://vueform.com/docs/validating-elements#using-rule-params-in-message)

We can combine our rule params with [message params](https://vueform.com/docs/validating-elements#message-aprams):

js

```
const uppercase = class extends Validator {
  get msg() {
    return 'The :attribute must only contain [:from-:to] letters'
  }

  get messageParams () {
    return {
      attribute: this.attributeName,
      from: this.from,
      to: this.to,
    }
  }

  get from () {
    return this.attributes[0] || 'A'
  }

  get to () {
    return this.attributes[1] || 'Z'
  }

  check(value) {
    let regexp = new RegExp(`^[${this.from}-${this.to}]*$`)
    
    return regexp.test(value)
  }
}
```

### Watching For Change [​](https://vueform.com/docs/validating-elements#watching-for-change)

Let's say we have a custom rule which needs to watch a property and revalidate when that property changes.

We can use the rule's `init()` method to create a watcher and revalidate the field when the value changes:

vue

```
<script setup>
import { ref, watch, onMounted } from 'vue'

const valueToWatch = ref(1)

const customRule = class extends Validator
{
  init() {
    watch(valueToWatch, () => {
      this.revalidate()
    })
  }

  check(value) {
    // ...
  }
}

onMounted(() => {
  setTimeout(() => {
    // This will trigger revalidation of the field that uses the custom rule
    valueToWatch.value++
  }, 1000)
})
</script>
```

### Async Validation [​](https://vueform.com/docs/validating-elements#async-validation)

Validation rules can also be `async` by adding `get isAsync()` which returns `true`:

js

```
const uppercase = class extends Validator {
  get isAsync() {
    return true
  }

  async check(value) {
    return (await axios.get('/validator/uppercase')).data.valid
  }
}
```

While async validation is in progress a loading spinner will automatically appear on the right side of the input.

### Registering Rule Globally [​](https://vueform.com/docs/validating-elements#registering-rule-globally)

Custom validation rules can be registered globally in [`vueform.config.js`](https://vueform.com/docs/configuration#rules):

js

```
// vueform.config.js

import { defineConfig, Validator } from '@vueform/vueform'

const uppercase = class extends Validator {
  async check(value) {
    return /^[A-Z]*$/.test(value)
  }
}

export default defineConfig({
  rules: {
    uppercase,
  },
  // ...
})
```

Once registered, they can be used as strings:

vue

`<TextElement rules="required|uppercase" ... />`

### Adding Rule Message to Locale [​](https://vueform.com/docs/validating-elements#adding-rule-message-to-locale)

An error message can be added to the global locale instead of using `get message()`:

js

```
// vueform.config.js

import { defineConfig, Validator } from '@vueform/vueform'
import en from '@vueform/vueform/locales/en'

en.validation.uppercase = 'The text must only contain uppercase letters'

const uppercase = class extends Validator {
  check(value) {
    return /^[A-Z]*$/.test(value)
  }
}

export default defineConfig({
  rules: {
    uppercase,
  },
  locales: { en }
  // ...
})
```
