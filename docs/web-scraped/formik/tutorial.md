# Formik Documentation
# Source: https://formik.org/docs/tutorial
# Path: /docs/tutorial

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# Tutorial

## Before we start

Welcome to the Formik tutorial. This will teach you everything you need to know to build simple and complex forms in React.

If you’re impatient and just want to start hacking on your machine locally, check outthe 60-second quickstart.

### What are we building?

In this tutorial, we’ll build a complex newsletter signup form with React and Formik.

You can see what we’ll be building here:Final Result. If the code doesn’t make sense to you, don’t worry! The goal of this tutorial is to help you understand Formik.

### Prerequisites

You’ll need to have familiarity with HTML, CSS,modern JavaScript, andReact(andReact Hooks) to fully understand Formik and how it works. In this tutorial, we’re usingarrow functions,let,const,spread syntax,destructuring,computed property names, andasync/await. You can use theBabel REPLto check what ES6 code compiles to.

## Setup for the Tutorial

There are two ways to complete this tutorial: you can either write the code in your browser, or you can set up a local development environment on your computer.

### Setup Option 1: Write Code in the Browser

This is the quickest way to get started!

First, open thisStarter Codein a new tab. The new tab should display an email address input, a submit button, and some React code. We’ll be editing the React code in this tutorial.

Skip the second setup option, and go to theOverviewsection to get an overview of Formik.

### Setup Option 2: Local Development Environment

This is completely optional and not required for this tutorial!

This setup requires more work, but allows you to complete the tutorial using an editor of your choice. Here are the steps to follow:

- Make sure you have a recent version ofNode.jsinstalled.
- Follow theinstallation instructions for Create React Appto make a new project.

```
npx create-react-app my-app
```

- Install Formik

```
npmi formik
```

Or

```
yarnaddformik
```

- Delete all files in thesrc/folder of the new project
`src/`
Note:

Don’t delete the entiresrcfolder, just the original source files inside it.We’ll replace the default source files with examples for this project in the next step.

`src`

```
1cdmy-app2cdsrc34# If you’re using a Mac or Linux:5rm-f *67# Or, if you’re on Windows:8del *910# Then, switch back to the project folder11cd..
```

- Add a file namedstyles.cssin thesrc/folder withthis CSS code.
Add a file namedstyles.cssin thesrc/folder withthis CSS code.

`styles.css`
`src/`
- Add a file namedindex.jsin thesrc/folder withthis JS code.
Add a file namedindex.jsin thesrc/folder withthis JS code.

`index.js`
`src/`
Now runnpm startin the project folder and openhttp://localhost:3000in the browser. You should see an email input and a submit button.

`npm start`
`http://localhost:3000`
We recommend followingthese instructionsto configure syntax highlighting for your editor.

### Help, I’m Stuck!

If you get stuck, check out Formik’sGitHub Discussions. In addition, theFormium Community Discord Serveris a great way to get help quickly too. If you don’t receive an answer, or if you remain stuck, please file an issue, and we’ll help you out.

## Overview: What is Formik?

Formik is a small group of React components and hooks for building forms in React and React Native. It helps with the three most annoying parts:

- Getting values in and out of form state
- Validation and error messages
- Handling form submission
By colocating all of the above in one place, Formik keeps things
organized--making testing, refactoring, and reasoning about your forms a breeze.

## The Basics

We’re going to start with themost verboseway of using Formik. While this may seem a bit long-winded, it’s important to see how Formik builds on itself so you have a full grasp of what’s possible and a complete mental model of how it works.

### A simple newsletter signup form

Imagine we want to add a newsletter signup form for a blog. To start, our form will have just one field namedemail. With Formik, this is just a few lines of code.

`email`

