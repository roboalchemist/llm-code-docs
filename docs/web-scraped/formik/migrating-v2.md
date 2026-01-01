# Formik Documentation
# Source: https://formik.org/docs/migrating-v2
# Path: /docs/migrating-v2

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# Migrating from v1.x to v2.x

## Breaking Changes

### Minimum Requirements

- Since Formik 2 is built on top of React Hooks, you must be on React 16.8.x or higher
- Since Formik 2 uses theunknowntype, you must be on TypeScript 3.0 or higher (if you use TypeScript)
`unknown`
There are a few breaking changes in Formik 2.x.Luckily, these probably won't impact many people:

### resetForm

`resetForm`
With Formik 2, we introduced the new props for more initial state:initialErrors,initialTouched,initialStatus. Therefore,resetForm's signature has changed. Instead of optionally accepting just the next initial values of the form. It now optionally accepts the partial next initial state of Formik.

`initialErrors`
`initialTouched`
`initialStatus`
`resetForm`
v1

```
1// Reset to `initialValues`2formik.resetForm();3// Reset form and set the next `initialValues` of the form4formik.resetForm({name:'',email:''});
```

v2

```
1// Reset the form. This will set the next initial state of2// Formik to the `initialValues`, `initialErrors`, `initialTouched`,3// `initialStatus` props.4formik.resetForm();56// Reset the form back to `initialXXXX` but change next7// `initialValues` to a custom value8formik.resetForm({9values:{name:'Custom initial values',email:''},10});1112// Reset form back to `initialXXXX`, but change next `initialValues`13// and `initialErrors` of the form14formik.resetForm({15values:{name:'',email:''},16errors:{name:'Something special'},17});1819// Reset form back to `initialXXXX`, but change next `initialStatus` to 'Foo'20formik.resetForm({21status:'Foo',22});
```

### setError

`setError`
This method has been deprecated for a while with a warning in v1.x releases. It's fully removed in v2. Please use Formik'ssetStatus(status)instead. It works identically. Note: this is/was notsetErrors(plural) which is still around.

`setStatus(status)`
`setErrors`

### validate

`validate`
As you may know, you can return a Promise of a validation error fromvalidate. In 1.x, it didn't matter if this promise is resolved or rejected as in both cases the payload of the promise was interpreted as the validation error. In 2.x, rejection will be interpreted as an actual exception and it won't update the form error state. Any validation function that returns a rejected promise of errors needs to be adjusted to return a resolved promise of errors instead.

`validate`

### ref

`ref`
Currently, you can't attach a ref to Formik using therefprop. However, you still can get around this issue using the propinnerRef. We have some WIP#2208to instead useReact.forwardRef.

`ref`
`innerRef`
`React.forwardRef`

### isValid

`isValid`
This property does not take the value ofdirtyinto account anymore. This means that if you want to disable a submit button when the form is notdirty(i.e. on first render and when values are unchanged), you have to explicitly check for it.

`dirty`
`dirty`

```
1<buttondisabled={!isValid||!dirty}type="submit">2Submit3</button>
```

### Typescript changes

#### FormikActions

`FormikActions`
FormikActionshas been renamed toFormikHelpersIt should be a straightforward change to import or alias the type

`FormikActions`
`FormikHelpers`
v1

```
import{FormikActions}from'formik';
```

v2

```
import{FormikHelpersasFormikActions}from'formik';
```

#### FieldProps

`FieldProps`
FieldPropsnow accepts two generic type parameters.Both parameters are optional, butFormValueshas been moved from the first to the second parameter.

`FieldProps`
`FormValues`
v1

```
typeProps=FieldProps<FormValues>;
```

v2

```
typeProps=FieldProps<FieldValue,FormValues>;
```

## What's New?

### Checkboxes and Select multiple

Similarly to Angular, Vue, or Svelte, Formik 2 "fixes" React checkboxes and multi-selects with built-in array binding and boolean behavior. This was one of the most confusing things for people in Formik 1.x.

