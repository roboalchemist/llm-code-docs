# Source: https://vueform.com/docs/handling-form-data

Title: Handling Form Data | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/handling-form-data

Markdown Content:
Learn how submit, store and manage form data using Vueform.

Submitting Form Data [​](https://vueform.com/docs/handling-form-data#submitting-form-data)
------------------------------------------------------------------------------------------

There are different ways to submit form data, eg. using an endpoint or writing a custom function.

### Submit via Endpoint [​](https://vueform.com/docs/handling-form-data#submit-via-endpoint)

We decide where to submit form data by setting `endpoint` and `method` props:

vue

```
<template>
  <Vueform endpoint="/form/submit" method="post">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>
```

The default values can be configured in [`vueform.config.js`](https://vueform.com/docs/configuration#endpoints) so all forms will submit to the same endpoint, unless overwritten at component level:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    submit: {
      url: '/form/submit',
      method: 'post'
    }
  }
})
```

### Submit via Function [​](https://vueform.com/docs/handling-form-data#submit-via-function)

The `endpoint` can also be an async function that receives [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) and [`form$`](https://vueform.com/reference/vueform#property-form_) params and must return an [Axios response](https://axios-http.com/docs/res_schema) object:

vue

```
<Vueform :endpoint="async (FormData, form$) => {
  // Using FormData will EXCLUDE conditional elements and it
  // will submit the form as "Content-Type: multipart/form-data".
  const formData = FormData

  // Using form$.data will INCLUDE conditional elements and it
  // will submit the form as "Content-Type: application/json".
  const data = form$.data

  // Using form$.requestData will EXCLUDE conditional elements and it
  // will submit the form as "Content-Type: application/json".
  const requestData = form$.requestData

  // Setting cancel token
  form$.cancelToken = form$.$vueform.services.axios.CancelToken.source()

  return await form$.$vueform.services.axios.post('/my/endpoint',
    formData /* | data | requestData */,
    {
      cancelToken: form$.cancelToken.token,
    }
  )
}">
```

When submitting via function, the form will trigger `@success`, `@error` and `@response` events which we will learn about in the [next section](https://vueform.com/docs/handling-form-data#handling-response).

A function can also be set a default endpoint for our forms in `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    submit: async () => {
      // ...
    }
  }
})
```

### Submit via Event [​](https://vueform.com/docs/handling-form-data#submit-via-event)

The `endpoint` can be disabled by setting its value to `false`. In this case we can rely on [`@submit`](https://vueform.com/reference/vueform#submit-event) method that is triggered after the validation is passed and elements are prepared.

vue

```
<Vueform :endpoint="false" @submit="async (form$, FormData) => {
  // Using FormData will EXCLUDE conditional elements and it
  // will submit the form as "Content-Type: multipart/form-data".
  const formData = FormData

  // Using form$.data will INCLUDE conditional elements and it
  // will submit the form as "Content-Type: application/json".
  const data = form$.data

  // Using form$.requestData will EXCLUDE conditional elements and it
  // will submit the form as "Content-Type: application/json".
  const requestData = form$.requestData

  // Show loading spinner
  form$.submitting = true

  // Setting cancel token
  form$.cancelToken = form$.$vueform.services.axios.CancelToken.source()

  let response

  try {
    // Sending the request
    response = await form$.$vueform.services.axios.request(
      '/my/endpoint',
      formData /* | data | requestData */,
      {
        cancelToken: form$.cancelToken.token,
      }
    )
  } catch (error) {
    // Handle error (status is outside of 2XX or other error)
    console.error('error', error)
    return
  } finally {
    // Hide loading spinner
    form$.submitting = false
  }

  // Handle success (status is 2XX)
  console.log('success', response)
}">
```

When submitting via event, the form will **not** trigger `@success`, `@error` and `@response` events, show loading spinner or set cancel token, therefore we need to take care of managing these all.

When [submitting via endpoint](https://vueform.com/docs/handling-form-data#submit-via-endpoint) the form will be submitted as `Content-Type: multipart/form-data` by default. To change that to `application/json`, add the following config in `vueform.config.js` to `axios`:

js

```
// vueform.config.js
 
import { defineConfig } from '@vueform/vueform'
import axios from 'axios'

axios.defaults.headers.post = {
  'Content-Type': 'application/json'
}