```
1importReactfrom'react';2import{useFormik}from'formik';34constSignupForm=()=>{5// Pass the useFormik() hook initial form values and a submit function that will6// be called when the form is submitted7constformik=useFormik({8initialValues:{9email:'',10},11onSubmit:values=>{12alert(JSON.stringify(values,null,2));13},14});15return(16<formonSubmit={formik.handleSubmit}>17<labelhtmlFor="email">Email Address</label>18<input19id="email"20name="email"21type="email"22onChange={formik.handleChange}23value={formik.values.email}24/>2526<buttontype="submit">Submit</button>27</form>28);29};
```

We pass our form’sinitialValuesand a submission function (onSubmit) to theuseFormik()hook. The hook then returns to us a goodie bag of form state and helper methods in a variable we callformik. For now, the only helper methods we care about are as follows:

`initialValues`
`onSubmit`
`useFormik()`
`formik`
- handleSubmit: A submission handler
`handleSubmit`
- handleChange: A change handler to pass to each<input>,<select>, or<textarea>
`handleChange`
`<input>`
`<select>`
`<textarea>`
- values: Our form’s current values
`values`
As you can see above, we pass each of these to their respective props...and that’s it! We can now have a working form powered by Formik. Instead of managing our form’s values on our own and writing our own custom event handlers for every single input, we can just useuseFormik().

`useFormik()`
This is pretty neat, but with just one single input, the benefits of usinguseFormik()are unclear. So let’s add two more inputs: one for the user’s first and last name, which we’ll store asfirstNameandlastNamein the form.

`useFormik()`
`firstName`
`lastName`

```
1importReactfrom'react';2import{useFormik}from'formik';34constSignupForm=()=>{5// Note that we have to initialize ALL of fields with values. These6// could come from props, but since we don’t want to prefill this form,7// we just use an empty string. If we don’t do this, React will yell8// at us.9constformik=useFormik({10initialValues:{11firstName:'',12lastName:'',13email:'',14},15onSubmit:values=>{16alert(JSON.stringify(values,null,2));17},18});19return(20<formonSubmit={formik.handleSubmit}>21<labelhtmlFor="firstName">First Name</label>22<input23id="firstName"24name="firstName"25type="text"26onChange={formik.handleChange}27value={formik.values.firstName}28/>2930<labelhtmlFor="lastName">Last Name</label>31<input32id="lastName"33name="lastName"34type="text"35onChange={formik.handleChange}36value={formik.values.lastName}37/>3839<labelhtmlFor="email">Email Address</label>40<input41id="email"42name="email"43type="email"44onChange={formik.handleChange}45value={formik.values.email}46/>4748<buttontype="submit">Submit</button>49</form>50);51};
```

If you look carefully at our new code, you’ll notice some patterns and symmetryforming.

- We reuse the same exact change handler functionhandleChangefor each HTML input
`handleChange`
- We pass anidandnameHTML attribute thatmatchesthe property we defined ininitialValues
`id`
`name`
`initialValues`
- We access the field’s value using the same name (email->formik.values.email)
`email`
`formik.values.email`
If you’re familiar with building forms with plain React, you can think of Formik’shandleChangeas working like this:

`handleChange`

```
1const[values,setValues]=React.useState({});23consthandleChange=event=>{4setValues(prevValues=>({5...prevValues,6// we use the name to tell Formik which key of `values` to update7[event.target.name]:event.target.value8});9}
```

## Validation

While our contact form works, it’s not quite feature-complete; users can submit it, but it doesn’t tell them which (if any) fields are required.

If we’re okay with using the browser’s built-in HTML input validation, we could add arequiredprop to each of our inputs, specify minimum/maximum lengths (maxlengthandminlength), and/or add apatternprop for regex validation for each of these inputs. These are great if we can get away with them. However, HTML validation has its limitations. First, it only works in the browser! So this clearly is not viable for React Native. Second, it’s hard/impossible to show custom error messages to our user. Third, it’s very janky.

`required`
`maxlength`
`minlength`
`pattern`
As mentioned earlier, Formik keeps track of not only your form’svalues, but also its validation and error messages. To add validation with JS, let’s specify a custom validation function and pass it asvalidateto theuseFormik()hook. If an error exists, this custom validation function should produce anerrorobject with a matching shape to ourvalues/initialValues. Again...symmetry...yes...

