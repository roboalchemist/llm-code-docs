# Source: https://vuelidate.js.org/

Title: Vuelidate | A Vue.js library.

URL Source: https://vuelidate.js.org/

Markdown Content:
Getting started
---------------

* * *

Package content
---------------

Simple, lightweight model-based validation for Vue.js

You can read the [introduction post](http://monterail.com/blog/2016/rethinking-validations-for-vue-js/) for more insight on how this solution differs from other validation libraries.

If you want to use Vuelidate with Vue 3, use the [Vuelidate Next](https://vuelidate-next.netlify.app/) version.

Installation
------------

Package is installable via npm

`npm install vuelidate --save`

Basic usage
-----------

You can import the library and use as a Vue plugin to enable the functionality globally on all components containing validation configuration.

JavaScript

```
import Vue from 'vue'
import Vuelidate from 'vuelidate'
Vue.use(Vuelidate)
```

Alternatively it is possible to import a mixin directly to components in which it will be used.

JavaScript

```
import { validationMixin } from 'vuelidate'

var Component = Vue.extend({
  mixins: [validationMixin],
  validations: { ... }
})
```

If you prefer using require, it can be used instead of import statements. This works especially great with destructuring syntax.

JavaScript

```
const { validationMixin, default: Vuelidate } = require('vuelidate')
const { required, minLength } = require('vuelidate/lib/validators')
```

The browser-ready bundle is also provided in the package.

Html

`<script src="vuelidate/dist/vuelidate.min.js"></script>`

JavaScript

```
// global
Vue.use(window.vuelidate.default)

// local mixin
var validationMixin = window.vuelidate.validationMixin
```

Check out the [JSFiddle example](https://jsfiddle.net/Frizi/b5v4faqf/) which uses this setup.

Examples
--------

* * *

Basic form
----------

For each value you want to validate, you have to create a key inside validations options. You can specify when input becomes dirty by using appropriate event on your input box.

Note that in this example, the red border, red text, and error message visibility are driven by the presence or absence of the form-group--error class on the surrounding div. Any markup relating to validation errors will show on initial load unless using a method like this, or by using validations without v-model (next section).

Name

Field is required

"$v.name":

"required":false

"minLength":true

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"required":1 property

"minLength":2 properties

Age

Must be between 20 and 30

Blur to see changes

"$v.age":

"between":false

"$model":0

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"between":3 properties

Code sample

JavaScript

```
import { required, minLength, between } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      name: '',
      age: 0
    }
  },
  validations: {
    name: {
      required,
      minLength: minLength(4)
    },
    age: {
      between: between(20, 30)
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.name.$error }")
    label.form__label Name
    input.form__input(v-model.trim="$v.name.$model")
  .error(v-if="!$v.name.required") Field is required
  .error(v-if="!$v.name.minLength")
    | Name must have at least {{$v.name.$params.minLength.min}} letters.
  tree-view(:data="$v.name", :options="{rootObjectKey: '$v.name', maxDepth: 2}")

  .form-group(:class="{ 'form-group--error': $v.age.$error }")
    label.form__label Age
    input.form__input(v-model.trim.lazy="$v.age.$model")
  .error(v-if="!$v.age.between")
    | Must be between {{$v.age.$params.between.min}} and {{$v.age.$params.between.max}}

  span(tabindex="0") Blur to see changes
  tree-view(:data="$v.age", :options="{rootObjectKey: '$v.age', maxDepth: 2}")
```

Without v-model
---------------

In case you don't want to modify your model directly, you can still use separate :input and @event bindings. This is especially useful if you are using data from external source, like Vuex store or props. In that case you have to manually take care of setting the $dirty by calling $touch() method when appropriate.

Name

Field is required

Age

Must be between 20 and 30

Blur to see changes

Code sample

JavaScript

```
import { required, minLength, between } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      name: '',
      age: 0
    }
  },
  validations: {
    name: {
      required,
      minLength: minLength(4)
    },
    age: {
      between: between(20, 30)
    }
  },

  methods: {
    setName(value) {
      this.name = value
      this.$v.name.$touch()
    },
    setAge(value) {
      this.age = value
      this.$v.age.$touch()
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.name.$error }")
    label.form__label Name
    input.form__input(v-model.trim="name", @input="setName($event.target.value)")
  .error(v-if="!$v.name.required") Field is required
  .error(v-if="!$v.name.minLength")
    | Name must have at least {{$v.name.$params.minLength.min}} letters.

  .form-group(:class="{ 'form-group--error': $v.age.$error }")
    label.form__label Age
    input.form__input(:value="age" @change="setAge($event.target.value)")
  .error(v-if="!$v.age.between")
    | Must be between {{$v.age.$params.between.min}} and {{$v.age.$params.between.max}}
  span(tabindex="0") Blur to see changes
```

Form submission
---------------

A common thing to do with validated forms is to check their validity before submission. You can accomplish this easily by checking for $invalid state before sending any requests.

Code sample

JavaScript

```
import { required, minLength } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      name: '',
      age: 0,
      submitStatus: null
    }
  },
  validations: {
    name: {
      required,
      minLength: minLength(4)
    }
  },
  methods: {
    submit() {
      console.log('submit!')
      this.$v.$touch()
      if (this.$v.$invalid) {
        this.submitStatus = 'ERROR'
      } else {
        // do your submit logic here
        this.submitStatus = 'PENDING'
        setTimeout(() => {
          this.submitStatus = 'OK'
        }, 500)
      }
    }
  }
}
```

Pug

```
form(@submit.prevent="submit")
  .form-group(:class="{ 'form-group--error': $v.name.$error }")
    label.form__label Name
    input.form__input(v-model.trim="$v.name.$model")
  .error(v-if="!$v.name.required") Name is required
  .error(v-if="!$v.name.minLength")
    | Name must have at least {{$v.name.$params.minLength.min}} letters.

  button.button(type="submit" :disabled="submitStatus === 'PENDING'") Submit!

  p.typo__p(v-if="submitStatus === 'OK'") Thanks for your submission!
  p.typo__p(v-if="submitStatus === 'ERROR'") Please fill the form correctly.
  p.typo__p(v-if="submitStatus === 'PENDING'") Sending...
```

Contextified validators
-----------------------

You can link related fields by contextified validators. An example of this being sameAs builtin validator.

Password

Password is required.

Repeat password

"$v":

"password":

"required":false

"minLength":true

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":2 properties

"repeatPassword":

"sameAsPassword":true

"$model":""

"$invalid":false

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"$model":null

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"password":null

"repeatPassword":null

Code sample

JavaScript

```
import { required, sameAs, minLength } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      password: '',
      repeatPassword: ''
    }
  },
  validations: {
    password: {
      required,
      minLength: minLength(6)
    },
    repeatPassword: {
      sameAsPassword: sameAs('password')
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.password.$error }")
    label.form__label Password
    input.form__input(v-model.trim="$v.password.$model")
  .error(v-if="!$v.password.required") Password is required.
  .error(v-if="!$v.password.minLength")
    | Password must have at least {{ $v.password.$params.minLength.min }} letters.

  .form-group(:class="{ 'form-group--error': $v.repeatPassword.$error }")
    label.form__label Repeat password
    input.form__input(v-model.trim="$v.repeatPassword.$model")
  .error(v-if="!$v.repeatPassword.sameAsPassword") Passwords must be identical.

  tree-view(:data="$v", :options="{rootObjectKey: '$v', maxDepth: 2}")
```

Data nesting
------------

You can nest validators to match your data as deep as you want. Parent validator is $invalid when any of its children validators reports an $invalid state. This might be very useful for overall form validation.

Nested A

Field is required.

Nested B

Field is required.

"$v.form":

"nestedA":

"required":false

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"nestedB":

"required":false

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"$model":

"nestedA":""

"nestedB":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"nestedA":null

"nestedB":null

Code sample

JavaScript

```
import { required } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      form: {
        nestedA: '',
        nestedB: ''
      }
    }
  },
  validations: {
    form: {
      nestedA: {
        required
      },
      nestedB: {
        required
      }
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.form.nestedA.$error }")
    label.form__label Nested A
    input.form__input(v-model.trim="$v.form.nestedA.$model")
  .error(v-if="!$v.form.nestedA.required") Field is required.
  .form-group(:class="{ 'form-group--error': $v.form.nestedB.$error }")
    label.form__label Nested B
    input.form__input(v-model.trim="$v.form.nestedB.$model")
  .error(v-if="!$v.form.nestedB.required") Field is required.

  .form-group(:class="{ 'form-group--error': $v.form.$error }")
  .error(v-if="$v.form.$error") Form is invalid.

  tree-view(:data="$v.form", :options="{rootObjectKey: '$v.form', maxDepth: 2}")
```

$error vs $anyError
-------------------

There are two common ways of considering if an error should be displayed. It is important to understand which one suits your use case better. You can use either $error or $anyError validation property, or by extension, the low-level variants: $dirty or $anyDirty. Note that this documentation uses mainly $error variant in it's examples, but the choice is yours to make.

Field A

Field A is required.

Field B

Field B is required.

Validation status:

*   Field A is $invalid.
*   Field B is $invalid.
*   Form is $invalid.

Code sample

JavaScript

```
import { required, minLength } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      fieldA: '',
      fieldB: ''
    }
  },
  validations: {
    fieldA: {
      required,
      minLength: minLength(3)
    },
    fieldB: {
      required,
      minLength: minLength(3)
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.fieldA.$error }")
    label.form__label Field A
    input.form__input(v-model.trim="$v.fieldA.$model")
  .error(v-if="!$v.fieldA.required") Field A is required.
  .error(v-if="!$v.fieldA.minLength")
    | Field A must have at least {{$v.fieldA.$params.minLength.min}} letters.
  .form-group(:class="{ 'form-group--error': $v.fieldB.$error }")
    label.form__label Field B
    input.form__input(v-model.trim="$v.fieldB.$model")
  .error(v-if="!$v.fieldB.required") Field B is required.
  .error(v-if="!$v.fieldB.minLength")
    | Field B must have at least {{$v.fieldB.$params.minLength.min}} letters.

  .form-group
    button.button(@click="$v.$reset") $reset
  .form-group
    label.form__label Validation status:
    ul.list__ul
      li(v-if="$v.fieldA.$invalid") Field A is <kbd>$invalid</kbd>.
      li(v-if="$v.fieldA.$error") Field A has <kbd>$error</kbd> and <kbd>$anyError</kbd>.

      li(v-if="$v.fieldB.$invalid") Field B is <kbd>$invalid</kbd>.
      li(v-if="$v.fieldB.$error") Field B has <kbd>$error</kbd> and <kbd>$anyError</kbd>.

      li(v-if="$v.$invalid") Form is <kbd>$invalid</kbd>.
      li(v-else) All fine.
      li(v-if="$v.$error"): strong Form has <kbd>$error</kbd>.
      li(v-if="$v.$anyError"): strong Form has <kbd>$anyError</kbd>.
```

Validation Groups
-----------------

If you want to create a validator that groups many otherwise unrelated fields together, you can create a validation group.

Flat A

Field is required.

Flat B

Field is required.

Nested field

Field is required.

"$v.validationGroup":

"flatA":

"required":false

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"flatB":

"required":false

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"forGroup.nested":

"required":false

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"$model":null

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"flatA":null

"flatB":null

"forGroup.nested":null

Code sample

JavaScript

```
import { required } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      flatA: '',
      flatB: '',
      forGroup: {
        nested: ''
      }
    }
  },
  validations: {
    flatA: { required },
    flatB: { required },
    forGroup: {
      nested: { required }
    },
    validationGroup: ['flatA', 'flatB', 'forGroup.nested']
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.flatA.$error }")
    label.form__label Flat A
    input.form__input(v-model.trim="$v.flatA.$model")
  .error(v-if="!$v.flatA.required") Field is required.
  .form-group(:class="{ 'form-group--error': $v.flatB.$error }")
    label.form__label Flat B
    input.form__input(v-model.trim="$v.flatB.$model")
  .error(v-if="!$v.flatB.required") Field is required.
  .form-group(:class="{ 'form-group--error': $v.forGroup.nested.$error }")
    label.form__label Nested field
    input.form__input(v-model.trim="$v.forGroup.nested.$model")
  .error(v-if="!$v.forGroup.nested.required") Field is required.

  .form-group(:class="{ 'form-group--error': $v.validationGroup.$error }")
  .error(v-if="$v.validationGroup.$error") Group is invalid.

  tree-view(:data="$v.validationGroup", :options="{rootObjectKey: '$v.validationGroup', maxDepth: 2}")
```

Collections validation
----------------------

Array support with $each keyword

Name for 0

Name for 1

Name is required.

List must have at least 3 elements.

"$v.people":

"required":true

"minLength":false

"$each":

"0":9 properties

"1":9 properties

"$iter":2 properties

"$model":

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":2 properties

"$model":

0:1 property

1:1 property

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"$each":null

"required":1 property

"minLength":2 properties

Code sample

JavaScript

```
import { required, minLength } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      people: [
        {
          name: 'John'
        },
        {
          name: ''
        }
      ]
    }
  },
  validations: {
    people: {
      required,
      minLength: minLength(3),
      $each: {
        name: {
          required,
          minLength: minLength(2)
        }
      }
    }
  }
}
```

Pug

```
div
  div(v-for="(v, index) in $v.people.$each.$iter")
    .form-group(:class="{ 'form-group--error': v.$error }")
      label.form__label Name for {{ index }}
      input.form__input(v-model.trim="v.name.$model")
    .error(v-if="!v.name.required") Name is required.
    .error(v-if="!v.name.minLength")
      | Name must have at least {{ v.name.$params.minLength.min }} letters.
  div
    button.button(@click="people.push({name: ''})") Add
    button.button(@click="people.pop()") Remove
  .form-group(:class="{ 'form-group--error': $v.people.$error }")
  .error(v-if="!$v.people.minLength")
    | List must have at least {{ $v.people.$params.minLength.min }} elements.
  .error(v-else-if="!$v.people.required") List must not be empty.
  .error(v-else-if="$v.people.$error") List is invalid.
  button.button(@click="$v.people.$touch") $touch
  button.button(@click="$v.people.$reset") $reset
  tree-view(:data="$v.people", :options="{rootObjectKey: '$v.people', maxDepth: 2}")
```

Asynchronous validation
-----------------------

Async support is provided out of the box. Just use a validator that returns a promise. Promise's success value is used for validation directly, failed promise just fails the validation and throws the error.

Any component's data has to be accessed synchronously for correct reactive behaviour. Store it as a variable in validator's scope if you need to use it in any asynchronous callback, for example in .then.

Validator is evaluated on every data change, as it is essentially a computed value. If you need to throttle an async call, do it on your data change event, not on the validator itself. You may end up with broken Vue observables otherwise.

Username

Username is required.

"$v.username":

"required":false

"isUnique":true

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"required":1 property

"isUnique":null

Code sample

JavaScript

```
import { required } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      username: ''
    }
  },
  validations: {
    username: {
      required,
      isUnique(value) {
        // standalone validator ideally should not assume a field is required
        if (value === '') return true

        // simulate async call, fail for all logins with even length
        return new Promise((resolve, reject) => {
          setTimeout(() => {
            resolve(typeof value === 'string' && value.length % 2 !== 0)
          }, 350 + Math.random() * 300)
        })
      }
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.username.$error, 'form-group--loading': $v.username.$pending }")
    label.form__label Username
    input.form__input(v-model.trim="$v.username.$model")
  .error(v-if="!$v.username.required")
    | Username is required.
  .error(v-if="!$v.username.isUnique")
    | This username is already registered.
  tree-view(:data="$v.username", :options="{rootObjectKey: '$v.username', maxDepth: 2}")
```

The async/await syntax is fully supported. It works especially great in combination with Fetch API.

JavaScript

```
validations: {
  async isUnique (value) {
    if (value === '') return true
    const response = await fetch(`/api/unique/${value}`)
    return Boolean(await response.json())
  }
}
```

Delayed validation errors
-------------------------

You can do anything you need with the $touch state, no matter how fancy your requirements are. It all boils down to calling $touch and $reset in the right moment. As an example of that, here is an easy to follow implementation of delayed error based on custom setTimeout logic. It triggers one second after last input.

Name

Field is required

"$v.name":

"required":false

"minLength":true

"maxLength":true

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"required":1 property

"minLength":2 properties

"maxLength":2 properties

Code sample

JavaScript

```
import { required, minLength, maxLength } from 'vuelidate/lib/validators'

const touchMap = new WeakMap()

export default {
  data() {
    return {
      name: ''
    }
  },
  validations: {
    name: {
      required,
      minLength: minLength(4),
      maxLength: maxLength(15)
    }
  },
  methods: {
    delayTouch($v) {
      $v.$reset()
      if (touchMap.has($v)) {
        clearTimeout(touchMap.get($v))
      }
      touchMap.set($v, setTimeout($v.$touch, 1000))
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.name.$error }")
    label.form__label Name
    input.form__input(v-model.trim="name" @input="delayTouch($v.name)")
  .error(v-if="!$v.name.required") Field is required
  .error(v-if="!$v.name.minLength")
    | Name must have at least {{$v.name.$params.minLength.min}} letters.
  .error(v-if="!$v.name.maxLength")
    | Name must have at most {{$v.name.$params.maxLength.max}} letters.

  tree-view(:data="$v.name", :options="{rootObjectKey: '$v.name', maxDepth: 2}")
```

Accessing validator parameters
------------------------------

You can access information about your validations through `$params` of a parent validator. This is be useful for reporting errors to users.

Username

Field is required.

Password

Field is required.

"$v":

"form":

"userName":10 properties

"password":10 properties

"$model":2 properties

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":2 properties

"$model":null

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"form":null

Code sample

JavaScript

```
import { required, minLength } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      form: {
        userName: '',
        password: ''
      }
    }
  },
  validations: {
    form: {
      userName: {
        required,
        minLength: minLength(5)
      },
      password: {
        required,
        minLength: minLength(8)
      }
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.form.userName.$error }")
    label.form__label Username
    input.form__input(v-model.trim="$v.form.userName.$model")
  .error(v-if="!$v.form.userName.required")
    | Field is required.
  .error(v-if="!$v.form.userName.minLength")
    | Field must have at least {{ $v.form.userName.$params.minLength.min }} characters.
  .form-group(:class="{ 'form-group--error': $v.form.password.$error }")
    label.form__label Password
    input.form__input(v-model.trim="$v.form.password.$model" type="password")
  .error(v-if="!$v.form.password.required")
    | Field is required.
  .error(v-if="!$v.form.password.minLength")
    | Field must have at least {{ $v.form.password.$params.minLength.min }} characters.

  .form-group(:class="{ 'form-group--error': $v.form.$error }")
    .error(v-if="$v.form.$error") Form is invalid.

  tree-view(:data="$v", :options="{rootObjectKey: '$v', maxDepth: 2}")
```

Dynamic validation schema
-------------------------

Validations schema can be a function, which will make it dynamic and possibly dependant on your model's data. Recomputations will happen automatically as if it was a computed value. Validation's $dirty state will be preserved as long as the key name won't change or disappear.

Name

Has description?

"$v":

"name":

"required":false

"$model":""

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"$model":null

"$invalid":true

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"name":null

Code sample

JavaScript

```
import { required } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      hasDescription: false,
      name: '',
      description: ''
    }
  },
  validations() {
    if (!this.hasDescription) {
      return {
        name: {
          required
        }
      }
    } else {
      return {
        name: {
          required
        },
        description: {
          required
        }
      }
    }
  }
}
```

Pug

```
div
  .form-group(:class="{ 'form-group--error': $v.name.$error}")
    label.form__label Name
    input.form__input(v-model.trim="$v.name.$model")
  .form-group
    label(for="hasDesc").form__label Has description?
    .toggle
      input#hasDesc(type="checkbox", v-model="hasDescription")
      label(for="hasDesc")
        .toggle__switch
  .form-group(v-if="hasDescription", :class="{ 'form-group--error': $v.description.$error}")
    label.form__label Description
    input.form__input(v-model.trim="$v.description.$model")
  tree-view(:data="$v", :options="{rootObjectKey: '$v', maxDepth: 2}")
```

Dynamic parameters
------------------

Because the whole validation process is based on computed properties, nothing prevents you from making the validator name dynamic. Such cases allows for very dynamic behaviour even when your data is changing in time.

Validator name

Dynamic min length

Name

"$v":

"name":

"validatorName":true

"$model":""

"$invalid":false

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":1 property

"$model":null

"$invalid":false

"$dirty":false

"$anyDirty":false

"$error":false

"$anyError":false

"$pending":false

"$params":

"name":null

Code sample

JavaScript

```
import { minLength } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      name: '',
      minLength: 3,
      valName: 'validatorName'
    }
  },
  validations() {
    return {
      name: {
        [this.valName]: minLength(this.minLength)
      }
    }
  }
}
```

Pug

```
div
  .form-group
    label.form__label Validator name
    input.form__input(v-model.trim="valName" @input="$v.$touch()")
  .form-group
    label.form__label Dynamic min length
    input.form__input(type="number" v-model.number="minLength" @input="$v.$touch()")
  .form-group(:class="{ 'form-group--error': $v.name.$error }")
    label.form__label Name
    input.form__input(v-model.trim="$v.name.$model")
  .error(v-if="!$v.name[valName]") Field is invalid
  tree-view(:data="$v", :options="{rootObjectKey: '$v', maxDepth: 2}")
```

API
---

* * *

There are two distinct structures present in _vuelidate_:

*   validations component option - the definition of your validation
*   $v structure - an object in your viewmodel that holds the validation state

$v values
---------

$v model represents the current state of validation. It does so by defining a set of properties which hold the output of user defined validation functions, following the validations option structure. The presence of those special reserved keywords means that you cannot specify your own validators with that name.

| Name | Type | Description |
| --- | --- | --- |
| $invalid | **boolean** | Indicates the state of validation for given model. becomes true when any of it's child validators specified in options returns a **falsy** value. In case of validation groups, all grouped validators are considered. |
| $dirty | **boolean** | A flag representing if the field under validation was touched by the user at least once. Usually it is used to decide if the message is supposed to be displayed to the end user. You can manage this flag manually by using $touch and $reset methods. It is set automatically when writing to $model value. The $dirty flag is considered true if given model was $touch ed or **all of it's children** are $dirty. |
| $anyDirty | **boolean** | A flag very similar to $dirty, with one exception. The $anyDirty flag is considered true if given model was $touch ed or **any of it's children** are $anyDirty. |
| $model | **any** | A reference to the original validated model. Reading this value will always give you exactly the same value as if you referenced the model directly. That means this.$v.value.$model is equivalent to this.value when read. Writing to that value will update the model and invoke $touch method automatically. This is very useful to use as v-model payload, providing a way of automatically marking given field as $dirty on first touch. Pairs well with .lazy modifier. |
| $error | **boolean** | Convenience flag to easily decide if a message should be displayed. Equivalent to this.$dirty && !this.$pending && this.$invalid. |
| $anyError | **boolean** | Convenience flag to easily decide if a message should be displayed. A variant that considers error to be displayed when itself or **at least one** of its children has $error equal to true. |
| $pending | **boolean** | Indicates if any child async validator is currently pending. Always false if all validators are synchronous. |
| $params | **object** | Contains types and parameters of all provided validators at the current level, as well as types and parameters of child validation groups, which may be declared using `withParams`. Useful as an input to your error rendering system. Safe to use in translated text. |
| $each | **object** | Holds all validation models of collection validator. Always preserves the keys of original model, but also holds additional names for all associated validators and special values like $invalid. A special $iter fields is preferred for usage inside v-for directives. |
| $iter | **object** | Only present as direct child of $each objects. Holds all validation models of collection validator and nothing else. It can be safely referenced in the v-for loop iterating over all your model validators. See [Collections Validation](https://vuelidate.js.org/#sub-collections-validation) for usage example. |

$v methods
----------

A set of methods to control the validation model. Accessible on every level of nesting. All methods are meant to be used on any event handler you wish. There is no extra syntax to decide when the dirty flag should be set. Just use standard @input or @blur bindings.

| Name | Description |
| --- | --- |
| $touch | Sets the $dirty flag of the model and all its children to true recursively. |
| $reset | Sets the $dirty flag of the model and all its children to false recursively. |
| $flattenParams | Returns an array of leaf params. |

Config keywords
---------------

| Name | Type | Description |
| --- | --- | --- |
| $each | **object** | A definition of nested validation applied to each prop of given model separately. Perfect for validation arrays, but can be used with any object or collection. |
| $trackBy | **string || func** | Must be a direct children of $each, but is optional. Defines the accessor to object's property by which $each tracks it's child models. Necessary to correctly preserve $dirty flag on random insertions. If this property not preset, the key is used for tracking. |

Validators
----------

* * *

_vuelidate_ comes with a set of builtin validators that you can just require and use, but it doesn't end there. All of those are just simple predicates - functions of data into boolean, which denotes if data is valid. You can easily write your own or use any function in this shape from any library you already have, like _.conformsTo from _lodash_ or higher order functions and chains like R.cond from _ramda_. Think of the possibilities.

This documentation presents every builtin validator with short description and presents an example custom validator implementation to help understanding them and writing your own as easy as possible.

Builtin validators
------------------

To use any of builtin validators, you have to import it from vuelidate library.

JavaScript

`import { required, maxLength } from 'vuelidate/lib/validators'`
You can also import specific validators directly, to avoid loading unused ones in case your bundler doesn't support tree shaking. This is not required for Rollup or Webpack 2 among others.

JavaScript

```
import required from 'vuelidate/lib/validators/required'
import maxLength from 'vuelidate/lib/validators/maxLength'
```

It is possible to use validators directly in browser by using a browser-ready bundle. Keep in mind this will always load all builtin validators at once.

Html

`<script src="vuelidate/dist/validators.min.js"></script>`

JavaScript

```
var required = validators.required
var maxLength = validators.maxLength
```

Here is a full list of provided validators.

| Name | Meta parameters | Description |
| --- | --- | --- |
| required | _none_ | Requires non-empty data. Checks for empty arrays and strings containing only whitespaces. |
| requiredIf | locator * | Requires non-empty data only if provided property or predicate is true. |
| requiredUnless | locator * | Requires non-empty data only if provided property or predicate is false. |
| minLength | min length | Requires the input to have a minimum specified length, inclusive. Works with arrays. |
| maxLength | max length | Requires the input to have a maximum specified length, inclusive. Works with arrays. |
| minValue | min | Requires entry to have a specified minimum numeric value or Date. |
| maxValue | max | Requires entry to have a specified maximum numeric value or Date. |
| between | min, max | Checks if a number or Date is in specified bounds. Min and max are both inclusive. |
| alpha | _none_ | Accepts only alphabet characters. |
| alphaNum | _none_ | Accepts only alphanumerics. |
| numeric | _none_ | Accepts only numerics. |
| integer | _none_ | Accepts positive and negative integers. |
| decimal | _none_ | Accepts positive and negative decimal numbers. |
| email | _none_ | Accepts valid email addresses. Keep in mind you still have to carefully verify it on your server, as it is impossible to tell if the address is real without sending verification email. |
| ipAddress | _none_ | Accepts valid IPv4 addresses in dotted decimal notation like _127.0.0.1_. |
| macAddress | separator=':' | Accepts valid MAC addresses like _00:ff:11:22:33:44:55_. Don't forget to call it macAddress(), as it has optional parameter. You can specify your own separator instead of ':'. Provide empty separator macAddress('') to validate MAC addresses like _00ff1122334455_. |
| sameAs | locator * | Checks for equality with a given property. |
| url | _none_ | Accepts only URLs. |
| or | validators... | Passes when at least one of provided validators passes. |
| and | validators... | Passes when all of provided validators passes. |
| not | validator | Passes when provided validator would not pass, fails otherwise. Can be chained with other validators like not(sameAs('field')). |
| withParams | $params, validator | Not really a validator, but a validator modifier. Adds a $params object to the provided validator. Can be used on validation functions or even entire nested field validation objects. Useful for creating your own custom validators. |

* Locator can be either a sibling property name or a function. When provided as a function, it receives the model under validation as argument and this is bound to the component instance so you can access all its properties and methods, even in the scope of a nested validation.

Example of conditional validations using a locator meta parameter:

JavaScript

```
export default {
  ...,
  data() {
    return {
      field: "foo",
      nested: {
        field: "bar",
        someFlag: true
      }
    }
  },
  computed: {
    isOptional() {
      return true // some conditional logic here...
    }
  },
  validations: {
    field: {
      required: requiredUnless('isOptional')
    },
    nested: {
      required: requiredIf(function (nestedModel) {
        return !this.isOptional && nestedModel.someFlag
      })
    }
  }
}
```

Validator parameters
--------------------

Every validator can save parameters. Validators are responsible for saving their type and parameters, because they are simple functions, and we may want to inform the user about them.

Use withParams to apply parameters to a validator. Declared parameters bubble up by one level, so they are included in the $params of the parent validation object. Vuelidate is designed in a way that does not allow the validation result to directly include params.

You may call the $flattenParams method on a validation object to get an array of validator params for all validators that exist in that validation object. For example, let's say a validation object contains a between validator to check that a value is between 5 and 10. Calling $flattenParams returns the following array.

`[{ path: [], name: 'between', params: { type: 'between', min: 5, max: 10 } }]`

Custom Validators
-----------------

* * *

You can easily write custom validators and combine them with builtin ones, as those are just a simple predicate functions.

Simplest example
----------------

Suppose you want a validator that checks if strings contains _cool_ substring in it. The way to approach this is to use normal javascript function that checks that.

JavaScript

```
const mustBeCool = (value) => value.indexOf('cool') >= 0
```

The second part is actually applying your validator. You can do it exactly the same way as with builtin ones.

JavaScript

```
validations: {
  myField: {
    required,
    mustBeCool
  }
}
```

Optional validator
------------------

Pattern presented above is often good enough, but this validator will always return false for empty input. This is not correct when your input is considered optional. For this reason, there exist a req helper, which is kinda stripped-down version of required validator. You can use it to make your validator behave well in presence of optional fields, that is the ones without required validator.

JavaScript

```
import { helpers } from 'vuelidate/lib/validators'
const mustBeCool = (value) => !helpers.req(value) || value.indexOf('cool') >= 0

// ...

validations: {
  myField: {
    mustBeCool
  }
}
```

If your validator needs to provide parameters, you can simply create a higher order function that returns the actual validator, like in between builtin validator.

JavaScript

```
import { helpers } from 'vuelidate/lib/validators'
const contains = (param) =>
  (value) => !helpers.req(value) || value.indexOf(param) >= 0

// ...

validations: {
  myField: {
    mustBeCool: contains('cool')
  }
}
```

$props support
--------------

This is all fine if you are not using the feature of $props property, for example in your translation system. To make your validator also generate some useful $props, you can use withParams helper. The easiest case is to simply add type metadata, which might be useful in choosing correct translation string later on.

JavaScript

```
import { helpers } from 'vuelidate/lib/validators'
const mustBeCool = helpers.withParams(
  { type: 'mustBeCool' },
  (value) => !helpers.req(value) || value.indexOf('cool') >= 0
)

// ...

console.log(this.$v.myField.$params.mustBeCool)
// -> { type: 'mustBeCool' }
```

The same behaviour extends to higher order validators, ones with extra parameters. You just must be careful to wrap the **inner** function with withParams call, as follows.

JavaScript

```
import { helpers } from 'vuelidate/lib/validators'
const contains = (param) =>
  helpers.withParams(
    { type: 'contains', value: param },
    (value) => !helpers.req(value) || value.indexOf(param) >= 0
  )

// ...
validations: {
  myField: {
    mustBeCool: contains('cool')
  }
}

// ...
console.log(this.$v.myField.$params.mustBeCool)
// -> { type: 'contains', value: 'cool' }
```

accessing component
-------------------

In more complex cases when access to the whole model is necessary, like sameAs, make use of the function context (this) to access any value on your component or use provided parentVm to access sibling properties.

JavaScript

```
// both equivalent
const otherFieldContainsMe =
  (value, vm) => vm.other.nested.field.contains(value)

function otherFieldContainsMe (value) {
  return this.other.nested.field.contains(value)
}
```

regex based validator
---------------------

Some validators can be easily expressed as regex. You can use a regex helper to quickly define full-fledged validator of this kind. This already includes handling optional fields and $params.

JavaScript

```
import { helpers } from 'vuelidate/lib/validators'
const alpha = helpers.regex('alpha', /^[a-zA-Z]*$/)
```

locator based validator
-----------------------

If you want to use locator strategy, exactly the same one as in sameAs or requiredIf builtin validators, you can use ref helper to accomplish that, in exactly the same way how it is used inside those two validators.

JavaScript

```
import { ref, withParams } from './common'
export default (equalTo) =>
  withParams({ type: 'sameAs', eq: equalTo }, function(value, parentVm) {
    return value === ref(equalTo, this, parentVm)
  })
```

JavaScript

```
import { req, ref, withParams } from './common'

export default (prop) =>
  withParams({ type: 'requiredIf', prop }, function(value, parentVm) {
    return ref(prop, this, parentVm) ? req(value) : true
  })
```

Note that imports are slightly different, as this is how the code looks like from library source point of view. This style is the correct one if you are willing to [contribute your own validators to vuelidate](https://github.com/monterail/vuelidate#fork-destination-box). You should still use helpers export inside your own code (as presented in previous examples).

List of helpers
---------------

This table contains all helpers that can be used to help you with writing your own validators. You can import them from validators library

JavaScript

```
import { helpers } from 'vuelidate/lib/validators'
```

| Helper | Description |
| --- | --- |
| withParams | Allows adding $params metadata to your validation function. |
| req | Minimal version of required validator. Use it to make your validator accept optional fields |
| ref | A locator helper. This allows for convenient referencing of other fields in the model. |
| len | Get length of any kind value, whatever makes sense in the context. This can mean array length, string length, or number of keys on the object |
| regex | Useful for quick creation of regex based validators. |