export default defineConfig({
  axios,
})
```

Here you can add other headers or configuration options to requests.

### Submitting Conditional Data [​](https://vueform.com/docs/handling-form-data#submitting-conditional-data)

When [submitting via endpoint](https://vueform.com/docs/handling-form-data#submit-via-endpoint) the [`requestData`](https://vueform.com/reference/vueform#property-request-data) gets submitted by default. It only contain the value of the fields which has no conditions or all of their conditions are met.

If we want to submit even fields that have failing conditions, we can replace [`requestData`](https://vueform.com/reference/vueform#property-request-data) with [`data`](https://vueform.com/reference/vueform#property-data):

vue

```
<template>
  <Vueform :form-data="form$ => form$.convertFormData(form$.data)">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>
```

### Formatting Data Before Submit [​](https://vueform.com/docs/handling-form-data#formatting-data-before-submit)

We can pass a function to `:format-data` option of Vueform or any elements, that will format its `requestData`:

Composition API Options API

vue

```
<template>
  <Vueform :format-data="formatFormData">
    <TextElement
      name="name"
      label="Name"
      default="John Doe"
      :format-data="formatName"
    />
    <TextElement
      name="email"
      label="Email"
      default="john@Doe.com"
      :format-data="formatEmail"
    />
  </Vueform>
</template>

<script setup>
const formatFormData = ({ name, email }) => {
  return {
    name: `<div>${name}</div>`,
    email: `<div>${email}</div>`,
  }
}

const formatName = (name, value) => {
  return { [name]: value.toUpperCase() } // must return an object
}

const formatEmail = (name, value) => {
  return { [name]: value.toLowerCase() } // must return an object
}
</script>
```

vue

```
<template>
  <Vueform :format-data="formatFormData">
    <TextElement
      name="name"
      label="Name"
      default="John Doe"
      :format-data="formatName"
    />
    <TextElement
      name="email"
      label="Email"
      default="john@Doe.com"
      :format-data="formatEmail"
    />
  </Vueform>
</template>

<script>
export default {
  mehtods: {
    formatFormData({ name, email }) {
      return {
        name: `<div>${name}</div>`,
        email: `<div>${email}</div>`,
      }
    },
    formatName(name, value) {
      return { [name]: value.toUpperCase() } // must return an object
    },
    formatEmail(name, value) {
      return { [name]: value.toLowerCase() } // must return an object
    }
  }
}
</script>
```

The submitted data will be:

js

```
{
  name: '<div>JOHN DOE</div>',
  email: '<div>john@doe.com</div>'
}
```

This can be used in conjuction with `formatLoad` methods to transform data between databases and forms.

### Preparing for Submit [​](https://vueform.com/docs/handling-form-data#preparing-for-submit)

We can pass an `async` function to `:prepare` option of Vueform, that will be executed before the form submits:

Composition API Options API

vue

```
<template>
  <Vueform :prepare="prepare">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
const prepare = async (form$) => { // form$ is the <Vueform> component
  try {
    await // async process
  } catch (error) {
    throw error // this will cancel the submit process
  }
}
</script>
```

vue

```
<template>
  <Vueform :prepare="prepare">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  methods: {
    async prepare(form$) { // form$ is the <Vueform> component
      try {
        await // async process
      } catch (error) {
        throw error // this will cancel the submit process
      }
    }
  }
}
</script>
```

The `prepare` function runs after submit was initiated, the elements are validated and none was found invalid.

The submit process halts until the prepare function is finished. The submit process can be cancelled by throwing an error in the `prepare` function.

Handling Response [​](https://vueform.com/docs/handling-form-data#handling-response)
------------------------------------------------------------------------------------

After receiving a response from the backend (or having an error), Vueform will first trigger either [`@success`](https://vueform.com/reference/vueform#event-sucess) or [`@error`](https://vueform.com/reference/vueform#event-error) event and after the [`@response`](https://vueform.com/reference/vueform#event-response) event in all cases.

### Handling All Responses [​](https://vueform.com/docs/handling-form-data#handling-all-responses)

When we receive a response from the backend (successful or failed) it can be handled with `@response` event:

Composition API Options API

vue

```
<template>
  <Vueform @response="handleResponse" />
</template>

