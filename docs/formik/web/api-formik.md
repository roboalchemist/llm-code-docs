# Formik Documentation
# Source: https://formik.org/docs/api/formik
# Path: /docs/api/formik

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# <Formik />

<Formik>is a component that helps you with building forms. It uses a render
props pattern made popular by libraries like React Motion and React Router.

`<Formik>`

## Example

```
1importReactfrom'react';2import{Formik}from'formik';34constBasicExample=()=>(5<div>6<h1>My Form</h1>7<Formik8initialValues={{name:'jared'}}9onSubmit={(values,actions)=>{10setTimeout(()=>{11alert(JSON.stringify(values,null,2));12actions.setSubmitting(false);13},1000);14}}15>16{props=>(17<formonSubmit={props.handleSubmit}>18<input19type="text"20onChange={props.handleChange}21onBlur={props.handleBlur}22value={props.values.name}23name="name"24/>25{props.errors.name&&<divid="feedback">{props.errors.name}</div>}26<buttontype="submit">Submit</button>27</form>28)}29</Formik>30</div>31);
```

#### Props

# Reference

## Props

### Formik render methods and props

There are 2 ways to render things with<Formik />

`<Formik />`
- <Formik component>
`<Formik component>`
- <Formik children>
`<Formik children>`
- <Formik render>Deprecated in 2.x
`<Formik render>`
Each render methods will be passed the same props:

#### dirty: boolean

`dirty: boolean`
Returnstrueif values are not deeply equal from initial values,falseotherwise.dirtyis a readonly computed property and should not be mutated directly.

`true`
`false`
`dirty`

#### errors: { [field: string]: string }

`errors: { [field: string]: string }`
Form validation errors. Should match the shape of your form'svaluesdefined
ininitialValues. If you are usingvalidationSchema(which you should be),
keys and shape will match your schema exactly. Internally, Formik transforms rawYup validation errorson your behalf. If you are usingvalidate, then that function will determine
theerrorsobjects shape.

`values`
`initialValues`
`validationSchema`
`validate`
`errors`

#### handleBlur: (e: any) => void

`handleBlur: (e: any) => void`
onBlurevent handler. Useful for when you need to track whether an input has
beentouchedor not. This should be passed to<input onBlur={handleBlur} ... />

`onBlur`
`touched`
`<input onBlur={handleBlur} ... />`

#### handleChange: (e: React.ChangeEvent<any>) => void

`handleChange: (e: React.ChangeEvent<any>) => void`
General input change event handler. This will update thevalues[key]wherekeyis the event-emitting input'snameattribute. If thenameattribute is
not present,handleChangewill look for an input'sidattribute. Note:
"input" here means all HTML inputs.

`values[key]`
`key`
`name`
`name`
`handleChange`
`id`

#### handleReset: () => void

`handleReset: () => void`
Reset handler. Will reset the form to its initial state. This should be passed
to<button onClick={handleReset}>...</button>

`<button onClick={handleReset}>...</button>`

#### handleSubmit: (e: React.FormEvent<HTMLFormElement>) => void

`handleSubmit: (e: React.FormEvent<HTMLFormElement>) => void`
Submit handler. This should be passed to<form onSubmit={props.handleSubmit}>...</form>. To learn more about the submission process, seeForm Submission.

`<form onSubmit={props.handleSubmit}>...</form>`

#### isSubmitting: boolean

`isSubmitting: boolean`
Submitting state of the form. Returnstrueif submission is in progress andfalseotherwise. IMPORTANT: Formik will set this totrueas soon as submission isattempted. To learn more about the submission process, seeForm Submission.

`true`
`false`
`true`

#### isValid: boolean

`isValid: boolean`
Returnstrueif there are noerrors(i.e. theerrorsobject is empty) andfalseotherwise.

`true`
`errors`
`errors`
`false`
Note:isInitialValidwas deprecated in 2.x. However, for backwards compatibility, if theisInitialValidprop is specified,isValidwill returntrueif the there are noerrors, or the result ofisInitialValidof the form if it is in "pristine" condition (i.e. notdirty).

`isInitialValid`
`isInitialValid`
`isValid`
`true`
`errors`
`isInitialValid`
`dirty`

#### isValidating: boolean

`isValidating: boolean`
Returnstrueif Formik is running validation during submission, or by calling[validateForm]directlyfalseotherwise. To learn more about what happens withisValidatingduring the submission process, seeForm Submission.

`true`
`validateForm`
`false`
`isValidating`

#### resetForm: (nextState?: Partial<FormikState<Values>>) => void

`resetForm: (nextState?: Partial<FormikState<Values>>) => void`
Imperatively reset the form. The only (optional) argument,nextState, is an object on which any of theseFormikStatefields are optional:

