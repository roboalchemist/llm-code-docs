# Formik Documentation
# Source: https://formik.org/docs/api/errormessage
# Path: /docs/api/errormessage

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# <ErrorMessage />

<ErrorMessage />is a component that renders the error message of a given field if that field has been visited (i.e.touched[name] === true) (and there is anerrormessage present). It expects that all error messages are stored for a given field as a string. Like<Field />,<FastField />, and<FieldArray />, lodash-like dot path and bracket syntax is supported.

`<ErrorMessage />`
`touched[name] === true`
`error`
`<Field />`
`<FastField />`
`<FieldArray />`

## Example

```
1import React from 'react';2import { Formik, Form, Field, ErrorMessage } from 'formik';3import * as Yup from "yup";45const SignupSchema = Yup.object().shape({6name: Yup.string()7.min(2, 'Too Short!')8.max(70, 'Too Long!')9.required('Required'),10email: Yup.string()11.email('Invalid email')12.required('Required'),13});1415export const ValidationSchemaExample = () => (16<div>17<h1>Signup</h1>18<Formik19initialValues={{20name: '',21email: '',22}}23validationSchema={SignupSchema}24onSubmit={values => {25// same shape as initial values26console.log(values);27}}28>29{({ errors, touched }) => (30<Form>31<Field name="name"  />32-{errors.name && touched.name ? (33-<div>{errors.name}</div>34-) : null}35+<ErrorMessage name="name" />36<Field name="email" type="email" />37-{errors.email && touched.email ? (38-<div>{errors.email}</div>39-) : null}40+<ErrorMessage name="email" />41<button type="submit">Submit</button>42</Form>43)}44</Formik>45</div>46);
```

#### Props

# Reference

## Props

### children

`children`
children?: ((message: string) => React.ReactNode)

`children?: ((message: string) => React.ReactNode)`
A function that returns a valid React element. Will only be called when the field has been touched and an error exists.

```
1// the render callback will only be called when the2// field has been touched and an error exists and subsequent updates.3<ErrorMessagename="email">{msg=><div>{msg}</div>}</ErrorMessage>
```

### component

`component`
component?: string | React.ComponentType<FieldProps>

`component?: string | React.ComponentType<FieldProps>`
Either a React component or the name of an HTML element to render. If not specified,<ErrorMessage>will just return a string.

`<ErrorMessage>`

```
1<ErrorMessagecomponent="div"name="email"/>2// --> {touched.email && error.email ? <div>{error.email}</div> : null}34<ErrorMessagecomponent="span"name="email"/>5// --> {touched.email && error.email ? <span>{error.email}</span> : null}67<ErrorMessagecomponent={Custom}name="email"/>8// --> {touched.email && error.email ? <Custom>{error.email}</Custom> : null}910<ErrorMessagename="email"/>11// This will return a string. React 16+.12// --> {touched.email && error.email ? error.email : null}
```

### id

`id`
id?: string

`id?: string`
A field's id in Formik state. To get access to DOM elements for e2e testing purposes, it doesn't impact the implementation in any way as the prop can still be omitted.

```
1// id will be used only for testing purposes2// not contributing anything to the core implementation.3<ErrorMessagename="email"id="form_email_id"/>
```

### name

`name`
name: stringRequired

`name: string`
A field's name in Formik state. To access nested objects or arrays, name can also accept lodash-like dot path likesocial.facebookorfriends[0].firstName

`social.facebook`
`friends[0].firstName`

### render

`render`
render?: (error: string) => React.ReactNode

`render?: (error: string) => React.ReactNode`
A function that returns a valid React element. Will only be called when the field has been touched and an error exists.

```
1// the render callback will only be called when the2// field has been touched and an error exists and subsequent updates.3<ErrorMessagename="email"render={msg=><div>{msg}</div>}/>
```

#### On this page

#### Resources

- Docs
- Learn
- Guides
- API Reference
- Blog

#### Community

- User Showcase
- Funding
- Community Chat
- Project Forum
- Releases
- Star

#### About Formium

- Home
- GitHub
- Twitter
- Contact Sales

#### Subscribe to our newsletter

The latest Formik news, articles, and resources, sent to your inbox.