# Formik Documentation
# Source: https://formik.org/docs/api/fieldarray
# Path: /docs/api/fieldarray

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# <FieldArray />

<FieldArray />is a component that helps with common array/list manipulations. You pass it anameproperty with the path to the key withinvaluesthat holds the relevant array.<FieldArray />will then give you access to array helper methods via render props. For convenience, calling these methods will trigger validation and also managetouchedfor you.

`<FieldArray />`
`name`
`values`
`<FieldArray />`
`touched`

```
1importReactfrom'react';2import{Formik,Form,Field,FieldArray}from'formik';34// Here is an example of a form with an editable list.5// Next to each input are buttons for insert and remove.6// If the list is empty, there is a button to add an item.7exportconstFriendList=()=>(8<div>9<h1>Friend List</h1>10<Formik11initialValues={{friends:['jared','ian','brent']}}12onSubmit={values=>13setTimeout(()=>{14alert(JSON.stringify(values,null,2));15},500)16}17render={({values})=>(18<Form>19<FieldArray20name="friends"21render={arrayHelpers=>(22<div>23{values.friends&&values.friends.length>0?(24values.friends.map((friend,index)=>(25<divkey={index}>26<Fieldname={`friends.${index}`}/>27<button28type="button"29onClick={()=>arrayHelpers.remove(index)}// remove a friend from the list30>31-32</button>33<button34type="button"35onClick={()=>arrayHelpers.insert(index,'')}// insert an empty string at a position36>37+38</button>39</div>40))41):(42<buttontype="button"onClick={()=>arrayHelpers.push('')}>43{/* show this when user has removed all friends from the list */}44Add a friend45</button>46)}47<div>48<buttontype="submit">Submit</button>49</div>50</div>51)}52/>53</Form>54)}55/>56</div>57);
```

### name: string

`name: string`
The name or path to the relevant key invalues.

`values`

### validateOnChange?: boolean

`validateOnChange?: boolean`
Default istrue. Determines if form validation should or should not be runafterany array manipulations.

`true`

## FieldArray Array of Objects

You can also iterate through an array of objects, by following a convention ofobject[index].propertyorobject.index.propertyfor the name attributes of<Field />or<input />elements in<FieldArray />.

`object[index].property`
`object.index.property`
`<Field />`
`<input />`
`<FieldArray />`

```
1<Form>2<FieldArray3name="friends"4render={arrayHelpers=>(5<div>6{values.friends.map((friend,index)=>(7<divkey={index}>8{/** both these conventions do the same */}9<Fieldname={`friends[${index}].name`}/>10<Fieldname={`friends.${index}.age`}/>1112<buttontype="button"onClick={()=>arrayHelpers.remove(index)}>13-14</button>15</div>16))}17<button18type="button"19onClick={()=>arrayHelpers.push({name:'',age:''})}20>21+22</button>23</div>24)}25/>26</Form>
```

## FieldArray Validation Gotchas

Validation can be tricky with<FieldArray>.

`<FieldArray>`
If you usevalidationSchemaand your form has array validation requirements (like a min length) as well as nested array field requirements, displaying errors can be tricky. Formik/Yup will show validation errors inside out. For example,

`validationSchema`

```
1constschema=Yup.object().shape({2friends:Yup.array()3.of(4Yup.object().shape({5name:Yup.string().min(4,'too short').required('Required'),// these constraints take precedence6salary:Yup.string().min(3,'cmon').required('Required'),// these constraints take precedence7})8)9.required('Must have friends')// these constraints are shown if and only if inner constraints are satisfied10.min(3,'Minimum of 3 friends'),11});
```

Since Yup and your custom validation function should always output error messages as strings, you'll need to sniff whether your nested error is an array or a string when you go to display it.