`nextState`
`FormikState`

```
1interfaceFormikState<Values>{2/** Form values */3values:Values;4/** map of field names to specific error for that field */5errors:FormikErrors<Values>;6/** map of field names to **whether** the field has been touched */7touched:FormikTouched<Values>;8/** whether the form is currently submitting */9isSubmitting:boolean;10/** whether the form is currently validating (prior to submission) */11isValidating:boolean;12/** Top level status state, in case you need it */13status?:any;14/** Number of times user tried to submit the form */15submitCount:number;16}
```

IfnextStateis specified, Formik will setnextState.valuesas the new "initial state" and use the related values ofnextStateto update the form'sinitialValuesas well asinitialTouched,initialStatus,initialErrors. This is useful for altering the initial state (i.e. "base") of the form after changes have been made.

`nextState`
`nextState.values`
`nextState`
`initialValues`
`initialTouched`
`initialStatus`
`initialErrors`

```
1// typescript usage2functionMyForm(props:MyFormProps){3// using TSX Generics here to set <Values> to <Blog>4return(5<Formik<Blog>6initialValues={props.initVals}7onSubmit={(values,actions)=>{8props.onSubmit(values).then(()=>{9actions.setSubmitting(false);10actions.resetForm({11values:{12// the type of `values` inferred to be Blog13title:'',14image:'',15body:'',16},17// you can also set the other form states here18});19});20}}21>22// etc23</Formik>24);25}
```

IfnextStateis omitted, then Formik will reset state to the original initial state. The latter is useful for callingresetFormwithincomponentDidUpdateoruseEffect.

`nextState`
`resetForm`
`componentDidUpdate`
`useEffect`

```
actions.resetForm();
```

#### setErrors: (fields: { [field: string]: string }) => void

`setErrors: (fields: { [field: string]: string }) => void`
Seterrorsimperatively.

`errors`

#### setFieldError: (field: string, errorMsg: string) => void

`setFieldError: (field: string, errorMsg: string) => void`
Set the error message of a field imperatively.fieldshould match the key oferrorsyou wish to update. Useful for creating custom input error handlers.

`field`
`errors`

#### setFieldTouched: (field: string, isTouched?: boolean, shouldValidate?: boolean) => Promise<void | FormikErrors>

Set the touched state of a field imperatively.fieldshould match the key oftouchedyou wish to update. Useful for creating custom input blur handlers. Calling this method will trigger validation to run ifvalidateOnBluris set totrue(which it is by default).isToucheddefaults totrueif not specified. You can also explicitly prevent/skip validation by passing a third argument asfalse.

`field`
`touched`
`validateOnBlur`
`true`
`isTouched`
`true`
`false`
IfvalidateOnBluris set totrueand there are errors, they will be resolved in the returnedPromise.

`validateOnBlur`
`true`
`Promise`

#### submitForm: () => Promise

`submitForm: () => Promise`
Trigger a form submission. The promise will be rejected if form is invalid.

#### submitCount: number

`submitCount: number`
Number of times user tried to submit the form. Increases whenhandleSubmitis called, resets after callinghandleReset.submitCountis readonly computed property and should not be mutated directly.

`handleSubmit`
`handleReset`
`submitCount`

#### setFieldValue: (field: string, value: React.SetStateAction<any>, shouldValidate?: boolean) => Promise<void | FormikErrors>

Set the value of a field imperatively.fieldshould match the key ofvaluesyou wish to update. Useful for creating custom input change handlers. Calling this will trigger validation to run ifvalidateOnChangeis set totrue(which it is by default). You can also explicitly prevent/skip validation by passing a third argument asfalse.

`field`
`values`
`validateOnChange`
`true`
`false`
IfvalidateOnChangeis set totrueand there are errors, they will be resolved in the returnedPromise.

`validateOnChange`
`true`
`Promise`

#### setStatus: (status?: any) => void

`setStatus: (status?: any) => void`
Set a top-levelstatusto anything you want imperatively. Useful for
controlling arbitrary top-level state related to your form. For example, you can
use it to pass API responses back into your component inhandleSubmit.

`status`
`handleSubmit`

#### setSubmitting: (isSubmitting: boolean) => void

`setSubmitting: (isSubmitting: boolean) => void`
SetisSubmittingimperatively. You would call it withsetSubmitting(false)in youronSubmithandler to finish the cycle. To learn more about the submission process, seeForm Submission.

`isSubmitting`
`setSubmitting(false)`
`onSubmit`

#### setTouched: (fields: { [field: string]: boolean }, shouldValidate?: boolean) => Promise<void | FormikErrors>

Settouchedimperatively. Calling this will trigger validation to run ifvalidateOnBluris set totrue(which it is by default). You can also explicitly prevent/skip validation by passing a second argument asfalse.

