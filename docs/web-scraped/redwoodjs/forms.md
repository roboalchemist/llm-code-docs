# Source: https://docs.redwoodjs.com/docs/forms

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Forms]

[Version: 8.8]

On this page

<div>

# Forms

</div>

Redwood provides several helpers to make building forms easier. All of Redwood\'s helpers are simple wrappers around [React Hook Form](https://react-hook-form.com/) (RHF) that make it even easier to use in most cases.

If Redwood\'s helpers aren\'t flexible enough for you, you can use React Hook Form directly. `@redwoodjs/forms` exports everything it does:

``` 
import 
   */
} from '@redwoodjs/forms'
```

## Overview[​](#overview "Direct link to Overview") 

`@redwoodjs/forms` exports the following components:

Component

Description

`<Form>`

Surrounds all components, providing form and error contexts

`<FormError>`

Displays error messages from the server. Typically placed at the top of your form

`<Label>`

Used in place of the HTML `<label>` tag. Accepts error-styling props

`<InputField>`

Used in place of the HTML `<input>` tag. Accepts validation and error-styling props (also see the list of input field components enumerated below)

`<SelectField>`

Used in place of the HTML `<select>` tag. Accepts validation and error-styling props

`<TextAreaField>`

Used in place of the HTML `<textarea>` tag. Accepts validation and error-styling props

`<FieldError>`

Displays error messages if the field with the same `name` prop has validation errors. Only renders if there\'s an error on the associated field

`<Submit>`

Used in place of `<button type="submit">`. Triggers validation and \"submission\" (executes the function passed to `<Form>`\'s `onSubmit` prop)

All HTML `<input>` types are also available as components. They follow the naming convention `<TypeField>` where `Type` is one of the [HTML input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types). We\'ll refer to them collectively as \"input fields\". The full list is:

-   `<ButtonField>`
-   `<CheckboxField>`
-   `<ColorField>`
-   `<DateField>`
-   `<DatetimeLocalField>`
-   `<EmailField>`
-   `<FileField>`
-   `<HiddenField>`
-   `<ImageField>`
-   `<MonthField>`
-   `<NumberField>`
-   `<PasswordField>`
-   `<RadioField>`
-   `<RangeField>`
-   `<ResetField>`
-   `<SearchField>`
-   `<SubmitField>`
-   `<TelField>`
-   `<TextField>`
-   `<TimeField>`
-   `<UrlField>`
-   `<WeekField>`

### Validation and Error-styling Props[​](#validation-and-error-styling-props "Direct link to Validation and Error-styling Props") 

All components ending in `Field` (i.e. all input fields, along with `<SelectField>` and `<TextAreaField>`) accept validation and error-styling props. By validation and error-styling props, we mean three props specifically:

-   `validation`, which accepts all of React Hook Form\'s [`register` options](https://react-hook-form.com/api/useform/register), plus the Redwood-exclusive coercion helpers `valueAsBoolean`, `valueAsJSON`
-   `errorClassName` and `errorStyle`, which are the classes and styles to apply if there\'s an error

Besides `name`, all other props passed to these components are forwarded to the tag they render. Here\'s a table for reference:

Prop

Description

`name`

The name of the field. React Hook Form uses it a key to hook it up with everything else

`validation`

All your validation logic. Accepts all of React Hook Form\'s [`register` options](https://react-hook-form.com/api/useform/register), plus the Redwood-exclusive coercion helpers `valueAsBoolean`, `valueAsJSON`

`errorClassName`

The class name to apply if there\'s an error

`errorStyle`

The style to apply if there\'s an error

### Example[​](#example "Direct link to Example") 

A typical React component using these helpers would look something like this:

``` 
import  from '@redwoodjs/forms'

const ContactPage = () => 

  return (
    <Form onSubmit=>
      <Label name="name" className="label" errorClassName="label error" />
      <TextField
        name="name"
        className="input"
        errorClassName="input error"
        validation=}
      />
      <FieldError name="name" className="error-message" />

      <Label name="email" className="label" errorClassName="label error" />
      <TextField
        name="email"
        className="input"
        errorClassName="input error"
        validation=,
        }}
      />
      <FieldError name="email" className="error-message" />

      <Label name="message" className="label" errorClassName="label error" />
      <TextAreaField
        name="message"
        className="input"
        errorClassName="input error"
        validation=}
      />
      <FieldError name="message" className="error-message" />

      <Submit className="button">Save</Submit>
    </Form>
  )
}
```

