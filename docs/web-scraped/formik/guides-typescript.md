# Formik Documentation
# Source: https://formik.org/docs/guides/typescript
# Path: /docs/guides/typescript

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# TypeScript

The Formik source code is written in TypeScript, so you can rest easy that Formik's
types will always be up-to-date. As a mental model, Formik's type signatures are very
similar to React Router 4's<Route>.

`<Route>`

#### Render props (<Formik />and<Field />)

`<Formik />`
`<Field />`

```
1import*asReactfrom'react';2import{3Formik,4FormikHelpers,5FormikProps,6Form,7Field,8FieldProps,9}from'formik';1011interfaceMyFormValues{12firstName:string;13}1415exportconstMyApp:React.FC<{}>=()=>{16constinitialValues:MyFormValues={firstName:''};17return(18<div>19<h1>My Example</h1>20<Formik21initialValues={initialValues}22onSubmit={(values,actions)=>{23console.log({values,actions});24alert(JSON.stringify(values,null,2));25actions.setSubmitting(false);26}}27>28<Form>29<label htmlFor="firstName">First Name</label>30<Field id="firstName"name="firstName"placeholder="First Name"/>31<button type="submit">Submit</button>32</Form>33</Formik>34</div>35);36};
```

#### withFormik()

`withFormik()`

```
1importReactfrom'react';2import*asYupfrom'yup';3import{withFormik,FormikProps,FormikErrors,Form,Field}from'formik';45// Shape of form values6interfaceFormValues{7email:string;8password:string;9}1011interfaceOtherProps{12message:string;13}1415// Aside: You may see InjectedFormikProps<OtherProps, FormValues> instead of what comes below in older code.. InjectedFormikProps was artifact of when Formik only exported a HoC. It is also less flexible as it MUST wrap all props (it passes them through).16constInnerForm=(props:OtherProps&FormikProps<FormValues>)=>{17const{touched,errors,isSubmitting,message}=props;18return(19<Form>20<h1>{message}</h1>21<Fieldtype="email"name="email"/>22{touched.email&&errors.email&&<div>{errors.email}</div>}2324<Fieldtype="password"name="password"/>25{touched.password&&errors.password&&<div>{errors.password}</div>}2627<buttontype="submit"disabled={isSubmitting}>28Submit29</button>30</Form>31);32};3334// The type of props MyForm receives35interfaceMyFormProps{36initialEmail?:string;37message:string;// if this passed all the way through you might do this or make a union type38}3940// Wrap our form with the withFormik HoC41constMyForm=withFormik<MyFormProps,FormValues>({42// Transform outer props into form values43mapPropsToValues:props=>{44return{45email:props.initialEmail||'',46password:'',47};48},4950// Add a custom validation function (this can be async too!)51validate:(values:FormValues)=>{52leterrors:FormikErrors<FormValues>={};53if(!values.email){54errors.email='Required';55}elseif(!isValidEmail(values.email)){56errors.email='Invalid email address';57}58returnerrors;59},6061handleSubmit:values=>{62// do submitting things63},64})(InnerForm);6566// Use <MyForm /> wherevs67constBasic=()=>(68<div>69<h1>My App</h1>70<p>This can be anywhere in your application</p>71<MyFormmessage="Sign up"/>72</div>73);7475exportdefaultBasic;
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