`touched`
`validateOnBlur`
`true`
`false`
IfvalidateOnBluris set totrueand there are errors, they will be resolved in the returnedPromise.

`validateOnBlur`
`true`
`Promise`

#### setValues: (fields: React.SetStateAction<{ [field: string]: any }>, shouldValidate?: boolean) => Promise<void | FormikErrors<Values>>

Setvaluesimperatively. Calling this will trigger validation to run ifvalidateOnChangeis set totrue(which it is by default). You can also explicitly prevent/skip validation by passing a second argument asfalse.

`values`
`validateOnChange`
`true`
`false`
IfvalidateOnChangeis set totrueand there are errors, they will be resolved in the returnedPromise.

`validateOnChange`
`true`
`Promise`

#### status?: any

`status?: any`
A top-level status object that you can use to represent form state that can't
otherwise be expressed/stored with other methods. This is useful for capturing
and passing through API responses to your inner component.

statusshould only be modified by callingsetStatus.

`status`
`setStatus`

#### touched: { [field: string]: boolean }

`touched: { [field: string]: boolean }`
Touched fields. Each key corresponds to a field that has been touched/visited.

#### values: { [field: string]: any }

`values: { [field: string]: any }`
Your form's values. Will have the shape of the result ofmapPropsToValues(if specified) or all props that are not functions passed to your wrapped
component.

`mapPropsToValues`

#### validateForm: (values?: any) => Promise<FormikErrors<Values>>

`validateForm: (values?: any) => Promise<FormikErrors<Values>>`
Imperatively call yourvalidateorvalidateSchemadepending on what was specified. You can optionally pass values to validate against and this modify Formik state accordingly, otherwise this will use the currentvaluesof the form.

`validate`
`validateSchema`
`values`

#### validateField: (field: string) => void

`validateField: (field: string) => void`
Imperatively call field'svalidatefunction if specified for given field or run schema validation usingYup'sschema.validateAtand the provided top-levelvalidationSchemaprop. Formik will use the current field value.

`validate`
`schema.validateAt`
`validationSchema`

### component?: React.ComponentType<FormikProps<Values>>

`component?: React.ComponentType<FormikProps<Values>>`

```
1<Formikcomponent={ContactForm}/>;23constContactForm=({4handleSubmit,5handleChange,6handleBlur,7values,8errors,9})=>(10<formonSubmit={handleSubmit}>11<input12type="text"13onChange={handleChange}14onBlur={handleBlur}15value={values.name}16name="name"17/>18{errors.name&&<div>{errors.name}</div>}19<buttontype="submit">Submit</button>20</form>21);
```

Warning:<Formik component>takes precedence over<Formik render>so
don’t use both in the same<Formik>.

`<Formik component>`
`<Formik render>`
`<Formik>`

### render: (props: FormikProps<Values>) => ReactNode

`render: (props: FormikProps<Values>) => ReactNode`
Deprecated in 2.x

```
1<Formikrender={props=><ContactForm{...props}/>}/>23<Formik4render={({handleSubmit,handleChange,handleBlur,values,errors})=>(5<formonSubmit={handleSubmit}>6<input7type="text"8onChange={handleChange}9onBlur={handleBlur}10value={values.name}11name="name"12/>13{errors.name&&14<div>15{errors.name}16</div>}17<buttontype="submit">Submit</button>18</form>19)}20/>
```

### children?: React.ReactNode | (props: FormikProps<Values>) => ReactNode

`children?: React.ReactNode | (props: FormikProps<Values>) => ReactNode`

```
1<Formikchildren={props=><ContactForm{...props}/>}/>23// or...45<Formik>6{({handleSubmit,handleChange,handleBlur,values,errors})=>(7<formonSubmit={handleSubmit}>8<input9type="text"10onChange={handleChange}11onBlur={handleBlur}12value={values.name}13name="name"14/>15{errors.name&&16<div>17{errors.name}18</div>}19<buttontype="submit">Submit</button>20</form>21)}22</Formik>
```

### enableReinitialize?: boolean

`enableReinitialize?: boolean`
Default isfalse. Control whether Formik should reset the form ifinitialValueschanges (using deep equality).

`false`
`initialValues`

### isInitialValid?: boolean

`isInitialValid?: boolean`
Deprecated in 2.x, useinitialErrorsinstead

`initialErrors`
Control the initial value ofisValidprop prior to
mount. You can also pass a function. Useful for situations when you want to
enable/disable a submit and reset buttons on initial mount.

`isValid`

### initialErrors?: FormikErrors<Values>

`initialErrors?: FormikErrors<Values>`
Initial field errors of the form, Formik will make these values available to
render methods component aserrors.