<script setup>
const handleResponse = (response, form$) => {
  console.log(response) // axios response
  console.log(response.status) // HTTP status code
  console.log(response.data) // response data

  console.log(form$) // <Vueform> instance
}
</script>
```

vue

```
<template>
  <Vueform @response="handleResponse" />
</template>

<script>
export default {
  methods: {
    handleResponse(response, form$) {
      console.log(response) // axios response
      console.log(response.status) // HTTP status code
      console.log(response.data) // response data

      console.log(form$) // <Vueform> instance
    }
  }
}
const 
</script>
```

The `@response` event will **not** be triggered if there is no response from the server, for example an error occurs while [preparing for submit](https://vueform.com/docs/handling-form-data#preparing-for-submit) or when there's no network connection.

Alternatively, we can subscribe to `@response` event via `on()` method:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$" />
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.on('response', (response, form$) => {
    // ...
  })
})
</script>
```

vue

```
<template>
  <Vueform ref="form$" />
</template>

<script>
export default {
  mounted() {
    this.$refs.$form$.on('response', (response, form$) => {
      // ...
    })
  }
}
</script>
```

### Handling Success Responses [​](https://vueform.com/docs/handling-form-data#handling-success-responses)

The `@success` event can be used to handle successful server responses (HTTP status `2xx`):

Composition API Options API

vue

```
<template>
  <Vueform @success="handleSuccess" />
</template>

<script setup>
const handleSuccess = (response, form$) => {
  console.log(response) // axios response
  console.log(response.status) // HTTP status code
  console.log(response.data) // response data

  form$.messageBag.clear() // clear message bag
  form$.messageBag.append('Form submitted', 'message') // add success message
  form$.reset() // reset form data
}
</script>
```

vue

```
<template>
  <Vueform @success="handleSuccess" />
</template>

<script>
export default {
  methods: {
    handleSuccess(response, form$) {
      console.log(response) // axios response
      console.log(response.status) // HTTP status code
      console.log(response.data) // response data

      form$.messageBag.clear() // clear message bag
      form$.messageBag.append('Form submitted', 'message') // add success message
      form$.reset() // reset form data
    }
  }
}
</script>
```

Alternatively, we can subscribe to `@success` event via `on()` method:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$" />
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.on('success', (response, form$) => {
    // ...
  })
})
</script>
```

vue

```
<template>
  <Vueform ref="form$" />
</template>

<script>
export default {
  mounted() {
    this.$refs.$form$.on('success', (response, form$) => {
      // ...
    })
  }
}
</script>
```

### Handling Errors and Failed Requests [​](https://vueform.com/docs/handling-form-data#handling-errors-and-failed-requests)

The `@error` event is triggered when something goes wrong while trying to submit the form. We can use `details.type` to determine what kind of error we are dealing with:

Composition API Options API

vue

```
<template>
  <Vueform @error="handleError" />
</template>

<script setup>
const handleError = (error, details, form$) => {
  form$.messageBag.clear() // clear message bag

  switch (details.type) {
    // Error occured while preparing elements (no submit happened)
    case 'prepare':
      console.log(error) // Error object

      form$.messageBag.append('Could not prepare form')
      break

    // Error occured because response status is outside of 2xx
    case 'submit':
      console.log(error) // AxiosError object
      console.log(error.response) // axios response
      console.log(error.response.status) // HTTP status code
      console.log(error.response.data) // response data

      form$.messageBag.append('Some error from the backend')
      break

    // Request cancelled (no response object)
    case 'cancel':
      console.log(error) // Error object

      form$.messageBag.append('Request cancelled')
      break

    // Some other errors happened (no response object)
    case 'other':
      console.log(error) // Error object

      form$.messageBag.append('Couldn\'t submit form')
      break
  }
}
</script>
```

vue

```
<template>
  <Vueform @error="handleError" />
</template>

