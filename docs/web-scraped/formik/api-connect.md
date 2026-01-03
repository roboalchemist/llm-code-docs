# Formik Documentation
# Source: https://formik.org/docs/api/connect
# Path: /docs/api/connect

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# connect()

connect()is a higher-order component (HoC) that allows you to hook anything into Formik's context. It is used internally to construct<Field>and<Form>, but you can use it to build out new components as your needs change.

`connect()`
`<Field>`
`<Form>`

## Type signature

```
connect<OuterProps,Values=any>(Comp:React.ComponentType<OuterProps&{formik:FormikContext<Values>}>)=>React.ComponentType<OuterProps>
```

## Example

```
1importReactfrom'react';2import{connect,getIn}from'formik';34// This component renders an error message if a field has5// an error and it's already been touched.6constErrorMessage=props=>{7// All FormikProps available on props.formik!8consterror=getIn(props.formik.errors,props.name);9consttouch=getIn(props.formik.touched,props.name);10returntouch&&error?error:null;11};1213exportdefaultconnect(ErrorMessage);
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