`errors`
Note:initialErrorsis not available to the higher-order componentwithFormik, usemapPropsToErrorsinstead.

`initialErrors`
`withFormik`
`mapPropsToErrors`

### initialStatus?: any

`initialStatus?: any`
An arbitrary value for the initialstatusof the form. If the form is reset, this value will be restored.

`status`
Note:initialStatusis not available to the higher-order componentwithFormik, usemapPropsToStatusinstead.

`initialStatus`
`withFormik`
`mapPropsToStatus`

### initialTouched?: FormikTouched<Values>

`initialTouched?: FormikTouched<Values>`
Initial visited fields of the form, Formik will make these values available to
render methods component astouched.

`touched`
Note:initialTouchedis not available to the higher-order componentwithFormik, usemapPropsToTouchedinstead.

`initialTouched`
`withFormik`
`mapPropsToTouched`

### initialValues: Values

`initialValues: Values`
Initial field values of the form, Formik will make these values available to
render methods component asvalues.

`values`
Even if your form is empty by default, you must initialize all fields with
initial values otherwise React will throw an error saying that you have changed
an input from uncontrolled to controlled.

Note:initialValuesnot available to the higher-order component, usemapPropsToValuesinstead.

`initialValues`
`mapPropsToValues`

### onReset?: (values: Values, formikBag: FormikBag) => void

`onReset?: (values: Values, formikBag: FormikBag) => void`
Your optional form reset handler. It is passed your formsvaluesand the
"FormikBag".

`values`

### onSubmit: (values: Values, formikBag: FormikBag) => void | Promise<any>

`onSubmit: (values: Values, formikBag: FormikBag) => void | Promise<any>`
Your form submission handler. It is passed your formsvaluesand the
"FormikBag", which includes an object containing a subset of theinjected props and methods(i.e. all the methods
with names that start withset<Thing>+resetForm) and any props that were
passed to the wrapped component.

`values`
`set<Thing>`
`resetForm`
Note:errors,touched,statusand all event handlers are NOT
included in theFormikBag.

`errors`
`touched`
`status`
`FormikBag`
IMPORTANT: IfonSubmitis async, then Formik will automatically setisSubmittingtofalseon your behalf once it has resolved. This means you do NOT need to callformikBag.setSubmitting(false)manually. However, if youronSubmitfunction is synchronous, then you need to callsetSubmitting(false)on your own.

`onSubmit`
`isSubmitting`
`false`
`formikBag.setSubmitting(false)`
`onSubmit`
`setSubmitting(false)`

### validate?: (values: Values) => FormikErrors<Values> | Promise<any>

`validate?: (values: Values) => FormikErrors<Values> | Promise<any>`
Note: I suggest usingvalidationSchemaand Yup for validation. However,validateis a dependency-free, straightforward way to validate your forms.

`validationSchema`
`validate`
Validate the form'svalueswith function. This function can either be:

`values`
- Synchronous and return anerrorsobject.
`errors`

```
1// Synchronous validation2constvalidate=values=>{3consterrors={};45if(!values.email){6errors.email='Required';7}elseif(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)){8errors.email='Invalid email address';9}1011//...1213returnerrors;14};
```

- Asynchronous and return a Promise that's resolves to an object containingerrors
`errors`

```
1// Async Validation2constsleep=ms=>newPromise(resolve=>setTimeout(resolve,ms));34constvalidate=values=>{5returnsleep(2000).then(()=>{6consterrors={};7if(['admin','null','god'].includes(values.username)){8errors.username='Nice try';9}10// ...11returnerrors;12});13};
```

### validateOnBlur?: boolean

`validateOnBlur?: boolean`
Default istrue. Use this option to run validations onblurevents. More
specifically, when eitherhandleBlur,setFieldTouched, orsetTouchedare called.

`true`
`blur`
`handleBlur`
`setFieldTouched`
`setTouched`

### validateOnChange?: boolean

`validateOnChange?: boolean`
Default istrue. Use this option to tell Formik to run validations onchangeevents andchange-related methods. More specifically, when eitherhandleChange,setFieldValue, orsetValuesare called.

`true`
`change`
`change`
`handleChange`
`setFieldValue`
`setValues`

### validateOnMount?: boolean

`validateOnMount?: boolean`
Default isfalse. Use this option to tell Formik to run validations when the<Formik />component mounts
and/orinitialValueschange.

`false`
`<Formik />`
`initialValues`

### validationSchema?: Schema | (() => Schema)

`validationSchema?: Schema | (() => Schema)`
A Yup schemaor a function that returns a Yup
schema. This is used for validation. Errors are mapped by key to the inner
component'serrors. Its keys should match those ofvalues.

`errors`
`values`

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