<script>
export default {
  methods: {
    handleError(error, details, form$) {
      form$.messageBag.clear() // clear message bag

      switch (details.type) {
        // Error occured while preparing elements (no submit happened)
        case 'prepare':
          console.log(error) // Error object

          form$.messageBag.append('Could not prepare form')
          break

        // Error occured because response status is outside of 2xx
        case 'submit':
          console.log(error) // AxiosError object
          console.log(error.response) // axios response
          console.log(error.response.status) // HTTP status code
          console.log(error.response.data) // response data

          form$.messageBag.append('Some error from the backend')
          break

        // Request cancelled (no response object)
        case 'cancel':
          console.log(error) // Error object

          form$.messageBag.append('Request cancelled')
          break

        // Some other errors happened (no response object)
        case 'other':
          console.log(error) // Error object

          form$.messageBag.append('Couldn\'t submit form')
          break
      }
    }
  }
}
</script>
```

Here are some of the common cases that trigger `@error`:

**1) response is outside of 2xx**

*   `@success(response, form$)` is not triggered
*   `@error(error, details, form$)` receives 
    *   `error`: the [AxiosError](https://axios-http.com/docs/handling_errors) (contains `error.response`)
    *   `details`: `details.type` is `'submit'`
    *   `form$`: [Vueform instance](https://vueform.com/reference/vueform)

*   `@response(response, form$)` receives 
    *   `response`: the [Axios response](https://axios-http.com/docs/res_schema)
    *   `form$`: [Vueform instance](https://vueform.com/reference/vueform)

**2) an error occured while [preparing for submit](https://vueform.com/docs/handling-form-data#preparing-for-submit)**

*   `@success(response, form$)` is not triggered
*   `@error(response, details, form$)` receives 
    *   `error`: the `Error` thrown by [`prepare`](https://vueform.com/reference/vueform#option-prepare) method
    *   `details`: `details.type` is `'prepare'`
    *   `form$`: [Vueform instance](https://vueform.com/reference/vueform)

*   `@response(response, form$)` is not triggered

**3) the request was cancelled, no response at all**

*   `@success(response, form$)` is not triggered
*   `@error(response, details, form$)` receives 
    *   `error`: the `Error` object
    *   `details`: `details.type` is `'cancel'`
    *   `form$`: [Vueform instance](https://vueform.com/reference/vueform)

*   `@response(response, form$)` is not triggered

**4) some other error occured, no response at all**

*   `@success(response, form$)` is not triggered
*   `@error(response, details, form$)` receives 
    *   `error`: the `Error` object
    *   `details`: `details.type` is `'other'`
    *   `form$`: [Vueform instance](https://vueform.com/reference/vueform)

*   `@response(response, form$)` is not triggered

Alternatively, we can subscribe to `@error` event via `on()` method:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$" />
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.on('error', (response, details, form$) => {
    // ...
  })
})
</script>
```

vue

```
<template>
  <Vueform ref="form$" />
</template>

<script>
export default {
  mounted() {
    this.$refs.$form$.on('error', (response, details, form$) => {
      // ...
    })
  }
}
</script>
```

### Displaying Success and Error Messages [​](https://vueform.com/docs/handling-form-data#displaying-success-and-error-messages)

We can display success and error messages for our form once it received a response:

Composition API Options API

vue

```
<template>
  <Vueform
    @success="handleSuccess"
    @error="handleError"
  />
</template>

<script setup>
const handleSuccess = (response, form$) => {
  form$.messageBag.clear() // clear message bag
  form$.messageBag.append('Form submitted', 'message')
}

const handleError = (response, details, form$) => {
  form$.messageBag.clear() // clear message bag
  form$.messageBag.append('Form has error')
}
</script>
```

vue

```
<template>
  <Vueform
    @success="handleSuccess"
    @error="handleError"
  />
</template>

<script>
export default {
  methods: {
    handleSuccess(response, form$) {
      form$.messageBag.clear() // clear message bag
      form$.messageBag.append('Form submitted', 'message')
    },
    handleError(response, details, form$) {
      form$.messageBag.clear() // clear message bag
      form$.messageBag.append('Form has error')
    },
  }
}
</script>
```