`values`
`validate`
`useFormik()`
`error`
`values`
`initialValues`

```
1importReactfrom'react';2import{useFormik}from'formik';34// A custom validation function. This must return an object5// which keys are symmetrical to our values/initialValues6constvalidate=values=>{7consterrors={};8if(!values.firstName){9errors.firstName='Required';10}elseif(values.firstName.length>15){11errors.firstName='Must be 15 characters or less';12}1314if(!values.lastName){15errors.lastName='Required';16}elseif(values.lastName.length>20){17errors.lastName='Must be 20 characters or less';18}1920if(!values.email){21errors.email='Required';22}elseif(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)){23errors.email='Invalid email address';24}2526returnerrors;27};2829constSignupForm=()=>{30// Pass the useFormik() hook initial form values, a validate function that will be called when31// form values change or fields are blurred, and a submit function that will32// be called when the form is submitted33constformik=useFormik({34initialValues:{35firstName:'',36lastName:'',37email:'',38},39validate,40onSubmit:values=>{41alert(JSON.stringify(values,null,2));42},43});44return(45<formonSubmit={formik.handleSubmit}>46<labelhtmlFor="firstName">First Name</label>47<input48id="firstName"49name="firstName"50type="text"51onChange={formik.handleChange}52value={formik.values.firstName}53/>54{formik.errors.firstName?<div>{formik.errors.firstName}</div>:null}5556<labelhtmlFor="lastName">Last Name</label>57<input58id="lastName"59name="lastName"60type="text"61onChange={formik.handleChange}62value={formik.values.lastName}63/>64{formik.errors.lastName?<div>{formik.errors.lastName}</div>:null}6566<labelhtmlFor="email">Email Address</label>67<input68id="email"69name="email"70type="email"71onChange={formik.handleChange}72value={formik.values.email}73/>74{formik.errors.email?<div>{formik.errors.email}</div>:null}7576<buttontype="submit">Submit</button>77</form>78);79};
```

formik.errorsis populated via the custom validation function. By default, Formik will validate after each keystroke (change event), each input’sblur event, as well as prior to submission. TheonSubmitfunction we passed touseFormik()will be executed only if there are no errors (i.e. if ourvalidatefunction returns{}).

`formik.errors`
`onSubmit`
`useFormik()`
`validate`
`{}`

## Visited fields

While our form works, and our users see each error, it’s not a great user experience for them. Since our validation function runs on each keystroke against theentireform’svalues, ourerrorsobject containsallvalidation errors at any given moment. In our component, we’re just checking if an error exists and then immediately showing it to the user. This is awkward since we’re going to show error messages for fields that the user hasn’t even visited yet. Most of the time, we only want to show a field’s error messageafterour user is done typing in that field.

`values`
`errors`
Likeerrorsandvalues, Formik keeps track of which fields have been visited. It stores this information in an object calledtouchedthat also mirrors the shape ofvalues/initialValues. The keys oftouchedare the field names, and the values oftouchedare booleanstrue/false.

`errors`
`values`
`touched`
`values`
`initialValues`
`touched`
`touched`
`true`
`false`
To take advantage oftouched, we passformik.handleBlurto each input’sonBlurprop. This function works similarly toformik.handleChangein that it uses thenameattribute to figure out which field to update.

`touched`
`formik.handleBlur`
`onBlur`
`formik.handleChange`
`name`

