# Formik Documentation
# Source: https://formik.org/docs/api/field
# Path: /docs/api/field

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# <Field />

<Field />will automagically hook up inputs to Formik. It uses thenameattribute to match up with Formik state.<Field />will default to an HTML<input />element.

`<Field />`
`name`
`<Field />`
`<input />`

## Rendering

There are a few different ways to render things with<Field>.

`<Field>`
- <Field as>
`<Field as>`
- <Field children>
`<Field children>`
- <Field component>
`<Field component>`
- <Field render>deprecated in 2.x. Using these will log warning
`<Field render>`
ascan either be a React component or the name of an HTML element to render. Formik will automagically injectonChange,onBlur,name, andvalueprops of the field designated by thenameprop to the (custom) component.

`as`
`onChange`
`onBlur`
`name`
`value`
`name`
childrencan either be an array of elements (e.g.<option>in the case of<Field as="select">) or a callback function (a.k.a render prop). The render props are an object containing:

`children`
`<option>`
`<Field as="select">`
- field: An object containingonChange,onBlur,name, andvalueof the field (seeFieldInputProps)
`field`
`onChange`
`onBlur`
`name`
`value`
`FieldInputProps`
- form: The Formik bag
`form`
- meta: An object containing metadata (i.e.value,touched,error, andinitialValue) about the field (seeFieldMetaProps)
`meta`
`value`
`touched`
`error`
`initialValue`
`FieldMetaProps`
componentcan either be a React component or the name of an HTML element to render. All additional props will be passed through.

`component`
In Formik 0.9 to 1.x, therenderprop could also be used for rendering. It has been deprecated since 2.x. While the code still lives within<Field>, usingrenderwill show a warning in the console.

`render`
`<Field>`
`render`

## Example

```
1importReactfrom'react';2import{Field,Form,Formik,FormikProps}from'formik';34constMyInput=({field,form,...props})=>{5return<input{...field}{...props}/>;6};78constExample=()=>(9<div>10<h1>My Form</h1>11<Formik12initialValues={{email:'',color:'red',firstName:'',lastName:''}}13onSubmit={(values,actions)=>{14setTimeout(()=>{15alert(JSON.stringify(values,null,2));16actions.setSubmitting(false);17},1000);18}}19>20{(props:FormikProps<any>) => (21<Form>22<Fieldtype="email"name="email"placeholder="Email"/>23<Fieldas="select"name="color">24<optionvalue="red">Red</option>25<optionvalue="green">Green</option>26<optionvalue="blue">Blue</option>27</Field>2829<Fieldname="lastName">30{({31field,// { name, value, onChange, onBlur }32form:{touched,errors},// also values, setXXXX, handleXXXX, dirty, isValid, status, etc.33meta,34})=>(35<div>36<inputtype="text"placeholder="Email"{...field}/>37{meta.touched&&meta.error&&(38<divclassName="error">{meta.error}</div>39)}40</div>41)}42</Field>43<Fieldname="lastName"placeholder="Doe"component={MyInput}/>44<buttontype="submit">Submit</button>45</Form>46)}47</Formik>48</div>49);
```

#### Props

# Reference

## Props

### as

`as`
as?: string | React.ComponentType<FieldProps['field']>

`as?: string | React.ComponentType<FieldProps['field']>`
Either a React component or the name of an HTML element to render. That is, one of the following:

- input
`input`
- select
`select`
- textarea
`textarea`
- A valid HTML element name
- A custom React component
Custom React components will be passedonChange,onBlur,name, andvalueplus any other props passed directly to<Field>.

`onChange`
`onBlur`
`name`
`value`
`<Field>`
Default is'input'(so an<input>is rendered by default)

`'input'`
`<input>`

```
1// Renders an HTML <input> by default2<Fieldname="lastName"placeholder="Last Name"/>34// Renders an HTML <select>5<Fieldname="color"as="select">6<optionvalue="red">Red</option>7<optionvalue="green">Green</option>8<optionvalue="blue">Blue</option>9</Field>1011// Renders a CustomInputComponent12<Fieldname="firstName"as={CustomInputComponent}placeholder="First Name"/>1314constCustomInputComponent=(props)=>(15<inputclassName="my-custom-input"type="text"{...props}/>16);
```

### children

`children`
children?: React.ReactNode | ((props: FieldProps) => React.ReactNode)

`children?: React.ReactNode | ((props: FieldProps) => React.ReactNode)`
Either JSX elements or callback function. Same asrender.

`render`

```
1// Children can be JSX elements2<Fieldname="color"as="select">3<optionvalue="red">Red</option>4<optionvalue="green">Green</option>5<optionvalue="blue">Blue</option>6</Field>78// Or a callback function9<Fieldname="firstName">10{({field,form,meta})=>(11<div>12<inputtype="text"{...field}placeholder="First Name"/>13{meta.touched&&14meta.error&&<divclassName="error">{meta.error}</div>}15</div>16)}17</Field>
```

### component

`component`
component?: string | React.ComponentType<FieldProps>

