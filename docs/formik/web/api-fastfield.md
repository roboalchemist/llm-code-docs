# Formik Documentation
# Source: https://formik.org/docs/api/fastfield
# Path: /docs/api/fastfield

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# <FastField />

## Before we start

<FastField />is meant for performanceoptimization. However, you really do not need to use it until you do. Only proceed if you are familiar with how React'sshouldComponentUpdate()works. You have been warned.

`<FastField />`
`shouldComponentUpdate()`
No. Seriously. Please review the following parts of the official React documentation before continuing

- ReactshouldComponentUpdate()Reference
`shouldComponentUpdate()`
- shouldComponentUpdatein Action
`shouldComponentUpdate`

## Overview

<FastField />is an optimized version of<Field />meant to be used on large forms (~30+ fields) or when a field has very expensive validation requirements.<FastField />has the same exact API as<Field>, but implementsshouldComponentUpdate()internally to block all additional re-renders unless there are direct updates to the<FastField />'s relevant parts/slice of Formik state.

`<FastField />`
`<Field />`
`<FastField />`
`<Field>`
`shouldComponentUpdate()`
`<FastField />`
For example,<FastField name="firstName" />will only re-render when there are:

`<FastField name="firstName" />`
- Changes tovalues.firstName,errors.firstName,touched.firstName, orisSubmitting. This is determined by shallow comparison. Note: dotpaths are supported.
`values.firstName`
`errors.firstName`
`touched.firstName`
`isSubmitting`
- A prop is added/removed to the<FastField name="firstName" />
`<FastField name="firstName" />`
- Thenameprop changes
`name`
Other than for these aforementioned situations,<FastField />will not re-render when other parts of Formik state change. However, all updates triggered by a<FastField />will trigger re-renders to other "vanilla"<Field />components.

`<FastField />`
`<FastField />`
`<Field />`

## When to use<FastField />

`<FastField />`
If a<Field />is "independent" of all other<Field />'s in your form, then you can use<FastField />.

`<Field />`
`<Field />`
`<FastField />`
More specifically, if the<Field />does not change behavior or render anything that is based on updates to another<Field />or<FastField />'s slice of Formik state AND it does not rely on other parts of top-level<Formik />state (e.g.isValidating,submitCount), then you can use<FastField />as a drop-in replacement to<Field />.

`<Field />`
`<Field />`
`<FastField />`
`<Formik />`
`isValidating`
`submitCount`
`<FastField />`
`<Field />`

## Example

```
1importReactfrom'react';2import{Formik,Field,FastField,Form}from'formik';3import*asYupfrom'yup';45constBasic=()=>(6<div>7<h1>Sign Up</h1>8<Formik9initialValues={{10firstName:'',11lastName:'',12email:'',13}}14validationSchema={Yup.object().shape({15firstName:Yup.string().required(),16middleInitial:Yup.string(),17lastName:Yup.string().required(),18email:Yup.string().email().required(),19})}20onSubmit={values=>{21setTimeout(()=>{22alert(JSON.stringify(values,null,2));23},500);24}}25>26{formikProps=>(27<Form>28{/** This <FastField> only updates for changes made to29values.firstName, touched.firstName, errors.firstName */}30<labelhtmlFor="firstName">First Name</label>31<FastFieldname="firstName"placeholder="Weezy"/>3233{/** Updates for all changes because it's from the34top-level formikProps which get all updates */}35{formikProps.touched.firstName&&formikProps.errors.firstName&&(36<div>{formikProps.errors.firstName}</div>37)}3839<labelhtmlFor="middleInitial">Middle Initial</label>40<FastFieldname="middleInitial"placeholder="F">41{({field,form,meta})=>(42<div>43<input{...field}/>44{/**45* This updates normally because it's from the same slice of Formik state,46* i.e. path to the object matches the name of this <FastField />47*/}48{meta.touched?meta.error:null}4950{/** This won't ever update since it's coming from51from another <Field>/<FastField>'s (i.e. firstName's) slice   */}52{form.touched.firstName&&form.errors.firstName53?form.errors.firstName54:null}5556{/* This doesn't update either */}57{form.submitCount}5859{/* Imperative methods still work as expected */}60<button61type="button"62onClick={form.setFieldValue('middleInitial','J')}63>64J65</button>66</div>67)}68</FastField>6970{/** Updates for all changes to Formik state71and all changes by all <Field>s and <FastField>s */}72<labelhtmlFor="lastName">LastName</label>73<Fieldname="lastName"placeholder="Baby">74{({field,form,meta})=>(75<div>76<input{...field}/>77{/**  Works because this is inside78of a <Field/>, which gets all updates */}79{form.touched.firstName&&form.errors.firstName80?form.errors.firstName81:null}82</div>83)}84</Field>8586{/** Updates for all changes to Formik state and87all changes by all <Field>s and <FastField>s */}88<labelhtmlFor="email">Email</label>89<Fieldname="email"placeholder="jane@acme.com"type="email"/>9091<buttontype="submit">Submit</button>92</Form>93)}94</Formik>95</div>96);
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