```
1importReactfrom'react';2import{useFormik}from'formik';34constvalidate=values=>{5consterrors={};67if(!values.firstName){8errors.firstName='Required';9}elseif(values.firstName.length>15){10errors.firstName='Must be 15 characters or less';11}1213if(!values.lastName){14errors.lastName='Required';15}elseif(values.lastName.length>20){16errors.lastName='Must be 20 characters or less';17}1819if(!values.email){20errors.email='Required';21}elseif(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)){22errors.email='Invalid email address';23}2425returnerrors;26};2728constSignupForm=()=>{29constformik=useFormik({30initialValues:{31firstName:'',32lastName:'',33email:'',34},35validate,36onSubmit:values=>{37alert(JSON.stringify(values,null,2));38},39});40return(41<formonSubmit={formik.handleSubmit}>42<labelhtmlFor="firstName">First Name</label>43<input44id="firstName"45name="firstName"46type="text"47onChange={formik.handleChange}48onBlur={formik.handleBlur}49value={formik.values.firstName}50/>51{formik.errors.firstName?<div>{formik.errors.firstName}</div>:null}5253<labelhtmlFor="lastName">Last Name</label>54<input55id="lastName"56name="lastName"57type="text"58onChange={formik.handleChange}59onBlur={formik.handleBlur}60value={formik.values.lastName}61/>62{formik.errors.lastName?<div>{formik.errors.lastName}</div>:null}6364<labelhtmlFor="email">Email Address</label>65<input66id="email"67name="email"68type="email"69onChange={formik.handleChange}70onBlur={formik.handleBlur}71value={formik.values.email}72/>73{formik.errors.email?<div>{formik.errors.email}</div>:null}7475<buttontype="submit">Submit</button>76</form>77);78};
```

Almost there! Now that we’re trackingtouched, we can now change our error message render logic toonlyshow a given field’s error message if it existsandif our user has visited that field.

`touched`

```
1importReactfrom'react';2import{useFormik}from'formik';34constvalidate=values=>{5consterrors={};67if(!values.firstName){8errors.firstName='Required';9}elseif(values.firstName.length>15){10errors.firstName='Must be 15 characters or less';11}1213if(!values.lastName){14errors.lastName='Required';15}elseif(values.lastName.length>20){16errors.lastName='Must be 20 characters or less';17}1819if(!values.email){20errors.email='Required';21}elseif(!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)){22errors.email='Invalid email address';23}2425returnerrors;26};2728constSignupForm=()=>{29constformik=useFormik({30initialValues:{31firstName:'',32lastName:'',33email:'',34},35validate,36onSubmit:values=>{37alert(JSON.stringify(values,null,2));38},39});40return(41<formonSubmit={formik.handleSubmit}>42<labelhtmlFor="firstName">First Name</label>43<input44id="firstName"45name="firstName"46type="text"47onChange={formik.handleChange}48onBlur={formik.handleBlur}49value={formik.values.firstName}50/>51{formik.touched.firstName&&formik.errors.firstName?(52<div>{formik.errors.firstName}</div>53):null}5455<labelhtmlFor="lastName">Last Name</label>56<input57id="lastName"58name="lastName"59type="text"60onChange={formik.handleChange}61onBlur={formik.handleBlur}62value={formik.values.lastName}63/>64{formik.touched.lastName&&formik.errors.lastName?(65<div>{formik.errors.lastName}</div>66):null}6768<labelhtmlFor="email">Email Address</label>69<input70id="email"71name="email"72type="email"73onChange={formik.handleChange}74onBlur={formik.handleBlur}75value={formik.values.email}76/>77{formik.touched.email&&formik.errors.email?(78<div>{formik.errors.email}</div>79):null}8081<buttontype="submit">Submit</button>82</form>83);84};
```

### Schema Validation with Yup

As you can see above, validation is left up to you. Feel free to write your own validators or use a 3rd-party helper library. Formik’s authors/a large portion of its users useJason Quense’s libraryYupfor object schema validation. Yup has an API that’s similar toJoiandReact PropTypes, but is also small enough for the browser and fast enough for runtime usage. You can try it out here with thisREPL.

Since Formik authors/usersloveYup so much, Formik has a special configuration prop for Yup calledvalidationSchemawhich will automatically transform Yup’s validation errors messages into a pretty object whose keys matchvalues/initialValues/touched(just like any custom validation function would have to). Anyways, you can install Yup from NPM/yarn like so...