## `<Form>`[​](#form "Direct link to form") 

Any form you want Redwood to validate and style in the presence errors should be surrounded by this tag.

Prop

Description

`config`

Accepts an object containing options for React Hook Form\'s [`useForm` hook](https://react-hook-form.com/api/useform)

`formMethods`

The functions returned from `useForm`. You only need to use this prop if you need to access to one of the functions that `useForm` returns (see example below)

`onSubmit`

Accepts a function to be called if validation succeeds. Called with an object containing name-value pairs of all the fields in your form

All other props are forwarded to the `<form>` tag that it renders.

### `<Form>` Explained[​](#form-explained "Direct link to form-explained") 

`<Form>` encapsulates React Hook Form\'s `useForm` hook and `<FormProvider>` context, along with Redwood\'s `ServerError` context. It\'s hard to talk about this component without getting into the nitty-gritty of React Hook Forms.

`useForm` is React Hook Form\'s major hook. It returns a bunch of functions, one of which is `register`, which you use to quite literally \"register\" fields into React Hook Form so it can validate them. (This has to do with [controlled vs. uncontrolled components](https://reactjs.org/docs/uncontrolled-components.html). React Hook Form takes the latter approach.)

All of Redwood\'s form helpers need the `register` function to do what they do. But they don\'t get it straight from `<Form>` because they could be nested arbitrarily deep. That\'s where `<FormProvider>` comes in: by passing the functions returned from `useForm` to `<FormProvider>`, Redwood\'s helpers can just use `useFormContext` to get what they need.

### Using `formMethods`[​](#using-formmethods "Direct link to using-formmethods") 

There are some functions that `useForm` returns that it\'d be nice to have access to. For example, `useForm` returns a function `reset`, which resets the form\'s fields. To access it, you have to call `useForm` yourself. But you still need to pass `useForm`\'s return to the `<FormProvider>` so that Redwood\'s helpers can register themselves:

``` 
import  from 'react-hook-form'

const ContactPage = () => 

  return (
    <Form formMethods= onSubmit=>
      // Still works!
      <TextField name="name" validation=}>
    </Form>
  )
}
```

## `<FormError>`[​](#formerror "Direct link to formerror") 

This helper renders a `<div>` containing a \"title\" message and a `<ul>` enumerating any errors reported by the server when trying to save your form. You can see it in a scaffold if you submit a form that somehow gets passed client-side validation:

![image](https://user-images.githubusercontent.com/32992335/138611080-9bb138a9-59cc-406d-b926-ef46f4aa7997.png)

For example, let\'s say you have a form with a `<TextField>` for a user\'s email address, but you didn\'t specify any validation on it:

``` 
import  from '@redwoodjs/web'

const CREATE_CONTACT = gql`
  mutation CreateContactMutation($input: ContactInput!) 
  }
`

const ContactPage = () => ] = useMutation(CREATE_CONTACT)

  const onSubmit = (data) => })
  }

  return (
    <Form onSubmit=>
      <FormError error=>
      // No validation—any email goes!
      <TextField name="email" />
    </Form>
  )
}
```

Since there\'s no validation, anything goes! On the client at least. GraphQL is built on types, so it\'s not going to let just anything through. Instead it\'ll throw an error and bubble it back up to the top (via the `error` object returned by the `useMutation` hook) where `<FormError>` can render something like:

``` 
<div>
  <p>Can't create new contact:</p>
  <ul>
    <li>email is not formatted like an email address</li>
  </ul>
</div>
```

## `<Label>`[​](#label "Direct link to label") 

Renders an HTML `<label>` tag with different `className` and `style` props depending on whether the field it\'s associated with has a validation error.

This tag can be self-closing, in which case the `name` becomes the text of the label:

``` 
<label name="name" className="input" errorClassName="input error" />

<!-- Renders: <label for="name" class="input">name</label> -->
```

It can also have standard separate open/close tags and take text inside, in which case that text is the text of the rendered `<label>`:

``` 
<label name="name" className="input" errorClassName="input error"
  >Your Name</label
>

<!-- Renders: <label for="name" class="input">Your Name</label> -->
```

All props are passed to the underlying `<label>` tag besides the ones listed below:

Prop

Description

`name`

The name of the field that this label is associated with. This should be the same as the `name` prop on the input field this label is for

`errorClassName`

The `className` that\'s used if the field with the same `name` has a validation error

`errorStyle`

The `style` that\'s used if the field with the same `name` has a validation error

## Input Fields[​](#input-fields "Direct link to Input Fields") 

Inputs are the backbone of most forms. While you can use `<InputField>` and it\'s `type` prop to make all the different kinds of input fields you\'d use in a form, it\'s often easier to reach for the named input fields (listed above) which have defaults for things like coercion configured where appropriate.

### Default coercion[​](#default-coercion "Direct link to Default coercion") 

Certain input fields handle coercion automatically, but you can always override the coercion or, if it\'s not built-in, set it manually via the `validation` prop\'s [setValueAs](https://react-hook-form.com/api/useform/register) property.

The input fields that coerce automatically are:

Field

Default coercion

`<CheckboxField>`

`valueAsBoolean`

`<NumberField>`

`valueAsNumber`

`<DateField>`

`valueAsDate`

`<DatetimeLocalField>`

`valueAsDate`

`valueAsDate` and `valueAsNumber` are built into React Hook Form and are based on the HTML standard. But because Redwood uses GraphQL on the backend, it\'s important that the types submitted by the form be what the GraphQL server expects. Instead of forcing users to make heavy-use of `setValueAs` for custom coercion, Redwood extends react hook form\'s `valueAs` properties with two more for convenience:

-   `valueAsBoolean`
-   `valueAsJSON`

### Default treatment of empty input values[​](#default-treatment-of-empty-input-values "Direct link to Default treatment of empty input values") 

Redwood provides a flexible treatment of empty input field value. Appropriate treatment of empty fields can make working with fields for database relations easier.

The treatment of empty field values is governed by the following:

1.  If `setValueAs` is specified by the user, the specified function will determine the behavior of empty fields.
2.  If the `emptyAs` prop is set, then the `emptyAs` prop will determine the field value on an empty condition. See below for `emptyAs` prop values.
3.  If the `validation = ` prop is set, an empty field will return null. However, the validation provided by react-hook-forms should engage and prevent submission of the form as an empty value would not satisfy the `required` validation.
4.  If the field is an `Id` field, that is its name ends in \"Id\", then an empty field will return `null`. A `null` value is the most appropriate value for most database relation fields. For scenarios where another value is required for empty cases, utilize the `emptyAs` prop.
5.  If none of the above cases apply, the field value will be set as follows for empty field scenarios:
    -   DateFields → null
    -   NumberFields → NaN
    -   TextFields with valueAsNumber set → NaN
    -   SelectFields with valueAsNumber set → NaN
    -   SelectFields without valueAsNumber set → \'\' (empty string)
    -   TextFields with valueAsJSON set → null
    -   TextFields and comparable → \'\' (empty string)

### emptyAs prop[​](#emptyas-prop "Direct link to emptyAs prop") 

The `emptyAs` prop allows the user to override the default value for an input field if the field is empty. Provided that a `setValueAs` prop is not specified, Redwood will allow you to override the default empty value returned. The possible values for `emptyAs` are:

-   `null`
-   `'undefined'`
-   `0`
-   `''` (empty string)

For example:

``` 
<NumberField name="quantity" emptyAs="undefined" />
<NumberField name="score" emptyAs= />
```

will return `undefined` if the field is empty.

### Custom Input Fields[​](#custom-input-fields "Direct link to Custom Input Fields") 

You can create a custom field that integrates with Redwood through the use of Redwood\'s `useRegister` and `useErrorStyles` hooks. Each of these serving a different purpose depending on what you are trying to build.