There are other methods to `messageBag`. Check out [Custom Errors and Messages](https://vueform.com/docs/validating-elements#custom-errors-and-messages) chapter for more info.

#### Displaying Error Message for Elements [​](https://vueform.com/docs/handling-form-data#displaying-error-message-for-elements)

We can also add error message to specific elements:

Composition API Options API

vue

```
<template>
  <Vueform @error="handleError">
    <TextElement name="name" />
    <EmailElement name="email" />
  </Vueform>
</template>

<script setup>
const handleError = (response, details, form$) => {
  let messageBag = form$.el$('email').messageBag
  messageBag.clear() // clear message bag

  if (response.data.errors.email) {
    messageBag.append(response.data.errors.email) // eg. 'This email is already taken'
  }
}
</script>
```

vue

```
<template>
  <Vueform @error="handleError">
    <TextElement name="name" />
    <EmailElement name="email" />
  </Vueform>
</template>

<script>
export default {
  methods: {
    handleError(response, details, form$) {
      let messageBag = form$.el$('email').messageBag
      messageBag.clear() // clear message bag

      if (response.data.errors.email) {
        messageBag.append(response.data.errors.email) // eg. 'This email is already taken'
      }
    },
  }
}
</script>
```

Storing Form Data [​](https://vueform.com/docs/handling-form-data#storing-form-data)
------------------------------------------------------------------------------------

By default Vueform stores form data internally which can be accessed via [`data`](https://vueform.com/reference/vueform#property-data) property:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  console.log(form$.value.data)
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  mounted() {
    console.log(this.$refs.form$.data)
  }
}
</script>
```

> Every time we are referencing `form$.value` using Composition API (`setup()`) it's equivalent to `this.$refs.form$` in Options API.

### Storing Data Externally [​](https://vueform.com/docs/handling-form-data#storing-data-externally)

We can have an external object to store form data using `v-model`:

Composition API Options API

vue

```
<template>
  <Vueform v-model="data">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref } from 'vue'

const data = ref({})
</script>
```

vue

```
<template>
  <Vueform v-model="data">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  data: () => ({
    data: {}
  })
}
</script>
```

Contrary to regular `v-model`, two-way data binding is disabled by default in Vueform.

This means that when the form data is changed internally (eg. by user input) the changes **are** reflected in the `v-model` object, but not the other way around. If the `v-model` object is changed outside of Vueform, changes will not be synchronize back to the elements. This is also true for any inital data the `v-model` object might have.

Alternatively we can use `:model-value` and `@update:modelValue` (`:value` and `@input` in Vue.js 2) to separately set and update form data instead of using `v-model`:

Composition API Options API

vue

```
<template>
  <Vueform :model-value="data" @update:modelValue="updateData"> <!-- :value="data" @input="updateData" in Vue.js 2 -->
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref } from 'vue'

const data = ref({})

const updateData = (formData) => {
  data.value = formData
}
</script>
```

vue

```
<template>
  <Vueform :model-value="data" @update:modelValue="updateData"> <!-- :value="data" @input="updateData" in Vue.js 2 -->
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  data: () => ({
    data: {}
  }),
  methods: {
    updateData(formData) {
      this.data = formData
    }
  }
}
</script>
```

### Synchronizing External Data [​](https://vueform.com/docs/handling-form-data#synchronizing-external-data)

Even though two-way data binding is disabled by default, it can be enabled with `sync`:

Composition API Options API

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const data = ref({
  name: 'John Doe',
  email: 'john@doe.com'
})
</script>
```

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  data: () => ({
    data: {
      name: 'John Doe',
      email: 'john@doe.com'
    }
  })
}
</script>
```

When `sync` is enabled whenever the data if `v-model` object is changed, the changes will be reflected in both the external object and form elements.

> When using a lot elements or deeply nested elements the performance can be affected if `sync` is enabled. Make sure to only use `sync` if you actually need two-way data binding.

### Using Vuex to Store Data [​](https://vueform.com/docs/handling-form-data#using-vuex-to-store-data)

To use Vueform with Vuex first we need to register an object in state and a mutation:

js

```
// stores/forms.js

export default {
  state: {
    forms: {
      registration: {}
    }
  },
  mutations: {
    UPDATE_FORM_DATA(state, value) {
      state.forms[value.form] = value.data
    }
  }
}
```

Then we can use `v-model` with a computed `data` property:

Composition API Options API

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

const data = computed({
  get: () => store.state.forms.registration,
  set: (data) => store.commit('UPDATE_FORM_DATA', {
    form: 'registration',
    data: data,
  })
})
</script>
```

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  computed: {
    data: {
      get() {
        return this.$store.state.forms.registration
      },
      set(data) {
        this.$store.commit('UPDATE_FORM_DATA', {
          form: 'registration',
          data: data,
        })
      }
    }
  },
}
</script>
```

### Using Pinia to Store Data [​](https://vueform.com/docs/handling-form-data#using-pinia-to-store-data)

To use Vueform with Pinia, first let's create a Pinia store:

js

```
// stores/forms.js