`validationSchema`
`values`
`initialValues`
`touched`

```
1npminstallyup --save23# or via yarn45yarnaddyup
```

To see how Yup works, let’s get rid of our custom validation functionvalidateand re-write our validation with Yup andvalidationSchema:

`validate`
`validationSchema`

```
1importReactfrom'react';2import{useFormik}from'formik';3import*asYupfrom'yup';45constSignupForm=()=>{6constformik=useFormik({7initialValues:{8firstName:'',9lastName:'',10email:'',11},12validationSchema:Yup.object({13firstName:Yup.string()14.max(15,'Must be 15 characters or less')15.required('Required'),16lastName:Yup.string()17.max(20,'Must be 20 characters or less')18.required('Required'),19email:Yup.string().email('Invalid email address').required('Required'),20}),21onSubmit:values=>{22alert(JSON.stringify(values,null,2));23},24});25return(26<formonSubmit={formik.handleSubmit}>27<labelhtmlFor="firstName">First Name</label>28<input29id="firstName"30name="firstName"31type="text"32onChange={formik.handleChange}33onBlur={formik.handleBlur}34value={formik.values.firstName}35/>36{formik.touched.firstName&&formik.errors.firstName?(37<div>{formik.errors.firstName}</div>38):null}3940<labelhtmlFor="lastName">Last Name</label>41<input42id="lastName"43name="lastName"44type="text"45onChange={formik.handleChange}46onBlur={formik.handleBlur}47value={formik.values.lastName}48/>49{formik.touched.lastName&&formik.errors.lastName?(50<div>{formik.errors.lastName}</div>51):null}5253<labelhtmlFor="email">Email Address</label>54<input55id="email"56name="email"57type="email"58onChange={formik.handleChange}59onBlur={formik.handleBlur}60value={formik.values.email}61/>62{formik.touched.email&&formik.errors.email?(63<div>{formik.errors.email}</div>64):null}6566<buttontype="submit">Submit</button>67</form>68);69};
```

Again, Yup is 100% optional. However, we suggest giving it a try. As you can see above, we expressed the exact same validation function with just 10 lines of code instead of 30. One of Formik’s core design principles is to help you stay organized. Yup definitely helps a lot with this--schemas are extremely expressive, intuitive (since they mirror your values), and reusable. Whether or not you use Yup, we highly recommended you share commonly used validation methods across your application. This will ensure that common fields (e.g. email, street addresses, usernames, phone numbers, etc.) are validated consistently and result in a better user experience.

## Reducing Boilerplate

### getFieldProps()

`getFieldProps()`
The code above is very explicit about exactly what Formik is doing.onChange->handleChange,onBlur->handleBlur, and so on. However, to save you time,useFormik()returns a helper method calledformik.getFieldProps()to make it faster to wire up inputs. Given some field-level info, it returns to you the exact group ofonChange,onBlur,value,checkedfor a given field. You can then spread that on aninput,select, ortextarea.

`onChange`
`handleChange`
`onBlur`
`handleBlur`
`useFormik()`
`formik.getFieldProps()`
`onChange`
`onBlur`
`value`
`checked`
`input`
`select`
`textarea`

```
1importReactfrom'react';2import{useFormik}from'formik';3import*asYupfrom'yup';45constSignupForm=()=>{6constformik=useFormik({7initialValues:{8firstName:'',9lastName:'',10email:'',11},12validationSchema:Yup.object({13firstName:Yup.string()14.max(15,'Must be 15 characters or less')15.required('Required'),16lastName:Yup.string()17.max(20,'Must be 20 characters or less')18.required('Required'),19email:Yup.string().email('Invalid email address').required('Required'),20}),21onSubmit:values=>{22alert(JSON.stringify(values,null,2));23},24});25return(26<formonSubmit={formik.handleSubmit}>27<labelhtmlFor="firstName">First Name</label>28<input29id="firstName"30type="text"31{...formik.getFieldProps('firstName')}32/>33{formik.touched.firstName&&formik.errors.firstName?(34<div>{formik.errors.firstName}</div>35):null}3637<labelhtmlFor="lastName">Last Name</label>38<inputid="lastName"type="text"{...formik.getFieldProps('lastName')}/>39{formik.touched.lastName&&formik.errors.lastName?(40<div>{formik.errors.lastName}</div>41):null}4243<labelhtmlFor="email">Email Address</label>44<inputid="email"type="email"{...formik.getFieldProps('email')}/>45{formik.touched.email&&formik.errors.email?(46<div>{formik.errors.email}</div>47):null}4849<buttontype="submit">Submit</button>50</form>51);52};
```