`component?: string | React.ComponentType<FieldProps>`
Either a React component or the name of an HTML element to render. That is, one of the following:

- input
`input`
- select
`select`
- textarea
`textarea`
- A custom React component
Custom React components will be passedFieldPropswhich is samerenderprop parameters of<Field render>plus any other props passed to directly to<Field>.

`FieldProps`
`render`
`<Field render>`
`<Field>`
Default is'input'(so an<input>is rendered by default)

`'input'`
`<input>`

```
1// Renders an HTML <input> by default2<Fieldname="lastName"placeholder="Last Name"/>34// Renders an HTML <select>5<Fieldname="color"component="select">6<optionvalue="red">Red</option>7<optionvalue="green">Green</option>8<optionvalue="blue">Blue</option>9</Field>1011// Renders a CustomInputComponent12<Fieldname="firstName"component={CustomInputComponent}placeholder="First Name"/>1314constCustomInputComponent=({15field,// { name, value, onChange, onBlur }16form:{touched,errors},// also values, setXXXX, handleXXXX, dirty, isValid, status, etc.17...props18})=>(19<div>20<inputtype="text"{...field}{...props}/>21{touched[field.name]&&22errors[field.name]&&<divclassName="error">{errors[field.name]}</div>}23</div>24);
```

### innerRef

`innerRef`
innerRef?: (el: React.HTMLElement<any> => void)

`innerRef?: (el: React.HTMLElement<any> => void)`
When you arenotusing a custom component and you need to access the underlying DOM node created byField(e.g. to callfocus), pass the callback to theinnerRefprop instead.

`Field`
`focus`
`innerRef`

### name

`name`
name: string

`name: string`
Required

A field's name in Formik state. To access nested objects or arrays, name can also accept lodash-like dot path likesocial.facebookorfriends[0].firstName

`social.facebook`
`friends[0].firstName`

### render

`render`
render?: (props: FieldProps) => React.ReactNode

`render?: (props: FieldProps) => React.ReactNode`
Deprecated in 2.x. Usechildreninstead.

`children`
A function that returns one or more JSX elements.

```
1// Renders an HTML <input> and passes FieldProps field property2<Field3name="firstName"4render={({field/* { name, value, onChange, onBlur } */})=>(5<input{...field}type="text"placeholder="firstName"/>6)}7/>89// Renders an HTML <input> and disables it while form is submitting10<Field11name="lastName"12render={({field,form:{isSubmitting}})=>(13<input{...field}disabled={isSubmitting}type="text"placeholder="lastName"/>14)}15/>1617// Renders an HTML <input> with custom error <div> element18<Field19name="lastName"20render={({field,form:{touched,errors}})=>(21<div>22<input{...field}type="text"placeholder="lastName"/>23{touched[field.name]&&24errors[field.name]&&<divclassName="error">{errors[field.name]}</div>}25</div>26)}27/>
```

### validate

`validate`
validate?: (value: any) => undefined | string | Promise<any>

`validate?: (value: any) => undefined | string | Promise<any>`
You can run independent field-level validations by passing a function to thevalidateprop. The function will respect thevalidateOnBlurandvalidateOnChangeconfig/props specified in the<Field>'sparent<Formik>/withFormik. This function can either be synchronous or asynchronous:

`validate`
`validateOnBlur`
`validateOnChange`
`<Field>'s`
`<Formik>`
`withFormik`
- Sync: if invalid, return astringcontaining the error message or
returnundefined.
Sync: if invalid, return astringcontaining the error message or
returnundefined.

`string`
`undefined`
- Async: return a Promise that resolves astringcontaining the error message.
This works like Formik'svalidate, but instead of returning anerrorsobject, it's just astring.
Async: return a Promise that resolves astringcontaining the error message.
This works like Formik'svalidate, but instead of returning anerrorsobject, it's just astring.

`string`
`validate`
`errors`
`string`

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';34// Synchronous validation function5constvalidate=value=>{6leterrorMessage;7if(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value)){8errorMessage='Invalid email address';9}10returnerrorMessage;11};1213// Async validation function14constsleep=ms=>newPromise(resolve=>setTimeout(resolve,ms));1516constvalidateAsync=value=>{17returnsleep(2000).then(()=>{18if(['admin','null','god'].includes(value)){19return'Nice try';20}21});22};2324// example usage25constMyForm=()=>(26<Formik27initialValues={{email:'',username:''}}28onSubmit={values=>alert(JSON.stringify(values,null,2))}29>30{({errors,touched})=>(31<Form>32<Fieldvalidate={validate}name="email"type="email"/>33{errors.email&&touched.email?<div>{errors.email}</div>:null}34<Fieldvalidate={validateAsync}name="username"/>35{errors.username&&touched.username?(36<div>{errors.username}</div>37):null}38<buttontype="submit">Submit</button>39</Form>40)}41</Formik>42);
```

Note: To allow for i18n libraries, the TypeScript typings forvalidateare
slightly relaxed and allow you to return aFunction(e.g.i18n('invalid')).

`validate`
`Function`
`i18n('invalid')`

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