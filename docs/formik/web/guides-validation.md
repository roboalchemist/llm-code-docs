# Formik Documentation
# Source: https://formik.org/docs/guides/validation
# Path: /docs/guides/validation

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# Validation

Formik is designed to manage forms with complex validation with ease. Formik supports synchronous and asynchronous
form-level and field-level validation. Furthermore, it comes with baked-in support for schema-based form-level validation through Yup. This guide will describe the ins and outs of all of the above.

## Flavors of Validation

### Form-level Validation

Form-level validation is useful because you have complete access to all of your form'svaluesand props whenever the function runs, so you can validate dependent fields at the same time.

`values`
There are 2 ways to do form-level validation with Formik:

- <Formik validate>andwithFormik({ validate: ... })
`<Formik validate>`
`withFormik({ validate: ... })`
- <Formik validationSchema>andwithFormik({ validationSchema: ... })
`<Formik validationSchema>`
`withFormik({ validationSchema: ... })`

#### validate

`validate`
<Formik>andwithFormik()take a prop/option calledvalidatethat accepts either a synchronous or asynchronous function.

`<Formik>`
`withFormik()`
`validate`

```
1// Synchronous validation2constvalidate=(values,props/* only available when using withFormik */)=>{3consterrors={};45if(!values.email){6errors.email='Required';7}elseif(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)){8errors.email='Invalid email address';9}1011//...1213returnerrors;14};1516// Async Validation17constsleep=ms=>newPromise(resolve=>setTimeout(resolve,ms));1819constvalidate=(values,props/* only available when using withFormik */)=>{20returnsleep(2000).then(()=>{21consterrors={};22if(['admin','null','god'].includes(values.username)){23errors.username='Nice try';24}25// ...26returnerrors;27});28};
```

For more information about<Formik validate>, see the API reference.

`<Formik validate>`

#### validationSchema

`validationSchema`
As you can see above, validation is left up to you. Feel free to write your own
validators or use a 3rd party library. At The Palmer Group, we useYupfor object schema validation. It has an
API that's pretty similar toJoiandReact PropTypesbut is small enough
for the browser and fast enough for runtime usage. Because we ❤️ Yup sooo
much, Formik has a special config option / prop for Yup object schemas calledvalidationSchemawhich will automatically transform Yup's validation errors into a pretty object whose keys matchvaluesandtouched. This symmetry makes it easy to manage business logic around error messages.

`validationSchema`
`values`
`touched`
To add Yup to your project, install it from NPM.

```
npm install yup --save
```

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';3import*asYupfrom'yup';45constSignupSchema=Yup.object().shape({6firstName:Yup.string()7.min(2,'Too Short!')8.max(50,'Too Long!')9.required('Required'),10lastName:Yup.string()11.min(2,'Too Short!')12.max(50,'Too Long!')13.required('Required'),14email:Yup.string().email('Invalid email').required('Required'),15});1617exportconstValidationSchemaExample=()=>(18<div>19<h1>Signup</h1>20<Formik21initialValues={{22firstName:'',23lastName:'',24email:'',25}}26validationSchema={SignupSchema}27onSubmit={values=>{28// same shape as initial values29console.log(values);30}}31>32{({errors,touched})=>(33<Form>34<Fieldname="firstName"/>35{errors.firstName&&touched.firstName?(36<div>{errors.firstName}</div>37):null}38<Fieldname="lastName"/>39{errors.lastName&&touched.lastName?(40<div>{errors.lastName}</div>41):null}42<Fieldname="email"type="email"/>43{errors.email&&touched.email?<div>{errors.email}</div>:null}44<buttontype="submit">Submit</button>45</Form>46)}47</Formik>48</div>49);
```

For more information about<Formik validationSchema>, see the API reference.

`<Formik validationSchema>`

### Field-level Validation

#### validate

`validate`
Formik supports field-level validation via thevalidateprop of<Field>/<FastField>components oruseFieldhook. This function can be synchronous or asynchronous (return a Promise). It will run after anyonChangeandonBlurby default. This behavior can be altered at the top level<Formik/>component using thevalidateOnChangeandvalidateOnBlurprops respectively. In addition to change/blur, all field-level validations are run at the beginning of a submission attempt and then the results are deeply merged with any top-level validation results.

`validate`
`<Field>`
`<FastField>`
`useField`
`onChange`
`onBlur`
`<Formik/>`
`validateOnChange`
`validateOnBlur`
Note: The<Field>/<FastField>components'validatefunction will only be executed on mounted fields. That is to say, if any of your fields unmount during the flow of your form (e.g. Material-UI's<Tabs>unmounts the previous<Tab>your user was on), those fields will not be validated during form validation/submission.

`<Field>/<FastField>`
`validate`
`<Tabs>`
`<Tab>`

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';34functionvalidateEmail(value){5leterror;6if(!value){7error='Required';8}elseif(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value)){9error='Invalid email address';10}11returnerror;12}1314functionvalidateUsername(value){15leterror;16if(value==='admin'){17error='Nice try!';18}19returnerror;20}2122exportconstFieldLevelValidationExample=()=>(23<div>24<h1>Signup</h1>25<Formik26initialValues={{27username:'',28email:'',29}}30onSubmit={values=>{31// same shape as initial values32console.log(values);33}}34>35{({errors,touched,isValidating})=>(36<Form>37<Fieldname="email"validate={validateEmail}/>38{errors.email&&touched.email&&<div>{errors.email}</div>}3940<Fieldname="username"validate={validateUsername}/>41{errors.username&&touched.username&&<div>{errors.username}</div>}4243<buttontype="submit">Submit</button>44</Form>45)}46</Formik>47</div>48);
```