import { defineStore } from 'pinia'

export const useFormsStore = defineStore('forms', {
  state: () => {
    return {
      registration: {}
    }
  },
})
```

Then we can create a computed `data` prop and use it with `v-model` and `sync:`

Composition API Options API

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { computed } from 'vue'
import { useFormsStore } from './stores/forms.js'

const store = useFormsStore()

const data = computed({
  get: () => store.registration,
  set: (data) => store.registration = data
})
</script>
```

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
import { mapStores } from 'pinia'
import { useFormsStore } from './stores/forms.js'

export default {
  computed: {
    ...mapStores(useFormsStore),
    data: {
      get() {
        return this.formsStore.registration
      },
      set(data) {
        this.formsStore.registration = data
      }
    }
  },
}
</script>
```

### Single Value Store [​](https://vueform.com/docs/handling-form-data#single-value-store)

Sometimes we have a single value that we want to make editable in a form. The problem is, that our form data must be an object as we can't add `v-model` to single elements.

In such scenarios, you can define a `computed` property that acts as the entire form model, constructed solely from the single value as its property:

Composition API Options API

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="username" label="Username" />
  </Vueform>
</template>

<script setup>
import { computed, reactive } from 'vue'
import { defineStore } from 'pinia'

const useUserStore = defineStore('user', {
  state: () => {
    return {
      username: 'johndoe'
    }
  },
})

const store = useUserStore()

const data = computed({
  get() {
    return reactive({
      username: store.username
    })
  },
  set(v) {
    store.username = v.username
  }
})
</script>
```

vue

```
<template>
  <Vueform v-model="data" sync>
    <TextElement name="username" label="Username" />
  </Vueform>
</template>

<script>
import { reactive } from 'cue'
import { defineStore, mapStores } from 'pinia'

const useUserStore = defineStore('user', {
  state: () => {
    return {
      username: 'johndoe'
    }
  },
})

export default {
  computed: {
    ...mapStores(useUserStore),
    data: {
      get() {
        return reactive({
          username: this.userStore.username
        })
      },
      set(data) {
        this.userStore.username = data.username
      }
    }
  },
}
</script>
```

Getting and Setting Form Data [​](https://vueform.com/docs/handling-form-data#getting-and-setting-form-data)
------------------------------------------------------------------------------------------------------------

If we aren't using `v-model` and Vueform data is handled internally we can still access and update it programmatically:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  console.log(form$.value.data) // outputs form data

  form$.value.update({ // updates form data
    name: 'John Doe',
    email: 'john@doe.com',
  })
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  mounted() {
    console.log(this.$refs.form$.data) // outputs form data

    this.$refs.form$.update({ // updates form data
      name: 'John Doe',
      email: 'john@doe.com',
    })
  }
}
</script>
```

We are using a `ref` to access `Vueform` component, which allows us to access its [API](https://vueform.com/reference/vueform#properties).

### Loading Form Data [​](https://vueform.com/docs/handling-form-data#loading-form-data)

When a form is mounted we can load initial data. Here's an example for loading user data from database:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const form$ = ref(null)

onMounted(async () => {
  const data = (await axios.get('/user/1')).data
  form$.value.load(data)
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
import axios from 'axios'

export default {
  async mounted() {
    const data = (await axios.get('/user/1')).data
    this.$refs.form$.value.load(data)
  }
}
</script>
```

When `load()` is used instead of `update()` all the elements will be cleared which don't have a value in the loaded data. This is useful when we load complete set of data and we want to make sure no previous values remain filled.

### Resetting Dirty State After Load [​](https://vueform.com/docs/handling-form-data#resetting-dirty-state-after-load)

When loading data the form fields will become `dirty`. You can reset the dirty state for all fields by using `await` on `load()`:

Composition API Options API

vue

```
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const form$ = ref(null)

onMounted(async () => {
  const data = (await axios.get('/user/1')).data
  await form$.value.load(data)
  form$.value.clean()
})
</script>
```

vue

```
<script>
import axios from 'axios'

export default {
  async mounted() {
    const data = (await axios.get('/user/1')).data
    await this.$refs.form$.value.load(data)
    this.$refs.form$.value.clean()
  }
}
</script>
```

### Formatting Loaded Form Data [​](https://vueform.com/docs/handling-form-data#formatting-loaded-form-data)