### Leveraging React Context

Our code above is again very explicit about exactly what Formik is doing.onChange->handleChange,onBlur->handleBlur, and so on. However, we still have to manually pass each input this "prop getter"getFieldProps(). To save you even more time, Formik comes withReact Context-powered API/components to make life easier and code less verbose:<Formik />,<Form />,<Field />, and<ErrorMessage />. More explicitly, they use React Context implicitly to connect with the parent<Formik />state/methods.

`onChange`
`handleChange`
`onBlur`
`handleBlur`
`getFieldProps()`
`<Formik />`
`<Form />`
`<Field />`
`<ErrorMessage />`
`<Formik />`
Since these components use React Context, we need to render aReact Context Providerthat holds our form state and helpers in our tree. If you did this yourself, it would look like:

```
1importReactfrom'react';2import{useFormik}from'formik';34// Create empty context5constFormikContext=React.createContext({});67// Place all of what’s returned by useFormik into context8exportconstFormik=({children,...props})=>{9constformikStateAndHelpers=useFormik(props);10return(11<FormikContext.Providervalue={formikStateAndHelpers}>12{typeofchildren==='function'13?children(formikStateAndHelpers)14:children}15</FormikContext.Provider>16);17};
```

Luckily, we’ve done this for you in a<Formik>component that works just like this.

`<Formik>`
Let’s now swap out theuseFormik()hook for Formik’s<Formik>component/render-prop. Since it’s a component, we’ll convert the object passed touseFormik()to JSX, with each key becoming a prop.

`useFormik()`
`<Formik>`
`useFormik()`

```
1importReactfrom'react';2import{Formik}from'formik';3import*asYupfrom'yup';45constSignupForm=()=>{6return(7<Formik8initialValues={{firstName:'',lastName:'',email:''}}9validationSchema={Yup.object({10firstName:Yup.string()11.max(15,'Must be 15 characters or less')12.required('Required'),13lastName:Yup.string()14.max(20,'Must be 20 characters or less')15.required('Required'),16email:Yup.string().email('Invalid email address').required('Required'),17})}18onSubmit={(values,{setSubmitting})=>{19setTimeout(()=>{20alert(JSON.stringify(values,null,2));21setSubmitting(false);22},400);23}}24>25{formik=>(26<formonSubmit={formik.handleSubmit}>27<labelhtmlFor="firstName">First Name</label>28<input29id="firstName"30type="text"31{...formik.getFieldProps('firstName')}32/>33{formik.touched.firstName&&formik.errors.firstName?(34<div>{formik.errors.firstName}</div>35):null}3637<labelhtmlFor="lastName">Last Name</label>38<input39id="lastName"40type="text"41{...formik.getFieldProps('lastName')}42/>43{formik.touched.lastName&&formik.errors.lastName?(44<div>{formik.errors.lastName}</div>45):null}4647<labelhtmlFor="email">Email Address</label>48<inputid="email"type="email"{...formik.getFieldProps('email')}/>49{formik.touched.email&&formik.errors.email?(50<div>{formik.errors.email}</div>51):null}5253<buttontype="submit">Submit</button>54</form>55)}56</Formik>57);58};
```