So...to display'Must have friends'and'Minimum of 3 friends'(our example's array validation constraints)...

`'Must have friends'`
`'Minimum of 3 friends'`
Bad

```
1// within a `FieldArray`'s render2constFriendArrayErrors=errors=>3errors.friends?<div>{errors.friends}</div>:null;// app will crash
```

Good

```
1// within a `FieldArray`'s render2constFriendArrayErrors=errors=>3typeoferrors.friends==='string'?<div>{errors.friends}</div>:null;
```

For the nested field errors, you should assume that no part of the object is defined unless you've checked for it. Thus, you may want to do yourself a favor and make a custom<ErrorMessage />component that looks like this:

`<ErrorMessage />`

```
1import{Field,getIn}from'formik';23constErrorMessage=({name})=>(4<Field5name={name}6render={({form})=>{7consterror=getIn(form.errors,name);8consttouch=getIn(form.touched,name);9returntouch&&error?error:null;10}}11/>12);1314// Usage15<ErrorMessagename="friends[0].name"/>;// => null, 'too short', or 'required'
```

NOTE: In Formik v0.12 / 1.0, a newmetaprop may be added toFieldandFieldArraythat will give you relevant metadata such aserror&touch, which will save you from having to use Formik or lodash's getIn or checking if the path is defined on your own.

`meta`
`Field`
`FieldArray`
`error`
`touch`

## FieldArray Helpers

The following methods are made available via render props.

- push: (obj: any) => void: Add a value to the end of an array
`push: (obj: any) => void`
- swap: (indexA: number, indexB: number) => void: Swap two values in an array
`swap: (indexA: number, indexB: number) => void`
- move: (from: number, to: number) => void: Move an element in an array to another index
`move: (from: number, to: number) => void`
- insert: (index: number, value: any) => void: Insert an element at a given index into the array
`insert: (index: number, value: any) => void`
- unshift: (value: any) => number: Add an element to the beginning of an array and return its length
`unshift: (value: any) => number`
- remove<T>(index: number): T | undefined: Remove an element at an index of an array and return it
`remove<T>(index: number): T | undefined`
- pop<T>(): T | undefined: Remove and return value from the end of the array
`pop<T>(): T | undefined`
- replace: (index: number, value: any) => void: Replace a value at the given index into the array
`replace: (index: number, value: any) => void`

## FieldArray render methods

There are three ways to render things with<FieldArray />

`<FieldArray />`
- <FieldArray name="..." component>
`<FieldArray name="..." component>`
- <FieldArray name="..." render>
`<FieldArray name="..." render>`
- <FieldArray name="..." children>
`<FieldArray name="..." children>`

### render: (arrayHelpers: ArrayHelpers) => React.ReactNode

`render: (arrayHelpers: ArrayHelpers) => React.ReactNode`

```
1importReactfrom'react';2import{Formik,Form,Field,FieldArray}from'formik'34exportconstFriendList=()=>(5<div>6<h1>Friend List</h1>7<Formik8initialValues={{friends:['jared','ian','brent']}}9onSubmit={...}10render={formikProps=>(11<FieldArray12name="friends"13render={({move,swap,push,insert,unshift,pop})=>(14<Form>15{/*... use these however you want */}16</Form>17)}18/>19/>20</div>21);
```

### component: React.ReactNode

`component: React.ReactNode`

```
1importReactfrom'react';2import{Formik,Form,Field,FieldArray}from'formik'345exportconstFriendList=()=>(6<div>7<h1>Friend List</h1>8<Formik9initialValues={{friends:['jared','ian','brent']}}10onSubmit={...}11render={formikProps=>(12<FieldArray13name="friends"14component={MyDynamicForm}15/>16)}17/>18</div>19);202122// In addition to the array helpers, Formik state and helpers23// (values, touched, setXXX, etc) are provided through a `form`24// prop25exportconstMyDynamicForm=({26move,swap,push,insert,unshift,pop,form27})=>(28<Form>29{/**  whatever you need to do */}30</Form>31);
```

### children: func

`children: func`

```
1importReactfrom'react';2import{Formik,Form,Field,FieldArray}from'formik'345exportconstFriendList=()=>(6<div>7<h1>Friend List</h1>8<Formik9initialValues={{friends:['jared','ian','brent']}}10onSubmit={...}11render={formikProps=>(12<FieldArrayname="friends">13{({move,swap,push,insert,unshift,pop,form})=>{14return(15<Form>16{/*... use these however you want */}17</Form>18);19}}20</FieldArray>21)}22/>23</div>24);
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