We can pass a function to the form's `:format-load` option, which transforms any data loaded through `load(data, true)`:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$" :format-load="formatLoadedData">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const formatLoadedData = (data) => {
  return {
    name: data.name.toUpperCase(),
    email: data.name.toLowerCase(),
  }
}

onMounted(() => {
  form$.value.load({
    name: 'John Doe',
    email: 'john@Doe.com'
  }, true) // `true` refers to `format: true` param
})
</script>
```

vue

```
<template>
  <Vueform ref="form$" :format-load="formatLoadedData">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  methods: {
    formatLoadedData(data) {
      return {
        name: data.name.toUpperCase(),
        email: data.name.toLowerCase(),
      }
    }
  },
  mounted() {
    this.$refs.form$.load({
      name: 'John Doe',
      email: 'john@Doe.com'
    }, true) // `true` refers to `format: true` param
  }
}
</script>
```

The loaded value will be:

js

```
{
  name: 'JOHN DOE',
  email: 'john@doe.com'
}
```

Getting and Setting Element Data [​](https://vueform.com/docs/handling-form-data#getting-and-setting-element-data)
------------------------------------------------------------------------------------------------------------------

We can also reach and update an element's data using the Vueform's [`el$(path)`](https://vueform.com/reference/vueform#method-el) method:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  const name = form$.value.el$('name')
  const email = form$.value.el$('email')

  // Get element value
  console.log(name.value) // getting `name` element value
  console.log(email.value) // getting `email` element value

  // Set element value
  name.update('John Doe') // setting `name` element value
  email.update('john@doe.com') // setting `email` element value
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" />
    <TextElement name="email" label="Email" />
  </Vueform>
</template>

<script>
export default {
  mounted(){
    const name = this.$refs.form$.el$('name')
    const email = this.$refs.form$.el$('email')

    // Get element value
    console.log(name.value) // getting `name` element value
    console.log(email.value) // getting `email` element value

    // Set element value
    name.update('John Doe') // setting `name` element value
    email.update('john@doe.com') // setting `email` element value
  }
}
</script>
```

### Object and Group Elements [​](https://vueform.com/docs/handling-form-data#object-and-group-elements)

Object and group elements can be reached with dot `.` syntax.

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <ObjectElement name="name" label="Name">
      <TextElement name="firstName" placeholder="First name" />
      <TextElement name="lastName" placeholder="Last name" />
    </ObjectElement>
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  const name = form$.value.el$('name')
  const firstName = form$.value.el$('name.firstName')
  const lastName = form$.value.el$('name.lastName')

  // Get element value
  console.log(name.value) // getting the whole `name` element value ({ firstname: '', lastname: '' })
  console.log(firstName.value) // getting the `firstName` element value
  console.log(lastName.value) // getting the `firstName` element value

  // Set element value
  name.update({ firstName: 'John', lastName: 'Doe' }) // setting `name` element value
  firstName.update('John') // setting `firstName` element value
  lastName.update('Doe') // setting `lastName` element value
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <ObjectElement name="name" label="Name">
      <TextElement name="firstName" placeholder="First name" />
      <TextElement name="lastName" placeholder="Last name" />
    </ObjectElement>
  </Vueform>
</template>