As you can see above, we swapped outuseFormik()hook and replaced it with the<Formik>component. The<Formik>component accepts a function as its children (a.k.a. arender prop). Its argument is theexactsame object returned byuseFormik()(in fact,<Formik>callsuseFormik()internally!). Thus, our form works the same as before, except now we can use new components to express ourselves in a more concise manner.

`useFormik()`
`<Formik>`
`<Formik>`
`useFormik()`
`<Formik>`
`useFormik()`

```
1importReactfrom'react';2import{Formik,Field,Form,ErrorMessage}from'formik';3import*asYupfrom'yup';45constSignupForm=()=>{6return(7<Formik8initialValues={{firstName:'',lastName:'',email:''}}9validationSchema={Yup.object({10firstName:Yup.string()11.max(15,'Must be 15 characters or less')12.required('Required'),13lastName:Yup.string()14.max(20,'Must be 20 characters or less')15.required('Required'),16email:Yup.string().email('Invalid email address').required('Required'),17})}18onSubmit={(values,{setSubmitting})=>{19setTimeout(()=>{20alert(JSON.stringify(values,null,2));21setSubmitting(false);22},400);23}}24>25<Form>26<labelhtmlFor="firstName">First Name</label>27<Fieldname="firstName"type="text"/>28<ErrorMessagename="firstName"/>2930<labelhtmlFor="lastName">Last Name</label>31<Fieldname="lastName"type="text"/>32<ErrorMessagename="lastName"/>3334<labelhtmlFor="email">Email Address</label>35<Fieldname="email"type="email"/>36<ErrorMessagename="email"/>3738<buttontype="submit">Submit</button>39</Form>40</Formik>41);42};
```

The<Field>component by default will render an<input>component that, given anameprop, will implicitly grab the respectiveonChange,onBlur,valueprops and pass them to the element as well as any props you pass to it. However, since not everything is an input,<Field>also accepts a few other props to let you render whatever you want. Some examples..

`<Field>`
`<input>`
`name`
`onChange`
`onBlur`
`value`
`<Field>`

```
1// <input className="form-input" placeHolder="Jane"  />2<Fieldname="firstName"className="form-input"placeholder="Jane"/>34// <textarea className="form-textarea"/></textarea>5<Fieldname="message"as="textarea"className="form-textarea"/>67// <select className="my-select"/>8<Fieldname="colors"as="select"className="my-select">9<optionvalue="red">Red</option>10<optionvalue="green">Green</option>11<optionvalue="blue">Blue</option>12</Field>
```

React is all about composition, and while we’ve cut down on a lot of theprop-drilling, we’re still repeating ourselves with alabel,<Field>, and<ErrorMessage>for each of our inputs. We can do better with an abstraction! With Formik, you can and should build reusable input primitive components that you can share around your application. Turns out our<Field>render-prop component has a sister and her name isuseFieldthat’s going to do the same thing, but via React Hooks! Check this out...

`label`
`<Field>`
`<ErrorMessage>`
`<Field>`
`useField`