### Manually Triggering Validation

You can manually trigger both form-level and field-level validation with Formik using thevalidateFormandvalidateFieldmethods respectively.

`validateForm`
`validateField`

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';34functionvalidateEmail(value){5leterror;6if(!value){7error='Required';8}elseif(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value)){9error='Invalid email address';10}11returnerror;12}1314functionvalidateUsername(value){15leterror;16if(value==='admin'){17error='Nice try!';18}19returnerror;20}2122exportconstFieldLevelValidationExample=()=>(23<div>24<h1>Signup</h1>25<Formik26initialValues={{27username:'',28email:'',29}}30onSubmit={values=>{31// same shape as initial values32console.log(values);33}}34>35{({errors,touched,validateField,validateForm})=>(36<Form>37<Fieldname="email"validate={validateEmail}/>38{errors.email&&touched.email&&<div>{errors.email}</div>}3940<Fieldname="username"validate={validateUsername}/>41{errors.username&&touched.username&&<div>{errors.username}</div>}42{/** Trigger field-level validation43imperatively */}44<buttontype="button"onClick={()=>validateField('username')}>45Check Username46</button>47{/** Trigger form-level validation48imperatively */}49<button50type="button"51onClick={()=>validateForm().then(()=>console.log('blah'))}52>53Validate All54</button>55<buttontype="submit">Submit</button>56</Form>57)}58</Formik>59</div>60);
```

## When Does Validation Run?

You can control when Formik runs validation by changing the values of<Formik validateOnChange>and/or<Formik validateOnBlur>props depending on your needs. By default, Formik will run validation methods as follows:

`<Formik validateOnChange>`
`<Formik validateOnBlur>`
After "change" events/methods(things that updatevalues)

`values`
- handleChange
`handleChange`
- setFieldValue
`setFieldValue`
- setValues
`setValues`
After "blur" events/methods(things that updatetouched)

`touched`
- handleBlur
`handleBlur`
- setTouched
`setTouched`
- setFieldTouched
`setFieldTouched`
Whenever submission is attempted

- handleSubmit
`handleSubmit`
- submitForm
`submitForm`
There are also imperative helper methods provided to you via Formik's render/injected props which you can use to imperatively call validation.

- validateForm
`validateForm`
- validateField
`validateField`

## Displaying Error Messages

Error messages are dependent on the form's validation. If an error exists, and the validation function produces an error object (as it should) with a matching shape to our values/initialValues, dependent field errors can be accessed from the errors object.

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';3import*asYupfrom'yup';45constDisplayingErrorMessagesSchema=Yup.object().shape({6username:Yup.string()7.min(2,'Too Short!')8.max(50,'Too Long!')9.required('Required'),10email:Yup.string().email('Invalid email').required('Required'),11});1213exportconstDisplayingErrorMessagesExample=()=>(14<div>15<h1>DisplayingErrorMessages</h1>16<Formik17initialValues={{18username:'',19email:'',20}}21validationSchema={DisplayingErrorMessagesSchema}22onSubmit={values=>{23// same shape as initial values24console.log(values);25}}26>27{({errors,touched})=>(28<Form>29<Fieldname="username"/>30{/* If this field has been touched, and it contains an error, display it31*/}32{touched.username&&errors.username&&<div>{errors.username}</div>}33<Fieldname="email"/>34{/* If this field has been touched, and it contains an error, display35it */}36{touched.email&&errors.email&&<div>{errors.email}</div>}37<button type="submit">Submit</button>38</Form>39)}40</Formik>41</div>42);
```

TheErrorMessagecomponent can also be used to display error messages.

## Frequently Asked Questions

IfisValidatingprop istrue

`isValidating`
`true`
No. Useundefinedinstead. Formik usesundefinedto represent empty states. If you usenull, several parts of Formik's computed props (e.g.isValidfor example), will not work as expected.

`undefined`
`undefined`
`null`
`isValid`
Formik has extensive unit tests for Yup validation so you do not need to test that. However, if you are rolling your own validation functions, you should simply unit test those. If you do need to test Formik's execution you should use the imperativevalidateFormandvalidateFieldmethods respectively.

`validateForm`
`validateField`

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