```
1importReactfrom'react';2import{Formik,Field,Form}from'formik';3import{Debug}from'./Debug';45constsleep=ms=>newPromise(resolve=>setTimeout(resolve,ms));67constCheckboxExample=()=>(8<div>9<h1>Checkboxes</h1>10<p>11This example demonstrates how to properly create checkboxes with Formik.12</p>13<Formik14initialValues={{15isAwesome:false,16terms:false,17newsletter:false,18jobType:['designer'],19location:[],20}}21onSubmit={asyncvalues=>{22awaitsleep(1000);23alert(JSON.stringify(values,null,2));24}}25>26{({isSubmitting,getFieldProps,handleChange,handleBlur,values})=>(27<Form>28{/*29This first checkbox will result in a boolean value being stored.30*/}31<divclassName="label">Basic Info</div>32<label>33<Fieldtype="checkbox"name="isAwesome"/>34Are you awesome?35</label>36{/*37Multiple checkboxes with the same name attribute, but different38value attributes will be considered a "checkbox group". Formik will automagically39bind the checked values to a single array for your benefit. All the add and remove40logic will be taken care of for you.41*/}42<divclassName="label">43What best describes you? (check all that apply)44</div>45<label>46<Fieldtype="checkbox"name="jobType"value="designer"/>47Designer48</label>49<label>50<Fieldtype="checkbox"name="jobType"value="developer"/>51Developer52</label>53<label>54<Fieldtype="checkbox"name="jobType"value="product"/>55Product Manager56</label>57{/*58You do not _need_ to use <Field>/useField to get this behavior,59using handleChange, handleBlur, and values works as well.60*/}61<label>62<input63type="checkbox"64name="jobType"65value="founder"66checked={values.jobType.includes('founder')}67onChange={handleChange}68onBlur={handleBlur}69/>70CEO / Founder71</label>7273{/*74The <select> element will also behave the same way if75you pass `multiple` prop to it.76*/}77<labelhtmlFor="location">Where do you work?</label>78<Field79component="select"80id="location"81name="location"82multiple={true}83>84<optionvalue="NY">New York</option>85<optionvalue="SF">San Francisco</option>86<optionvalue="CH">Chicago</option>87<optionvalue="OTHER">Other</option>88</Field>89<label>90<Fieldtype="checkbox"name="terms"/>I accept the terms and91conditions.92</label>93{/* Here's how you can use a checkbox to show / hide another field */}94{!!values.terms?(95<div>96<label>97<Fieldtype="checkbox"name="newsletter"/>98Send me the newsletter<emstyle={{color:'rebeccapurple'}}>99(This is only shown if terms = true)100</em>101</label>102</div>103):null}104<buttontype="submit"disabled={isSubmitting}>105Submit106</button>107<Debug/>108</Form>109)}110</Formik>111</div>112);113114exportdefaultCheckboxExample;
```

### useField()

`useField()`
Just what you think, it's like<Field>, but with a hook. See docs for usage.

`<Field>`

### useFormikContext()

`useFormikContext()`
A hook that is equivalent toconnect().

`connect()`

### <Field as>

`<Field as>`
<Field/>now accepts a prop calledaswhich will injectonChange,onBlur,valueetc. directly through to the component or string. This is useful for folks using Emotion or Styled components as they no longer need to clean upcomponent's render props in a wrapped function.

`<Field/>`
`as`
`onChange`
`onBlur`
`value`
`component`

```
1// <input className="form-input" placeholder="Jane"  />2<Fieldname="firstName"className="form-input"placeholder="Jane"/>34// <textarea className="form-textarea"/></textarea>5<Fieldname="message"as="textarea"className="form-textarea"/>67// <select className="my-select"/>8<Fieldname="colors"as="select"className="my-select">9<optionvalue="red">Red</option>10<optionvalue="green">Green</option>11<optionvalue="blue">Blue</option>12</Field>1314// with styled-components/emotion15constMyStyledInput=styled.input`16padding:.5em;17border:1pxsolid#eee;18/* ... */19`20constMyStyledTextarea=MyStyledInput.withComponent('textarea');2122// <input className="czx_123" placeholder="google.com"  />23<Fieldname="website"as={MyStyledInput}placeholder="google.com"/>2425// <textarea placeholder="Post a message..." rows={5}></textarea>26<Fieldname="message"as={MyStyledTextArea}placeholder="Post a message.."rows={4}/>
```

### getFieldProps(nameOrProps)

`getFieldProps(nameOrProps)`
There are two useful additions toFormikProps,getFieldPropsandgetFieldMeta. These are Kent C. Dodds-esque prop getters that can be useful if you love prop drilling, arenotusing the context-based API's, or if you are building a customuseField.

`FormikProps`
`getFieldProps`
`getFieldMeta`
`useField`

```
1exportinterfaceFieldInputProps<Value>{2/** Value of the field */3value:Value;4/** Name of the field */5name:string;6/** Multiple select? */7multiple?:boolean;8/** Is the field checked? */9checked?:boolean;10/** Change event handler */11onChange:FormikHandlers['handleChange'];12/** Blur event handler */13onBlur:FormikHandlers['handleBlur'];14}
```

### getFieldMeta(name)

`getFieldMeta(name)`
Given a name it will return an object:

```
1exportinterfaceFieldMetaProps<Value>{2/** Value of the field */3value:Value;4/** Error message of the field */5error?:string;6/** Has the field been visited? */7touched:boolean;8/** Initial value of the field */9initialValue?:Value;10/** Initial touched state of the field */11initialTouched:boolean;12/** Initial error message of the field */13initialError?:string;14}
```

### Misc

- FormikContextis now exported
`FormikContext`
- validateOnMount?: boolean = false
`validateOnMount?: boolean = false`
- initialErrors,initialTouched,initialStatushave been added
`initialErrors`
`initialTouched`
`initialStatus`

## Deprecation Warnings

### Allrenderprops have been deprecated with a console warning.

`render`
For<Field>,<FastField>,<Formik>,<FieldArray>, therenderprop has been deprecated with a warning as it will be removed in future versions. Instead, use a child callback function. This deprecation is meant to parallel React Context Consumer's usage.

`<Field>`
`<FastField>`
`<Formik>`
`<FieldArray>`
`render`

```
1-<Field name="firstName" render={props => ....} />2+<Field name="firstName">{props => ... }</Field>
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