```
1importReactfrom'react';2importReactDOMfrom'react-dom';3import{Formik,Form,useField}from'formik';4import*asYupfrom'yup';56constMyTextInput=({label,...props})=>{7// useField() returns [formik.getFieldProps(), formik.getFieldMeta()]8// which we can spread on <input>. We can use field meta to show an error9// message if the field is invalid and it has been touched (i.e. visited)10const[field,meta]=useField(props);11return(12<>13<labelhtmlFor={props.id||props.name}>{label}</label>14<inputclassName="text-input"{...field}{...props}/>15{meta.touched&&meta.error?(16<divclassName="error">{meta.error}</div>17):null}18</>19);20};2122constMyCheckbox=({children,...props})=>{23// React treats radios and checkbox inputs differently from other input types: select and textarea.24// Formik does this too! When you specify `type` to useField(), it will25// return the correct bag of props for you -- a `checked` prop will be included26// in `field` alongside `name`, `value`, `onChange`, and `onBlur`27const[field,meta]=useField({...props,type:'checkbox'});28return(29<div>30<labelclassName="checkbox-input">31<inputtype="checkbox"{...field}{...props}/>32{children}33</label>34{meta.touched&&meta.error?(35<divclassName="error">{meta.error}</div>36):null}37</div>38);39};4041constMySelect=({children,label,...props})=>{42const[field,meta]=useField(props);43return(44<div>45<labelhtmlFor={props.id||props.name}>{label}</label>46<select{...field}{...props}/>47{children}48{meta.touched&&meta.error?(49<divclassName="error">{meta.error}</div>50):null}51</div>52);53};5455// And now we can use these56constSignupForm=()=>{57return(58<>59<h1>Subscribe!</h1>60<Formik61initialValues={{62firstName:'',63lastName:'',64email:'',65acceptedTerms:false,// added for our checkbox66jobType:'',// added for our select67}}68validationSchema={Yup.object({69firstName:Yup.string()70.max(15,'Must be 15 characters or less')71.required('Required'),72lastName:Yup.string()73.max(20,'Must be 20 characters or less')74.required('Required'),75email:Yup.string()76.email('Invalid email address')77.required('Required'),78acceptedTerms:Yup.boolean()79.required('Required')80.oneOf([true],'You must accept the terms and conditions.'),81jobType:Yup.string()82.oneOf(83['designer','development','product','other'],84'Invalid Job Type'85)86.required('Required'),87})}88onSubmit={(values,{setSubmitting})=>{89setTimeout(()=>{90alert(JSON.stringify(values,null,2));91setSubmitting(false);92},400);93}}94>95<Form>96<MyTextInput97label="First Name"98name="firstName"99type="text"100placeholder="Jane"101/>102103<MyTextInput104label="Last Name"105name="lastName"106type="text"107placeholder="Doe"108/>109110<MyTextInput111label="Email Address"112name="email"113type="email"114placeholder="jane@formik.com"115/>116117<MySelectlabel="Job Type"name="jobType">118<optionvalue="">Select a job type</option>119<optionvalue="designer">Designer</option>120<optionvalue="development">Developer</option>121<optionvalue="product">Product Manager</option>122<optionvalue="other">Other</option>123</MySelect>124125<MyCheckboxname="acceptedTerms">126I accept the terms and conditions127</MyCheckbox>128129<buttontype="submit">Submit</button>130</Form>131</Formik>132</>133);134};
```

As you can see above,useField()gives us the ability to connect any kind input of React component to Formik as if it were a<Field>+<ErrorMessage>. We can use it to build a group of reusable inputs that fit our needs.

`useField()`
`<Field>`
`<ErrorMessage>`

## Wrapping Up

Congratulations! You’ve created a signup form with Formik that:

- Has complex validation logic and rich error messages
- Properly displays errors messages to the user at the correct time (after they have blurred a field)
- Leverages your own custom input components you can use on other forms in your app
Nice work! We hope you now feel like you have a decent grasp on how Formik works.

Check out the final result here:Final Result.

If you have extra time or want to practice your new Formik skills, here are some ideas for improvements that you could make to the signup form which are listed in order of increasing difficulty:

- Disable the submit button while the user has attempted to submit (hint:formik.isSubmitting)
`formik.isSubmitting`
- Add a reset button withformik.handleResetor<button type="reset">.
`formik.handleReset`
`<button type="reset">`
- Pre-populateinitialValuesbased on URL query string or props passed to<SignupForm>.
`initialValues`
`<SignupForm>`
- Change the input border color to red when a field has an error and isn’t focused
- Add a shake animation to each field when it displays an error and has been visited
- Persist form state to the browser’ssessionStorageso that form progress is kept in between page refreshes
Throughout this tutorial, we touched on Formik concepts including form state, fields, validation, hooks, render props, and React context. For a more detailed explanation of each of these topics, check out the rest of thedocumentation. To learn more about defining the components and hooks in the tutorial, check out theAPI reference.

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