<script>
export default {
  mounted(){
    const name = this.$refs.form$.el$('name')
    const firstName = this.$refs.form$.el$('name.firstName')
    const lastName = this.$refs.form$.el$('name.lastName')

    // Get element value
    console.log(name.value) // getting the whole `name` element value as an object
    console.log(firstName.value) // getting the `firstName` element value
    console.log(lastName.value) // getting the `firstName` element value

    // Set element value
    name.update({ firstName: 'John', lastName: 'Doe' }) // setting `name` element value
    firstName.update('John') // setting `firstName` element value
    lastName.update('Doe') // setting `lastName` element value
  }
}
</script>
```

### List Elements [​](https://vueform.com/docs/handling-form-data#list-elements)

List elements can be reached with dot `.` syntax.

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <ListElement name="todos">
      <template #default="{ index }">
        <TextElement :name="index" placeholder="To-do" />
      </template>
    </ListElement>
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  const todos = form$.value.el$('todos')

  // Get element value
  console.log(todos.value) // getting the `todos` as an array

  // Set element value
  todos.update(['Write unit tests', 'Run tests' ]) // setting `todos` element value

  const firstTodo = form$.value.el$('todos.0')
  const secondTodo = form$.value.el$('todos.1')

  console.log(firstTodo.value) // getting 'Write unit tests'
  console.log(secondTodo.value) // getting 'Run unit tests'

  // Set element value
  firstTodo.update('Write e2e tests') // setting `todos.0` element value
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <ListElement name="todos">
      <template #default="{ index }">
        <TextElement :name="index" placeholder="To-do" />
      </template>
    </ListElement>
  </Vueform>
</template>

<script>
export default {
  mounted(){
    const todos = this.$refs.form$.el$('todos')

    // Get element value
    console.log(todos.value) // getting the `todos` as an array

    // Set element value
    todos.update(['Write unit tests', 'Run tests' ]) // setting `todos` element value

    const firstTodo = this.$refs.form$.el$('todos.0')
    const secondTodo = this.$refs.form$.el$('todos.1')

    console.log(firstTodo.value) // getting 'Write unit tests'
    console.log(secondTodo.value) // getting 'Run unit tests'

    // Set element value
    firstTodo.update('Write e2e tests') // setting `todos.0` element value
  }
}
</script>
```

### Nested List Elements [​](https://vueform.com/docs/handling-form-data#nested-list-elements)

Object and group elements can be reached with dot `.` syntax.

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <ListElement name="todos">
      <template #default="{ index }">
        <ObjectElement :name="index">
          <TextElement name="todo" placeholder="To-do" />
          <ToggleElement name="ready" text="Ready" />
        </ObjectElement>
      </template>
    </ListElement>
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  const todos = form$.value.el$('todos')

  // Get element value
  console.log(todos.value) // getting the `todos` as an array

  // Set element value
  todos.update([
    { todo: 'Write unit tests', ready: false },
    { todo: 'Run unit tests', ready: false },
  ]) // setting `todos` element value

  const firstTodoReady = form$.value.el$('todos.0.ready')

  console.log(firstTodoReady.value) // getting 'false'

  // Set element value
  firstTodoReady.update(true) // setting `todos.0.ready` element value
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <ListElement name="todos">
      <template #default="{ index }">
        <ObjectElement :name="index">
          <TextElement name="todo" placeholder="To-do" />
          <ToggleElement name="ready" text="Ready" />
        </ObjectElement>
      </template>
    </ListElement>
  </Vueform>
</template>

<script>
export default {
  mounted(){
    const todos = this.$refs.form$.el$('todos')

    // Get element value
    console.log(todos.value) // getting the `todos` as an array

    // Set element value
    todos.update([
      { todo: 'Write unit tests', ready: false },
      { todo: 'Run unit tests', ready: false },
    ]) // setting `todos` element value

    const firstTodoReady = this.$refs.form$.el$('todos.0.ready')

    console.log(firstTodoReady.value) // getting 'false'

    // Set element value
    firstTodoReady.update(true) // setting `todos.0.ready` element value
  }
}
</script>
```

### Formatting Loaded Element Data [​](https://vueform.com/docs/handling-form-data#formatting-loaded-element-data)

We can pass a function to the form's `:format-load` option, which transforms any data loaded through `load(data, true)`:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" :format-load="formatLoadedName" />
    <TextElement name="email" label="Email" :format-load="formatLoadedEmail" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const formatLoadedName = (value) => {
  return value.toUpperCase()
}

const formatLoadedEmail = (value) => {
  return value.toLowerCase()
}

onMounted(() => {
  form$.value.load({
    name: 'John Doe',
    email: 'john@Doe.com'
  }, true)
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <TextElement name="name" label="Name" :format-load="formatLoadedName" />
    <TextElement name="email" label="Email" :format-load="formatLoadedEmail" />
  </Vueform>
</template>

<script>
export default {
  methods: {
    formatLoadedName (value) {
      return value.toUpperCase()
    },
    formatLoadedEmail (value) {
      return value.toLowerCase()
    },
  },
  mounted() {
    this.$refs.form$.load({
      name: 'John Doe',
      email: 'john@Doe.com'
    }, true)
  }
}
</script>
```

The loaded value will be:

js

```
{
  name: 'JOHN DOE',
  email: 'john@doe.com'
}
```

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
