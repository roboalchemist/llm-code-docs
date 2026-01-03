# Formik Documentation
# Source: https://formik.org/docs/overview
# Path: /docs/overview

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# Overview

Let's face it, forms are really verbose inReact. To make matters worse, most form
helpers do wayyyy too much magic and often have a significant performance cost
associated with them. Formik is a small library that helps you with the 3 most
annoying parts:

- Getting values in and out of form state
- Validation and error messages
- Handling form submission
By colocating all of the above in one place, Formik will keep things
organized--making testing, refactoring, and reasoning about your forms a breeze.

## Motivation

I (@jaredpalmer) wrote Formik while building a large internal administrative dashboard with@eonwhite. With around ~30 unique forms, it
quickly became obvious that we could benefit by standardizing not just our input
components but also the way in which data flowed through our forms.

### Why not Redux-Form?

By now, you might be thinking, "Why didn't you just useRedux-Form?" Good question.

- According to our prophet Dan Abramov,form state is inherently ephemeral and local, so tracking it in Redux (or any kind of Flux library) is unnecessary
- Redux-Form calls your entire top-level Redux reducer multiple times ON EVERY
SINGLE KEYSTROKE. This is fine for small apps, but as your Redux app grows,
input latency will continue to increase if you use Redux-Form.
- Redux-Form is 22.5 kB minified gzipped (Formik is 12.7 kB)
My goal with Formik was to create a scalable, performant, form helper with a
minimal API that does the really really annoying stuff, and leaves the rest up
to you.

My talk at React Alicante goes much deeper into Formik's motivation and philosophy, introduces the library (by watching me build a mini version of it), and demos how to build a non-trivial form (with arrays, custom inputs, etc.) using the real thing.

## Influences

Formik started by expanding onthis little higher order componentbyBrent Jackson, some naming conventions from
Redux-Form, and (most recently) the render props approach popularized byReact-MotionandReact-Router 4. Whether you
have used any of the above or not, Formik only takes a few minutes to get
started with.

## Installation

You can install Formik withNPM,Yarn, or a good ol'<script>viaunpkg.com.

`<script>`

### NPM

```
npm install formik --save
```

or

```
yarn add formik
```

Formik is compatible with React v15+ and works with ReactDOM and React Native.

You can also try before you buy with thisdemo of Formik on CodeSandbox.io

### In-browser Playgrounds

You can play with Formik in your web browser with these live online playgrounds.

- CodeSandbox (ReactDOM)
- Snack (React Native)

## The Gist

Formik keeps track of your form's state and then exposes it plus a few reusable
methods and event handlers (handleChange,handleBlur, andhandleSubmit) to
your form viaprops.handleChangeandhandleBlurwork exactly as
expected--they use anameoridattribute to figure out which field to
update.

`handleChange`
`handleBlur`
`handleSubmit`
`props`
`handleChange`
`handleBlur`
`name`
`id`

```
1importReactfrom'react';2import{Formik}from'formik';34constBasic=()=>(5<div>6<h1>Anywhere in your app!</h1>7<Formik8initialValues={{email:'',password:''}}9validate={values=>{10consterrors={};11if(!values.email){12errors.email='Required';13}elseif(14!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)15){16errors.email='Invalid email address';17}18returnerrors;19}}20onSubmit={(values,{setSubmitting})=>{21setTimeout(()=>{22alert(JSON.stringify(values,null,2));23setSubmitting(false);24},400);25}}26>27{({28values,29errors,30touched,31handleChange,32handleBlur,33handleSubmit,34isSubmitting,35/* and other goodies */36})=>(37<formonSubmit={handleSubmit}>38<input39type="email"40name="email"41onChange={handleChange}42onBlur={handleBlur}43value={values.email}44/>45{errors.email&&touched.email&&errors.email}46<input47type="password"48name="password"49onChange={handleChange}50onBlur={handleBlur}51value={values.password}52/>53{errors.password&&touched.password&&errors.password}54<buttontype="submit"disabled={isSubmitting}>55Submit56</button>57</form>58)}59</Formik>60</div>61);6263exportdefaultBasic;
```

### Reducing boilerplate

The code above is very explicit about exactly what Formik is doing.onChange->handleChange,onBlur->handleBlur, and so on. However, to save you time, Formik comes with a few extra components to make life easier and less verbose:<Form />,<Field />, and<ErrorMessage />. They use React context to hook into the parent<Formik />state/methods.

`onChange`
`handleChange`
`onBlur`
`handleBlur`
`<Form />`
`<Field />`
`<ErrorMessage />`
`<Formik />`

```
1// Render Prop2importReactfrom'react';3import{Formik,Form,Field,ErrorMessage}from'formik';45constBasic=()=>(6<div>7<h1>Any place in your app!</h1>8<Formik9initialValues={{email:'',password:''}}10validate={values=>{11consterrors={};12if(!values.email){13errors.email='Required';14}elseif(15!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)16){17errors.email='Invalid email address';18}19returnerrors;20}}21onSubmit={(values,{setSubmitting})=>{22setTimeout(()=>{23alert(JSON.stringify(values,null,2));24setSubmitting(false);25},400);26}}27>28{({isSubmitting})=>(29<Form>30<Fieldtype="email"name="email"/>31<ErrorMessagename="email"component="div"/>32<Fieldtype="password"name="password"/>33<ErrorMessagename="password"component="div"/>34<buttontype="submit"disabled={isSubmitting}>35Submit36</button>37</Form>38)}39</Formik>40</div>41);4243exportdefaultBasic;
```

Read below for more information...

### Complementary Packages

As you can see above, validation is left up to you. Feel free to write your own
validators or use a 3rd party library. Personally, I useYupfor object schema validation. It has an
API that's pretty similar toJoi/React PropTypesbut is small enough
for the browser and fast enough for runtime usage. Because I ❤️ Yup sooo
much, Formik has a special config option / prop for Yup calledvalidationSchemawhich will
automatically transform Yup's validation errors into a pretty object whose keys
matchvaluesandtouched. Anyways, you can
install Yup from npm...

`validationSchema`
`values`
`touched`

```
npm install yup--save
```

or

```
yarn add yup
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