`useRegister` registers the field with react-hook-form and is a wrapper for [`register`](https://react-hook-form.com/api/useform/register).

`useErrorStyles` sets up error styling for your custom input field.

Using these two together you can create custom input fields that replicate a Redwood input field while also allowing for custom domain logic.

In the following example we have an all-in-one custom required input field with label, input, and error display.

``` 
import  from '@redwoodjs/forms'

const RequiredField = () => 
  })

  const  = useErrorStyles()

  const  = useErrorStyles()

  return (
    <>
      <label className= style=></label>
      <input
        className=
        style=
        type="text"
        
      />
      <FieldError name=>
    </>
  )
}
```

### Controlled Component Fields[​](#controlled-component-fields "Direct link to Controlled Component Fields") 

If you\'re working with a fully-featured component library, or have your own production-ready components, you may want to integrate them with Redwood\'s forms seamlessly. You can via Redwood forms\' `useErrorStyles` hook and React Hook Form\'s `Controller` component. The following example shows how you could go about integrating a component from [`primereact`](https://www.primefaces.org/primereact/) for use in in Redwood\'s forms like any of the named-input fields listed above:

web/src/components/ToggleButtonField/ToggleButtonField.tsx

``` 
import  from 'primereact/togglebutton'
import type  from 'primereact/togglebutton'

import  from '@redwoodjs/forms'

interface Props extends ToggleButtonProps 

const ToggleButtonField = (props: Props) =>  = props

  const  =
    useErrorStyles()

  return (
    <Controller
      name=
      defaultValue=
      rules=
      render= }) => (
        <ToggleButton
          
          checked=
          onChange=
          onBlur=
          ref=
          name=
          className=
          style=}
        />
      )}
    />
  )
}

export default ToggleButtonField
```

## `<SelectField>`[​](#selectfield "Direct link to selectfield") 

Renders an HTML `<select>` tag. It\'s possible to select multiple values using the `multiple` prop. When `multiple` is `true`, this field returns an array of values in the same order as the list of options, not in the order they were selected.

``` 
<SelectField name="toppings" multiple=>
  <option>'lettuce'</option>
  <option>'tomato'</option>
  <option>'pickle'</option>
  <option>'cheese'</option>
</SelectField>

// If the user chooses lettuce, tomato, and cheese,
// the onSubmit handler receives:
//
// 
//
```

### Validation[​](#validation "Direct link to Validation") 

In these two examples, one with multiple-field selection, validation requires that a field be selected and that the user doesn\'t select the first value in the dropdown menu:

``` 
<SelectField
  name="selectSingle"
  validation=,
    },
  }}
>
  <option>Please select an option</option>
  <option>Option 1</option>
  <option>Option 2</option>
</SelectField>
<FieldError name="selectSingle" style=} />
```

``` 
<SelectField
  multiple=
  name="selectMultiple"
  validation=)
        return returnValue[0]
      },
    },
  }}
>
  <option>Please select an option</option>
  <option>Option 1</option>
  <option>Option 2</option>
</SelectField>
<FieldError name="selectMultiple" style=} />
```

### Coercion[​](#coercion "Direct link to Coercion") 

Typically, a `<SelectField>` returns a string, but you can use one of the `valueAs` properties to return another type. An example use-case is when `<SelectField>` is being used to select a numeric identifier. Without the `valueAsNumber` property, `<SelectField>` returns a string. But, as per the example below, the `valueAsNumber` can be used to return an `Int`:

``` 
<SelectField name="select" validation=}>
  <option value=>Option 1</option>
  <option value=>Option 2</option>
  <option value=>Option 3</option>
</SelectField>
```

If `Option 3` is selected, the `<Form>`\'s `onSubmit` function is passed data as follows:

``` 

```

## `<FieldError>`[​](#fielderror "Direct link to fielderror") 

Renders a `<span>` containing a validation error message if the field with the same `name` attribute has a validation error. Otherwise renders nothing.

``` 
<FieldError name="name" className="error-message">
  <!-- Renders: <span class="error-message">name is required</span> --></FieldError
>
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/forms.md)